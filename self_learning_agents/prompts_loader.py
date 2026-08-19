"""Ładowanie promptów z plików Markdown w folderze ``prompts/``.

Każdy agent/subagent ma własny plik ``prompts/<nazwa>.md``.
"""

from pathlib import Path
from functools import lru_cache

PROMPTS_DIR = Path(__file__).parent / "prompts"


@lru_cache(maxsize=None)
def load_prompt(name: str) -> str:
    """Wczytaj prompt z pliku ``prompts/<name>.md``.

    Args:
        name: Nazwa pliku bez rozszerzenia, np. ``"orchestrator"`` lub
            ``"research-agent"``.
    """
    path = PROMPTS_DIR / f"{name}.md"
    if not path.is_file():
        raise FileNotFoundError(f"Brak pliku promptu: {path}")
    return path.read_text(encoding="utf-8").strip()
