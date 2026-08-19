# Wyniki ewaluacji (self_learning_agents)

## [P1.1] (zestaw 1) ✅ dobra
**Pytanie:** Jaki jest numer PESEL (testowy) klientki Anny Katarzyny Kowalskiej?

**Oczekiwana:** 85072812345 (oznaczony jako testowy).

**Odpowiedź agenta:** Numer PESEL (testowy) klientki Anna Katarzyna Kowalska: 85072812345.

Źródła: KYC-00123; zapis do grafu: learned::2cff07f6449acde3.  
Uwaga: wcześniej w grafie występował wpis PESEL bez przypisanego źródła — po weryfikacji dodano zweryfikowany fakt (fact_id above) i zapisano wskazówkę jakościową (learning id: learning::7fb6ec3146f6715f).

**Ocena:** dobra — Odpowiedź agenta zawiera poprawny, testowy numer PESEL zgodny z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00123']; w odpowiedzi ['KYC-00123']; pokrycie 1.0

---

## [P1.2] (zestaw 1) ✅ dobra
**Pytanie:** Na jaką kwotę opiewa kredyt hipoteczny w umowie UM-7788?

**Oczekiwana:** 480 000,00 PLN.

**Odpowiedź agenta:** Kwota kredytu hipotecznego w umowie UM-7788 wynosi 480 000,00 PLN (źródło: UM-7788).

Zapisano zweryfikowany fakt do grafu wiedzy (fact_id: learned::a93a426d2cea181e) i dodano wskazówkę jakościową (learning_id: learning::f42c9ce3173d43d3). Weryfikacja: POTWIERDZONA (źródło: UM-7788).

**Ocena:** dobra — Odpowiedź agenta precyzyjnie podaje oczekiwaną kwotę kredytu hipotecznego zgodnie z pytaniem.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['UM-7788']; w odpowiedzi ['UM-7788']; pokrycie 1.0

---

## [P1.3] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi miesięczna rata w harmonogramie HS-7788?

**Oczekiwana:** 3 688,83 PLN (300 rat annuitetowych).

**Odpowiedź agenta:** Miesięczna rata w harmonogramie HS-7788 wynosi 3 688,83 PLN (raty annuitetowe). (źródło: HS-7788)

Fakt został zapisany do grafu wiedzy jako zweryfikowany: graph_id = learned::29f71397a237b072 (adnotacja: „zweryfikowano przez verifier; potwierdzona wartość raty miesięcznej”).

**Ocena:** dobra — Odpowiedź agenta zawiera dokładnie tę samą wartość miesięcznej raty oraz typ rat, co odpowiedź oczekiwana.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788']; w odpowiedzi ['HS-7788']; pokrycie 1.0

---

## [P1.4] (zestaw 1) ✅ dobra
**Pytanie:** Jaki jest maksymalny standardowy wskaźnik LTV według polityki ryzyka kredytowego?

**Oczekiwana:** 80% (standard; LTV 80–90% dopuszczalne wyjątkowo z dodatkowym zabezpieczeniem/ubezpieczeniem i wyższą marżą).

**Odpowiedź agenta:** Maksymalny standardowy wskaźnik LTV według Polityki Ryzyka Kredytowego wynosi do 80%.  
(źródła: POL-RYZYKO-01; graf-wiedzy ID: learned::d1448b7642e33700)

Potwierdzenie zapisu do grafu: zweryfikowany fakt "maksymalny_standardowy_LTV = ≤ 80%" został zapisany w grafie pod ID learned::d1448b7642e33700 i powiązany z dokumentem POL-RYZYKO-01.

Jeśli chcesz, mogę sprawdzić dokumenty pod kątem wyjątków/produktów, dla których obowiązują inne limity LTV.

**Ocena:** dobra — Odpowiedź agenta zgodnie wskazuje maksymalny standardowy LTV na poziomie 80%, co odpowiada oczekiwanej informacji.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['POL-RYZYKO-01']; w odpowiedzi ['POL-RYZYKO-01']; pokrycie 1.0

---

## [P1.5] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi wartość wskaźnika NRR 3M w tabeli oprocentowania na I kwartał 2025?

**Oczekiwana:** 5,85% w skali roku.

**Odpowiedź agenta:** Wartość wskaźnika NRR 3M w tabeli oprocentowania na I kwartał 2025 wynosi 5,85% rocznie (źródło: TO-2025-Q1).

Informuję również, że fakt został zapisany do grafu wiedzy (ID zapisu: learned::d29b278269f521a4).

**Ocena:** dobra — Odpowiedź agenta jest w pełni zgodna merytorycznie z oczekiwaną wartością wskaźnika NRR 3M wynoszącą 5,85% rocznie.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['TO-2025-Q1']; w odpowiedzi ['TO-2025-Q1']; pokrycie 1.0

---

## [P1.6] (zestaw 1) ✅ dobra
**Pytanie:** Jaka jest stawka prowizji przygotowawczej dla kredytu hipotecznego w tabeli opłat Q1 2025?

**Oczekiwana:** 2,00% kwoty kredytu.

**Odpowiedź agenta:** Stawka prowizji przygotowawczej dla kredytu hipotecznego w tabeli opłat Q1 2025 wynosi 2,00% kwoty kredytu (źródła: TOP-2025-Q1, REG-KH-02).

Uwaga dodatkowa: informacja została znaleziona w pamięci grafowej i zweryfikowana (verdict: POTWIERDZONA). Nie wykonano zapisu do grafu, ponieważ ten fakt był już wcześniej zapisany.

**Ocena:** dobra — Odpowiedź agenta dokładnie podaje tę samą merytoryczną wartość stawki prowizji przygotowawczej co odpowiedź oczekiwana.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['TOP-2025-Q1']; w odpowiedzi ['REG-KH-02', 'TOP-2025-Q1']; pokrycie 1.0

---

## [P1.7] (zestaw 1) ✅ dobra
**Pytanie:** Kto jest beneficjentem rzeczywistym (UBO) spółki „Bursztyn Handel Sp. z o.o."?

**Oczekiwana:** Andrzej Lewiński — 100% udziałów.

**Odpowiedź agenta:** Beneficjentem rzeczywistym (UBO) spółki „Bursztyn Handel Sp. z o.o.” jest Andrzej Lewiński — 100% udziałów (źródła: KYC-00129, SAR-0052).

Szczegóły i uwagi:
- Potwierdzenie w dokumentach:
  - KYC-00129 (data: 2025-06-11): "Beneficjent rzeczywisty (UBO): Andrzej Lewiński — 100% udziałów".
  - SAR-0052 (data: 2025-06-10): "UBO: Andrzej Lewiński (100% udziałów)".
- Uwaga dotycząca wcześniejszych wpisów: w grafie pierwotnie istniał wpis odwołujący się do UM-4523 i DN-1189 (ostatnia data w grafie: 2023-09-15), jednak te dokumenty nie znajdują się w repozytorium i nie zostały odnalezione podczas weryfikacji.
- Działania wykonane: na podstawie zweryfikowanych dokumentów (KYC-00129, SAR-0052) zapisano zweryfikowany fakt do grafu wiedzy oraz dodano jakościową wskazówkę (informacja o braku UM-4523/DN-1189 i preferencji użycia dokumentów KYC/SAR do potwierdzeń). Zapis do grafu został wykonany.

Jeśli chcesz, mogę przesłać pełne fragmenty dokumentów KYC-00129 i SAR-0052 lub poszukać kopii UM-4523/DN-1189.

**Ocena:** dobra — Odpowiedź agenta w pełni potwierdza kluczową informację oczekiwaną, wskazując konkretnie Andrzeja Lewińskiego jako beneficjenta rzeczywistego z 100% udziałów.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00129']; w odpowiedzi ['KYC-00129', 'SAR-0052', 'UM-4523']; pokrycie 1.0

---

## [P1.8] (zestaw 1) ✅ dobra
**Pytanie:** Jakie rozstrzygnięcie zapadło w decyzji kredytowej DC-2250?

**Oczekiwana:** Decyzja NEGATYWNA (odmowa udzielenia kredytu gotówkowego).

**Odpowiedź agenta:** Decyzja kredytowa DC-2250 była NEGATYWNA. (źródło: DC-2250, KYC-00456)

Główne przyczyny:
- Klasa ryzyka E (RR-0012)  
- Wzmożone środki AML / EDD (odniesienie do POL-AML-01)  
- Brak możliwości ustalenia źródła środków  
- Rekomendacja wstrzymania nowych produktów  
(źródła: DC-2250, KYC-00456, WN-4508, ZD-4508)

Powiązane dokumenty: WN-4508, ZD-4508, KYC-00456, DC-2250.

Zapis do grafu: zweryfikowany fakt dotyczący DC-2250 został zapisany w grafie jako learned::98abf89960ce2bd2 (potwierdzenie zapisu).

**Ocena:** dobra — Odpowiedź agenta potwierdza kluczowy fakt negatywnej decyzji kredytowej DC-2250, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250']; w odpowiedzi ['DC-2250', 'KYC-00456', 'POL-AML-01', 'RR-0012', 'WN-4508', 'ZD-4508']; pokrycie 1.0

---

## [P1.9] (zestaw 1) ✅ dobra
**Pytanie:** Jaki limit kredytowy przyznano na karcie kredytowej w decyzji DC-2204?

**Oczekiwana:** 15 000,00 PLN.

**Odpowiedź agenta:** W decyzji DC-2204 przyznano limit kredytowy na karcie w wysokości 15 000 PLN (data decyzji: 6 marca 2025 r.) (źródło: DC-2204).

Werdykt weryfikatora: POTWIERDZONA. Fakt był już dostępny w grafie; dodatkowo zapisano potwierdzenie do grafu (fact_id: learned::129f3da8ccc63a88) (źródło zapisu: DC-2204).

**Ocena:** dobra — Odpowiedź agenta zawiera poprawną kwotę limitu kredytowego zgodną z oczekiwaną odpowiedzią.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → WERYFIKUJĘ odpowiedź w dokumentach → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2204']; w odpowiedzi ['DC-2204']; pokrycie 1.0

---

## [P1.10] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi minimalna kwota do zapłaty w cyklu rozliczeniowym karty kredytowej „Nordvik Karta"?

**Oczekiwana:** 5% zadłużenia, nie mniej niż 50 PLN.

**Odpowiedź agenta:** Minimalna kwota do zapłaty w cyklu rozliczeniowym karty kredytowej „Nordvik Karta” wynosi 5% zadłużenia, nie mniej niż 50 PLN (źródło: REG-KK-03).

Zweryfikowałem informację i zapisałem ją do grafu wiedzy (fact_id: learned::5a50bb08d4f192a1). Dodałem też wskazówkę jakościową: poprzednie powiązanie tego faktu z UM-7788 było błędne — przy pytaniach o karty należy sprawdzać REG-KK-03 (Regulamin produktu — karta kredytowa) oraz powiązane tabele TO-2025-Q1 / TOP-2025-Q1.

**Ocena:** dobra — Odpowiedź agenta jest zgodna z oczekiwaną, podając minimalną kwotę do zapłaty jako 5% zadłużenia, nie mniej niż 50 PLN.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KK-03']; w odpowiedzi ['REG-KK-03', 'TO-2025-Q1', 'TOP-2025-Q1', 'UM-7788']; pokrycie 1.0

---

## [P1.11] (zestaw 1) ✅ dobra
**Pytanie:** Jak długi jest okres bezodsetkowy (grace period) karty kredytowej dla transakcji bezgotówkowych?

**Oczekiwana:** Do 56 dni (pod warunkiem spłaty całości zadłużenia w terminie).

**Odpowiedź agenta:** Ok. Oto odpowiedź:

- Okres bezodsetkowy (grace period) dla transakcji bezgotówkowych karty kredytowej „Nordvik Karta” wynosi 56 dni pod warunkiem spłaty całości zadłużenia w terminie.
- Wypłaty gotówki nie są objęte okresem bezodsetkowym — odsetki są naliczane od dnia transakcji.
- Minimalna kwota do zapłaty: 5% zadłużenia, nie mniej niż 50 PLN.

Źródła: REG-KK-03 (§3.1, §3.3, §4.1).  
Uwaga: fakt zapisano do grafu wiedzy (ID faktu: learned::b73b268cbe714a3b) oraz dodano wskazówkę jakościową (ID: learning::b73b268cbe714a3b).

**Ocena:** dobra — Odpowiedź agenta zawiera kluczową informację o 56-dniowym okresie bezodsetkowym przy spłacie całości zadłużenia, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KK-03']; w odpowiedzi ['REG-KK-03']; pokrycie 1.0

---

## [P1.12] (zestaw 1) ✅ dobra
**Pytanie:** Do jakiego podmiotu i jakiej jurysdykcji trafiały przelewy zagraniczne z rachunku w historii transakcji HT-00456?

**Oczekiwana:** Do „Vantia Global Trade LLC" w Republice Vantia (jurysdykcja wysokiego ryzyka); łącznie ok. 464 950,00 PLN.

**Odpowiedź agenta:** Przelewy zagraniczne z rachunku HT-00456 trafiały do podmiotu Vantia Global Trade LLC (siedziba: Republika Vantia) — kraj sklasyfikowany jako jurysdykcja wysokiego ryzyka; w historii są 5 przelewów SWIFT o łącznej wartości 464 950,00 PLN (źródło: HT-00456).

Weryfikacja: POTWIERDZONA (verifier) — rekomendowane źródło: HT-00456.

Graf przed zapytaniem: zawierał te informacje — tak.  
Zapis do grafu: wykonano. Do grafu dodano zweryfikowane fakty powiązane z HT-00456 (odbiorca, kraj/siedziba, jurysdykcja wysokiego ryzyka, liczba przelewów, łączna kwota) — zapis potwierdzony (źródło zapisu: HT-00456).

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe informacje z odpowiedzi oczekiwanej: podmiot, jurysdykcję wysokiego ryzyka oraz łączną kwotę przelewów z rachunku HT-00456.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HT-00456']; w odpowiedzi ['HT-00456']; pokrycie 1.0

---

## [P1.13] (zestaw 1) 🟡 czesciowa
**Pytanie:** Jaki średni miesięczny dochód netto potwierdza zaświadczenie ZD-4503?

**Oczekiwana:** 8 200,00 PLN (klientka Katarzyna Lewandowska, Nadmorskie Centrum Medyczne Sp. z o.o.).

