"""Zaawansowana ewaluacja systemu self_learning_agents (pamięć + GraphRAG + weryfikacja).

Przebieg:
  FAZA 1 (bootstrap) — agenci najpierw poznają dokumenty i budują wiedzę:
    * graf wiedzy w Neo4j (narzędzie graph_build) — jeśli Neo4j jest skonfigurowany,
    * pamięć w pliku AGENTS.md (agent przegląda korpus i zapisuje esencję).
  FAZA 2 (Q&A) — pytania z ``nordvik-pytania``:
    * agent próbuje odpowiedzieć z PAMIĘCI i GRAFU,
    * gdy nie znajdzie → przeszukuje DOKUMENTY ponownie i aktualizuje pamięć,
    * weryfikator sprawdza odpowiedź; przy niepotwierdzeniu pętla szukania rusza znów.

Na żywo wypisywane są zdarzenia (fallback do dokumentów, aktualizacja pamięci,
weryfikacja, kolejne rundy). Wyniki + oceny + statystyki trafiają do
``eval-wyniki-advanced/``.

Użycie:
    python evaluate-self-learning.py --limit 2         # po 2 pytania z każdego zestawu
    python evaluate-self-learning.py --skip-graph      # pomiń budowę grafu (Neo4j)

Wymaga OPENAI_API_KEY (agent + sędzia). GraphRAG wymaga NEO4J_URI/USERNAME/PASSWORD.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
from pathlib import Path

logging.getLogger("neo4j.notifications").setLevel(logging.ERROR)

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage

from self_learning_agents import build_orchestrator
from self_learning_agents.agent import DEFAULT_MODEL, ORCHESTRATOR_MODEL
from self_learning_agents.tools.graph_tools import count_learned_nodes
from self_learning_agents.tools import graph_tools as gt

PYTANIA_DIR = Path(__file__).parent / "nordvik-pytania"
WYNIKI_DIR = Path(__file__).parent / "eval-wyniki-advanced"
SET_FILES = {
    "1": "ZESTAW-1-jeden-dokument.md",
    "2": "ZESTAW-2-powiazania.md",
    "3": "ZESTAW-3-zlozone.md",
}
CONFIG = {"recursion_limit": 200}

_ID_RE = re.compile(
    r"\b(?:KYC|KL|WN|DC|UM|HS|REG-[A-ZĄĆĘŁŃÓŚŹŻ]+|TOP|TO|POL-[A-ZĄĆĘŁŃÓŚŹŻ]+|SAR|RR|ZD|HT)-[0-9A-Za-z-]+\b"
)

def parse_questions(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    out: list[dict] = []
    for m in re.finditer(r"(?ms)^\*\*(P\d+\.\d+)\.\*\*\s*(.*?)(?=^\*\*P\d+\.\d+\.\*\*|\Z)", text):
        qid, body = m.group(1), m.group(2)
        oczek = re.search(
            r"-\s*\*\*Oczekiwana odpowiedź.*?:\*\*\s*(.*?)(?=\n-\s*\*\*Dokument|\Z)", body, re.S
        )
        src = re.search(r"-\s*\*\*Dokument[^:]*:\*\*\s*(.*)", body, re.S)
        out.append({
            "id": qid,
            "question": (body[: oczek.start()] if oczek else body).strip(),
            "expected": oczek.group(1).strip() if oczek else "",
            "expected_sources": sorted(set(_ID_RE.findall(src.group(1) if src else ""))),
        })
    return out


def _text(content) -> str:
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        return "\n".join(
            b["text"] for b in content
            if isinstance(b, dict) and b.get("type") == "text" and b.get("text")
        ).strip()
    return ""


def run_with_events(agent, prompt: str, live: bool = True) -> tuple[str, list[str]]:
    """Uruchom agenta strumieniowo; zwróć (końcowa_odpowiedź, lista_zdarzeń)."""
    events: list[str] = []
    last_text = ""
    counters = {"retriever": 0}

    def emit(msg: str) -> None:
        events.append(msg)
        if live:
            print(f"      · {msg}")

    for chunk in agent.stream(
        {"messages": [{"role": "user", "content": prompt}]},
        stream_mode="updates",
        config=CONFIG,
    ):
        for value in chunk.values():
            if not isinstance(value, dict):
                continue
            for msg in value.get("messages", []) or []:
                if not isinstance(msg, BaseMessage):
                    continue
                for call in getattr(msg, "tool_calls", None) or []:
                    name = call.get("name")
                    args = call.get("args") or {}
                    if name == "task":
                        sub = args.get("subagent_type") or args.get("subagent") or "?"
                        if sub == "retriever":
                            counters["retriever"] += 1
                            emit(
                                "nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY"
                                if counters["retriever"] == 1
                                else "niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach"
                            )
                        elif sub == "graph-retriever":
                            emit("odpytuję pamięć GRAFOWĄ (Neo4j)")
                        elif sub == "verifier":
                            emit("WERYFIKUJĘ odpowiedź w dokumentach")
                        elif sub == "answerer":
                            emit("formułuję odpowiedź")
                    elif name in ("graph_add_learned_fact", "graph_add_learning", "graph_update"):
                        emit("📝 AKTUALIZUJĘ GRAF (zapis wiedzy/wskazówki)")
                    elif name in ("edit_file", "write_file"):
                        fp = str(args.get("file_path", "")).lower()
                        if "memor" in fp:
                            emit("📝 AKTUALIZUJĘ PAMIĘĆ (zapis nowej wiedzy)")
                txt = _text(msg.content)
                if txt and not getattr(msg, "tool_calls", None):
                    last_text = txt
    return last_text, events


JUDGE_PROMPT = """Jesteś rygorystycznym sędzią oceniającym odpowiedzi systemu Q&A.
Porównaj ODPOWIEDŹ AGENTA z ODPOWIEDZIĄ OCZEKIWANĄ na PYTANIE. Oceń tylko zgodność
merytoryczną (kluczowe fakty i liczby), ignorując styl.

