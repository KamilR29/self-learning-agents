"""Ewaluacja agenta RAG na zestawach pytań z folderu ``nordvik-pytania``.

Dla każdego pytania:
  1. uruchamia orkiestratora i pobiera końcową odpowiedź,
  2. porównuje ją z odpowiedzią oczekiwaną (LLM jako sędzia: dobra/częściowa/zła),
  3. sprawdza pokrycie dokumentów źródłowych (po ID),
  4. zapisuje wynik.

Wyniki trafiają do folderu ``eval-wyniki/``:
  - ``odpowiedzi.md``   — szczegóły per pytanie (pytanie, oczekiwana, odpowiedź agenta, ocena),
  - ``wyniki.json``     — dane maszynowe,
  - ``statystyki.md``   — ile pytań z każdego pliku ocenionych na „dobra”.

Użycie:
    python evaluate-rag.py                 # wszystkie zestawy
    python evaluate-rag.py --limit 3       # po 3 pytania z każdego zestawu (szybki test)
    python evaluate-rag.py --sets 1 2      # tylko zestaw 1 i 2

Wymaga OPENAI_API_KEY (agent + sędzia).
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage

from simple_agents import build_orchestrator
from simple_agents.agent import DEFAULT_MODEL, ORCHESTRATOR_MODEL

PYTANIA_DIR = Path(__file__).parent / "nordvik-pytania"
WYNIKI_DIR = Path(__file__).parent / "eval-wyniki"
SET_FILES = {
    "1": "ZESTAW-1-jeden-dokument.md",
    "2": "ZESTAW-2-powiazania.md",
    "3": "ZESTAW-3-zlozone.md",
}

_ID_RE = re.compile(
    r"\b(?:KYC|KL|WN|DC|UM|HS|REG-[A-ZĄĆĘŁŃÓŚŹŻ]+|TOP|TO|POL-[A-ZĄĆĘŁŃÓŚŹŻ]+|SAR|RR|ZD|HT)-[0-9A-Za-z-]+\b"
)


def parse_questions(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    questions: list[dict] = []
    pattern = re.compile(
        r"(?ms)^\*\*(P\d+\.\d+)\.\*\*\s*(.*?)(?=^\*\*P\d+\.\d+\.\*\*|\Z)"
    )
    for m in pattern.finditer(text):
        qid, body = m.group(1), m.group(2)
        oczek = re.search(
            r"-\s*\*\*Oczekiwana odpowiedź.*?:\*\*\s*(.*?)(?=\n-\s*\*\*Dokument|\Z)",
            body, re.S,
        )
        src = re.search(r"-\s*\*\*Dokument[^:]*:\*\*\s*(.*)", body, re.S)
        question = (body[: oczek.start()] if oczek else body).strip()
        expected = oczek.group(1).strip() if oczek else ""
        sources_raw = src.group(1).strip() if src else ""
        questions.append({
            "id": qid,
            "question": question,
            "expected": expected,
            "expected_sources": sorted(set(_ID_RE.findall(sources_raw))),
        })
    return questions


def _extract_text(content) -> str:
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = [
            b["text"] for b in content
            if isinstance(b, dict) and b.get("type") == "text" and b.get("text")
        ]
        return "\n".join(parts).strip()
    return ""


def extract_final_answer(result: dict) -> str:
    msgs = result.get("messages", [])
    for msg in reversed(msgs):
        if not isinstance(msg, BaseMessage):
            continue
        if getattr(msg, "tool_calls", None):
            continue
        text = _extract_text(msg.content)
        if text:
            return text
    return ""


JUDGE_PROMPT = """Jesteś rygorystycznym sędzią oceniającym odpowiedzi systemu Q&A.
Porównaj ODPOWIEDŹ AGENTA z ODPOWIEDZIĄ OCZEKIWANĄ na dane PYTANIE.
Oceń wyłącznie zgodność merytoryczną (kluczowe fakty i liczby), ignorując styl.