**Odpowiedź agenta:** Zaświadczenie ZD-4503 potwierdza średni miesięczny dochód netto w wysokości 8 200,00 PLN (okres: sierpień 2024 – styczeń 2025). (źródło: ZD-4503, WN-4502)

Zapis do grafu wiedzy został wykonany: learned::87abf68bee1c9229.

**Ocena:** czesciowa — Agent poprawnie podał kwotę 8 200,00 PLN, ale nie wymienił klientki Katarzyny Lewandowskiej ani podmiotu Nadmorskie Centrum Medyczne Sp. z o.o., co jest częścią odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['ZD-4503']; w odpowiedzi ['WN-4502', 'ZD-4503']; pokrycie 1.0

---

## [P1.14] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi wartość wykupu przedmiotu leasingu we wniosku WN-4503?

**Oczekiwana:** 1% wartości = 1 800,00 PLN netto.

**Odpowiedź agenta:** Wartość wykupu przedmiotu leasingu we wniosku WN-4503 wynosi 1 800,00 PLN netto (źródło: WN-4503).  
Weryfikator: POTWIERDZONA.  
Zapis do grafu wykonany — fact ID: learned::1b1957a218ede577.

**Ocena:** dobra — Odpowiedź agenta zawiera poprawną wartość wykupu 1 800,00 PLN netto zgodnie z odpowiedzią oczekiwaną, pomijając jedynie procentową wartość, która jednak jest implikowana przez kwotę.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['WN-4503']; w odpowiedzi ['WN-4503']; pokrycie 1.0

---

## [P1.15] (zestaw 1) ✅ dobra
**Pytanie:** Jaki wewnętrzny próg alertu dla wpłat gotówkowych określa polityka AML?

**Oczekiwana:** 15 000 PLN (rozbijanie wpłat poniżej progu = structuring).

**Odpowiedź agenta:** Wewnętrzny próg alertu dla wpłat gotówkowych w polityce AML wynosi 15 000 PLN (źródło: POL-AML-01; wcześniejsza wzmianka w grafie: POL-AML-2023). Weryfikacja: POTWIERDZONA (sprawdzono: POL-AML-01). Zapis do grafu wykonany — fakt dodany jako learned::21a80bc32c3a7ea3.

**Ocena:** dobra — Odpowiedź agenta poprawnie podaje wewnętrzny próg alertu jako 15 000 PLN, zgodnie z polityką AML i oczekiwaną odpowiedzią.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['POL-AML-01']; w odpowiedzi ['POL-AML-01', 'POL-AML-2023']; pokrycie 1.0

---

## [P1.16] (zestaw 1) ✅ dobra
**Pytanie:** Jaka jest klasa ryzyka kredytowego klienta KL-00124 (Katarzyna Lewandowska)?

**Oczekiwana:** Klasa A (scoring 92/100), ryzyko niskie.

**Odpowiedź agenta:** Klasa ryzyka kredytowego klientki KL-00124 (Katarzyna Lewandowska) to A (najniższe ryzyko). Scoring 92/100 i wskaźnik DTI 13,23% potwierdzają niskie ryzyko; źródła: KYC-00124, DC-2202. (Zapisano do grafu: tak, encja: KL-00124)

**Ocena:** dobra — Odpowiedź agenta w pełni zgadza się z odpowiedzią oczekiwaną, podając tę samą klasę A, scoring 92/100 oraz niskie ryzyko; dodatkowe dane nie wpływają negatywnie na merytoryczną zgodność.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź

**Źródła:** oczekiwane ['KYC-00124']; w odpowiedzi ['DC-2202', 'KL-00124', 'KYC-00124']; pokrycie 1.0

---

## [P1.17] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi opłata roczna za kartę kredytową i kiedy jest znoszona?

**Oczekiwana:** 120,00 PLN; znoszona przy rocznym obrocie bezgotówkowym ≥ 12 000 PLN.

**Odpowiedź agenta:** Opłata roczna za kartę kredytową wynosi 120 PLN; jest znoszona przy rocznym obrocie bezgotówkowym co najmniej 12 000 PLN (źródło: TOP-2025-Q1).

Zapis do grafu: zweryfikowany fakt zapisano jako learned::4159bec9850b4e80, a wskazówkę jakościową zapisano jako learning::b951cbfda279ea8c. (Uwaga: wskazówka nie została automatycznie powiązana z istniejącym węzłem encji — warto zweryfikować encję „Karta kredytowa - opłata roczna”.)

**Ocena:** dobra — Odpowiedź agenta jest zgodna merytorycznie z oczekiwaną, podając te same kwoty i warunki zniesienia opłaty rocznej za kartę kredytową.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KK-03', 'TOP-2025-Q1']; w odpowiedzi ['TOP-2025-Q1']; pokrycie 0.5

---

## [P1.18] (zestaw 1) 🟡 czesciowa
**Pytanie:** Jakie oprocentowanie limitu w rachunku firmowym przyznano w decyzji DC-2205?

**Oczekiwana:** 12,50% w skali roku (zmienne); limit 50 000 PLN, prowizja za limit 1% rocznie = 500 PLN.

**Odpowiedź agenta:** Oprocentowanie limitu w rachunku firmowym przyznane w decyzji DC-2205 wynosi 12,50% w skali roku (źródło: DC-2205).

Zapis do grafu wiedzy wykonano: saved: true, node_id: learned::b12f3b0fb50a94f7.

**Ocena:** czesciowa — Agent podał prawidłowe oprocentowanie 12,50% w skali roku, ale pominął informacje o limicie 50 000 PLN i prowizji 1% rocznie.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2205']; w odpowiedzi ['DC-2205']; pokrycie 1.0

---

## [P2.1] (zestaw 2) ✅ dobra
**Pytanie:** Czy rata w harmonogramie HS-7788 jest zgodna z kwotą kredytu i oprocentowaniem z umowy oraz tabeli oprocentowania?

**Oczekiwana:** Tak. Umowa UM-7788: 480 000 PLN na 300 mies.; oprocentowanie 7,95% = NRR 3M 5,85% + marża 2,10% (TO-2025-Q1); rata annuitetowa 3 688,83 PLN — zgodna z HS-7788.

**Odpowiedź agenta:** Tak — rata 3 688,83 PLN w harmonogramie HS-7788 jest zgodna z parametrami umowy i tabeli oprocentowania.

Krótko:
- Parametry użyte do weryfikacji: kwota kredytu 480 000,00 PLN; oprocentowanie nominalne 7,95% rocznie (NRR 3M = 5,85% + marża = 2,10%); okres 300 rat; rodzaj rat: annuitetowe. (źródła: HS-7788, UM-7788, TO-2025-Q1)
- Metoda: rata annuitetowa (rata równa) obliczona dla miesięcznej stopy 0,0795/12 daje ratę 3 688,83 PLN — zgodnie ze szczegółowym harmonogramem spłat w HS-7788. (źródła: HS-7788, UM-7788, TO-2025-Q1)

Weryfikacja:
- Werdykt weryfikatora: POTWIERDZONA — wszystkie kluczowe wartości (kwota, oprocentowanie i jego składniki, okres, rodzaj rat oraz wysokość raty) są spójne między HS-7788, UM-7788 i TO-2025-Q1. (źródła: HS-7788, UM-7788, TO-2025-Q1)

Zapis do grafu (nauka):
- Zaktualizowałem graf wiedzy i zapisałem zweryfikowany fakt oraz wskazówkę jakościową dla encji HS-7788:
  - learned fact ID: learned::17929beaa7666751 — fakt: rata 3 688,83 PLN zgodna z parametrami (480 000 PLN; 7,95% = 5,85% NRR3M + 2,10% marża; 300 rat; raty annuitetowe). (źródła: HS-7788, UM-7788, TO-2025-Q1)
  - learning hint ID: learning::9ccd6259f0e92b70 — wskazówka: „Sprawdzać zgodność raty annuitetowej z NRR 3M + marżą; w obliczeniach użyto miesięcznej stopy 0,0795/12”. 

Użyte fakty / główne źródła:
- HS-7788: kwota 480 000,00 PLN; typ rat annuitetowe; rata w harmonogramie 3 688,83 PLN; okres 300 rat.
- UM-7788: potwierdzenie kwoty, okresu i rodzaju rat.
- TO-2025-Q1: NRR 3M = 5,85% i marża = 2,10% → oprocentowanie nominalne 7,95%.

Jeżeli chcesz, mogę pokazać szczegółowy rachunek (formuła annuitetowa i kroki obliczeń) lub wypisać fragmenty dokumentów potwierdzające poszczególne wartości.

**Ocena:** dobra — Odpowiedź agenta kompletnie i zgodnie z oczekiwaniami potwierdza zgodność raty 3 688,83 PLN z parametrami umowy i tabeli oprocentowania, podając wszystkie kluczowe wartości i ich poprawne źródła.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788', 'TO-2025-Q1', 'UM-7788']; w odpowiedzi ['HS-7788', 'TO-2025-Q1', 'UM-7788']; pokrycie 1.0

---

## [P2.2] (zestaw 2) ✅ dobra
**Pytanie:** Na podstawie której decyzji zawarto umowę UM-7788 i jaki wskaźnik DTI przyjęto w tej decyzji?

**Oczekiwana:** Decyzja DC-2201 (pozytywna); DTI = 36,52% (rata 3 688,83 / dochód netto 10 100).

**Odpowiedź agenta:** Umowa UM-7788 została zawarta na podstawie decyzji DC-2201; w tej decyzji przyjęto wskaźnik DTI = 36,52% (źródło: DC-2201, graf).

Informacja była dostępna w grafie; zweryfikowany fakt zapisano do grafu pod ID learned::0a0c72790fcb2932 i dodano jakościową wskazówkę powiązaną z encją UM-7788 o konieczności sprawdzania powiązań UM→DC oraz potwierdzania DTI (źródło: DC-2201, graf).

**Ocena:** dobra — Odpowiedź agenta w pełni zgadza się z oczekiwaną co do decyzji podstawowej (DC-2201) oraz wskaźnika DTI (36,52%).

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j) → odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź

**Źródła:** oczekiwane ['DC-2201', 'UM-7788']; w odpowiedzi ['DC-2201', 'UM-7788']; pokrycie 1.0

---

## [P2.3] (zestaw 2) ✅ dobra
**Pytanie:** Dlaczego wniosek WN-4508 został odrzucony, skoro klient miał wystarczającą zdolność kredytową?

**Oczekiwana:** Decyzja DC-2250 była negatywna nie z powodu zdolności (DTI 16,20% — akceptowalne), lecz z powodu klasy ryzyka E nadanej w raporcie RR-0012 na podstawie zgłoszeń SAR-0034 i SAR-0041 oraz braku możliwości ustalenia źródła środków (AML).

**Odpowiedź agenta:** Wniosek WN-4508 został odrzucony nie z powodu braku zdolności kredytowej, lecz z powodów związanych z AML/KYC: nadano klientowi wysoką klasę ryzyka (klasa E) i nie udało się wiarygodnie ustalić źródła środków, dlatego decyzja DC-2250 była odmowna mimo prawidłowej oceny finansowej (DTI 16,20%, scoring 66/100). Odrzucenie było więc skutkiem braków we weryfikacji dokumentacji, nie problemów z obsługą rat. (źródła: DC-2250, KYC-00456, WN-4508, ZD-4508)

Zapis do grafu wiedzy: fakt został dodany (ID: learned::b9bba2d0d3cc35c3) i zapisana została jakościowa wskazówka dotycząca procedury KYC/AML (ID: learning::e15688b2b4eb9af6).

**Ocena:** dobra — Odpowiedź agenta w pełni pokrywa kluczowe fakty z odpowiedzi oczekiwanej, wskazując na negatywną decyzję z powodu klasy ryzyka E, braku możliwości ustalenia źródła środków oraz akceptowalnej zdolności kredytowej (DTI 16,20%).

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250', 'RR-0012', 'WN-4508']; w odpowiedzi ['DC-2250', 'KYC-00456', 'WN-4508', 'ZD-4508']; pokrycie 0.67

---

## [P2.4] (zestaw 2) 🟡 czesciowa
**Pytanie:** Który regulamin i którą politykę powołuje decyzja kredytowa DC-2201?

**Oczekiwana:** Regulamin kredytu hipotecznego REG-KH-02 oraz Politykę ryzyka kredytowego POL-RYZYKO-01 (dodatkowo tabelę TO-2025-Q1 dla parametrów cenowych).

**Odpowiedź agenta:** Decyzja kredytowa DC-2201 powołuje:
- Regulamin produktu kredytowego REG-KH-02 (REG-KH-02),
- Politykę ryzyka kredytowego POL-RYZYKO-01 (POL-RYZYKO-01).

Informacja pochodzi z grafu wiedzy (relacje dla DC-2201) i została zweryfikowana w dokumentach — werdykt: POTWIERDZONA. Źródła: DC-2201, REG-KH-02, POL-RYZYKO-01.  
Graf już zawierał te powiązania, nie było potrzeby dopisywania nowego faktu.

**Ocena:** czesciowa — Odpowiedź agenta prawidłowo wskazuje regulamin i politykę, ale pomija tabelę TO-2025-Q1 wymienioną w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['DC-2201', 'POL-RYZYKO-01', 'REG-KH-02']; w odpowiedzi ['DC-2201', 'POL-RYZYKO-01', 'REG-KH-02']; pokrycie 1.0

---

## [P2.5] (zestaw 2) ✅ dobra
**Pytanie:** Jakie warunki postawiła decyzja warunkowa DC-2203 i w jaki sposób zostały spełnione w umowie leasingu UM-7790?

**Oczekiwana:** DC-2203 wymagała albo podwyższenia opłaty wstępnej do 30%, albo dodatkowego zabezpieczenia. W UM-7790 klient wybrał drugi wariant: ustanowił poręczenie cywilne Tomasza Górskiego oraz weksel własny in blanco, zachowując opłatę wstępną 20% (36 000 PLN); dostarczył też zaświadczenia ZUS/US.

**Odpowiedź agenta:** Odpowiedź (z dokumentów/grafu):

1) Warunek: poręczenie cywilne Tomasza Górskiego (alternatywnie podwyższenie opłaty wstępnej do 30%).
   - Spełnienie w UM-7790: umowa ustanawia poręczenie cywilne Tomasza Górskiego jako zabezpieczenie (zapis dotyczący zabezpieczeń w treści UM-7790). (źródło: DC-2203, UM-7790)

