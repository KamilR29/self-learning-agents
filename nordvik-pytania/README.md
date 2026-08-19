# Nordvik Finanse — zestawy pytań testowych (multi-hop retrieval)

Trzy zestawy pytań do zbioru dokumentów w [`../nordvik-dataset`](../nordvik-dataset).
Służą do testowania agenta AI wykonującego wyszukiwanie w dokumentach.

Każde pytanie ma format:
- **Pytanie** — treść zadania dla agenta,
- **Oczekiwana odpowiedź** — poprawna odpowiedź (ground truth),
- **Dokumenty źródłowe** — ID dokumentów, z których wynika odpowiedź (do oceny, czy agent trafił we właściwe źródła).

## Zestawy

| Plik | Poziom | Charakterystyka |
|------|--------|-----------------|
| [ZESTAW-1-jeden-dokument.md](ZESTAW-1-jeden-dokument.md) | łatwy | Odpowiedź w **jednym** dokumencie (retrieval pojedynczego faktu). |
| [ZESTAW-2-powiazania.md](ZESTAW-2-powiazania.md) | średni | Odpowiedź wymaga połączenia **2–3** dokumentów (multi-hop). |
| [ZESTAW-3-zlozone.md](ZESTAW-3-zlozone.md) | trudny | Odpowiedź **złożona**, syntetyzowana z **wielu** dokumentów, często z obliczeniami i rozumowaniem. |

> Wszystkie dane w dokumentach są fikcyjne/testowe. Odpowiedzi liczbowe wynikają
> z wartości zapisanych w zbiorze (spójnych i przeliczonych).