PYTANIE:
{question}

ODPOWIEDŹ OCZEKIWANA:
{expected}

ODPOWIEDŹ AGENTA:
{answer}

Zwróć WYŁĄCZNIE obiekt JSON w formacie:
{{"ocena": "dobra" | "czesciowa" | "zla", "uzasadnienie": "<jedno zdanie>"}}
- "dobra": wszystkie kluczowe fakty/liczby zgodne z oczekiwaną,
- "czesciowa": część zgodna, część brakująca lub błędna,
- "zla": błędna, sprzeczna albo brak odpowiedzi."""


def judge(judge_model, question: str, expected: str, answer: str) -> dict:
    prompt = JUDGE_PROMPT.format(question=question, expected=expected, answer=answer or "(brak)")
    try:
        resp = judge_model.invoke(prompt)
        raw = resp.content if isinstance(resp.content, str) else _extract_text(resp.content)
        m = re.search(r"\{.*\}", raw, re.S)
        data = json.loads(m.group(0)) if m else {}
        ocena = str(data.get("ocena", "zla")).lower()
        if ocena not in {"dobra", "czesciowa", "zla"}:
            ocena = "zla"
        return {"ocena": ocena, "uzasadnienie": data.get("uzasadnienie", "")}
    except Exception as exc:
        return {"ocena": "blad_oceny", "uzasadnienie": f"Błąd sędziego: {exc!r}"}


def main() -> None:
    load_dotenv()
    ap = argparse.ArgumentParser()
    ap.add_argument("--sets", nargs="*", choices=["1", "2", "3"], default=["1", "2", "3"])
    ap.add_argument("--limit", type=int, default=None, help="maks. liczba pytań z każdego zestawu")
    ap.add_argument("--model", default=None, help="model orkiestratora i sędziego (domyślnie z env/DEFAULT)")
    args = ap.parse_args()

    # model_id = model subagentów i sędziego; orkiestrator ma osobny, mocniejszy
    # model (ORCHESTRATOR_MODEL w agent.py), tak jak w systemie samouczącym się
    model_id = args.model or os.environ.get("SUBAGENT_MODEL", DEFAULT_MODEL)
    agent = build_orchestrator(subagent_model=model_id)
    judge_model = init_chat_model(model_id)
    orch_id = os.environ.get("ORCHESTRATOR_MODEL", ORCHESTRATOR_MODEL)
    print(f"Model orkiestratora: {orch_id} | subagenci i sędzia: {model_id}")

    WYNIKI_DIR.mkdir(exist_ok=True)
    all_results: list[dict] = []
    stats: dict[str, dict] = {}

    for set_key in args.sets:
        path = PYTANIA_DIR / SET_FILES[set_key]
        questions = parse_questions(path)
        if args.limit:
            questions = questions[: args.limit]
        counts = {"dobra": 0, "czesciowa": 0, "zla": 0, "blad_oceny": 0}
        print(f"\n=== ZESTAW {set_key}: {len(questions)} pytań ===")

        for q in questions:
            print(f"  [{q['id']}] ...", end=" ", flush=True)
            try:
                res = agent.invoke(
                    {"messages": [{"role": "user", "content": q["question"]}]},
                    config={"recursion_limit": 100},
                )
                answer = extract_final_answer(res)
            except Exception as exc:
                answer = f"(BŁĄD URUCHOMIENIA: {exc!r})"

            verdict = judge(judge_model, q["question"], q["expected"], answer)
            found_sources = sorted(set(_ID_RE.findall(answer)))
            exp = set(q["expected_sources"])
            src_hit = len(exp & set(found_sources))
            src_cov = round(src_hit / len(exp), 2) if exp else None

            counts[verdict["ocena"]] = counts.get(verdict["ocena"], 0) + 1
            print(verdict["ocena"], f"(źródła {src_hit}/{len(exp)})" if exp else "")

            all_results.append({
                "zestaw": set_key,
                "id": q["id"],
                "pytanie": q["question"],
                "oczekiwana": q["expected"],
                "odpowiedz_agenta": answer,
                "ocena": verdict["ocena"],
                "uzasadnienie_oceny": verdict["uzasadnienie"],
                "zrodla_oczekiwane": q["expected_sources"],
                "zrodla_w_odpowiedzi": found_sources,
                "pokrycie_zrodel": src_cov,
            })

        total = sum(counts.values())
        stats[set_key] = {
            "plik": SET_FILES[set_key],
            "liczba_pytan": total,
            **counts,
            "dokladnosc_dobra": round(counts["dobra"] / total, 3) if total else 0.0,
            "dokladnosc_z_czesciowymi": round(
                (counts["dobra"] + 0.5 * counts["czesciowa"]) / total, 3
            ) if total else 0.0,
        }

    _write_outputs(all_results, stats)
    print(f"\nGotowe. Wyniki zapisane w: {WYNIKI_DIR}")


def _write_outputs(results: list[dict], stats: dict) -> None:
    # 1) JSON
    (WYNIKI_DIR / "wyniki.json").write_text(
        json.dumps({"wyniki": results, "statystyki": stats}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # 2) Odpowiedzi (markdown)
    lines = ["# Wyniki ewaluacji — odpowiedzi agenta\n"]
    icon = {"dobra": "[OK]", "czesciowa": "[~]", "zla": "[X]", "blad_oceny": "[!]"}
    for r in results:
        lines.append(f"## [{r['id']}] (zestaw {r['zestaw']}) {icon.get(r['ocena'], '')} {r['ocena']}")
        lines.append(f"**Pytanie:** {r['pytanie']}\n")
        lines.append(f"**Oczekiwana:** {r['oczekiwana']}\n")
        lines.append(f"**Odpowiedź agenta:** {r['odpowiedz_agenta']}\n")
        lines.append(f"**Ocena sędziego:** {r['ocena']} — {r['uzasadnienie_oceny']}\n")
        lines.append(
            f"**Źródła:** oczekiwane {r['zrodla_oczekiwane']}; "
            f"w odpowiedzi {r['zrodla_w_odpowiedzi']}; pokrycie {r['pokrycie_zrodel']}\n"
        )
        lines.append("---\n")
    (WYNIKI_DIR / "odpowiedzi.md").write_text("\n".join(lines), encoding="utf-8")

    # 3) Statystyki (markdown)
    s = ["# Statystyki ewaluacji\n", "| Zestaw | Plik | Pytań | Dobra | Częściowa | Zła | Dokładność (dobra) | Dokładność (z częściowymi) |",
         "|--------|------|------:|------:|----------:|----:|-------------------:|---------------------------:|"]
    tot = {"liczba_pytan": 0, "dobra": 0, "czesciowa": 0, "zla": 0}
    for k, v in stats.items():
        s.append(
            f"| {k} | {v['plik']} | {v['liczba_pytan']} | {v['dobra']} | "
            f"{v['czesciowa']} | {v['zla']} | {v['dokladnosc_dobra']:.0%} | "
            f"{v['dokladnosc_z_czesciowymi']:.0%} |"
        )
        for key in tot:
            tot[key] += v.get(key, 0)
    acc = tot["dobra"] / tot["liczba_pytan"] if tot["liczba_pytan"] else 0
    acc2 = (tot["dobra"] + 0.5 * tot["czesciowa"]) / tot["liczba_pytan"] if tot["liczba_pytan"] else 0
    s.append(
        f"| **Σ** | **wszystkie** | **{tot['liczba_pytan']}** | **{tot['dobra']}** | "
        f"**{tot['czesciowa']}** | **{tot['zla']}** | **{acc:.0%}** | **{acc2:.0%}** |"
    )
    (WYNIKI_DIR / "statystyki.md").write_text("\n".join(s) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