2) Warunek: weksel własny in blanco spółki z deklaracją wekslową.
   - Spełnienie w UM-7790: weksel własny in blanco wraz z deklaracją wekslową zostały przewidziane/ustanowione w UM-7790 (§ dotyczące zabezpieczeń). (źródło: DC-2203, UM-7790)

3) Warunek: dostarczenie zaświadczeń o niezaleganiu wobec ZUS i US (data w DC-2203).
   - Spełnienie w UM-7790: umowa potwierdza dostarczenie zaświadczeń o niezaleganiu; w grafie zapisano datę zaświadczeń 2025-03-14 wskazaną w dokumentach. (źródło: DC-2203, UM-7790)

4) Warunek: zawarcie umowy ubezpieczenia przedmiotu (AC/OC) z cesją na Finansującego przed wydaniem przedmiotu.
   - Spełnienie w UM-7790: UM-7790 wymaga i dokumentuje ubezpieczenie AC/OC z cesją na Finansującego; ubezpieczenie było zawarte przed wydaniem pojazdu (wydanie: 2025-03-25). (źródło: DC-2203, UM-7790)

Braki / uwagi:
- Nie stwierdzono brakujących szczegółów w grafie dla tego zapytania (wszystkie wymienione warunki i potwierdzenia ich spełnienia były dostępne). (źródło: graf/analiza dokumentów: DC-2203, UM-7790)

Zapis do grafu (nauka):
- Zweryfikowane fakty dotyczące DC-2203 oraz potwierdzenie ich spełnienia w UM-7790 zostały zapisane do grafu wiedzy (graph_add_learned_fact dla DC-2203 i UM-7790).
- Dodatkowo zapisana została krótkia wskazówka jakościowa powiązana z encją DC-2203: „Uwaga: decyzja dopuszcza alternatywę opłaty wstępnej 30% zamiast zabezpieczeń — sprawdzić w dokumentach, którą opcję wybrano; w grafie zapisać zawsze daty zaświadczeń i datę wydania przedmiotu”.
- Zapis zakończony powodzeniem; nie zgłoszono konfliktów ani duplikatów.

Podsumowanie: DC-2203 postawiła cztery główne warunki (poręczenie / alternatywa 30% opłaty wstępnej, weksel in blanco, zaświadczenia ZUS/US, ubezpieczenie AC/OC z cesją). UM-7790 dokumentuje spełnienie każdego z tych warunków zgodnie z powyższym. (źródło: DC-2203, UM-7790)

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe warunki decyzji DC-2203 oraz ich spełnienie w umowie UM-7790, zgodnie z oczekiwaną odpowiedzią, z dodatkiem szczegółów ubezpieczenia, które nie odbiegają od merytorycznej treści wymagań.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2203', 'UM-7790']; w odpowiedzi ['DC-2203', 'UM-7790']; pokrycie 1.0

---

## [P2.6] (zestaw 2) ✅ dobra
**Pytanie:** Jak zmieniła się rata kredytu hipotecznego UM-7788 po zmianie wskaźnika i co było przyczyną?

**Oczekiwana:** Rata spadła z 3 688,83 PLN na 3 531,88 PLN, ponieważ NRR 3M spadł z 5,85% (TO-2025-Q1) do 5,35% (TO-2025-Q2), co przy marży 2,10% dało oprocentowanie 7,45% zamiast 7,95%. Nowy harmonogram to HS-7794 (obowiązuje od raty nr 2).

**Odpowiedź agenta:** Odpowiedź:

Rata kredytu hipotecznego UM-7788 zmniejszyła się z 3 688,83 PLN do 3 531,88 PLN w kwietniu 2025 roku. Przyczyną była kwartalna aktualizacja wskaźnika NRR 3M — spadek NRR 3M z 5,85% do 5,35%, co obniżyło oprocentowanie kredytu z 7,95% do 7,45% i spowodowało aktualizację harmonogramu rat (bez konieczności aneksu). (źródło: UM-7788, HS-7788, HS-7794, TO-2025-Q1, TO-2025-Q2, REG-KH-02)

Zapis do grafu:
- Zweryfikowane fakty dotyczące UM-7788 zostały zapisane w grafie (ID faktów: learned::9085a128b4746d04, learned::8660e4e4a96b4a36, learned::5ea8f5879b3fb55a, learned::96425dd250243784).
- Dodano jakościową wskazówkę (ID: learning::c5c27d2c0c0d700b) powiązaną z UM-7788: „Uwaga: zmiany rat wynikają z kwartalnej aktualizacji NRR 3M; przy weryfikacji historycznych rat sprawdzać TO-2025-Q1/Q2 i HS-7794 dla daty wejścia w życie”.

Czy chcesz, żebym przesłał szczegółowy porównawczy harmonogram rat (przed i po) lub wskazał konkretne daty rat zmienionych w harmonogramie?

**Ocena:** dobra — Odpowiedź agenta poprawnie podaje zmiany raty, wskaźnika NRR 3M, oprocentowania oraz odniesienie do nowego harmonogramu HS-7794, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7794', 'REG-KH-02', 'TO-2025-Q2', 'UM-7788']; w odpowiedzi ['HS-7788', 'HS-7794', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'UM-7788']; pokrycie 1.0

---

## [P2.7] (zestaw 2) ✅ dobra
**Pytanie:** Którego klienta i na podstawie jakich zgłoszeń przeklasyfikowano do najwyższej klasy ryzyka (E)?

**Oczekiwana:** Klienta KL-00456 (Marek Nowicki, JDG „MN Trade"). Podstawa: zgłoszenia SAR-0034 (structuring) i SAR-0041 (pass-through) → raport ryzyka RR-0012 → aktualizacja karty KYC-00456 do klasy E.

**Odpowiedź agenta:** Klient Marek Andrzej Nowicki (client_id: KL-00456) został przeklasyfikowany do najwyższej klasy ryzyka (E) w dniu 2025-04-16 na podstawie zgłoszeń SAR-0034 i SAR-0041 (podejrzenia AML) oraz raportu RR-0012. (źródła: KYC-00456, SAR-0034, SAR-0041, RR-0012)

Fakt był dostępny w grafie wiedzy i został zweryfikowany — werdykt: POTWIERDZONA. Zapis do grafu nie był wymagany, ponieważ informacja już istniała.

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe fakty i liczby zgodne z odpowiedzią oczekiwaną, pomimo drobnych różnic w formacie nazwiska i dodaniu daty.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['KYC-00456', 'RR-0012', 'SAR-0034', 'SAR-0041']; w odpowiedzi ['KL-00456', 'KYC-00456', 'RR-0012', 'SAR-0034', 'SAR-0041']; pokrycie 1.0

---

## [P2.8] (zestaw 2) ✅ dobra
**Pytanie:** Jaka jest relacja między zaświadczeniem ZD-4501, wnioskiem WN-4501 i decyzją DC-2201?

**Oczekiwana:** ZD-4501 jest załącznikiem nr 1 do wniosku WN-4501 i potwierdza dochód netto 10 100 PLN; ten dochód został użyty w decyzji DC-2201 do wyliczenia wskaźnika DTI (36,52%).

**Odpowiedź agenta:** Relacje między dokumentami ZD-4501, WN-4501 i DC-2201:

- ZD-4501 jest załącznikiem nr 1 do wniosku WN-4501 — zaświadczenie stanowi integralny załącznik dostarczający informacje o dochodzie klienta (źródło: ZD-4501, WN-4501).
- WN-4501 jest wnioskiem rozstrzyganym przez decyzję DC-2201 — DC-2201 odnosi się bezpośrednio do rozpatrzenia wniosku WN-4501 (źródło: DC-2201, WN-4501).
- Dochód wykazany w ZD-4501 został użyty przy wyliczeniu wskaźnika DTI w decyzji DC-2201 — dane z zaświadczenia bezpośrednio wpłynęły na analizę zdolności kredytowej w DC-2201 (źródło: DC-2201, ZD-4501).
- Dodatkowo, DC-2201 odwołuje się w treści do następujących dokumentów: WN-4501, KYC-00123, ZD-4501, POL-RYZYKO-01, REG-KH-02, TO-2025-Q1, UM-7788 (źródło: DC-2201).

Uwaga o grafie wiedzy: pierwotnie graf nie zawierał bezpośrednich relacji między DC-2201 a ZD-4501/WN-4501. Po weryfikacji zapisano te relacje do grafu (ID zapisów: learned::b8232335d72e89ec — ROZSTRZYGA DC-2201 -> WN-4501; learned::a480bfff311a88e4 — UŻYWA_DOCHOD_Z DC-2201 -> ZD-4501) oraz dodano wskazówkę jakościową learning::ce211b21bb12a110 przypisaną do DC-2201 (źródła: DC-2201, WN-4501, ZD-4501).

Jeśli chcesz, mogę teraz odczytać i streścić dodatkowe dokumenty wymienione w DC-2201 (np. KYC-00123, POL-RYZYKO-01, REG-KH-02, TO-2025-Q1, UM-7788).

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe elementy relacji między dokumentami wymienione w odpowiedzi oczekiwanej, w tym rolę ZD-4501 jako załącznika do WN-4501, wykorzystanie dochodu z ZD-4501 w decyzji DC-2201 oraz wyliczenie wskaźnika DTI na poziomie 36,52%.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'WN-4501', 'ZD-4501']; w odpowiedzi ['DC-2201', 'KYC-00123', 'POL-RYZYKO-01', 'REG-KH-02', 'TO-2025-Q1', 'UM-7788', 'WN-4501', 'ZD-4501']; pokrycie 1.0

---

## [P2.9] (zestaw 2) ✅ dobra
**Pytanie:** Ile wynosi rata leasingowa netto i brutto oraz z czego wynika różnica?

**Oczekiwana:** Rata netto 3 586,87 PLN, brutto 4 411,85 PLN; różnica to VAT 23% doliczany do raty leasingu.

**Odpowiedź agenta:** Rata leasingowa wynosi:
- netto: 3 586,87 PLN (źródło: HS-7790, UM-7790)
- brutto: 4 411,85 PLN (źródło: HS-7790, UM-7790)

Różnica i jej przyczyna:
- Kwota VAT: 824,98 PLN (4 411,85 − 3 586,87 = 824,98 PLN) — VAT naliczony w wysokości 23% (źródło: HS-7790, UM-7790).
- Wyjaśnienie: różnica wynika z doliczenia podatku VAT (23%) do raty netto; netto to część kapitałowa i odsetkowa raty, a brutto to ta sama kwota powiększona o VAT.

Dodatkowe istotne składniki umowy (źródła: HS-7790, UM-7790):
- wartość przedmiotu (netto): 180 000,00 PLN
- opłata wstępna (netto): 36 000,00 PLN (20%)
- wartość wykupu (netto): 1 800,00 PLN
- okres: 48 miesięcy
- stopa leasingowa: 9,05% w skali roku

Cytaty:
- „Rata leasingowa: 3 586,87 PLN netto (4 411,85 PLN brutto z VAT 23%)” (HS-7790)
- „Wartość przedmiotu netto: 180 000,00 PLN” (HS-7790)
- „Wartość wykupu: 1 800,00 PLN netto” (UM-7790)

Informuję też, że powyższe, zweryfikowane fakty zostały zapisane do grafu wiedzy (encja: rata_leasingowa_KL-00125) na podstawie dokumentów HS-7790 i UM-7790. Jeśli chcesz, mogę pokazać harmonogram rat (rozbicie część kapitałowa/odsetkowa) lub obliczenia potwierdzające kwoty.

**Ocena:** dobra — Odpowiedź agenta podaje dokładne kwoty rat netto i brutto zgodne z oczekiwaniami oraz poprawnie wyjaśnia, że różnicę stanowi VAT 23%, zawierając dodatkowe szczegóły potwierdzające zgodność merytoryczną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7790', 'UM-7790']; w odpowiedzi ['HS-7790', 'UM-7790']; pokrycie 1.0

---

## [P2.10] (zestaw 2) ✅ dobra
**Pytanie:** Czy profil ryzyka klienta KL-00124 jest zgodny z pozytywnym rozstrzygnięciem decyzji DC-2202?

**Oczekiwana:** Tak. KYC-00124: klasa A, scoring 92/100, brak zobowiązań; DC-2202: DTI 13,23%, spełnione kryteria POL-RYZYKO-01 — decyzja pozytywna spójna z profilem.

**Odpowiedź agenta:** Tak — profil ryzyka klienta KL-00124 jest zgodny z pozytywnym rozstrzygnięciem decyzji DC-2202.

Kluczowe fakty (źródła):
- Klasyfikacja ryzyka: A (źródło: KYC-00124).
- Scoring: 92 (źródło: KYC-00124).
- DTI: 13,23% (źródło: KYC-00124).
- Zgodność z polityką POL-RYZYKO-01 potwierdzona (źródło: POL-RYZYKO-01, DC-2202).
- Decyzja pozytywna: DC-2202 (źródło: DC-2202).
- Powiązana decyzja warunkowa: DC-2203 (wskazana we wskazówkach) (źródło: DC-2203).

Status grafu i zapis:
- Fakt był już obecny w grafie (found: true).
- Na podstawie tej weryfikacji zapisałem do grafu zweryfikowany fakt (ID: learned::132c8e88ecd6a3f0) oraz wskazówkę jakościową dotycząca KL-00124 (ID: learning::77e733405686e7c6).

Źródła: KYC-00124, DC-2202, POL-RYZYKO-01, DC-2203.

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe fakty i liczby zgodne z odpowiedzią oczekiwaną, w tym klasę A, scoring 92, DTI 13,23% oraz potwierdzenie zgodności z polityką POL-RYZYKO-01 i pozytywną decyzję DC-2202.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2202', 'KYC-00124', 'POL-RYZYKO-01']; w odpowiedzi ['DC-2202', 'DC-2203', 'KL-00124', 'KYC-00124', 'POL-RYZYKO-01']; pokrycie 1.0

---

## [P2.11] (zestaw 2) ✅ dobra
**Pytanie:** Kto jest kredytobiorcą w umowie UM-7789, jaki jest cel kredytu i na jaki rachunek następuje spłata?

**Oczekiwana:** Katarzyna Maria Lewandowska (KL-00124); cel: remont mieszkania; rachunek spłaty (testowy) PL33 9999 1000 0000 0077 8900 0002.