PYTANIE:
{question}

ODPOWIEDŹ OCZEKIWANA:
{expected}

ODPOWIEDŹ AGENTA:
{answer}

Zwróć WYŁĄCZNIE JSON: {{"ocena": "dobra"|"czesciowa"|"zla", "uzasadnienie": "<jedno zdanie>"}}"""


def judge(model, question: str, expected: str, answer: str) -> dict:
    try:
        raw = model.invoke(JUDGE_PROMPT.format(question=question, expected=expected, answer=answer or "(brak)"))
        raw = raw.content if isinstance(raw.content, str) else _text(raw.content)
        data = json.loads(re.search(r"\{.*\}", raw, re.S).group(0))
        ocena = str(data.get("ocena", "zla")).lower()
        return {"ocena": ocena if ocena in {"dobra", "czesciowa", "zla"} else "zla",
                "uzasadnienie": data.get("uzasadnienie", "")}
    except Exception as exc:
        return {"ocena": "blad_oceny", "uzasadnienie": f"Błąd sędziego: {exc!r}"}


def main() -> None:
    load_dotenv()
    ap = argparse.ArgumentParser()
    ap.add_argument("--sets", nargs="*", choices=["1", "2", "3"], default=["1", "2", "3"])
    ap.add_argument("--limit", type=int, default=None, help="maks. pytań z każdego zestawu")
    ap.add_argument("--model", default=None, help="model agentów i sędziego")
    ap.add_argument("--skip-graph", action="store_true", help="pomiń budowę grafu (Neo4j)")
    ap.add_argument("--docs-limit", type=int, default=0, help="ile dokumentów do grafu (0=wszystkie)")
    args = ap.parse_args()


    model_id = args.model or os.environ.get("SUBAGENT_MODEL", DEFAULT_MODEL)
    agent = build_orchestrator(subagent_model=model_id)   
    judge_model = init_chat_model(model_id, max_retries=8)  
    orch_id = os.environ.get("ORCHESTRATOR_MODEL", ORCHESTRATOR_MODEL)
    print(f"Model orkiestratora: {orch_id} | subagenci i sędzia: {model_id}")

    print("\n===== FAZA 1: BUDOWA WIEDZY =====")
    if args.skip_graph:
        print("[graf] pominięto (--skip-graph)")
    elif not gt.is_configured():
        print("[graf] pominięto — brak konfiguracji Neo4j (NEO4J_URI/USERNAME/PASSWORD)")
    else:
        zakres = f"{args.docs_limit} dokument(ów)" if args.docs_limit else "WSZYSTKIE dokumenty"
        print(f"[graf] buduję knowledge graph — {zakres}.")
        try:
            print("      ", gt.graph_build.invoke({"limit": args.docs_limit}))
        except Exception as exc:
            print(f"      [graf] nieudane: {exc!r} — kontynuuję bez grafu.")
    print("[przepływ] prowadzony przez orkiestratora deepagents (reguły w prompcie).")


    print("\n===== FAZA 2: ODPOWIADANIE NA PYTANIA =====")
    WYNIKI_DIR.mkdir(exist_ok=True)
    results: list[dict] = []
    stats: dict[str, dict] = {}

    for set_key in args.sets:
        questions = parse_questions(PYTANIA_DIR / SET_FILES[set_key])
        if args.limit:
            questions = questions[: args.limit]
        counts = {"dobra": 0, "czesciowa": 0, "zla": 0, "blad_oceny": 0}
        print(f"\n=== ZESTAW {set_key}: {len(questions)} pytań ===")

        for q in questions:
            print(f"  [{q['id']}] {q['question'][:70]}...")
            mem_before = count_learned_nodes()
            try:
                answer, events = run_with_events(agent, q["question"])
            except Exception as exc:
                answer, events = f"(BŁĄD: {exc!r})", [f"błąd: {exc!r}"]

            verdict = judge(judge_model, q["question"], q["expected"], answer)
            found = sorted(set(_ID_RE.findall(answer)))
            exp = set(q["expected_sources"])
            src_cov = round(len(exp & set(found)) / len(exp), 2) if exp else None
            counts[verdict["ocena"]] = counts.get(verdict["ocena"], 0) + 1
            fallback = any("DOKUMENTY" in e for e in events)
            fb_events: list[str] = []

            if verdict["ocena"] in ("zla", "czesciowa"):
                fb_prompt = (
                    f"INFORMACJA ZWROTNA do wcześniejszego pytania: „{q['question']}”. "
                    f"Twoja odpowiedź została oceniona jako {verdict['ocena']}. "
                    f"Uwaga oceniającego: {verdict['uzasadnienie']} "
                    "Potraktuj to jak feedback weryfikatora (zasada 5): PRZETWÓRZ tę "
                    "uwagę, poszukaj w dokumentach brakujących/niezgodnych danych, "
                    "UZUPEŁNIJ GRAF o te dane (graph_add_learned_fact / graph_update) "
                    "oraz dopisz jakościową wskazówkę (graph_add_learning) dowiązaną do "
                    "encji z pytania. NIE zapisuj gotowej odpowiedzi i nie odpowiadaj "
                    "ponownie na to pytanie."
                )
                try:
                    _, fb_events = run_with_events(agent, fb_prompt, live=False)
                    print("      · 📌 feedback → uzupełnienie grafu + wskazówka (sterowane promptem)")
                except Exception as exc:
                    print(f"      · feedback nieudany: {exc!r}")


            mem_after = count_learned_nodes()
            if mem_before >= 0 and mem_after >= 0:
                mem_upd = mem_after > mem_before
            else:
                mem_upd = any("GRAF" in e and "AKTUALIZ" in e for e in events + fb_events)
            print(f"      => ocena: {verdict['ocena']}"
                  f"{' | fallback do dokumentów' if fallback else ''}"
                  f"{' | graf zaktualizowany' if mem_upd else ''}")

            results.append({
                "zestaw": set_key, "id": q["id"], "pytanie": q["question"],
                "oczekiwana": q["expected"], "odpowiedz_agenta": answer,
                "ocena": verdict["ocena"], "uzasadnienie_oceny": verdict["uzasadnienie"],
                "zrodla_oczekiwane": q["expected_sources"], "zrodla_w_odpowiedzi": found,
                "pokrycie_zrodel": src_cov, "zdarzenia": events,
                "fallback_do_dokumentow": fallback, "pamiec_zaktualizowana": mem_upd,
            })

        total = sum(counts.values())
        stats[set_key] = {
            "plik": SET_FILES[set_key], "liczba_pytan": total, **counts,
            "dokladnosc_dobra": round(counts["dobra"] / total, 3) if total else 0.0,
            "fallback_count": sum(1 for r in results if r["zestaw"] == set_key and r["fallback_do_dokumentow"]),
            "memory_updates": sum(1 for r in results if r["zestaw"] == set_key and r["pamiec_zaktualizowana"]),
        }

    _write_outputs(results, stats)
    print(f"\nGotowe. Wyniki: {WYNIKI_DIR}")


def _write_outputs(results: list[dict], stats: dict) -> None:
    (WYNIKI_DIR / "wyniki.json").write_text(
        json.dumps({"wyniki": results, "statystyki": stats}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    icon = {"dobra": "✅", "czesciowa": "🟡", "zla": "❌", "blad_oceny": "⚠️"}
    lines = ["# Wyniki ewaluacji (self_learning_agents)\n"]
    for r in results:
        lines += [
            f"## [{r['id']}] (zestaw {r['zestaw']}) {icon.get(r['ocena'], '')} {r['ocena']}",
            f"**Pytanie:** {r['pytanie']}\n",
            f"**Oczekiwana:** {r['oczekiwana']}\n",
            f"**Odpowiedź agenta:** {r['odpowiedz_agenta']}\n",
            f"**Ocena:** {r['ocena']} — {r['uzasadnienie_oceny']}\n",
            f"**Zdarzenia:** {' → '.join(r['zdarzenia']) or 'brak'}\n",
            f"**Źródła:** oczekiwane {r['zrodla_oczekiwane']}; w odpowiedzi {r['zrodla_w_odpowiedzi']}; pokrycie {r['pokrycie_zrodel']}\n",
            "---\n",
        ]
    (WYNIKI_DIR / "odpowiedzi.md").write_text("\n".join(lines), encoding="utf-8")

    s = ["# Statystyki ewaluacji (self_learning_agents)\n",
         "| Zestaw | Plik | Pytań | Dobra | Częściowa | Zła | Dokładność | Fallback→dok. | Aktualizacje pamięci |",
         "|--------|------|------:|------:|----------:|----:|-----------:|--------------:|---------------------:|"]
    tot = {"liczba_pytan": 0, "dobra": 0, "czesciowa": 0, "zla": 0, "fallback_count": 0, "memory_updates": 0}
    for k, v in stats.items():
        s.append(f"| {k} | {v['plik']} | {v['liczba_pytan']} | {v['dobra']} | {v['czesciowa']} | "
                 f"{v['zla']} | {v['dokladnosc_dobra']:.0%} | {v['fallback_count']} | {v['memory_updates']} |")
        for key in tot:
            tot[key] += v.get(key, 0)
    acc = tot["dobra"] / tot["liczba_pytan"] if tot["liczba_pytan"] else 0
    s.append(f"| **Σ** | **wszystkie** | **{tot['liczba_pytan']}** | **{tot['dobra']}** | "
             f"**{tot['czesciowa']}** | **{tot['zla']}** | **{acc:.0%}** | **{tot['fallback_count']}** | "
             f"**{tot['memory_updates']}** |")
    (WYNIKI_DIR / "statystyki.md").write_text("\n".join(s) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
