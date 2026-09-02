

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).parent
OUT_DIR = ROOT / "eval-metryki"


RUNS: list[tuple[str, Path]] = [
    ("bazowy", ROOT / "eval-wyniki" / "wyniki.json"),
    ("samouczacy-1", ROOT / "eval-wyniki-advanced" / "wyniki1.json"),
    ("samouczacy-2", ROOT / "eval-wyniki-advanced" / "wyniki2.json"),
    ("samouczacy-3", ROOT / "eval-wyniki-advanced" / "wyniki3.json"),
    ("samouczacy-4", ROOT / "eval-wyniki-advanced" / "wyniki4.json"),
]

SETS = ["1", "2", "3"]
OCENA_SCORE = {"dobra": 1.0, "czesciowa": 0.5, "zla": 0.0}



def source_prf(found: list[str], expected: list[str]) -> tuple[float, float, float] | None:
    """Precyzja, czułość i F1 dla cytowanych ID źródeł. None, gdy brak wzorca."""
    f, e = set(found), set(expected)
    if not e:
        return None
    inter = len(f & e)
    prec = inter / len(f) if f else 0.0
    rec = inter / len(e)
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
    return prec, rec, f1


def _lcs_len(a: list[str], b: list[str]) -> int:
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def rouge_l(pred: str, ref: str) -> float:
    """ROUGE-L jako F1 na podstawie najdłuższego wspólnego podciągu tokenów."""
    p, r = pred.lower().split(), ref.lower().split()
    if not p or not r:
        return 0.0
    lcs = _lcs_len(p, r)
    prec, rec = lcs / len(p), lcs / len(r)
    return 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0


def _mean(xs: list[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0



def compute_similarity(rows: list[dict], embed_model: str) -> list[float]:
    """Cosinus embeddingów odpowiedzi i wzorca (odpowiednik RAGAS answer_similarity)."""
    from langchain_openai import OpenAIEmbeddings

    emb = OpenAIEmbeddings(model=embed_model)
    answers = [(r.get("odpowiedz_agenta") or " ") for r in rows]
    refs = [(r.get("oczekiwana") or " ") for r in rows]
    va = emb.embed_documents(answers)
    vr = emb.embed_documents(refs)
    sims = []
    for a, b in zip(va, vr):
        dot = sum(x * y for x, y in zip(a, b))
        na = math.sqrt(sum(x * x for x in a))
        nb = math.sqrt(sum(y * y for y in b))
        sims.append(dot / (na * nb) if na and nb else 0.0)
    return sims



def score_run(path: Path, use_similarity: bool, embed_model: str) -> dict:
    rows = json.loads(path.read_text(encoding="utf-8"))["wyniki"]
    sims = compute_similarity(rows, embed_model) if use_similarity else [None] * len(rows)

    for r, sim in zip(rows, sims):
        prf = source_prf(r.get("zrodla_w_odpowiedzi", []), r.get("zrodla_oczekiwane", []))
        r["_src_p"], r["_src_r"], r["_src_f1"] = prf if prf else (None, None, None)
        r["_rouge_l"] = rouge_l(r.get("odpowiedz_agenta", ""), r.get("oczekiwana", ""))
        r["_corr"] = OCENA_SCORE.get(r.get("ocena"))
        r["_as"] = sim

    def agg(subset: list[dict]) -> dict:
        return {
            "n": len(subset),
            "src_precision": _mean([r["_src_p"] for r in subset if r["_src_p"] is not None]),
            "src_recall": _mean([r["_src_r"] for r in subset if r["_src_r"] is not None]),
            "src_f1": _mean([r["_src_f1"] for r in subset if r["_src_f1"] is not None]),
            "rouge_l": _mean([r["_rouge_l"] for r in subset]),
            "correctness_judge": _mean([r["_corr"] for r in subset if r["_corr"] is not None]),
            "answer_similarity": _mean([r["_as"] for r in subset if r.get("_as") is not None]),
        }

    per_set = {sk: agg([r for r in rows if str(r["zestaw"]) == sk]) for sk in SETS}
    return {"ogolem": agg(rows), "zestawy": per_set}



def write_report(results: dict, use_similarity: bool) -> None:
    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "metryki.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    cols = ["src_precision", "src_recall", "src_f1", "rouge_l", "correctness_judge"]
    if use_similarity:
        cols += ["answer_similarity"]
    header = "| Przebieg | " + " | ".join(cols) + " |"
    sep = "|" + "---|" * (len(cols) + 1)

    lines = ["# Metryki offline (z zapisanych odpowiedzi)\n", "## Wyniki łączne (per przebieg)\n", header, sep]
    for label, res in results.items():
        o = res["ogolem"]
        lines.append("| " + label + " | " + " | ".join(f"{o[c]:.3f}" for c in cols) + " |")

    for sk in SETS:
        lines += [f"\n## Zestaw {sk} (per przebieg)\n", header, sep]
        for label, res in results.items():
            s = res["zestawy"][sk]
            lines.append("| " + label + " | " + " | ".join(f"{s[c]:.3f}" for c in cols) + " |")

    (OUT_DIR / "metryki.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--similarity", action="store_true", help="dolicz answer_similarity (embeddingi; wymaga OPENAI_API_KEY)")
    ap.add_argument("--embed", default="text-embedding-3-small", help="model embeddingów")
    args = ap.parse_args()

    if args.similarity:
        from dotenv import load_dotenv
        load_dotenv()

    results: dict[str, dict] = {}
    for label, path in RUNS:
        if not path.exists():
            print(f"[pomijam] brak pliku: {path}")
            continue
        print(f"[licze] {label}: {path.name}")
        results[label] = score_run(path, args.similarity, args.embed)

    write_report(results, args.similarity)
    print(f"\nGotowe. Metryki: {OUT_DIR}")


if __name__ == "__main__":
    main()