**Odpowiedź agenta:** Odpowiedź:

- Kredytobiorca: Katarzyna Maria Lewandowska, PESEL 90111067321.  
  Potwierdzenie: „Umowa kredytu ... pomiędzy Nordvik Finanse S.A. a Katarzyną Marią Lewandowską PESEL 90111067321” (źródło: UM-7789; dodatkowo KYC-00124).

- Cel kredytu: remont mieszkania.  
  Potwierdzenie: „cel: remont mieszkania” (źródło: UM-7789; potwierdzenie w decyzji DC-2202).

- Rachunek do spłaty: PL33 9999 1000 0000 0077 8900 0002.  
  Potwierdzenie: „rachunek spłaty PL33 9999 1000 0000 0077 8900 0002” (źródło: UM-7789; harmonogram HS-7789).

Dodatkowe informacje o procesie (meta):
- Przy pierwszym sprawdzeniu grafu pamięci znaleziono jedynie dane kredytobiorcy; cel kredytu i rachunek spłaty nie były w grafie.  
- Po weryfikacji w dokumentach (UM-7789, HS-7789, DC-2202, KYC-00124) zapisano do grafu zweryfikowane fakty (borrower, purpose, repayment_account) oraz dodano wskazówkę jakościową: „Graf początkowo nie zawierał tych danych; wcześniejsza, niezweryfikowana odpowiedź pomieszała dane z UM-7788. Przy odpowiadaniu sprawdzać zgodność numeru umowy i powiązanych HS/DC/KYC.” Operacje zapisu wykonano pomyślnie (graph_add_learned_fact + graph_add_learning).

Źródła: UM-7789, HS-7789, DC-2202, KYC-00124.

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe fakty i liczby zgodne z odpowiedzią oczekiwaną: identycznego kredytobiorcę, cel kredytu oraz rachunek spłaty.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00124', 'UM-7789']; w odpowiedzi ['DC-2202', 'HS-7789', 'KYC-00124', 'UM-7788', 'UM-7789']; pokrycie 1.0

---

## [P2.12] (zestaw 2) 🟡 czesciowa
**Pytanie:** Które oprocentowanie zastosowano w kredycie gotówkowym z wniosku WN-4506 i skąd ono pochodzi?

**Oczekiwana:** 10,90% stałe (przedział 20 001–60 000 PLN) — z tabeli TO-2025-Q2 (wniosek złożony w Q2 2025). Rata 980,74 PLN dla 30 000 PLN na 36 mies.

**Odpowiedź agenta:** Oprocentowanie zastosowane w kredycie gotówkowym z wniosku WN-4506 wynosi 10,90% — wartość pochodzi bezpośrednio z wniosku WN-4506 i jest potwierdzona przez decyzję DC-2206 (źródła: WN-4506, DC-2206).

Werdykt weryfikatora: POTWIERDZONA.

Surowe dane zapisane/wykorzystane:
- {fact: "oprocentowanie kredytu gotówkowego", value: "10,90%", related_entity: "WN-4506", source_doc_id: "WN-4506"}

Zapis do grafu wiedzy: wykonany — fakt zapisano jako learned::d09f06ae127e56a2 (nota: „Zapisano nauczony fakt o oprocentowaniu kredytu gotówkowego 10,90%, powiązany z encjami WN-4506 i DC-2206”).

**Ocena:** czesciowa — Agent podał prawidłową wartość oprocentowania 10,90% oraz źródła, ale pominął informację o stałym oprocentowaniu, przedziale kwotowym, tabeli TO-2025-Q2 oraz wysokości raty i okresie spłaty.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2206', 'TO-2025-Q2', 'WN-4506']; w odpowiedzi ['DC-2206', 'WN-4506']; pokrycie 0.67

---

## [P2.13] (zestaw 2) ✅ dobra
**Pytanie:** Czym różnią się dwie historie transakcji (HT-00123 i HT-00456) i jakie skutki compliance z nich wynikły?

**Oczekiwana:** HT-00123 (KL-00123) to normalny profil detaliczny (wynagrodzenie, spłata raty, wydatki bytowe) — brak przesłanek AML. HT-00456 (KL-00456) wykazuje structuring i transfery pass-through do jurysdykcji wysokiego ryzyka — skutkuje zgłoszeniami SAR-0034/0041.

**Odpowiedź agenta:** Krótko — główne różnice i skutki compliance:

1) HT-00123 to historia rachunku osobistego z regularnymi wpływami wynagrodzenia, spłatami rat kredytu hipotecznego i wydatkami typowymi dla klienta detalicznego; w analizie AML nie stwierdzono nieprawidłowości i nie zainicjowano zgłoszeń SAR (źródło: HT-00123).  
2) W HT-00123 odnotowano też zmianę wysokości raty kredytu od kwietnia 2025 (zmiana wynikająca ze zmiany stopy/repricingu) — zmiana widoczna w harmonogramie płatności (źródło: HT-00123).  
3) HT-00456 dotyczy rachunku firmowego (JDG) z licznymi rozbitymi wpłatami gotówkowymi (~54 wpłaty po 9,4–9,9k PLN) oraz serią dużych przelewów SWIFT do Republiki Vantia (pass‑through) — typologia wskazuje structuring i pass‑through (źródło: HT-00456).  
4) W oparciu o HT-00456 przygotowano zgłoszenia SAR-0034 (structuring) i SAR-0041 (transfery pass‑through) oraz sporządzono raport ryzyka RR-0012 (źródła: SAR-0034, SAR-0041, RR-0012).  
5) RR-0012 sklasyfikował klienta z HT-00456 jako wysokiego ryzyka (klasa E), rekomendując EDD, wzmożony monitoring oraz wstrzymanie udzielania nowych produktów kredytowych, a także rozważenie zakończenia relacji; raport wpłynął na decyzje kredytowe powiązane z tym klientem (źródło: RR-0012).  
6) Skutki compliance: HT-00123 — brak działań AML/Brak SAR; HT-00456 — eskalacja do zespołu AML, zgłoszenia SAR, raport ryzyka i rekomendowane restrykcje produktowe oraz wpływ na decyzję kredytową (WN-4508 / DC-2250) (źródła: HT-00123; HT-00456; SAR-0034; SAR-0041; RR-0012).

Informacja o nauce (zapis do grafu): zweryfikowane fakty zapisano do grafu wiedzy: (a) dla HT-00456 — wynik: wygenerowano SAR-0034 i SAR-0041 oraz raport RR-0012 z rekomendacjami (reklasyfikacja do klasy E, EDD, wstrzymanie nowych produktów, wpływ na DC-2250/WN-4508); (b) dla HT-00123 — wynik: brak nieprawidłowości AML, normalny profil detaliczny; (c) dla HT-00456 — ekspozycje/kwoty (ok. 470k PLN rozbite, SWIFT 464 950,00 PLN). Dodano też jakościowe wskazówki (learnings) dla HT-00456 i HT-00123 dotyczące kryteriów eskalacji i weryfikacji rat (zapis wykonany na podstawie dokumentów HT-00123, HT-00456, SAR-0034, SAR-0041, RR-0012).  

Jeśli chcesz, mogę: (1) pokazać wybrane cytaty z poszczególnych dokumentów, (2) sprawdzić dokument decyzji kredytowej DC-2250 / WN-4508 dla szczegółów odmowy.

**Ocena:** dobra — Odpowiedź agenta w pełni odzwierciedla kluczowe fakty i liczby z odpowiedzi oczekiwanej, uwzględniając różnice w profilach HT-00123 i HT-00456 oraz ich konsekwencje compliance, w tym SAR i raporty ryzyka.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HT-00123', 'HT-00456', 'SAR-0034', 'SAR-0041']; w odpowiedzi ['DC-2250', 'HT-00123', 'HT-00456', 'RR-0012', 'SAR-0034', 'SAR-0041', 'WN-4508']; pokrycie 1.0

---

## [P2.14] (zestaw 2) ✅ dobra
**Pytanie:** Jakie zabezpieczenia ustanowiono dla kredytu hipotecznego UM-7788 i jak mają się one do wymogów polityki ryzyka?

**Oczekiwana:** Hipoteka umowna do 720 000 PLN (150% kwoty), cesja z polisy ubezpieczenia nieruchomości, ubezpieczenie pomostowe do wpisu hipoteki — zgodne z wymogiem zabezpieczenia hipotecznego z POL-RYZYKO-01 §4.

**Odpowiedź agenta:** Odpowiedź w oparciu o dokumenty i graf wiedzy:

1) Jakie zabezpieczenia ustanowiono dla kredytu UM-7788
- Hipoteka umowna do kwoty 720 000,00 PLN (150% kwoty kredytu) na nieruchomości wpisanej w KW GD1Y/00099999/9 (źródło: UM-7788 §6.1; DC-2201 §V.2).
- Cesja praw z polisy ubezpieczenia nieruchomości od ognia i zdarzeń losowych na rzecz Banku (źródło: UM-7788 §6.2; DC-2201 §V.3).
- Ubezpieczenie pomostowe obowiązujące do dnia prawomocnego wpisu hipoteki; w umowie wskazano, że wpis nastąpił przed uruchomieniem kredytu (źródło: UM-7788 §6.3; DC-2201 §V.4).
(źródła: UM-7788, DC-2201, HS-7788)

2) Jak to ma się do wymogów polityki ryzyka (POL-RYZYKO-01)
- POL-RYZYKO-01 wymaga jako zabezpieczenia podstawowego wpisanej hipoteki oraz – do czasu wpisu – ubezpieczenia pomostowego; dodatkowo limit standardowy LTV = 80% (źródło: POL-RYZYKO-01 §4).
- W UM-7788: kwota kredytu 480 000,00 PLN (UM-7788 §1.1), hipoteka ustanowiona do 720 000,00 PLN (150% kredytu) => zabezpieczenie hipoteczne przewyższa wymóg (720 000 / 480 000 = 150% → LTV ≤ 80%). W związku z tym zabezpieczenia spełniają wymagania POL-RYZYKO-01 (wymóg hipoteki wpisanej + ubezpieczenie pomostowe do wpisu) (źródła: UM-7788, POL-RYZYKO-01, DC-2201).
- Weryfikator ocenił zgodność jako POTWIERDZONĄ (źródła: UM-7788, DC-2201, HS-7788, POL-RYZYKO-01).

3) Braki / rekomendacje
- W grafie (przed uzupełnieniem) brakowało potwierdzenia numeru polisy ubezpieczenia nieruchomości oraz zapisu jednoznacznego dowodu prawomocnego wpisu hipoteki. UM-7788 jednak stwierdza, że wpis nastąpił przed uruchomieniem; numer polisy nadal niezweryfikowany w dokumentach przeglądanych do tej pory (źródło: UM-7788).
- Rekomendacja: pozyskać dokument polisy/cesji z numerem polisy i (jeśli konieczne) wyciąg z KW potwierdzający prawomocny wpis hipoteki, a następnie dodać numer polisy do grafu.

4) Zapis w grafie (nauka)
- Ponieważ te informacje nie były wcześniej kompletne w grafie, zapisałem do grafu zweryfikowane fakty dotyczące UM-7788:
  1. Hipoteka umowna do 720 000,00 PLN na KW GD1Y/00099999/9.
  2. Cesja praw z polisy ubezpieczenia nieruchomości jako zabezpieczenie.
  3. Ubezpieczenie pomostowe obowiązuje do prawomocnego wpisu; wpis dokonany przed uruchomieniem kredytu.
  4. Kwota kredytu: 480 000,00 PLN; hipoteka = 150% kwoty kredytu → LTV ≤ 80%.
- Dodałem także jakościową wskazówkę: brak numeru polisy w grafie — pozyskać dokument polisy i zapisać numer.
(Operacje zapisu wykonane: graph_add_learned_fact x4 oraz graph_add_learning dla UM-7788; źródła użyte: UM-7788, DC-2201, POL-RYZYKO-01.)

Jeśli chcesz, mogę:
- Poszukać i dołączyć numer polisy oraz/lub wyciąg z KW (jeżeli są w repozytorium dokumentów), 
- Przygotować krótką checklistę dokumentów potrzebnych do ostatecznego zamknięcia warunków uruchomienia.

**Ocena:** dobra — Odpowiedź agenta precyzyjnie odpowiada na pytanie, podając wszystkie kluczowe zabezpieczenia (hipoteka do 720 000 PLN jako 150% kwoty, cesję polisy, ubezpieczenie pomostowe) oraz potwierdzając ich zgodność z wymogami polityki ryzyka POL-RYZYKO-01 §4.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['POL-RYZYKO-01', 'UM-7788']; w odpowiedzi ['DC-2201', 'HS-7788', 'POL-RYZYKO-01', 'UM-7788']; pokrycie 1.0

---

## [P3.1] (zestaw 3) ✅ dobra
**Pytanie:** Prześledź kompletny łańcuch kredytu hipotecznego Anny Kowalskiej — od profilu klienta do harmonogramu — i zweryfikuj spójność kluczowych liczb.

**Oczekiwana:** - Łańcuch: KYC-00123 → WN-4501 → (załącznik ZD-4501) → DC-2201 → UM-7788 → HS-7788.
  - Klient klasy B (scoring 78), dochód netto 10 100 PLN (ZD-4501).
  - Kredyt 480 000 PLN, nieruchomość warta 600 000 PLN → **LTV 80%**; wkład własny 120 000 PLN.
  - Oprocentowanie 7,95% (NRR 3M 5,85% + marża 2,10%, TO-2025-Q1); **rata 3 688,83 PLN** na 300 mies.
  - **DTI 36,52%** (3 688,83 / 10 100) < limit 45% (POL-RYZYKO-01) → decyzja pozytywna.
  - Prowizja 9 600 PLN (2%, TOP-2025-Q1), RRSO 8,50%, suma odsetek 626 649,94 PLN.
  - Liczby są spójne w całym łańcuchu.

**Odpowiedź agenta:** Podsumowanie wykonanych kroków i wyników (konkretne fakty oparte WYŁĄCZNIE na dokumentach/grafie):

1) Przeszukanie grafu i dokumentów
- Graf zawierał dokumenty KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789, ale wszystkie odnoszą się do klienta o nazwie Katarzyna Maria Lewandowska (owner KL-00124), nie do Anny Kowalskiej (źródła: KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789). (wynik weryfikatora: NIEPOTWIERDZONA)

2) Skrócone streszczenie dokumentów i kluczowe liczby (pozycja — najważniejsze liczby; źródło):
- KYC-00124: profil klienta — dochód netto 8 200,00 PLN (KYC-00124).
- WN-4502 (wniosek): kwota kredytu 50 000,00 PLN; okres 60 miesięcy; oprocentowanie nominalne 10,90% w skali roku; prowizja 2 000,00 PLN (4,00%); miesięczna rata 1 084,63 PLN; typ spłaty równe (annuitetowe). (WN-4502; rata także w HS-7789)
- DC-2202 (decyzja): DTI 13,23%; scoring (dokument) powiązany z KL-00124. (DC-2202)
- UM-7789 (umowa): data pierwszej płatności 2025-04-10. (UM-7789)
- HS-7789 (harmonogram): miesięczna rata 1 084,63 PLN, typ spłaty annuitet. (HS-7789)

3) Ocena spójności kluczowych liczb
- Dla klienta wskazanego w dokumentach (Katarzyna Maria Lewandowska / KL-00124) — kluczowe liczby są wewnętrznie spójne między dokumentami: kwota 50 000 PLN, okres 60 mies., oprocentowanie 10,90%, prowizja 2 000 PLN (4%), rata 1 084,63 PLN, typ annuitet, data pierwszej płatności 10.04.2025 (źródła: WN-4502, HS-7789, UM-7789, DC-2202, KYC-00124).
- Dla osoby Anna Kowalska — brak dokumentów potwierdzających jakiekolwiek elementy łańcucha kredytu o takim kliencie pod podanymi ID. Zatem nie można potwierdzić spójności dla Anny Kowalskiej.

4) Niespójności / problemy istotne dla zadania
- Najważniejsza rozbieżność: dokumenty przypisane wcześniej do Anny Kowalskiej należą faktycznie do Katarzyny Marii Lewandowskiej (KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789). (źródła: odczyt dokumentów)
- W proponowanej (pierwotnej) odpowiedzi pojawiły się wartości dla „Anny Kowalskiej” takie jak: dochód 10 100 PLN, kwota 480 000 PLN, okres 300 mies., oprocentowanie 7,95%, NRR 3M 5,85%, prowizja 9 600 PLN, rata 3 688,83 PLN, data pierwszej płatności 15.03.2025 — ŻADNE z tych wartości nie zostały potwierdzone w dokumentach powiązanych z klientem KL-00124 (zamiast tego dokumenty zawierają wartości wymienione w pkt.2). (porównanie: WN-4502, DC-2202, HS-7789)
- Brak w dokumentach dla KL-00124 odrębnych pól „marża” i „NRR 3M” — kredyt jest opisany jako oprocentowanie nominalne stałe 10,90%, bez rozbicia na marżę + indeks. (WN-4502, DC-2202)

5) Działania wykonane w grafie (moment nauki)
- Zapisano zweryfikowane fakty do grafu (graph_add_learned_fact):
  - KYC-00124, właściciel: Katarzyna Maria Lewandowska (KL-00124).
  - Dochód netto 8 200 PLN (KYC-00124).
  - Kwota kredytu 50 000 PLN (WN-4502).
  - Okres 60 miesięcy (WN-4502).
  - Oprocentowanie nominalne 10,90% (WN-4502).
  - Prowizja 2 000 PLN (4,00%) (WN-4502).
  - Miesięczna rata 1 084,63 PLN (WN-4502 / HS-7789).
  - Typ spłaty: annuitet (WN-4502 / HS-7789).
  - DTI 13,23% (DC-2202).
  - Data pierwszej płatności 2025-04-10 (UM-7789).
- Zapisano także fakt uczący: „Nie znaleziono dokumentów powiązanych z klientem Anna Kowalska o podanych ID; wcześniejsze przypisanie było błędne.” (graph_add_learned_fact).
- Dodano jakościową wskazówkę (graph_add_learning) powiązaną z KYC-00124: "Uwaga: wcześniej źródła były błędnie przypisane do innego klienta (Anna Kowalska). Przy pobieraniu danych zweryfikować zgodność nazwiska i identyfikatora klienta (owner ID)."

Potwierdzenie: zapisy do grafu wykonane (fakty i wskazówka są teraz w grafie).

6) Wnioski i następne kroki (co mogę dalej zrobić)
- Jeśli Twoim celem było prześledzenie łańcucha kredytu Anny Kowalskiej — obecnie brak dokumentów dla tej klientki pod przeszukiwanymi ID; proszę podaj dodatkowe identyfikatory (PESEL, numer klienta, inny ID dokumentu) lub zezwól na przeszukanie całej bazy po nazwisku „Anna Kowalska”.
- Jeśli potrzebujesz pełnego, szczegółowego porównania obliczeń rat (np. weryfikacja metodologii obliczenia raty 1 084,63 PLN), mogę przeprowadzić szczegółowe obliczenia amortyzacji na podstawie zapisanych parametrów (zapisane w grafie) i zweryfikować krok po kroku.

Główne źródła (ID): KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789.

Jeżeli chcesz, szukam teraz dokumentów bez założeń ID dla klientki „Anna Kowalska” lub kontynuuję analizę obliczeń dla klientki KL-00124. Co preferujesz?

**Ocena:** dobra — Odpowiedź Agenta poprawnie wskazuje na brak dokumentów dotyczących Anny Kowalskiej i precyzyjnie przedstawia fakty dotyczące innego klienta, co jest zgodne z weryfikacją merytoryczną podaną w pytaniu.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'HS-7788', 'KYC-00123', 'POL-RYZYKO-01', 'REG-KH-02', 'TO-2025-Q1', 'TOP-2025-Q1', 'UM-7788', 'WN-4501', 'ZD-4501']; w odpowiedzi ['DC-2202', 'HS-7789', 'KL-00124', 'KYC-00124', 'UM-7789', 'WN-4502']; pokrycie 0.0

---

## [P3.2] (zestaw 3) 🟡 czesciowa
**Pytanie:** Wyjaśnij, w jaki sposób działania compliance doprowadziły do odmowy kredytu Markowi Nowickiemu — od transakcji do decyzji. Wskaż całą sekwencję.

**Oczekiwana:** - Rachunek firmowy (HT-00456) wykazał wpłaty gotówkowe rozbijane poniżej progu 15 000 PLN (structuring) i szybkie transfery ~464 950 PLN do Vantia (pass-through).
  - Powstały zgłoszenia SAR-0034 (structuring) i SAR-0041 (pass-through), oba na podstawie POL-AML-01.
  - Raport ryzyka RR-0012 zagregował oba SAR-y i rekomendował klasę E oraz wstrzymanie nowych kredytów.
  - Kartę KYC-00456 zaktualizowano do klasy E (WYSOKIE), wdrożono EDD.
  - Kolejny wniosek WN-4508 (kredyt 80 000 PLN) otrzymał decyzję **negatywną DC-2250** — mimo DTI 16,20% — z powodu klasy E i braku możliwości ustalenia źródła środków.
  - To pełna pętla zwrotna: transakcje → ryzyko → odmowa.

**Odpowiedź agenta:** Krótko: odmowa kredytu była wynikiem procesu compliance — wykrycia podejrzanych transakcji (structuring i transfery pass‑through) i braku wiarygodnego źródła środków, co podwyższyło klasę ryzyka klienta do „E”, nałożono EDD i rekomendowano wstrzymanie nowych produktów; w efekcie Komitet Kredytowy odrzucił wniosek. (Źródła: KYC-00456, HT-00456, WN-4508, ZD-4508, DC-2250)

Chronologiczna sekwencja (z przypisanymi źródłami)
- Monitoring transakcji (01.02.2025–31.03.2025): wielokrotne wpłaty gotówkowe o podobnych kwotach (~9 400–9 900 PLN) wskazujące na „rozbijanie” (structuring) oraz szybkie przelewy zagraniczne do Republiki Vantia (jurysdykcja wysokiego ryzyka). (źródło: HT-00456; potwierdzenie w KYC-00456)
- Analiza KYC i ryzyka: na podstawie wyciągów i zgłoszeń (SAR) zaktualizowano profil klienta do klasy ryzyka E i nałożono wzmocnione środki bezpieczeństwa (EDD); zwrócono uwagę na brak dokumentacji handlowej uzasadniającej obroty. (źródło: KYC-00456, HT-00456)
- Wniosek kredytowy: klient złożył 05.05.2025 wniosek WN-4508 o 80 000 PLN (produkt „Nordvik Gotówka”), dołączając ZD-4508 (dochód netto 12 500 PLN). Wniosek został oceniany z uwzględnieniem flagi compliance (wysokie ryzyko). (źródło: WN-4508, ZD-4508)
- Decyzja kredytowa: 12.05.2025 podjęto decyzję odmowną (DC-2250). Jako przyczynę wskazano wysoki poziom ryzyka AML (klasa E), brak możliwości ustalenia wiarygodnego źródła środków oraz obowiązujące ograniczenia banku dla klientów z takim profilem ryzyka. (źródło: DC-2250)

Braki dokumentacyjne (uniemożliwiają pełne odtworzenie wszystkich szczegółów)
- Pełna treść raportu ryzyka RR-0012 (wykaz rekomendacji i szczegółów analizy).
- Treść raportów zgłoszeń SAR przypisywanych do sprawy (SAR-0034, SAR-0041).
- Pełne opinie/ekspertyzy Departamentu Zgodności (compliance) i ewentualne notatki wewnętrzne potwierdzające przebieg konsultacji.
- Szczegółowe alerty AML/monitoringu (jeżeli zapisane osobno od KYC/HT).

Weryfikacja i nauka (stan repozytorium)
- Weryfikator potwierdził zgodność powyższej sekwencji z dokumentami (werdykt: POTWIERDZONA — źródła: KYC-00456, HT-00456, WN-4508, ZD-4508, DC-2250).
- Zweryfikowany fakt został zapisany do grafu wiedzy (ID faktu: learned::55043ed89ebc5989).
- Zapisano także jakościową wskazówkę (learning) powiązaną z klientem KL-00456 (ID learning::cf9aef733d4c52fe) — wskazanie brakujących SAR/RR‑0012 oraz rekomendacja alternatywnych wzorców nazewnictwa przy wyszukiwaniu (np. ALERT-*, SAR_REPORT-*, COMPL-SAR-*).

Źródła: KYC-00456, HT-00456, WN-4508, ZD-4508, DC-2250.

**Ocena:** czesciowa — Odpowiedź agenta poprawnie opisuje kluczowe elementy procesu i decyzji, jednak pomija szczegółowe nazwy i numery zgłoszeń SAR oraz raportu ryzyka RR-0012, które są istotne dla pełnej zgodności merytorycznej z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250', 'HT-00456', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'WN-4508']; w odpowiedzi ['DC-2250', 'HT-00456', 'KL-00456', 'KYC-00456', 'RR-0012', 'SAR-0034', 'SAR-0041', 'WN-4508', 'ZD-4508']; pokrycie 0.78

---

## [P3.3] (zestaw 3) 🟡 czesciowa
**Pytanie:** Porównaj trzy typy decyzji kredytowych w zbiorze (pozytywną, warunkową, negatywną) i wskaż, jak profil ryzyka z KYC oraz polityki determinowały wynik każdej z nich.

**Oczekiwana:** - **Pozytywna — DC-2201** (Anna Kowalska): klasa B, DTI 36,52%, LTV 80% — wszystkie kryteria POL-RYZYKO-01 spełnione → udzielenie kredytu.
  - **Warunkowa — DC-2203** (Bałtyk Logistyka): klasa C przy podwyższonym zadłużeniu → zgoda pod warunkiem opłaty wstępnej 30% lub dodatkowego zabezpieczenia (POL-RYZYKO-01 §5).
  - **Negatywna — DC-2250** (Marek Nowicki): zdolność wystarczająca (DTI 16,20%), ale klasa E z RR-0012 (AML) → odmowa (POL-RYZYKO-01 §5, POL-AML-01).
  - Wniosek: o wyniku decydował nie tylko wskaźnik finansowy, lecz klasa ryzyka (w tym override z tytułu AML).

**Odpowiedź agenta:** Oto porównanie i wyjaśnienie, oparte wyłącznie na zawartości grafu i dokumentów (wskazane źródła poniżej).

1) Decyzja POZYTYWNA
- Przykład: DC-2202 — decyzja oznaczona jako pozytywna. Powiązana KYC: KYC-00124 (klasa A, scoring 92/100). 
- Jak profil i polityka zadziałały: POL-RYZYKO-01 mapuje klasy A–C (przy scoring ≥60) na decyzję pozytywną — więc klient z klasą A i scoring 92 spełnia warunki do decyzji pozytywnej. 
- Źródła: DC-2202, KYC-00124, POL-RYZYKO-01.

2) Decyzja WARUNKOWA
- Przykład: DC-2203 — decyzja warunkowa (pozytywna pod warunkiem spełnienia dodatkowych wymogów). Powiązana KYC: KYC-00125 (klasa C, scoring 70/100).
- Jak profil i polityka zadziałały: POL-RYZYKO-01 określa, że klasy C–D typowo prowadzą do decyzji warunkowej (wymagane dodatkowe zabezpieczenia/warunki). Klasa C ze średnim scoringiem skutkuje nałożeniem warunków zgodnie z polityką. 
- Źródła: DC-2203, KYC-00125, POL-RYZYKO-01.

3) Decyzja NEGATYWNA
- Przykład: DC-2250 — decyzja negatywna. Powiązana KYC: KYC-00456 (klasa E — wysoki ryzyk, scoring 66/100, ale klasa nadpisana do E z powodu ryzyka AML).
- Jak profil i polityka zadziałały: POL-RYZYKO-01 przypisuje klasie E decyzję negatywną; dodatkowo oceny AML (POL-AML-01) spowodowały podwyższenie ryzyka i wzmocnione środki (EDD), co uzasadniło odmowę. 
- Źródła: DC-2250, KYC-00456, POL-RYZYKO-01, POL-AML-01.

Krótka synteza zasad determinujących wynik
- Główna reguła (POL-RYZYKO-01): klasy ryzyka mapują się na typ decyzji — A–C → pozytywna (jeśli scoring ≥60), C–D → warunkowa (wymagane dodatkowe warunki), E → negatywna. Dodatkowe czynniki (np. sygnały AML, przekroczenia limitów, negatywna historia) mogą przeważyć i zmienić klasyfikację/wywołać odmowę niezależnie od nominalnego scoringu. Źródło: POL-RYZYKO-01; przykłady: DC-2202, DC-2203, DC-2250.

Kompletność danych i zapis do grafu (nauka)
- Na etapie weryfikacji wykryto rozbieżności w początkowej odpowiedzi; brakujące/ skorygowane fakty zostały zapisane do grafu. Zaktualizowano i dodano zweryfikowane fakty (identyfikatory zapisu): learned::3a2d5451156426ed, learned::6189f45f4f7afb40, learned::20039a1113abd9bd, learned::ff41b06db4661b33.  
- Dodano wskazówki jakościowe (learnings): learning::505263244cabf24f (do DC-2202) i learning::8718040c67423169 (ogólna wskazówka do POL-RYZYKO-01). Status zapisu: ok.
- Dzięki temu graf zawiera obecnie kompletne, zweryfikowane przykłady trzech typów decyzji (DC-2202, DC-2203, DC-2250) oraz powiązane profile KYC i reguły polityki.  
- Potwierdzone źródła użyte przy odpowiedzi: DC-2202, DC-2203, DC-2250, KYC-00124, KYC-00125, KYC-00456, POL-RYZYKO-01, POL-AML-01.

Jeśli chcesz, mogę: 
- dostarczyć krótkie wyciągi fragmentów dokumentów (cytaty) dla każdego punktu, albo 
- wygenerować tabelę porównawczą z kluczowymi liczbami (scoring, klasa, wymagane warunki) na podstawie powyższych dokumentów.

**Ocena:** czesciowa — Agent poprawnie opisuje wpływ klas ryzyka i polityk na decyzje, ale podaje inne przykładowe kody decyzji i wartości profilu (np. klasę A zamiast B i LTV/DTI), co nie odpowiada konkretnym danym oczekiwanej odpowiedzi.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'DC-2203', 'DC-2250', 'KYC-00123', 'KYC-00125', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012']; w odpowiedzi ['DC-2202', 'DC-2203', 'DC-2250', 'KYC-00124', 'KYC-00125', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01']; pokrycie 0.67

---

## [P3.4] (zestaw 3) 🟡 czesciowa
**Pytanie:** Oblicz łączną kwotę odsetek dla wszystkich kredytów/leasingów z zawartymi umowami w zbiorze i podaj źródła.

**Oczekiwana:** - Kredyt hipoteczny UM-7788: odsetki 626 649,94 PLN wg pierwotnego HS-7788 (lub 579 719,78 PLN po repricingu wg HS-7794, przy założeniu utrzymania 7,45%).
  - Kredyt gotówkowy UM-7789: odsetki 15 077,76 PLN (HS-7789).
  - Leasing UM-7790: część odsetkowa 28 169,56 PLN netto (HS-7790).
  - **Suma (wariant pierwotny hipoteki):** 626 649,94 + 15 077,76 + 28 169,56 = **669 897,26 PLN**.
  - (Uwaga: umowa karty UM-7791 nie ma z góry ustalonych odsetek — zależą od wykorzystania limitu; wniosek WN-4508 odrzucono, więc go nie liczymy.)

**Odpowiedź agenta:** Odpowiedź oparta wyłącznie na pamięci grafowej i dokumentach (patrz źródła niżej).

Wynik
- Łączna kwota odsetek dla umów oznaczonych w grafie jako „umowa zawarta”: 607 889,34 PLN.
  - Składniki:
    - UM-7790 (leasing operacyjny): 28 169,56 PLN (źródła: UM-7790, HS-7790, DC-2203). Uwaga: wcześniejsza wartość w grafie 43 247,32 PLN została zweryfikowana jako nieaktualna/ błędna (źródło: REG-KG-01).
    - UM-7788 (kredyt hipoteczny): 579 719,78 PLN — wartość po aktualizacji harmonogramu (HS-7794). Pierwotna kwota odsetek wg UM-7788 / HS-7788 wynosiła 626 649,94 PLN; do sumy przyjęto zaktualizowaną kwotę z HS-7794 (źródła: UM-7788, HS-7788, HS-7794, DC-2201).

Dodatkowe ustalenia
- UM-7789 zawiera w dokumentach kwotę odsetek 15 077,76 PLN (źródło: UM-7789 §5.3), ale nie był wyraźnie oznaczony w grafie jako „umowa zawarta” w przeszukaniu początkowym — dlatego nie został włączony do powyższej sumy. Jeśli chcesz, policzę sumę również z UM-7789 (wynik wtedy: 623 0 966, (28 169,56 + 579 719,78 + 15 077,76) = 622 967,10 PLN) — potwierdź, czy ma być uwzględniony.

Zapis w grafie (wykonane działania)
- Zapisano zweryfikowane fakty do grafu (uczyniłem to po weryfikacji dokumentów):
  - UM-7790: interest_total = 28 169,56 PLN (id faktu: learned::748060defd2b1a1e). Poprzednia wartość 43 247,32 PLN zapisana jako interest_total_prev (źródło: REG-KG-01).
  - UM-7788: interest_total_original = 626 649,94 PLN oraz interest_total_updated = 579 719,78 PLN (id faktu: learned::097a4c67b2663297).
  - UM-7789: interest_total = 15 077,76 PLN (id faktu: learned::43031e5d60ccc1b3).
  - Dodano jakościową wskazówkę dla UM-7790 wyjaśniającą rozbieżność i zalecenie sprawdzania harmonogramów (id learning::0fab3d8bdee8167d).

Źródła (dokumenty użyte do obliczeń i weryfikacji)
- UM-7790, HS-7790, DC-2203 (dla UM-7790: 28 169,56 PLN)
- UM-7788, HS-7788, HS-7794, DC-2201 (dla UM-7788: oryg. 626 649,94 PLN; zaktualiz. 579 719,78 PLN — użyto zaktualizowanej kwoty)
- UM-7789 (§5.3) (15 077,76 PLN — istnieje w dokumentach, status umowy nieoznaczony jako „zawarta” w początkowym przeszukaniu)
- REG-KG-01 (źródło poprzedniej wartości 43 247,32 PLN powiązanej wcześniej z UM-7790)

Jeżeli chcesz:
- uwzględnię UM-7789 w sumie (zaktualizuję wynik),
- prześlę szczegółowy rozbieg obliczeń (sumowanie odsetek po ratach z harmonogramów) wraz z cytatami fragmentów dokumentów.

**Ocena:** czesciowa — Odpowiedź agenta zawiera poprawne dane o odsetkach i źródłach, lecz nie podaje sumy dla wszystkich umów zawartych w zbiorze (pomija UM-7789 z powodu braku oznaczenia „umowa zawarta”), co powoduje niepełną zgodność z oczekiwaniami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788', 'HS-7789', 'HS-7790', 'HS-7794', 'UM-7788', 'UM-7789', 'UM-7790']; w odpowiedzi ['DC-2201', 'DC-2203', 'HS-7788', 'HS-7790', 'HS-7794', 'REG-KG-01', 'UM-7788', 'UM-7789', 'UM-7790']; pokrycie 0.86

---

## [P3.5] (zestaw 3) ✅ dobra
**Pytanie:** Opisz mechanizm i finansowy skutek zmiany wskaźnika NRR 3M dla kredytu hipotecznego — wskaż dokumenty i kwoty.

**Oczekiwana:** - NRR 3M spadł z 5,85% (TO-2025-Q1) do 5,35% (TO-2025-Q2), tj. o 0,50 p.p.
  - Zgodnie z REG-KH-02 §3 (oprocentowanie zmienne, aktualizacja kwartalna, marża stała), oprocentowanie UM-7788 zmieniło się z 7,95% na 7,45% bez aneksu.
  - Bank sporządził zaktualizowany harmonogram HS-7794 (od raty nr 2): rata spadła z 3 688,83 na **3 531,88 PLN** (o 156,95 PLN).
  - Łączne odsetki spadły z 626 649,94 do 579 719,78 PLN (oszczędność ok. 46 930,16 PLN przy utrzymaniu 7,45%).
  - Efekt widoczny na wyciągu HT-00123 (rata 1 = 3 688,83, raty 2–3 = 3 531,88).

**Odpowiedź agenta:** Krótko — mechanizm i skutek finansowy zmiany NRR 3M dla kredytu hipotecznego (na podstawie dokumentów banku Nordvik Finanse S.A.):

Mechanizm
- NRR 3M jest składnikiem oprocentowania zmiennego kredytu; oprocentowanie nominalne = NRR_3M + marża umowna. Zmiana wartości NRR 3M powoduje kwartalną aktualizację oprocentowania i sporządzenie zaktualizowanego harmonogramu spłat — aktualizacja następuje automatycznie, bez konieczności aneksu do umowy (źródła: TO-2025-Q1, TO-2025-Q2, UM-7788; odwołanie do REG-KH-02 §3 w dokumentach).

Ilościowy przykład (konkretny kredyt UM-7788)
- Kwota kredytu: 480 000,00 PLN (UM-7788).  
- Parametry przed zmianą (stan Q1 2025):  
  - NRR 3M = 5,85% (TO-2025-Q1)  
  - Marża = 2,10% (UM-7788 / TO-2025-Q1)  
  - Oprocentowanie nominalne = 7,95% (5,85% + 2,10%) (TO-2025-Q1, UM-7788)  
  - Miesięczna rata (harmonogram HS-7788) = 3 688,83 PLN (HS-7788)  
  - Całkowite odsetki (wg pierwotnego harmonogramu) = 626 649,94 PLN (HS-7788 / UM-7788)
- Parametry po zmianie (stan Q2 2025, repricing):  
  - NRR 3M = 5,35% (TO-2025-Q2)  
  - Marża = 2,10% (bez zmiany)  
  - Oprocentowanie nominalne = 7,45% (5,35% + 2,10%) (TO-2025-Q2, HS-7794)  
  - Miesięczna rata po repricingu (od raty nr 2, HS-7794) = 3 531,88 PLN (HS-7794)  
  - Całkowite odsetki po repricingu (łącznie, uwzględniając pierwszą ratę na starych warunkach) = 579 719,78 PLN (HS-7794)
- Skutek finansowy / oszczędność: około 46 930,16 PLN mniejsze odsetki w całym okresie przy utrzymaniu niższego NRR 3M (porównanie HS-7788 vs HS-7794).

Użyte dokumenty (źródła)
- TO-2025-Q1 (tabela oprocentowania, Q1 2025) — NRR 3M = 5,85%, marża 2,10%  
- TO-2025-Q2 (tabela oprocentowania, Q2 2025) — NRR 3M = 5,35%  
- UM-7788 (umowa kredytu hipotecznego) — kwota 480 000 PLN, marża, warunek repricingu  
- HS-7788 (pierwotny harmonogram) — rata 3 688,83 PLN, całk. odsetki 626 649,94 PLN  
- HS-7794 (zaktualizowany harmonogram po repricingu) — rata 3 531,88 PLN, całk. odsetki 579 719,78 PLN

Braki / rekomendacja
- Decyzje kredytowe DC-* (np. DC-2201) nie zostały odnalezione w przeszukanym zbiorze — zalecam dołączenie/odczyt dokumentów DC-* dla pełnej ścieżki decyzyjnej i audytowej.

Zapis do grafu (nauka)
- Zweryfikowane fakty dotyczące UM-7788 i powiązanych harmonogramów zostały zapisane do grafu wiedzy. ID zapisanych faktów (learned):  
  b937c9c64cf3b248, 47ea7b8d4f3c08bb, c9093de6bec965bf, 920678baab842f82, a6024577bbc3ca92, a3ea6fe1f3913e13, 51416a2a7397d208, 78133baa9bb0868e, 521c13968568874e, bbc2b8d699714817, 945fbf6c6e7cff3d, 3930043eacf9d1a6, a4dc159705d7f970.  
- Dodano też jakościową wskazówkę (learning) powiązaną z UM-7788: ID c3a7b05e0f327143 — przypomnienie o sprawdzaniu DC-* i przechowywaniu obu wersji harmonogramu (HS-7788, HS-7794).

Jeśli chcesz, mogę teraz: 1) odczytać/załączyć brakujące decyzje DC-2201 i inne DC-*, lub 2) przygotować krótką tabelę porównawczą „przed vs po” z rozbiciem rat na kapitał/odsetki dla kilku pierwszych lat.

**Ocena:** dobra — Odpowiedź agenta w pełni odpowiada wymogom merytorycznym oczekiwanej, zawierając precyzyjne dane procentowe, kwoty rat i odsetek, dokumenty oraz opis mechanizmu bez istotnych błędów.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788', 'HS-7794', 'HT-00123', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'UM-7788']; w odpowiedzi ['DC-2201', 'HS-7788', 'HS-7794', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'UM-7788']; pokrycie 0.86

---

## [P3.6] (zestaw 3) 🟡 czesciowa
**Pytanie:** Zidentyfikuj wszystkich klientów objętych wzmożonymi środkami bezpieczeństwa (EDD) i opisz podstawę oraz skutki dla ich klasy ryzyka.

**Oczekiwana:** - **KL-00456 (Marek Nowicki):** EDD z powodu SAR-0034 i SAR-0041 → RR-0012; klasa ryzyka podniesiona z C do **E**; wstrzymanie nowych kredytów (skutek: odmowa DC-2250).
  - **KL-00129 (Bursztyn Handel Sp. z o.o.):** EDD z powodu SAR-0052 (nietypowe wpłaty gotówkowe + transakcje z podmiotem powiązanym); klasa ryzyka podniesiona z C do **D**; nowe zaangażowania warunkowe/wstrzymane.
  - Obaj objęci zakazem tipping-off (POL-AML-01 §7).

**Odpowiedź agenta:** Odnalezione encje objęte EDD:

- client_id: KYC-00456  
  client_name: Marek Andrzej Nowicki  
  podstawa objęcia EDD: zgłoszenia podejrzanych transakcji (SAR-0034, SAR-0041) i klasyfikacja jako wysokie ryzyko (klasa E) (źródła: KYC-00456, RR-0012).  
  skutki dla klasy ryzyka: zmiana klasyfikacji na wysokie ryzyko (E); wstrzymanie nowych zaangażowań kredytowych do wyjaśnienia; wdrożenie wzmocnionego monitoringu transakcji (źródła: KYC-00456, RR-0012, DC-2250).  
  źródła: KYC-00456, RR-0012, DC-2250 (wspierające: SAR-0034, SAR-0041)

Brak informacji o innych klientach objętych EDD w grafie/dokumentach.

Zapis do grafu: zweryfikowany fakt został zapisany (fact_id: learned::485a6ff114064d6f). Dodatkowo zapisałem wskazówkę jakościową dla encji KYC-00456 (learning_id: learning::522c34696db50622): "Przy EDD z SAR upewnić się, że decyzja o wstrzymaniu produktów jest odnotowana w DC i RR; monitorować powiązane SARy i aktualizować status po wyjaśnieniu." (źródła zapisu: KYC-00456, RR-0012, DC-2250).

Źródła: KYC-00456, RR-0012, DC-2250.

**Ocena:** czesciowa — Agent poprawnie zidentyfikował klienta KL-00456 i wskazał poprawną podstawę oraz skutki, ale nie uwzględnił drugiego klienta KL-00129 oraz braku zakazu tipping-off, co powoduje brak pełnej zgodności merytorycznej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00129', 'KYC-00456', 'POL-AML-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'SAR-0052']; w odpowiedzi ['DC-2250', 'KYC-00456', 'RR-0012', 'SAR-0034', 'SAR-0041']; pokrycie 0.57

---

## [P3.7] (zestaw 3) 🟡 czesciowa
**Pytanie:** Które tabele oprocentowania i opłat obowiązują dla poszczególnych umów, biorąc pod uwagę daty ich zawarcia i zasady aktualizacji?

**Oczekiwana:** - Umowy zawarte w I kw. 2025 (UM-7788 z 14.02, UM-7789 z 05.03, UM-7790 z 20.03, UM-7791 z 12.03) bazują na TO-2025-Q1 i TOP-2025-Q1.
  - Kredyty stałoprocentowe (gotówkowy UM-7789) i leasing (UM-7790) zachowują stopę z dnia zawarcia.
  - Kredyt hipoteczny UM-7788 (zmienny) jest repricowany od Q2 wg TO-2025-Q2 (nowy harmonogram HS-7794).
  - Wniosek WN-4506 (10.05.2025, Q2) bazuje na TO-2025-Q2 i TOP-2025-Q2.

**Odpowiedź agenta:** Odpowiedź — które tabele oprocentowania i opłat obowiązują dla poszczególnych umów (z uwzględnieniem dat zawarcia i zasad aktualizacji):

1) UM-7788  
- data_zawarcia: 2025-02-14 (źródło: UM-7788)  
- tabele_oprocentowania:  
  - TO-2025-Q1 — obowiązuje od 2025-01-01 (źródło: TO-2025-Q1)  
- tabele_opłat:  
  - TOP-2025-Q1 — obowiązuje od 2025-01-01 (źródło: TOP-2025-Q1)  
- zasady_aktualizacji:  
  - Oprocentowanie zmienne aktualizowane kwartalnie, automatycznie wg wartości NRR 3M z ostatniego dnia roboczego poprzedniego kwartału; zmiana NRR 3M nie wymaga aneksu (źródło: REG-KH-02).  
(źródła: UM-7788, TO-2025-Q1, TOP-2025-Q1, REG-KH-02)

2) UM-7789  
- data_zawarcia: 2025-03-05 (źródło: UM-7789)  
- tabele_oprocentowania:  
  - TO-2025-Q1 — obowiązuje od 2025-01-01; w umowie wskazane oprocentowanie stałe 10,90% (źródło: UM-7789, TO-2025-Q1)  
- tabele_opłat:  
  - TOP-2025-Q1 — obowiązuje od 2025-01-01 (źródło: UM-7789, TOP-2025-Q1)  
- zasady_aktualizacji:  
  - Produkt gotówkowy objęty REG-KG-01 — oprocentowanie ustalone jako stałe w umowie i nie podlega kwartalnym zmianom (źródło: REG-KG-01, UM-7789).  
Dodatkowe powiązania: decyzja DC-2202 i harmonogram HS-7789 zawierają parametry kalkulacji rat dla UM-7789 (źródła: DC-2202, HS-7789).

Podsumowanie (krótkie):  
- UM-7788 (hipoteczna) stosuje TO-2025-Q1 i TOP-2025-Q1; oprocentowanie zmienne — kwartalna automatyczna aktualizacja wg NRR 3M (REG-KH-02). (źródła: UM-7788, TO-2025-Q1, REG-KH-02, TOP-2025-Q1)  
- UM-7789 (gotówkowa) stosuje TO-2025-Q1 i TOP-2025-Q1; oprocentowanie w umowie jest stałe (10,90%) i nie podlega aktualizacjom kwartalnym (REG-KG-01). (źródła: UM-7789, TO-2025-Q1, REG-KG-01, TOP-2025-Q1)

Czy graf został uzupełniony: tak — po weryfikacji fakt dla UM-7789 zapisano do grafu (id: learned::6004c3b68dc4bb5a) oraz dodano wskazówkę jakościową powiązaną z UM-7789 (id: learning::a0a9d1de4e10aed4).

Jeśli chcesz, mogę:  
- odczytać i przytoczyć konkretne fragmenty (linie) z wymienionych dokumentów;  
- sprawdzić inne umowy (lista UM-*) i ich powiązania z tabelami;  
- porównać konkretne parametry (marża, NRR) dla UM-7788 na podstawie TO-2025-Q1.

**Ocena:** czesciowa — Agent opisuje poprawnie tabele i zasady dla UM-7788 i UM-7789 z I kw. 2025 oraz zasady aktualizacji oprocentowania dla tych umów, jednak nie uwzględnia leasingu UM-7790 i jego stałej stopy ani repricingu kredytu hipotecznego UM-7788 z Q2 zgodnie z oczekiwaną odpowiedzią.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KG-01', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'TOP-2025-Q1', 'TOP-2025-Q2', 'UM-7788', 'WN-4506']; w odpowiedzi ['DC-2202', 'HS-7789', 'REG-KG-01', 'REG-KH-02', 'TO-2025-Q1', 'TOP-2025-Q1', 'UM-7788', 'UM-7789']; pokrycie 0.62

---

## [P3.8] (zestaw 3) ✅ dobra
**Pytanie:** Sprawdź spójność danych osobowych i finansowych klientki KL-00124 we wszystkich dokumentach, w których występuje.

**Oczekiwana:** - Katarzyna Maria Lewandowska, PESEL 90111067321 — identyczne w KYC-00124, ZD-4503, WN-4502, UM-7789.
  - Dochód netto 8 200 PLN — spójny w ZD-4503, WN-4502, DC-2202.
  - Kredyt 50 000 PLN / 60 mies / 10,90% / rata 1 084,63 PLN — spójny w WN-4502, DC-2202, UM-7789, HS-7789.
  - Klasa ryzyka A (scoring 92) — KYC-00124, potwierdzona w DC-2202.
  - Brak sprzeczności.

**Odpowiedź agenta:** Podsumowanie kontroli spójności danych klientki KL-00124

Werdykt: POTWIERDZONA — dane osobowe i finansowe są spójne między dokumentami, ale nadal niekompletne (braki wskazane dalej). (weryfikator: POTWIERDZONA; źródła: KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789, ZD-4503)

1) Pole po polu — wartości i dokumenty potwierdzające
- Imię i nazwisko: Katarzyna Maria Lewandowska (KYC-00124; WN-4502; DC-2202; UM-7789; ZD-4503).  
- PESEL: 90111067321 (KYC-00124; WN-4502; DC-2202; UM-7789; ZD-4503).  
- Data urodzenia: 10.11.1990 (tylko KYC-00124).  
- Adres zamieszkania: ul. Słoneczna 5 m. 2, 80-100 Gdańsk (KYC-00124; WN-4502; UM-7789; ZD-4503).  
- Adres korespondencyjny: brak we wszystkich sprawdzonych dokumentach (brak: KYC-00124; WN-4502; DC-2202; UM-7789; HS-7789; ZD-4503).  
- Dokument tożsamości: dowód osobisty DEF 246810, ważny do 22.03.2032 (KYC-00124). Brak paszportu w dokumentach.  
- NIP klienta: brak we wszystkich dokumentach; jest NIP pracodawcy 584-222-33-44 (KYC-00124; ZD-4503).  
- Dochód netto i źródło: 8 200,00 PLN netto; umowa o pracę w Nadmorskie Centrum Medyczne Sp. z o.o. (KYC-00124; WN-4502; ZD-4503).  
- Zobowiązania bieżące: 0,00 PLN (KYC-00124; WN-4502; DC-2202).  
- Scoring / klasa ryzyka: 92/100, klasa A (KYC-00124; DC-2202).  
- DTI: 13,23% (WN-4502; DC-2202). Uwagi: KYC wskazuje brak zobowiązań (0,00 PLN), co jest zgodne z przyjętym DTI w dokumentach wniosku/dec.  
- Decyzja kredytowa: pozytywna, kwota 50 000,00 PLN (DC-2202).  
- Umowa kredytowa i harmonogram: UM-7789 — 50 000,00 PLN, 60 miesięcy, oprocentowanie stałe 10,90%, rata 1 084,63 PLN, prowizja 2 000,00 PLN, data zawarcia 2025-03-05, uruchomienie 2025-03-07; HS-7789 harmonogram zgodny (pierwsza rata 10.04.2025, ostatnia 10.03.2030). (UM-7789; HS-7789)

2) Wykryte braki / niepełności
- Brak adresu korespondencyjnego we wszystkich dokumentach (KYC-00124; WN-4502; DC-2202; UM-7789; HS-7789; ZD-4503).  
- Brak NIP klienta (tylko NIP pracodawcy jest dostępny: 584-222-33-44) (KYC-00124; ZD-4503).  
- Brak dokumentu tożsamości innego niż dowód osobisty (np. paszport) — tylko dowód osobisty jest zaewidencjonowany (KYC-00124).

Rekomendacja: uzupełnić w KYC i systemie klienta pola: adres korespondencyjny, NIP klienta (jeśli ma), dodatkowy dokument tożsamości/paszport (jeśli wymagany przez procedury). (źródła potwierdzające brak: wszystkie powyższe dokumenty)

3) Dokumenty sprawdzone
KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789, ZD-4503.

4) Stan w grafie pamięci i zapis „nauki”
- Początkowo graf oznaczył encję KL-00124 jako "Incomplete" (braki: address_correspondence, client_NIP, passport).  
- Na podstawie powyższej weryfikacji zapisałem zweryfikowany fakt do grafu (graph_add_learned_fact) i dodałem jakościową wskazówkę (graph_add_learning). Zapisano: fakt id learned::29567ab48de7af06 oraz wskazówkę id learning::be21f9974dfbf1dd (źródła użyte przy zapisie: KYC-00124; WN-4502; DC-2202; UM-7789; HS-7789; ZD-4503).  
(Uwaga: jeśli potrzebujesz, mogę pobrać pełne metadane zapisu z grafu, w tym timestamp modyfikacji.)

5) Krótkie podsumowanie
Dane osobowe i finansowe klientki KL-00124 są wewnętrznie spójne między wszystkimi dokumentami (POTWIERDZONA zgodność). Nadal jednak brakuje trzech pól wymagających uzupełnienia w KYC/systemie: adres korespondencyjny, NIP klienta oraz dokument tożsamości inny niż dowód (jeśli procedury tego wymagają). Zapis do grafu został wykonany (learned::29567ab48de7af06) i dodano krótką wskazówkę jakościową (learning::be21f9974dfbf1dd).  

Jeśli chcesz, mogę: 1) wystawić listę pól do uzupełnienia w formacie do przesłania do działu KYC; 2) pobrać z grafu timestamp zapisanego faktu; 3) uruchomić powiadomienie do KYC o brakujących polach. Co preferujesz?

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe dane do potwierdzenia spójności zgodne z oczekiwaniami oraz dodatkowe informacje o brakach, nie naruszając merytorycznej zgodności.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2202', 'HS-7789', 'KYC-00124', 'UM-7789', 'WN-4502', 'ZD-4503']; w odpowiedzi ['DC-2202', 'HS-7789', 'KL-00124', 'KYC-00124', 'UM-7789', 'WN-4502', 'ZD-4503']; pokrycie 1.0

---

## [P3.9] (zestaw 3) ✅ dobra
**Pytanie:** Na podstawie polityk banku opisz, jak przetwarzany jest wniosek klienta wysokiego ryzyka AML oraz jakie ograniczenia praw wynikają z zasad ochrony danych.

**Oczekiwana:** - Ocena ryzyka i klasyfikacja: POL-RYZYKO-01 (klasy A–E, override jakościowy) w powiązaniu z POL-AML-01 (CDD/EDD, monitoring, SAR).
  - Dla klienta wysokiego ryzyka: wzmożone środki (EDD), ustalenie źródła środków, możliwe wstrzymanie nowych usług i blokady; zakaz tipping-off.
  - RODO (POL-DANE-01): przetwarzanie na podstawie obowiązku prawnego (AML) — prawo do usunięcia i sprzeciwu NIE ma zastosowania do dokumentacji AML; okresy przechowywania wynikają z przepisów AML.
  - Przykład zastosowania: KL-00456/DC-2250 oraz KL-00129/SAR-0052.

**Odpowiedź agenta:** Poniżej zwięzłe podsumowanie — wyłącznie na podstawie polityk i dokumentów banku (cytaty ID pod punktami).

1) Kroki procesu przetwarzania wniosku klienta wysokiego ryzyka AML
- Przyjęcie wniosku, identyfikacja klienta i beneficjenta rzeczywistego oraz wstępna ocena KYC (CDD). (źródło: KYC-00123, POL-AML-01)  
- Zastosowanie wzmożonych środków należytej staranności (EDD): pogłębiona weryfikacja tożsamości, ustalenie źródła majątku/środków, uzupełniająca dokumentacja. (źródło: POL-AML-01)  
- Monitoring relacji i transakcji oraz częstsze przeglądy (EDD). (źródło: POL-AML-01)  
- W przypadku sygnału podejrzanej transakcji: pracownik zgłasza zdarzenie do zespołu AML → analityk AML przygotowuje zgłoszenie SAR → MLRO zatwierdza zgłoszenie → przekazanie do KJAF. (źródło: POL-AML-01)  
- Bank może wstrzymać świadczenie usług / zablokować transakcje w toku wyjaśnienia. (źródło: POL-AML-01)  
- Wnioski/decisions kredytowe powiązane z umową i regulaminem produktu są przechowywane zgodnie z zasadami dokumentacji kredytowej. (źródło: UM-7788, REG-KH-02)

2) Wymagane dokumenty / dane (KYC/EDD)
- Dokumenty identyfikacyjne klienta i beneficjenta rzeczywistego. (KYC-00123)  
- Dokumenty potwierdzające źródło majątku i pochodzenie środków (EDD). (POL-AML-01)  
- Karty KYC / dokumentacja EDD zgodna z wewnętrzną polityką. (POL-AML-01, KYC-00123)

3) Eskalacje i odpowiedzialności
- Pracownik pierwszego kontaktu: identyfikacja i zgłoszenie sygnału. (POL-AML-01)  
- Zespół/Analityk AML: analiza, przygotowanie SAR. (POL-AML-01)  
- MLRO (Inspektor ds. AML): zatwierdzenie zgłoszeń SAR i decyzje o dalszych działaniach. (POL-AML-01)  
- Dział Zgodności / Compliance: nadzór, przeglądy polityk i monitorowanie zgodności. (POL-AML-01, POL-DANE-01)  
- Dział kredytowy realizuje wydane decyzje kredytowe i odniesienia do umów (UM-7788, REG-KH-02).

4) Ograniczenia prawne wynikające z zasad ochrony danych (RODO i polityka wewnętrzna)
- Podstawy przetwarzania: obowiązek prawny (np. obowiązki AML) oraz wykonanie umowy są dopuszczalnymi podstawami przetwarzania danych. (POL-DANE-01, POL-AML-01)  
- Zasada minimalizacji i celowości: przetwarzane tylko dane niezbędne do celów AML i realizacji umowy. (POL-DANE-01)  
- Prawa osób: prawo dostępu, sprostowania, ograniczenia przetwarzania, przenoszenia danych i sprzeciwu — jednak prawa te mogą być ograniczone, gdy przetwarzanie wynika z obowiązku prawnego (np. obowiązek retencji dokumentacji AML). (POL-DANE-01, POL-AML-01)  
- Retencja: dokumentacja kredytowa i AML przechowywana przez okresy wymagane przepisami (retencja wynikająca z przepisów AML i polityk wewnętrznych). (POL-DANE-01, POL-AML-01)  
- Udostępnianie danych: dopuszczalne tylko uprawnionym podmiotom i organom na podstawie prawa; powierzenie przetwarzania wyłącznie zaufanym podmiotom przy zabezpieczeniu T/O. (POL-DANE-01)  
- Zakaz tipping-off: bank nie może ujawniać klientowi faktu lub treści zgłoszenia SAR (zakaz „tipping‑off”). (POL-AML-01)  
- Środki bezpieczeństwa: techniczne i organizacyjne zabezpieczenia (szyfrowanie, kontrola dostępu, rejestrowanie operacji); obowiązek zgłoszenia naruszenia w ciągu 72 godzin, gdy wymagane. (POL-DANE-01)

Uwaga organizacyjna (praktyczna): dokumentacja ogólnych zasad AML i RODO opisuje procesy i obowiązki, natomiast nie znaleziono jednego spójnego, szczegółowego „proceduralnego” dokumentu krok‑po‑kroku dedykowanego wyłącznie obsłudze wniosku wysokiego ryzyka (brak jednego kompletnego SOP — zob. missing info w wewnętrznych zasobach). (źródła: przegląd dokumentów: POL-AML-01, POL-DANE-01, KYC-00123, UM-7788, REG-KH-02)

Potwierdzenie zapisu do grafu wiedzy (nauka)
- Zweryfikowany fakt dotyczący procedury przetwarzania wniosku klienta wysokiego ryzyka AML został zapisany do grafu: learned::71040b6de5aa5b23.  
- Dodatkowa wskazówka jakościowa zapisana jako learning::71040b6de5aa5b23.  
- Uwaga: wskazówka nie została automatycznie powiązana z istniejącą encją „wniosek klienta wysokiego ryzyka AML” w grafie — mogę dopomóc w mapowaniu encji, jeśli chcesz, aby wskazówka była powiązana.

Źródła wykorzystane: POL-AML-01, POL-DANE-01, KYC-00123, UM-7788, REG-KH-02.

Jeżeli chcesz, przygotuję:
- szczegółowy schemat procedury (flowchart) krok‑po‑kroku na podstawie dostępnych dokumentów, albo  
- wykonam powiązanie wskazówki w grafie z konkretną encją (i potwierdzę wykonanie).

**Ocena:** dobra — Odpowiedź agenta w pełni odzwierciedla kluczowe elementy i ograniczenia przedstawione w odpowiedzi oczekiwanej, w tym procedury AML, wzmożone środki, zakaz tipping-off oraz ograniczenia wynikające z RODO zgodnie z politykami banku.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250', 'KYC-00129', 'KYC-00456', 'POL-AML-01', 'POL-DANE-01', 'POL-RYZYKO-01', 'SAR-0052']; w odpowiedzi ['KYC-00123', 'POL-AML-01', 'POL-DANE-01', 'REG-KH-02', 'UM-7788']; pokrycie 0.29

---

## [P3.10] (zestaw 3) ✅ dobra
**Pytanie:** Zbuduj pełną mapę powiązań węzła TO-2025-Q1 — wskaż wszystkie dokumenty, które z niego korzystają, i wyjaśnij, dlaczego jest to „wspólny węzeł" istotny dla spójności zbioru.

**Oczekiwana:** - TO-2025-Q1 jest przywoływana przez: REG-KH-02, REG-KG-01, REG-LE-04, REG-KK-03 (regulaminy), DC-2201, DC-2202, DC-2203, DC-2204 (decyzje), UM-7788, UM-7789, UM-7790, UM-7791 (umowy), HS-7788, HS-7789, HS-7790 (harmonogramy), WN-4502, WN-4503, WN-4504 (wnioski).
  - Ustala wspólną wartość NRR 3M (5,85%) i marże/stopy dla wielu produktów — jej zmiana (TO-2025-Q2) propaguje się na oprocentowanie umów o stopie zmiennej (repricing hipoteki, HS-7794).
  - Dlatego jest kluczowa dla spójności liczbowej całego zbioru.

**Odpowiedź agenta:** Oto uporządkowana odpowiedź na Twoje polecenie — pełna mapa powiązań węzła TO-2025-Q1 oraz wyjaśnienie jego roli jako „wspólnego węzła”.

1) Krótka definicja
- TO-2025-Q1 — tabela oprocentowania obowiązująca w I kwartale 2025 (01.01.2025–31.03.2025), zawierająca wartość wskaźnika referencyjnego NRR 3M = 5,85% oraz nominalne oprocentowania dla produktów: kredyt hipoteczny, kredyt gotówkowy, karta kredytowa i leasing (źródło: TO-2025-Q1).

2) Pełna mapa powiązań

- Relacje bezpośrednie (dokument — typ relacji):
  • REG-KH-02 — APPLIES_POLICY / GOVERNED_BY (odnosi się do TO-2025-Q1 w zakresie oprocentowania) (źródło: REG-KH-02)  
  • REG-KG-01 — USES_RATE_TABLE (źródło: REG-KG-01)  
  • TOP-2025-Q1 — USES_RATE_TABLE / GOVERNED_BY (źródło: TOP-2025-Q1)  
  • TO-2025-Q2 — USES_RATE_TABLE (źródło: TO-2025-Q2)  
  • WN-4504 — USES_RATE_TABLE (źródło: WN-4504)  
  • REG-LE-04 — USES_RATE_TABLE / ATTACHED_TO (źródło: REG-LE-04)  
  • ZD-4508 — HAS_SCHEDULE (wiąże harmonogramy wynikające z tabeli) (źródło: ZD-4508)  
  • HS-7788 — HAS_SCHEDULE (harmonogram spłat wyliczony przy oprocentowaniu z TO-2025-Q1) (źródło: HS-7788)  
  • UM-7788 — USES_RATE_TABLE (umowa kredytowa stosująca wartości NRR i marżę z TO-2025-Q1) (źródło: UM-7788)  
  • Wniosek kredytowy — USES_RATE_TABLE (źródło: Wniosek kredytowy)  
  • DC-2202 / DC-2201 — USES_RATE_TABLE (decyzje kredytowe ustalające cenę na bazie tabeli) (źródła: DC-2202, DC-2201)  
  • Nordvik Karta — USES_RATE_TABLE (produkt kartowy odwołujący się do tabeli) (źródło: Nordvik Karta)  
  • Marek Nowicki (encja klienta) — USES_RATE_TABLE (przypadki/wnioski powiązane z tabelą) (źródło: Marek Nowicki)  
  • PL41 9999 1000 0000 0077 9000 0003 — HAS_ACCOUNT (powiązanie operacyjne) (źródło: graf)

- Powiązania pośrednie (2-hop) — przykłady dokumentów korzystających z dokumentów bezpośrednio powiązanych z TO-2025-Q1:
  • UM-7789, UM-7790, UM-7791 — USES (korzystają pośrednio przez regulacje/wytyczne bazujące na TO-2025-Q1) (źródła: UM-7789, UM-7790, UM-7791)  
  • HS-7790 — USES (harmonogramy powiązane z tymi umowami) (źródło: HS-7790)  
  • WN-4502, WN-4503, WN-4508 — USES (wnioski i dokumenty operacyjne korzystające z pośrednich regulacji) (źródła: WN-4502, WN-4503, WN-4508)  
  • REG-KH-02, UM-7788, DC-2201 (w relacji pośredniej wskazują na wpływ tabeli na decyzje/umowy) (źródła: REG-KH-02, UM-7788, DC-2201)

3) Dlaczego TO-2025-Q1 jest „wspólnym węzłem” istotnym dla spójności zbioru
- Jedno odniesienie dla oprocentowania: TO-2025-Q1 dostarcza jednolite wartości referencyjne (NRR 3M) i stawki nominalne używane przez regulaminy, decyzje kredytowe, umowy i harmonogramy. Dzięki temu różne dokumenty liczą raty, ustalają cenę kredytu i opisują warunki produktu na tej samej podstawie (źródła: TO-2025-Q1, REG-KH-02, UM-7788).  
- Centralny wpływ na decyzje i umowy: decyzje kredytowe (DC-2201/DC-2202) i umowy (UM-7788 i inne) odwołują się do tabeli przy ustalaniu oprocentowania i marży, a więc to właśnie TO-2025-Q1 determinuje realne koszty dla klienta. Zmiana tabeli powoduje konsekwencje w harmonogramach i rozliczeniach (źródła: DC-2201, UM-7788, HS-7788).  
- Spójność harmonogramów i rozliczeń: harmonogramy spłat (HS-7788, HS-7790) są wyliczone przy założeniu stawek z TO-2025-Q1; dzięki temu harmonogramy są porównywalne i zgodne z umowami.  
- Powiązanie z politykami i regulacjami: regulaminy produktów (REG-KH-02, REG-KG-01, REG-LE-04) odwołują się do tej tabeli, co zapewnia zgodność produktów z aktualną polityką cenową banku.

4) Czy graf zawiera wystarczające informacje / czego brakuje
- Ocena: graf ma wystarczające informacje, by zbudować pełną mapę powiązań TO-2025-Q1 i opisać jego wpływ na dokumenty (sufficient = tak). Potwierdzono bezpośrednie relacje i atrybuty tabeli (źródła: TO-2025-Q1, REG-KH-02, DC-2201, UM-7788, HS-7788).  
- Braki: brak (wg stanu grafu i dokumentów nie zidentyfikowano brakujących pól ani dokumentów). Jeśli chcesz jednak pełnej listy wszystkich umów/wniosków klientów powiązanych historycznie z tą tabelą, mogę rozszerzyć wyszukiwanie (może być dużo encji).

5) Zapisy do grafu (nauka)
- Zapisano jakościową wskazówkę dotyczącą korzystania z TO-2025-Q1: learning id = learning::e044b95becd10b20 (treść: „Przy korzystaniu z TO-2025-Q1 zawsze sprawdzać powiązane umowy i decyzje (np. UM-7788, DC-2201) czy nie zawierają aneksów/repricingów; upewniać się, że NRR 3M (5,85%) została właściwie zastosowana przy wyliczeniach rat.”).  
- Zapisano również zweryfikowany fakt opisowy dotyczący TO-2025-Q1: fact id = learned::4b23a753da93a7d4.

6) Źródła użyte w odpowiedzi
TO-2025-Q1, REG-KH-02, REG-KG-01, TOP-2025-Q1, TO-2025-Q2, WN-4504, REG-LE-04, ZD-4508, HS-7788, UM-7788, Wniosek kredytowy, DC-2202, DC-2201, Nordvik Karta, Marek Nowicki, PL41 9999 1000 0000 0077 9000 0003, UM-7789, UM-7790, UM-7791, HS-7790, WN-4502, WN-4503, WN-4508.

Jeżeli chcesz, mogę:
- wygenerować graficzną mapę (diagram) tych powiązań,  
- wypisać pełną listę wszystkich umów/wniosków klientów powiązanych z TO-2025-Q1,  
- albo przeanalizować wpływ hipotetycznej zmiany NRR 3M na konkretne umowy (np. UM-7788).

**Ocena:** dobra — Odpowiedź agenta zawiera pełną i szczegółową mapę powiązań dokumentów wskazanych w odpowiedzi oczekiwanej oraz precyzyjnie wyjaśnia rolę TO-2025-Q1 jako wspólnego węzła decydującego o spójności zbioru, uwzględniając kluczowe fakty i wartości takie jak NRR 3M (5,85%).

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → odpytuję pamięć GRAFOWĄ (Neo4j) → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7794', 'TO-2025-Q1', 'TO-2025-Q2']; w odpowiedzi ['DC-2201', 'DC-2202', 'HS-7788', 'HS-7790', 'REG-KG-01', 'REG-KH-02', 'REG-LE-04', 'TO-2025-Q1', 'TO-2025-Q2', 'TOP-2025-Q1', 'UM-7788', 'UM-7789', 'UM-7790', 'UM-7791', 'WN-4502', 'WN-4503', 'WN-4504', 'WN-4508', 'ZD-4508']; pokrycie 0.67

---
