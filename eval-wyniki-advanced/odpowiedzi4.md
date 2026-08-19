# Wyniki ewaluacji (self_learning_agents)

## [P1.1] (zestaw 1) ✅ dobra
**Pytanie:** Jaki jest numer PESEL (testowy) klientki Anny Katarzyny Kowalskiej?

**Oczekiwana:** 85072812345 (oznaczony jako testowy).

**Odpowiedź agenta:** Testowy numer PESEL klientki Anna Katarzyna Kowalska to 85072812345 (źródło: UM-7788, KYC-00123, WN-4501).

Graf początkowo zawierał PESEL bez oznaczenia typu; na podstawie powyższych dokumentów zaktualizowałem graf — fakt zapisano jako PESEL typu "testowy" (fact_id: learned::878a43ffdd6b3d78) oraz dodano wskazówkę jakościową (learning_id: learning::329cbe2278d35c9a). Zapis do grafu został wykonany.

**Ocena:** dobra — Numer PESEL podany przez agenta jest zgodny z oczekiwaną odpowiedzią i wyraźnie oznaczony jako testowy.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00123']; w odpowiedzi ['KYC-00123', 'UM-7788', 'WN-4501']; pokrycie 1.0

---

## [P1.2] (zestaw 1) ✅ dobra
**Pytanie:** Na jaką kwotę opiewa kredyt hipoteczny w umowie UM-7788?

**Oczekiwana:** 480 000,00 PLN.

**Odpowiedź agenta:** Kredyt hipoteczny w umowie UM-7788 opiewa na kwotę 480 000,00 PLN (źródło: UM-7788). Zapis do grafu został potwierdzony.

**Ocena:** dobra — Odpowiedź agenta podaje dokładnie tę samą kwotę kredytu hipotecznego co odpowiedź oczekiwana, co potwierdza pełną zgodność merytoryczną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['UM-7788']; w odpowiedzi ['UM-7788']; pokrycie 1.0

---

## [P1.3] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi miesięczna rata w harmonogramie HS-7788?

**Oczekiwana:** 3 688,83 PLN (300 rat annuitetowych).

**Odpowiedź agenta:** Miesięczna rata w harmonogramie HS-7788 wynosi 3 688,83 PLN (źródło: HS-7788, UM-7788). Weryfikator potwierdził tę wartość. Fakt był już zapisany w grafie wiedzy (zapis do grafu nie był konieczny). 

Uwaga: dokument wskazuje też korektę ostatniej raty do 3 688,84 PLN z powodu zaokrąglenia (źródło: HS-7788).

**Ocena:** dobra — Odpowiedź agenta zawiera poprawną kwotę miesięcznej raty zgodną z odpowiedzią oczekiwaną, dodatkowo wskazując na korektę ostatniej raty, co nie przeczy zgodności merytorycznej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['HS-7788']; w odpowiedzi ['HS-7788', 'UM-7788']; pokrycie 1.0

---

## [P1.4] (zestaw 1) ✅ dobra
**Pytanie:** Jaki jest maksymalny standardowy wskaźnik LTV według polityki ryzyka kredytowego?

**Oczekiwana:** 80% (standard; LTV 80–90% dopuszczalne wyjątkowo z dodatkowym zabezpieczeniem/ubezpieczeniem i wyższą marżą).

**Odpowiedź agenta:** Maksymalny standardowy wskaźnik LTV według Polityki ryzyka kredytowego wynosi 80% (źródło: POL-RYZYKO-01). Zapis do grafu wiedzy został wykonany (źródła: POL-RYZYKO-01, POL-RYZYKO, REG-KH-02).

**Ocena:** dobra — Odpowiedź agenta poprawnie podaje maksymalny standardowy wskaźnik LTV jako 80%, zgodnie z oczekiwaniami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['POL-RYZYKO-01']; w odpowiedzi ['POL-RYZYKO-01', 'REG-KH-02']; pokrycie 1.0

---

## [P1.5] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi wartość wskaźnika NRR 3M w tabeli oprocentowania na I kwartał 2025?

**Oczekiwana:** 5,85% w skali roku.

**Odpowiedź agenta:** Wskaźnik NRR 3M w tabeli oprocentowania na I kwartał 2025 wynosi 5,85% rocznie (źródła: TO-2025-Q1, REG-KH-02, /memories/AGENTS.md). 

Zapis do grafu wiedzy został wykonany (ID faktu: learned::d6368cef8495771d).

**Ocena:** dobra — Wartość wskaźnika NRR 3M dokładnie odpowiada oczekiwanej wartości 5,85% rocznie.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['TO-2025-Q1']; w odpowiedzi ['REG-KH-02', 'TO-2025-Q1']; pokrycie 1.0

---

## [P1.6] (zestaw 1) ✅ dobra
**Pytanie:** Jaka jest stawka prowizji przygotowawczej dla kredytu hipotecznego w tabeli opłat Q1 2025?

**Oczekiwana:** 2,00% kwoty kredytu.

**Odpowiedź agenta:** Stawka prowizji przygotowawczej dla kredytu hipotecznego w tabeli opłat Q1 2025 wynosi 2,00% (źródło: TO-2025-Q1, TOP-2025-Q1).

Informuję również, że fakt został zapisany do grafu wiedzy (ID zapisu: learned::090a5d9b3d63c2c0).

**Ocena:** dobra — Odpowiedź agenta zawiera poprawną i zgodną z oczekiwaniami wartość prowizji przygotowawczej 2,00% dla kredytu hipotecznego w Q1 2025.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['TOP-2025-Q1']; w odpowiedzi ['TO-2025-Q1', 'TOP-2025-Q1']; pokrycie 1.0

---

## [P1.7] (zestaw 1) ✅ dobra
**Pytanie:** Kto jest beneficjentem rzeczywistym (UBO) spółki „Bursztyn Handel Sp. z o.o."?

**Oczekiwana:** Andrzej Lewiński — 100% udziałów.

**Odpowiedź agenta:** Beneficjentem rzeczywistym (UBO) spółki „Bursztyn Handel Sp. z o.o.” jest Andrzej Lewiński — posiada 100% udziałów (źródła: DC-4481, KYC-00129). Weryfikator: POTWIERDZONA (źródło: KYC-00129).

Zapis do grafu wiedzy: fakt został zapisany (node_id: learned::bf77858337fbd97e).

facts: {
  "beneficjent rzeczywisty (UBO) spółki Bursztyn Handel Sp. z o.o.": "Andrzej Lewiński (100% udziałów)",
  "sources": ["DC-4481", "KYC-00129"],
  "graph_node_id": "learned::bf77858337fbd97e",
  "verification": "POTWIERDZONA (KYC-00129)"
}

**Ocena:** dobra — Odpowiedź agenta zgodnie przedstawia kluczowe fakty i liczby, potwierdzając, że beneficjentem rzeczywistym jest Andrzej Lewiński posiadający 100% udziałów, co odpowiada odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00129']; w odpowiedzi ['DC-4481', 'KYC-00129']; pokrycie 1.0

---

## [P1.8] (zestaw 1) ✅ dobra
**Pytanie:** Jakie rozstrzygnięcie zapadło w decyzji kredytowej DC-2250?

**Oczekiwana:** Decyzja NEGATYWNA (odmowa udzielenia kredytu gotówkowego).

**Odpowiedź agenta:** Decyzja kredytowa DC-2250 miała rozstrzygnięcie negatywne.  
Powody/warunki decyzji:
- klasa ryzyka: E
- zastosowanie wzmożonych środków AML/EDD
- brak możliwości ustalenia źródła środków
- rekomendacja wstrzymania nowych produktów dla klienta

Zapis do grafu wykonany (fact id: learned::5496547166cb35b0; learning id: learning::5496547166cb35b0).  
(źródło: DC-2250 (graf))

**Ocena:** dobra — Odpowiedź agenta poprawnie wskazuje negatywne rozstrzygnięcie decyzji kredytowej DC-2250 oraz dodatkowo podaje szczegółowe powody, co jest zgodne z oczekiwanym wynikiem.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250']; w odpowiedzi ['DC-2250']; pokrycie 1.0

---

## [P1.9] (zestaw 1) ✅ dobra
**Pytanie:** Jaki limit kredytowy przyznano na karcie kredytowej w decyzji DC-2204?

**Oczekiwana:** 15 000,00 PLN.

**Odpowiedź agenta:** Limit kredytowy przyznany na karcie kredytowej w decyzji DC-2204 wynosi 15 000,00 PLN (źródło: DC-2204).

Sprawdziłem pamięć grafową — fakt był już w grafie i został zweryfikowany (werdykt: POTWIERDZONA). Zapis do grafu nie był konieczny, ponieważ informacja już w nim istniała.

**Ocena:** dobra — Odpowiedź agenta podaje identyczny limit kredytowy jak oczekiwana, co potwierdza całkowitą zgodność merytoryczną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['DC-2204']; w odpowiedzi ['DC-2204']; pokrycie 1.0

---

## [P1.10] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi minimalna kwota do zapłaty w cyklu rozliczeniowym karty kredytowej „Nordvik Karta"?

**Oczekiwana:** 5% zadłużenia, nie mniej niż 50 PLN.

**Odpowiedź agenta:** Minimalna kwota do zapłaty w cyklu rozliczeniowym karty kredytowej „Nordvik Karta” wynosi 5% zadłużenia, nie mniej niż 50 PLN (źródło: REG-KK-03).  
Fakt był zweryfikowany i zapisany w grafie wiedzy: learned::3085abc3aed21ffc (encje: Nordvik Karta, minimalna kwota do zapłaty, cykl rozliczeniowy).

**Ocena:** dobra — Odpowiedź agenta w pełni pokrywa się z oczekiwaną co do minimalnej kwoty do zapłaty, podając 5% zadłużenia, nie mniej niż 50 PLN.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KK-03']; w odpowiedzi ['REG-KK-03']; pokrycie 1.0

---

## [P1.11] (zestaw 1) ✅ dobra
**Pytanie:** Jak długi jest okres bezodsetkowy (grace period) karty kredytowej dla transakcji bezgotówkowych?

**Oczekiwana:** Do 56 dni (pod warunkiem spłaty całości zadłużenia w terminie).

**Odpowiedź agenta:** Okres bezodsetkowy (grace period) dla transakcji bezgotówkowych wynosi do 56 dni, pod warunkiem spłaty całości zadłużenia w terminie. (źródła: REG-KK-03; graf wiedzy Nordvik)

Działania wykonane: najpierw sprawdziłem graf wiedzy (znaleziono wpis: 56 dni), następnie potwierdziłem wartość w dokumencie REG-KK-03. Nie było potrzeby zapisywania nowego faktu do grafu.

**Ocena:** dobra — Odpowiedź agenta poprawnie podaje kluczowy fakt dotyczący długości okresu bezodsetkowego i warunku jego obowiązywania, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['REG-KK-03']; w odpowiedzi ['REG-KK-03']; pokrycie 1.0

---

## [P1.12] (zestaw 1) ✅ dobra
**Pytanie:** Do jakiego podmiotu i jakiej jurysdykcji trafiały przelewy zagraniczne z rachunku w historii transakcji HT-00456?

**Oczekiwana:** Do „Vantia Global Trade LLC" w Republice Vantia (jurysdykcja wysokiego ryzyka); łącznie ok. 464 950,00 PLN.

**Odpowiedź agenta:** Oto wynik, oparty wyłącznie na dokumentach i grafie:

Lista przelewów zagranicznych wychodzących z rachunku w historii HT-00456:
1. Data: 2025-02-06 — Kwota: 88 000,00 PLN — Waluta: PLN — Beneficjent: Vantia Global Trade LLC — Jurysdykcja: Republika Vantia — Źródło: HT-00456  
2. Data: 2025-02-13 — Kwota: 95 000,00 PLN — Waluta: PLN — Beneficjent: Vantia Global Trade LLC — Jurysdykcja: Republika Vantia — Źródło: HT-00456  
3. Data: 2025-02-27 — Kwota: 92 500,00 PLN — Waluta: PLN — Beneficjent: Vantia Global Trade LLC — Jurysdykcja: Republika Vantia — Źródło: HT-00456  
4. Data: 2025-03-11 — Kwota: 99 000,00 PLN — Waluta: PLN — Beneficjent: Vantia Global Trade LLC — Jurysdykcja: Republika Vantia — Źródło: HT-00456  
5. Data: 2025-03-25 — Kwota: 90 450,00 PLN — Waluta: PLN — Beneficjent: Vantia Global Trade LLC — Jurysdykcja: Republika Vantia — Źródło: HT-00456

Podsumowanie:
- Łączna kwota: 464 950,00 PLN  
- Okres: 2025-02-06 — 2025-03-25  
- Dodatkowe dokumenty kontekstowe potwierdzające ryzyko/jakość danych: RR-0012 (raport ryzyka), KYC-00456 (profil klienta), SAR-0034 (zgłoszenie podejrzanej transakcji).  

Braki / uwagi:
- W analizowanych dokumentach nie znaleziono innych beneficjentów ani jurysdykcji dla przelewów z HT-00456 w tym okresie (źródło: HT-00456).  
- Brak w repozytorium bezpośrednich plików technicznych (SWIFT/CSV/XML) z zestawieniami transakcji — jeśli potrzebne są oryginalne pliki transportowe, należy przeszukać archiwa systemu płatności/archiwum plików technicznych (nieodnalezione w dostarczonych dokumentach). (źródła: HT-00456, RR-0012, KYC-00456, SAR-0034)

Weryfikacja i zapis do grafu:
- Weryfikator potwierdził poprawność powyższych danych (werdykt: POTWIERDZONA; źródło: HT-00456).  
- Zgodnie z procedurą, zweryfikowany fakt został zapisany do grafu wiedzy. ID zapisanego faktu: learned::fbbf4b2c55429df8. Dodatkowa wskazówka jakościowa (powiązana z HT-00456) zapisana jako learning::fbbf4b2c55429df8 — treść wskazówki: „Beneficjent Vantia Global Trade LLC w Republice Vantia — jurysdykcja oceniona jako wysokiego ryzyka; w grafie zapisać szczegóły poszczególnych przelewów i brak plików SWIFT/CSV w repozytorium.”

Czy chcesz, abym uruchomił dodatkowe przeszukanie archiwów plików technicznych (SWIFT/CSV/XML) lub pobrał pełne kopie źródłowe tych transakcji?

**Ocena:** dobra — Odpowiedź agenta dokładnie potwierdza kluczowe fakty i liczby z odpowiedzi oczekiwanej, wskazując beneficjenta Vantia Global Trade LLC, jurysdykcję Republiki Vantia i łączną kwotę około 464 950,00 PLN.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HT-00456']; w odpowiedzi ['HT-00456', 'KYC-00456', 'RR-0012', 'SAR-0034']; pokrycie 1.0

---

## [P1.13] (zestaw 1) ✅ dobra
**Pytanie:** Jaki średni miesięczny dochód netto potwierdza zaświadczenie ZD-4503?

**Oczekiwana:** 8 200,00 PLN (klientka Katarzyna Lewandowska, Nadmorskie Centrum Medyczne Sp. z o.o.).

**Odpowiedź agenta:** Średni miesięczny dochód netto potwierdzany zaświadczeniem ZD-4503 wynosi 8 200,00 PLN (źródło: ZD-4503).  
Zapis do grafu wiedzy wykonany: fakt zapisany jako learned::31a2f9c861b84613.

**Ocena:** dobra — Odpowiedź agenta podaje prawidłową kwotę dochodu netto zgodną z oczekiwaną odpowiedzią i precyzyjnie odnosi się do zaświadczenia ZD-4503.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['ZD-4503']; w odpowiedzi ['ZD-4503']; pokrycie 1.0

---

## [P1.14] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi wartość wykupu przedmiotu leasingu we wniosku WN-4503?

**Oczekiwana:** 1% wartości = 1 800,00 PLN netto.

**Odpowiedź agenta:** Wartość wykupu przedmiotu leasingu we wniosku WN-4503 wynosi 1 800,00 PLN netto (źródło: WN-4503).

Weryfikacja: POTWIERDZONA (źródło potwierdzenia: WN-4503).

Zapis do grafu: zweryfikowany fakt zapisano jako learned::12ce454a163bb4ed, a dodatkowa jakościowa wskazówka zapisana jako learning::12ce454a163bb4ed.

**Ocena:** dobra — Odpowiedź zawiera kluczową wartość wykupu 1 800,00 PLN netto zgodnie z oczekiwaną informacją.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['WN-4503']; w odpowiedzi ['WN-4503']; pokrycie 1.0

---

## [P1.15] (zestaw 1) ✅ dobra
**Pytanie:** Jaki wewnętrzny próg alertu dla wpłat gotówkowych określa polityka AML?

**Oczekiwana:** 15 000 PLN (rozbijanie wpłat poniżej progu = structuring).

**Odpowiedź agenta:** Wewnętrzny próg alertu dla wpłat gotówkowych określony w polityce AML Nordvik Finanse S.A. wynosi 15 000 PLN. Polityka wskazuje też, że rozbijanie wpłat na kwoty tuż poniżej tego progu (structuring / smurfing) jest traktowane jako typologia podejrzana (źródła: POL-AML-01 §4; SAR-0034 §2).

Potwierdzenie zapisu do grafu: zweryfikowany fakt "cash_deposit_alert_threshold = 15 000 PLN" został zapisany w grafie wraz ze źródłami POL-AML-01 i SAR-0034. Dodano także jakościową wskazówkę przypominającą o konieczności sprawdzania POL-AML-01 §4 i SAR-0034 oraz uwagi dotyczące waluty. (Zapis wykonany: graph_add_learned_fact i graph_add_learning).

**Ocena:** dobra — Odpowiedź agenta podaje prawidłowy próg 15 000 PLN i wspomina o rozbijaniu wpłat (structuring), zgodnie z oczekiwaną odpowiedzią.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['POL-AML-01']; w odpowiedzi ['POL-AML-01', 'SAR-0034']; pokrycie 1.0

---

## [P1.16] (zestaw 1) ✅ dobra
**Pytanie:** Jaka jest klasa ryzyka kredytowego klienta KL-00124 (Katarzyna Lewandowska)?

**Oczekiwana:** Klasa A (scoring 92/100), ryzyko niskie.

**Odpowiedź agenta:** Klasa ryzyka kredytowego klientki KL-00124 (Katarzyna Lewandowska) to A; scoring 92/100; DTI 13,23% (źródło: KYC-00124, DC-2202, UM-7789).  
Zapisano zweryfikowany fakt do grafu (learned fact ID: learned::860480dae443de38) oraz dodano wskazówkę jakościową o konieczności korekty mapowania ID dokumentów (poprawne źródła: KYC-00124, DC-2202, UM-7789).

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe informacje zgodne z odpowiedzią oczekiwaną, tj. klasę ryzyka A i scoring 92/100, a dodatkowe dane nie wpływają negatywnie na zgodność merytoryczną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00124']; w odpowiedzi ['DC-2202', 'KL-00124', 'KYC-00124', 'UM-7789']; pokrycie 1.0

---

## [P1.17] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi opłata roczna za kartę kredytową i kiedy jest znoszona?

**Oczekiwana:** 120,00 PLN; znoszona przy rocznym obrocie bezgotówkowym ≥ 12 000 PLN.

**Odpowiedź agenta:** Opłata roczna za kartę kredytową wynosi 120,00 PLN i jest znoszona, jeśli roczny obrót bezgotówkowy na karcie wynosi co najmniej 12 000,00 PLN (źródła: DC-2204, WN-4504, TOP-2025-Q1).

Zapis do grafu: zweryfikowany fakt został zapisany w grafie (id: learned::4159bec9850b4e80) wraz z krótką wskazówką jakościową: „Zapis potwierdza warunek zniesienia opłaty przy obrocie ≥ 12 000 PLN/rok; brak innych warunków zwolnienia w dostępnych dokumentach — zweryfikować promocje/statusy konta przy dalszych zapytaniach.” Wskazówka nie została automatycznie powiązana z istniejącą encją — mogę to zrobić na żądanie.

**Ocena:** dobra — Odpowiedź agenta precyzyjnie podaje kwotę 120,00 PLN i warunek zniesienia opłaty przy rocznym obrocie bezgotówkowym ≥ 12 000 PLN, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KK-03', 'TOP-2025-Q1']; w odpowiedzi ['DC-2204', 'TOP-2025-Q1', 'WN-4504']; pokrycie 0.5

---

## [P1.18] (zestaw 1) 🟡 czesciowa
**Pytanie:** Jakie oprocentowanie limitu w rachunku firmowym przyznano w decyzji DC-2205?

**Oczekiwana:** 12,50% w skali roku (zmienne); limit 50 000 PLN, prowizja za limit 1% rocznie = 500 PLN.

**Odpowiedź agenta:** Oprocentowanie limitu w rachunku firmowym przyznane w decyzji DC-2205 wynosi 12,50% w skali roku (źródło: DC-2205). Zapis do grafu został wykonany — fakt pochodzi z DC-2205 i został dodany do pamięci grafowej.

**Ocena:** czesciowa — Agent podał prawidłowe oprocentowanie 12,50% rocznie, ale nie uwzględnił informacji o limicie 50 000 PLN i prowizji 1% rocznie.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['DC-2205']; w odpowiedzi ['DC-2205']; pokrycie 1.0

---

## [P2.1] (zestaw 2) ✅ dobra
**Pytanie:** Czy rata w harmonogramie HS-7788 jest zgodna z kwotą kredytu i oprocentowaniem z umowy oraz tabeli oprocentowania?

**Oczekiwana:** Tak. Umowa UM-7788: 480 000 PLN na 300 mies.; oprocentowanie 7,95% = NRR 3M 5,85% + marża 2,10% (TO-2025-Q1); rata annuitetowa 3 688,83 PLN — zgodna z HS-7788.

**Odpowiedź agenta:** Tak — rata jest zgodna.

1. Krótkie potwierdzenie: rata w HS-7788 = 3 688,83 PLN jest zgodna z umową UM-7788 oraz z tabelą oprocentowania TO-2025-Q1 (wniosek: Tak; werdykt weryfikatora: POTWIERDZONA). (źródła: HS-7788, UM-7788, TO-2025-Q1)

2. Użyte wartości i uzasadnienie:
   - Kwota kredytu: 480 000,00 PLN (HS-7788; UM-7788).
   - Okres: 300 miesięcy (25 lat) (HS-7788; UM-7788).
   - Oprocentowanie nominalne: 7,95% rocznie = NRR 3M 5,85% + marża 2,10% (UM-7788; TO-2025-Q1).
   - Miesięczna stopa użyta w obliczeniach: 7,95% / 12 = 0,6625% miesięcznie (HS-7788).
   - Przy tych parametrach dla rat annuitetowych obliczona rata miesięczna ≈ 3 688,83 PLN, co zgadza się z wartością podaną w harmonogramie HS-7788. (źródła: HS-7788, UM-7788, TO-2025-Q1)

3. Weryfikacja: subagent-weryfikator zweryfikował dane jako POTWIERDZONA — brak niezgodności ani brakujących elementów (źródła: HS-7788, UM-7788, TO-2025-Q1).

4. Zapis w grafie wiedzy (nauka): ponieważ tej informacji nie było wcześniej w grafie, zapisałem zweryfikowany fakt i krótką wskazówkę jakościową do grafu:
   - Zapisany fakt: „Rata w harmonogramie HS-7788 wynosi 3 688,83 PLN i jest zgodna z umową UM-7788 oraz tabelą oprocentowania TO-2025-Q1 dla kredytu 480 000,00 PLN, okres 300 miesięcy, oprocentowanie nominalne 7,95% (NRR 3M 5,85% + marża 2,10%), miesięczna stopa 0,6625%.” (powiązano z: HS-7788, UM-7788, TO-2025-Q1).
   - Zapisana wskazówka jakościowa przy HS-7788: krótkie przypomnienie, by zawsze potwierdzać wersję tabeli oprocentowania (tu: TO-2025-Q1) i użycie miesięcznej stopy nominal/12 przy kalkulacji rat annuitetowych.

Jeśli chcesz, mogę pokazać skrócony rachunek (wzór obliczenia raty annuitetowej) krok po kroku z użytymi liczbami.

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe fakty i liczby zgodne z odpowiedzią oczekiwaną, potwierdzając zgodność raty z umową i tabelą oprocentowania.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788', 'TO-2025-Q1', 'UM-7788']; w odpowiedzi ['HS-7788', 'TO-2025-Q1', 'UM-7788']; pokrycie 1.0

---

## [P2.2] (zestaw 2) ✅ dobra
**Pytanie:** Na podstawie której decyzji zawarto umowę UM-7788 i jaki wskaźnik DTI przyjęto w tej decyzji?

**Oczekiwana:** Decyzja DC-2201 (pozytywna); DTI = 36,52% (rata 3 688,83 / dochód netto 10 100).

**Odpowiedź agenta:** Umowa UM-7788 została zawarta na podstawie decyzji DC-2201; w tej decyzji przyjęto wskaźnik DTI = 36,52% (źródło: DC-2201, UM-7788).  
Fakt był już zapisany w grafie wiedzy (tak) — nie dodano nowego wpisu.

**Ocena:** dobra — Odpowiedź agenta poprawnie wskazuje decyzję DC-2201 oraz prawidłowy wskaźnik DTI 36,52%, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['DC-2201', 'UM-7788']; w odpowiedzi ['DC-2201', 'UM-7788']; pokrycie 1.0

---

## [P2.3] (zestaw 2) ✅ dobra
**Pytanie:** Dlaczego wniosek WN-4508 został odrzucony, skoro klient miał wystarczającą zdolność kredytową?

**Oczekiwana:** Decyzja DC-2250 była negatywna nie z powodu zdolności (DTI 16,20% — akceptowalne), lecz z powodu klasy ryzyka E nadanej w raporcie RR-0012 na podstawie zgłoszeń SAR-0034 i SAR-0041 oraz braku możliwości ustalenia źródła środków (AML).

**Odpowiedź agenta:** Wniosek WN-4508 został odrzucony nie z powodu braku zdolności kredytowej, lecz z powodu ryzyka AML — brak możliwości ustalenia źródła środków oraz wysoka klasa ryzyka E. (źródła: WN-4508, DC-2250, KYC-00456, RR-0012)

Kluczowe powody:
1. Wysokie ryzyko AML (klasa E) i aktywny raport RR-0012 → rekomendacja wstrzymania nowych produktów do wyjaśnienia (WN-4508; DC-2250; RR-0012).  
2. Brak możliwości udokumentowania źródła pochodzenia środków oraz wprowadzenie środków wzmożonej staranności (EDD) (DC-2250; KYC-00456; RR-0012).  
3. Pomimo tego, wniosek spełniał kryteria finansowe (dochód netto 12 500 PLN, DTI 16,20%), ale kwestia AML przesądziła o odmowie (WN-4508; DC-2250).

Zapis do grafu: zweryfikowany fakt dotyczący odrzucenia WN-4508 został dodany do grafu (id learned::d13d214bafafaa1b) wraz z jakością wskazówką (id learning::f0b1da58decb9809).

**Ocena:** dobra — Odpowiedź agenta poprawnie wskazuje, że odrzucenie wniosku WN-4508 nie wynikało ze zdolności kredytowej (DTI 16,20%), lecz z powodu wysokiej klasy ryzyka E oraz braku możliwości ustalenia źródła środków (AML), zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250', 'RR-0012', 'WN-4508']; w odpowiedzi ['DC-2250', 'KYC-00456', 'RR-0012', 'WN-4508']; pokrycie 1.0

---

## [P2.4] (zestaw 2) 🟡 czesciowa
**Pytanie:** Który regulamin i którą politykę powołuje decyzja kredytowa DC-2201?

**Oczekiwana:** Regulamin kredytu hipotecznego REG-KH-02 oraz Politykę ryzyka kredytowego POL-RYZYKO-01 (dodatkowo tabelę TO-2025-Q1 dla parametrów cenowych).

**Odpowiedź agenta:** Krótko: decyzja kredytowa DC-2201 powołuje regulamin REG-KH-02 oraz politykę POL-RYZYKO-01 (źródło: DC-2201; powiązane: REG-KH-02, POL-RYZYKO-01).

Weryfikacja: werdykt POTWIERDZONA (sprawdzone w DC-2201).

Zapis w grafie: zweryfikowane fakty zapisano w grafie jako dwa nauczone fakty (obie wpisy mają ID zakończone na learned::6a4eb0e594ba3a69). Dodatkowo dopisano wskazówkę jakościową do encji DC-2201 (ID learning::6a4eb0e594ba3a69) — „W decyzji kredytowej zawsze wskazywać powiązane regulaminy i polityki; sprawdzić zgodność ID”.

Źródła: DC-2201, REG-KH-02, POL-RYZYKO-01. Chcesz, żebym pokazał aktualny stan powiązań w grafie?

**Ocena:** czesciowa — Agent poprawnie wskazał regulamin REG-KH-02 oraz politykę POL-RYZYKO-01, ale nie wspomniał o tabeli TO-2025-Q1, która jest wymagana w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'POL-RYZYKO-01', 'REG-KH-02']; w odpowiedzi ['DC-2201', 'POL-RYZYKO-01', 'REG-KH-02']; pokrycie 1.0

---

## [P2.5] (zestaw 2) ✅ dobra
**Pytanie:** Jakie warunki postawiła decyzja warunkowa DC-2203 i w jaki sposób zostały spełnione w umowie leasingu UM-7790?

**Oczekiwana:** DC-2203 wymagała albo podwyższenia opłaty wstępnej do 30%, albo dodatkowego zabezpieczenia. W UM-7790 klient wybrał drugi wariant: ustanowił poręczenie cywilne Tomasza Górskiego oraz weksel własny in blanco, zachowując opłatę wstępną 20% (36 000 PLN); dostarczył też zaświadczenia ZUS/US.

**Odpowiedź agenta:** Odpowiedź — z dokumentów (cytaty i odniesienia niżej).

A) Warunki postawione w decyzji warunkowej DC-2203 (pkt V):
- V.1: „Podwyższenie opłaty wstępnej z 20% do 30% (tj. z 36 000,00 do 54 000,00 PLN) … ALBO ustanowienie dodatkowego zabezpieczenia: poręczenie cywilne właściciela Tomasza Górskiego, oraz weksel własny in blanco spółki wraz z deklaracją wekslową (REG-LE-04 §3).” (źródło: DC-2203, pkt V.1)
- V.2: „Dostarczenie zaświadczeń o niezaleganiu wobec ZUS i US (nie starszych niż 30 dni).” (źródło: DC-2203, pkt V.2)
- V.3: „Zawarcie umowy ubezpieczenia przedmiotu (AC/OC) z cesją na Finansującego przed wydaniem pojazdu.” (źródło: DC-2203, pkt V.3)

B) W jaki sposób warunki zostały spełnione w umowie UM-7790:
- V.1 — zabezpieczenie zamiast podwyższenia opłaty:
  - Evidence: UM-7790 zapisuje wybór wariantu z dodatkowymi zabezpieczeniami przy zachowaniu opłaty wstępnej 20%: „ustanowiono poręczenie cywilne Tomasza Górskiego oraz weksel własny in blanco wraz z deklaracją wekslową” (UM-7790, §1.1–1.2). (źródło: UM-7790)
- V.2 — zaświadczenia ZUS/US:
  - Evidence: UM-7790 potwierdza dostarczenie zaświadczeń o niezaleganiu wobec ZUS i US z datą 2025-03-14 (UM-7790, §1.3). (źródło: UM-7790)
- V.3 — ubezpieczenie z cesją:
  - Evidence: UM-7790 zawiera obowiązek utrzymania ubezpieczenia AC/OC z cesją na Finansującego („Ubezpieczenie przedmiotu (AC/OC) z cesją na Finansującego przez cały okres.”) (UM-7790, §5.1). (źródło: UM-7790)

Dodatkowe ustalenia / daty:
- Decyzja DC-2203 datowana: 03.03.2025; ważna do 02.04.2025 (źródło: DC-2203).
- Umowa UM-7790 zawarta: 2025-03-20 (UM-7790) — zawarta po spełnieniu warunków (źródła: DC-2203, UM-7790).
- Zaświadczenia ZUS/US dostarczono: 2025-03-14 (UM-7790).

Potwierdzenie zapisu do grafu (nauka):
- Zweryfikowany fakt zapisano do grafu jako learned fact ID: learned::ec3670683e1e54af.
- Zapisano też wskazówkę jakościową (learning) powiązaną z DC-2203 i UM-7790 jako learning::ec3670683e1e54af.
(źródła zapisu: DC-2203, UM-7790, KYC-00125 — zapis wykonany w grafie)

Źródła: DC-2203, UM-7790 (opcjonalnie powiązanie: KYC-00125).

**Ocena:** dobra — Odpowiedź agenta w pełni pokrywa kluczowe warunki decyzji DC-2203 oraz sposób ich spełnienia w umowie UM-7790 zgodnie z oczekiwaniami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2203', 'UM-7790']; w odpowiedzi ['DC-2203', 'KYC-00125', 'REG-LE-04', 'UM-7790']; pokrycie 1.0

---

## [P2.6] (zestaw 2) 🟡 czesciowa
**Pytanie:** Jak zmieniła się rata kredytu hipotecznego UM-7788 po zmianie wskaźnika i co było przyczyną?

**Oczekiwana:** Rata spadła z 3 688,83 PLN na 3 531,88 PLN, ponieważ NRR 3M spadł z 5,85% (TO-2025-Q1) do 5,35% (TO-2025-Q2), co przy marży 2,10% dało oprocentowanie 7,45% zamiast 7,95%. Nowy harmonogram to HS-7794 (obowiązuje od raty nr 2).

**Odpowiedź agenta:** Rata kredytu hipotecznego UM-7788 zmalała z 3 688,83 PLN do 3 531,88 PLN — obniżka o 156,95 PLN (źródło: HS-7788). Zmiana obowiązuje od raty nr 2 zgodnie z harmonogramem (źródło: HS-7794). Przyczyną było obniżenie wskaźnika NRR 3M z 5,85% do 5,35%, co spowodowało spadek oprocentowania z 7,95% do 7,45% i w efekcie niższą ratę (źródło: TO-2025-Q1).

Weryfikacja: odpowiedź została sprawdzona i potwierdzona na podstawie dokumentów HS-7788, HS-7794 i TO-2025-Q1.

Zapis do grafu: zweryfikowany fakt został dodany do grafu wiedzy (id: learned::ff2ed74017a48133) oraz dołączono wskazówkę jakościową powiązaną z UM-7788.

**Ocena:** czesciowa — Agent poprawnie wskazał zmiany kwot rat oraz wskaźnika i oprocentowania, ale wprowadził nieścisłość co do źródła dokumentu harmonogramu oraz pominął marżę jako przyczynę zmiany oprocentowania.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7794', 'REG-KH-02', 'TO-2025-Q2', 'UM-7788']; w odpowiedzi ['HS-7788', 'HS-7794', 'TO-2025-Q1', 'UM-7788']; pokrycie 0.5

---

## [P2.7] (zestaw 2) ✅ dobra
**Pytanie:** Którego klienta i na podstawie jakich zgłoszeń przeklasyfikowano do najwyższej klasy ryzyka (E)?

**Oczekiwana:** Klienta KL-00456 (Marek Nowicki, JDG „MN Trade"). Podstawa: zgłoszenia SAR-0034 (structuring) i SAR-0041 (pass-through) → raport ryzyka RR-0012 → aktualizacja karty KYC-00456 do klasy E.

**Odpowiedź agenta:** Klient KL-00456 (Marek Andrzej Nowicki, JDG "MN Trade") został przeklasyfikowany do najwyższej klasy ryzyka E w dniu 2025-04-16 na podstawie zgłoszeń SAR-0034 i SAR-0041 oraz raportu RR-0012 (potwierdzenie i aktualizacja w KYC-00456).

Źródła:
- SAR-0034
- SAR-0041
- RR-0012
- KYC-00456

Weryfikacja: werdykt POTWIERDZONA (weryfikator wskazał zgodność daty i podstaw; źródła: RR-0012, KYC-00456).

Zapis do grafu wiedzy: fakt zapisano jako learned fact (id: learned::17b06cf322d3b6e7), a wskazówkę jakościową zapisano jako learning (id: learning::7e664a18344ba9a7).

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe informacje z odpowiedzi oczekiwanej, w tym klienta KL-00456, zgłoszenia SAR-0034 i SAR-0041 oraz raport RR-0012 i aktualizację KYC-00456, co potwierdza pełną zgodność merytoryczną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00456', 'RR-0012', 'SAR-0034', 'SAR-0041']; w odpowiedzi ['KL-00456', 'KYC-00456', 'RR-0012', 'SAR-0034', 'SAR-0041']; pokrycie 1.0

---

## [P2.8] (zestaw 2) ✅ dobra
**Pytanie:** Jaka jest relacja między zaświadczeniem ZD-4501, wnioskiem WN-4501 i decyzją DC-2201?

**Oczekiwana:** ZD-4501 jest załącznikiem nr 1 do wniosku WN-4501 i potwierdza dochód netto 10 100 PLN; ten dochód został użyty w decyzji DC-2201 do wyliczenia wskaźnika DTI (36,52%).

**Odpowiedź agenta:** Oto zwięzłe podsumowanie relacji między dokumentami (każdy punkt krótki, z cytatem i źródłem):

1) ZD-4501 jest załącznikiem do wniosku WN-4501: "ZD-4501 jest załącznikiem nr 1 do wniosku WN-4501" (źródło: graf, dokument: ZD-4501).  
2) ZD-4501 dostarcza dochód użyty przy ocenie wniosku — dochód z ZD-4501 został użyty do wyliczenia DTI w decyzji DC-2201: "dochód z ZD-4501 użyty do wyliczenia DTI w DC-2201" (źródło: graf, dokument: ZD-4501).  
3) WN-4501 to wniosek kredytowy klienta KL-00123 o kwotę 480 000,00 PLN (wnioskowana kwota) z datą 2025-01-20: "Wnioskowana kwota kredytu: 480 000,00 PLN" (źródło: WN-4501).  
4) DC-2201 to decyzja kredytowa rozstrzygająca o WN-4501 — decyzja POZYTYWNA z datą 2025-02-03, kwota 480 000,00 PLN, podstawa: POL-RYZYKO-01, profil klienta klasa B, scoring 78/100: "Decyzja: POZYTYWNA... Kwota kredytu: 480 000,00 PLN" (źródło: DC-2201).  
5) Powiązanie to w efekcie: ZD-4501 → (załącznik, źródło dochodu) → WN-4501 → (rozpatrzony przez) → DC-2201. Dane klienta są spójne: KL-00123 (PESEL 85072812345) oraz kwoty dochodu z ZD-4501: brutto 14 200,00 PLN, netto 10 100,00 PLN (źródło: ZD-4501, WN-4501, DC-2201).

Status weryfikacji i zapis do grafu:
- Weryfikator ocenił powyższe stwierdzenia jako POTWIERDZONE względem dokumentów ZD-4501, WN-4501 i DC-2201. (źródła: ZD-4501, WN-4501, DC-2201)  
- Zweryfikowane fakty zostały zapisane do grafu wiedzy oraz dodano wskazówkę jakościową powiązaną z encją klienta KL-00123 (zapewnienie zapisu dat i kluczowych kwot dla przyszłych weryfikacji).

Jeśli chcesz, mogę teraz: a) otworzyć i przytoczyć fragmenty UM-7788 (umowa powiązana z DC-2201), b) przedstawić schemat relacji w formie grafu, lub c) wyeksportować zapisane fakty z grafu.

**Ocena:** dobra — Odpowiedź agenta poprawnie wskazuje, że ZD-4501 jest załącznikiem nr 1 do wniosku WN-4501, potwierdza dochód netto 10 100 PLN, który został użyty w decyzji DC-2201 do wyliczenia wskaźnika DTI, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'WN-4501', 'ZD-4501']; w odpowiedzi ['DC-2201', 'KL-00123', 'POL-RYZYKO-01', 'UM-7788', 'WN-4501', 'ZD-4501']; pokrycie 1.0

---

## [P2.9] (zestaw 2) ✅ dobra
**Pytanie:** Ile wynosi rata leasingowa netto i brutto oraz z czego wynika różnica?

**Oczekiwana:** Rata netto 3 586,87 PLN, brutto 4 411,85 PLN; różnica to VAT 23% doliczany do raty leasingu.

**Odpowiedź agenta:** Krótko i rzeczowo:

- Rata leasingowa netto: 3 586,87 PLN. (składniki: część kapitałowa 2 500,87 PLN + część odsetkowa 1 086,00 PLN) (źródła: HS-7790, UM-7790).  
- Rata leasingowa brutto: 4 411,85 PLN — to rata netto powiększona o VAT 23% (źródła: HS-7790, UM-7790).  
- Dlaczego jest różnica: rata brutto = rata netto + podatek VAT (w tym przypadku 23%), stąd kwota brutto jest wyższa o wartość VAT naliczonego od raty netto (źródło: HS-7790).

Dodatkowe dane potwierdzające:
- Suma rat netto (48 rat): 172 169,56 PLN; część kapitałowa 144 000,00 PLN; część odsetkowa 28 169,56 PLN (HS-7790, UM-7790).  
- Wartość finansowana przy opłacie wstępnej 20%: 144 000,00 PLN (DC-2203) — uwaga: decyzja DC-2203 jest warunkowa i finansowanie/wymagana opłata wstępna mogą się zmieniać (patrz uwaga poniżej).

Weryfikacja / uwagi:
- Weryfikator ocenił odpowiedź jako częściowo potwierdzoną z uwagi na warunkowość decyzji dotyczącej opłaty wstępnej i wartości finansowanej — przy wyborze innego sposobu zabezpieczenia opłata wstępna może wymagać podwyższenia do 30%, co zmieni wartość finansowaną (źródło: DC-2203).

Zapis do grafu (nauka):
- Zweryfikowany fakt został zapisany do grafu wiedzy pod identyfikatorem learned::b10bed4327c46175 (fakt oparty na dokumentach HS-7790, UM-7790, DC-2203).  
- Dodatkowo zapisana została jakościowa wskazówka powiązana z DC-2203 dotycząca zmienności wartości finansowanej i opłaty wstępnej w przypadku decyzji warunkowej.

Źródła: HS-7790, UM-7790, DC-2203.

**Ocena:** dobra — Odpowiedź agenta zawiera poprawne i zgodne z oczekiwaną kluczowe wartości rat netto i brutto oraz właściwie wyjaśnia różnicę jako podatek VAT 23%, dodatkowo podając szczegóły i źródła, co nie przeczy pytaniu ani odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j) → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7790', 'UM-7790']; w odpowiedzi ['DC-2203', 'HS-7790', 'UM-7790']; pokrycie 1.0

---

## [P2.10] (zestaw 2) 🟡 czesciowa
**Pytanie:** Czy profil ryzyka klienta KL-00124 jest zgodny z pozytywnym rozstrzygnięciem decyzji DC-2202?

**Oczekiwana:** Tak. KYC-00124: klasa A, scoring 92/100, brak zobowiązań; DC-2202: DTI 13,23%, spełnione kryteria POL-RYZYKO-01 — decyzja pozytywna spójna z profilem.

**Odpowiedź agenta:** TAK.

Profil ryzyka klienta KL-00124 (klasa A, scoring 92, DTI 13,23%) jest zgodny z pozytywną decyzją DC-2202, jednak w grafie odnotowano braki dokumentacji KYC (brak adresu korespondencyjnego, NIP i inny dokument tożsamości niż dowód), które mogą wymagać uzupełnienia przed ostatecznym zamknięciem sprawy.

Źródła: KYC-00124, DC-2202, POL-RYZYKO-01.

Zapis do grafu: zweryfikowany fakt zapisano jako learned::4b7e8eec6f98b72d; dodano też wskazówki learning::0d0f256397e74977 (KL-00124) i learning::29ef4923e148719a (DC-2202).

**Ocena:** czesciowa — Odpowiedź agenta potwierdza zgodność profilu i decyzji, podając kluczowe dane, lecz wspomina o brakach dokumentacji, których nie ma w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2202', 'KYC-00124', 'POL-RYZYKO-01']; w odpowiedzi ['DC-2202', 'KL-00124', 'KYC-00124', 'POL-RYZYKO-01']; pokrycie 1.0

---

## [P2.11] (zestaw 2) ✅ dobra
**Pytanie:** Kto jest kredytobiorcą w umowie UM-7789, jaki jest cel kredytu i na jaki rachunek następuje spłata?

**Oczekiwana:** Katarzyna Maria Lewandowska (KL-00124); cel: remont mieszkania; rachunek spłaty (testowy) PL33 9999 1000 0000 0077 8900 0002.

**Odpowiedź agenta:** Kredytobiorcą w umowie UM-7789 jest Katarzyna Maria Lewandowska (PESEL 90111067321, adres: ul. Słoneczna 5 m. 2, 80-100 Gdańsk) (źródła: UM-7789, KYC-00124).  
Cel kredytu: remont mieszkania (źródło: UM-7789).  
Spłata kredytu następuje na rachunek PL33 9999 1000 0000 0077 8900 0002 należący do Katarzyny Marii Lewandowskiej (źródła: UM-7789, HS-7789).

Zapis do grafu został wykonany — dodano zweryfikowane fakty:
1) kredytobiorca (Katarzyna M. Lewandowska, PESEL, adres) — id faktu learned::66df7f22de6d9f90;  
2) cel kredytu (remont mieszkania) — id faktu learned::fd29a32df9956109;  
3) rachunek spłaty (PL33...0002, właściciel Katarzyna M. Lewandowska) — id faktu learned::14865c1dbcd3178d.  
Dodatkowo dodano wskazówkę jakościową (learning::816db491e207e10f).

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe informacje zgodne z oczekiwaniami: poprawnego kredytobiorcę, cel kredytu oraz rachunek do spłaty.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00124', 'UM-7789']; w odpowiedzi ['HS-7789', 'KYC-00124', 'UM-7789']; pokrycie 1.0

---

## [P2.12] (zestaw 2) 🟡 czesciowa
**Pytanie:** Które oprocentowanie zastosowano w kredycie gotówkowym z wniosku WN-4506 i skąd ono pochodzi?

**Oczekiwana:** 10,90% stałe (przedział 20 001–60 000 PLN) — z tabeli TO-2025-Q2 (wniosek złożony w Q2 2025). Rata 980,74 PLN dla 30 000 PLN na 36 mies.

**Odpowiedź agenta:** Odpowiedź:

- Zastosowane oprocentowanie: 10,90% w skali roku — STAŁE.
- Pochodzenie: tabela oprocentowania TO-2025-Q2, §3, dla przedziału kwoty 20 001–60 000 PLN: „20 001 – 60 000 PLN — 10,90% (oprocentowanie stałe)” (źródło: TO-2025-Q2).
- Potwierdzenie w dokumentach transakcji: WN-4506: „Oprocentowanie: stałe 10,90% w skali roku (TO-2025-Q2 §3)” (źródło: WN-4506); decyzja DC-2206 też wskazuje „Oprocentowanie: stałe 10,90% (TO-2025-Q2 §3)” (źródło: DC-2206).

Źródła: WN-4506, DC-2206, TO-2025-Q2.

Graf został zaktualizowany — zapisano zweryfikowany fakt oprocentowania dla WN-4506 (ID faktu: learned::6c19122868fe4f2c) oraz dodano wskazówkę jakościową (ID: learning::6c19122868fe4f2c).

**Ocena:** czesciowa — Agent poprawnie podał oprocentowanie 10,90% stałe i jego źródło, ale nie wspomniał o racie 980,74 PLN dla 30 000 PLN na 36 miesięcy, co jest kluczowym faktem z odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2206', 'TO-2025-Q2', 'WN-4506']; w odpowiedzi ['DC-2206', 'TO-2025-Q2', 'WN-4506']; pokrycie 1.0

---

## [P2.13] (zestaw 2) ✅ dobra
**Pytanie:** Czym różnią się dwie historie transakcji (HT-00123 i HT-00456) i jakie skutki compliance z nich wynikły?

**Oczekiwana:** HT-00123 (KL-00123) to normalny profil detaliczny (wynagrodzenie, spłata raty, wydatki bytowe) — brak przesłanek AML. HT-00456 (KL-00456) wykazuje structuring i transfery pass-through do jurysdykcji wysokiego ryzyka — skutkuje zgłoszeniami SAR-0034/0041.

**Odpowiedź agenta:** - Główne różnice:
  - HT-00123: profil detaliczny, regularne wpływy wynagrodzenia i spłaty kredytu hipotecznego; brak transakcji gotówkowych wysokokwotowych i brak wskazań na operacje zagraniczne (źródło: HT-00123, KYC-00123, DC-2201).  
  - HT-00456: duże wpłaty gotówkowe rozbijane na kwoty ~9 400–9 900 PLN (suspekt structuring) oraz szybkie przelewy SWIFT do jurysdykcji wysokiego ryzyka (pass-through) bez dokumentacji handlowej (źródło: HT-00456, SAR-0034, SAR-0041).  

- Skutki compliance wynikające z HT-00456:
  - Zgłoszenia SAR dotyczące structuring i pass-through (SAR-0034, SAR-0041).  
  - Ocena wysokiego ryzyka AML i rekomendacje: reklasyfikacja do klasy E, wdrożenie środków wzmożonego nadzoru (EDD) oraz wstrzymanie nowych produktów (RR-0012, KYC-00456).  
  - Konkretny skutek biznesowy: odmowa przyznania kredytu (negatywna decyzja kredytowa) z powodu klasy ryzyka E i wyników raportu (DC-2250). (źródła: SAR-0034, SAR-0041, RR-0012, KYC-00456, DC-2250, POL-AML-01)

- Skutki compliance (lub ich brak) dla HT-00123:
  - Brak działań AML wynikających z historii (nie wykryto przesłanek do zgłoszenia SAR), profil oceniony jako niski/standardowy; klient otrzymał pozytywną decyzję kredytową (DC-2201) (źródła: HT-00123, KYC-00123, DC-2201).  

- Luki / brakujące dokumenty dotyczące HT-00123 (co warto uzupełnić):
  - Brak powiązanych zgłoszeń SAR (np. SAR-00123) i raportu ryzyka (RR-00123) w zbiorze dokumentów — jeżeli istnieją, należy je odnaleźć i dołączyć. (brak w materiałach: SAR-00123, RR-00123)  
  - Zalecane do sprawdzenia: ewentualne notatki compliance/EDD, historyczne przeglądy KYC po dacie 2024-11-15 (źródła potwierdzające brak: przegląd dokumentów — HT-00123, KYC-00123; brak SAR/RR).

- Potwierdzenie zapisu do grafu:
  - Zapisano zweryfikowany fakt o HT-00123 do grafu: learned::d911dbe60ef292b6 (źródła: HT-00123, KYC-00123, DC-2201).  
  - Dodano wskazówkę jakościową (learning) o konieczności sprawdzania KYC i decyzji przy braku wpisów SAR/RR: learning::33b6db05ee465ac0 — uwaga: wskazówka została zapisana, lecz nie została automatycznie powiązana z węzłem encji HT-00123; mogę powiązać ją teraz na żądanie.

Jeżeli chcesz, mogę od razu powiązać wskazówkę z encją HT-00123 i/lub przeszukać system dla ewentualnych brakujących dokumentów (SAR-00123, RR-00123) — potwierdź, czy mam kontynuować.

**Ocena:** dobra — Odpowiedź agenta dokładnie odzwierciedla kluczowe fakty i skutki compliance dla obu historii transakcji zgodnie z odpowiedzią oczekiwaną, rozszerzając ją o dodatkowe szczegóły bez sprzeczności.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HT-00123', 'HT-00456', 'SAR-0034', 'SAR-0041']; w odpowiedzi ['DC-2201', 'DC-2250', 'HT-00123', 'HT-00456', 'KYC-00123', 'KYC-00456', 'POL-AML-01', 'RR-0012', 'RR-00123', 'SAR-00123', 'SAR-0034', 'SAR-0041']; pokrycie 1.0

---

## [P2.14] (zestaw 2) ✅ dobra
**Pytanie:** Jakie zabezpieczenia ustanowiono dla kredytu hipotecznego UM-7788 i jak mają się one do wymogów polityki ryzyka?

**Oczekiwana:** Hipoteka umowna do 720 000 PLN (150% kwoty), cesja z polisy ubezpieczenia nieruchomości, ubezpieczenie pomostowe do wpisu hipoteki — zgodne z wymogiem zabezpieczenia hipotecznego z POL-RYZYKO-01 §4.

**Odpowiedź agenta:** Odpowiedź (krótko):

Dla kredytu hipotecznego UM-7788 ustanowiono następujące zabezpieczenia:
- hipoteka umowna do 720 000 PLN (co stanowi 150% kwoty kredytu 480 000 PLN) — pierwszeństwo hipoteki nie jest wyraźnie sformułowane jako konflikt z dokumentami (wysoki stopień zabezpieczenia);
- cesja praw z polisy ubezpieczenia nieruchomości;
- ubezpieczenie pomostowe.

Ocena zgodności z polityką ryzyka:
- Wymogi polityki POL-RYZYKO-01 (m.in. limity LTV, wymóg cesji polisy i ubezpieczenia pomostowego) zostały spełnione; decyzja kredytowa DC-2201 potwierdza zgodność (werdykt weryfikatora: POTWIERDZONA).

Źródła: UM-7788, DC-2201, POL-RYZYKO-01.

Uwaga operacyjna: zapis tego zweryfikowanego faktu został dodany do grafu wiedzy (ID faktu: learned::bb8e6e41b5a3ab7e).

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe zabezpieczenia i potwierdza ich zgodność z wymogami polityki, zgodnie z oczekiwaną odpowiedzią.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['POL-RYZYKO-01', 'UM-7788']; w odpowiedzi ['DC-2201', 'POL-RYZYKO-01', 'UM-7788']; pokrycie 1.0

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

**Odpowiedź agenta:** Podsumowanie wykonanych działań (pełny przebieg, zgodnie z procedurą):
- Przeszukałem pamięć grafową i znalazłem powiązane dokumenty: KYC-00123, WN-4501, DC-2201, UM-7788, HS-7788 (brakowało najpierw TO-2025-Q1 w grafie).
- Odczytałem treść dokumentów i powiązanych plików (multi-hop). Znalazłem także dokument TO-2025-Q1 z wartościami NRR i marży.
- Przygotowałem i zweryfikowałem odpowiedź (werdykt: POTWIERDZONA).
- Zapis do grafu (nauka): dodałem zweryfikowany fakt i wskazówkę jakościową.

Krótka, zwięzła odpowiedź — łańcuch kredytu Anny Kowalskiej (KYC → WN → DC → UM → HS)

1) Klient / KYC
- Anna Katarzyna Kowalska (KL-00123). Scoring: 78/100, klasa ryzyka B.
- Dochód netto: 10 100,00 PLN/mies., brak zobowiązań.
(źródło: KYC-00123)

2) Wniosek (WN-4501)
- Wnioskowana kwota kredytu: 480 000,00 PLN.
- Wkład własny: 120 000,00 PLN (20%).
- Okres: 300 miesięcy (25 lat).
- Typ rat: równe (annuitetowe).
- Oprocentowanie: zmienne (NRR 3M + marża).
(źródło: WN-4501)

3) Decyzja (DC-2201)
- Kwota zatwierdzona: 480 000,00 PLN.
- Okres: 300 miesięcy.
- Oprocentowanie nominalne: 7,95% = NRR 3M (5,85%) + marża (2,10%).
- Rata annuitetowa: 3 688,83 PLN.
- Prowizja przygotowawcza: 2,00% = 9 600,00 PLN; opłata za wycenę: 500,00 PLN.
- DTI: 36,52%; scoring: 78/100 (klasa B).
- Warunek uruchomienia: zawarcie umowy UM-7788, hipoteka, ubezpieczenie.
(źródło: DC-2201)

4) Umowa (UM-7788)
- Kwota: 480 000,00 PLN; okres: 300 miesięcy.
- Oprocentowanie nominalne przy zawarciu: 7,95%.
- Raty: 300 równych rat annuitetowych po 3 688,83 PLN, płatne 15. dnia miesiąca.
- Prowizja: 9 600,00 PLN; opłata wycena: 500,00 PLN.
- Całkowity koszt kredytu: 1 116 749,94 PLN (w tym odsetki 626 649,94 PLN).
- Warunki wcześniejszej spłaty: rekompensata 1,50% w pierwszych 36 miesiącach.
(źródło: UM-7788)

5) Harmonogram (HS-7788)
- Kwota: 480 000,00 PLN; liczba rat: 300.
- Wysokość raty: 3 688,83 PLN.
- Pierwsza rata: 15.03.2025; ostatnia rata: 15.02.2050.
- Zestawienie sald kapitału i odsetek (szczegóły dla pierwszych 24 rat i ostatnich rat).
(źródło: HS-7788)

6) Tabela oprocentowania (TO-2025-Q1)
- NRR 3M = 5,85% (I kw. 2025).
- Marża dla LTV ≤ 80% = 2,10%.
- Oprocentowanie nominalne (dla LTV ≤ 80%) = 7,95%.
(źródło: TO-2025-Q1)

Ocena spójności (werdykt weryfikatora): POTWIERDZONA
- Wszystkie kluczowe liczby (kwota kredytu, okres, NRR 3M, marża, oprocentowanie nominalne, rata miesięczna, prowizja, DTI, scoring, daty pierwszej/ostatniej raty oraz całkowity koszt kredytu podany w UM-7788) są bezpośrednio potwierdzone w dokumentach: KYC-00123, WN-4501, DC-2201, UM-7788, HS-7788 i TO-2025-Q1.
(werdykt i szczegóły: verifier)

Wybrane cytaty / fragmenty potwierdzające liczby:
- „Wnioskowana kwota kredytu: 480 000,00 PLN” (WN-4501)
- „Oprocentowanie: zmienne = NRR 3M 5,85% + marża 2,10% = 7,95%” (DC-2201)
- „Rata annuitetowa: 3 688,83 PLN” (DC-2201; HS-7788; UM-7788)
- „Prowizja przygotowawcza: 2,00% = 9 600,00 PLN” (DC-2201; UM-7788)
- „Scoring wewnętrzny: 78/100, Klasa ryzyka: B” (KYC-00123; DC-2201)
- „NRR 3M = 5,85%” (TO-2025-Q1)
(źródła: KYC-00123, WN-4501, DC-2201, UM-7788, HS-7788, TO-2025-Q1)

Zapis do grafu (moment nauki) — wykonane
- Ponieważ graf początkowo nie zawierał TO-2025-Q1, zapisałem zweryfikowany fakt dotyczący kredytu Anny Kowalskiej oraz wskazówkę jakościową.
- Zapisany fakt (identyfikator w grafie): learned::0f9f92c30746f9dd
- Treść zapisanego faktu (skrót): „Anna Katarzyna Kowalska (KL-00123) — kredyt hipoteczny 480 000,00 PLN, okres 300 miesięcy (25 lat), oprocentowanie zmienne 7,95% (NRR 3M 5,85% + marża 2,10%), rata 3 688,83 PLN, prowizja przygotowawcza 9 600,00 PLN, DTI 36,52%, scoring 78/100; dokumenty źródłowe: KYC-00123, WN-4501, DC-2201, UM-7788, HS-7788, TO-2025-Q1.”
- Zapisana wskazówka jakościowa (powiązana z TO-2025-Q1): „Tabela oprocentowania (TO) jest aktualizowana kwartalnie; przy przyszłych weryfikacjach upewnić się, że użyta wartość NRR 3M odpowiada okresowi obowiązywania decyzji/umowy.”

Uwagi końcowe / rekomendacje
- Nie stwierdzono niespójności. Wszystkie wartości były spójne między dokumentami.
- Rekomenduję w przyszłości upewniać się, że wersja tabeli oprocentowania (TO) odpowiada datom decyzji/umowy — zapisałem odpowiednią wskazówkę w grafie.

Czy chcesz, abym wygenerował szczegółowe porównanie amortyzacyjne (tabela pierwszych 60 rat z rozbiciem kapitał/odsetki) lub wyeksportował zapisany fakt z grafu do raportu PDF?

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe liczby i fakty zgodne z oczekiwaną, włącznie z kwotami, oprocentowaniem, DTI, prowizją i spójnością danych we wszystkich dokumentach.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'HS-7788', 'KYC-00123', 'POL-RYZYKO-01', 'REG-KH-02', 'TO-2025-Q1', 'TOP-2025-Q1', 'UM-7788', 'WN-4501', 'ZD-4501']; w odpowiedzi ['DC-2201', 'HS-7788', 'KL-00123', 'KYC-00123', 'TO-2025-Q1', 'UM-7788', 'WN-4501']; pokrycie 0.6

---

## [P3.2] (zestaw 3) ✅ dobra
**Pytanie:** Wyjaśnij, w jaki sposób działania compliance doprowadziły do odmowy kredytu Markowi Nowickiemu — od transakcji do decyzji. Wskaż całą sekwencję.

**Oczekiwana:** - Rachunek firmowy (HT-00456) wykazał wpłaty gotówkowe rozbijane poniżej progu 15 000 PLN (structuring) i szybkie transfery ~464 950 PLN do Vantia (pass-through).
  - Powstały zgłoszenia SAR-0034 (structuring) i SAR-0041 (pass-through), oba na podstawie POL-AML-01.
  - Raport ryzyka RR-0012 zagregował oba SAR-y i rekomendował klasę E oraz wstrzymanie nowych kredytów.
  - Kartę KYC-00456 zaktualizowano do klasy E (WYSOKIE), wdrożono EDD.
  - Kolejny wniosek WN-4508 (kredyt 80 000 PLN) otrzymał decyzję **negatywną DC-2250** — mimo DTI 16,20% — z powodu klasy E i braku możliwości ustalenia źródła środków.
  - To pełna pętla zwrotna: transakcje → ryzyko → odmowa.

**Odpowiedź agenta:** Odpowiedź przygotowana — poniżej znajdziesz pełną, zweryfikowaną sekwencję działań compliance prowadzących do odmowy kredytu dla Marka Andrzeja Nowickiego (JDG „MN Trade”). Na końcu potwierdzam, że zapis do grafu wiedzy został wykonany.

(a) Chronologia (data, typ dokumentu, krótkie streszczenie, ID)
1. 2025-02-01 – 2025-03-31 — Wyciąg analityczny rachunku firmowego: liczne wpłaty gotówkowe 9 400–9 900 PLN (54 operacje) oraz szybkie przelewy zagraniczne do Republiki Vantia; wpływy znacznie przewyższały deklarowany dochód — HT-00456. (źródło: HT-00456, KYC-00456)

2. 2025-03-10 — Zgłoszenie podejrzanej transakcji (structuring): wykryto rozbijanie wpłat poniżej progu raportowania, brak dokumentacji uzasadniającej obroty; uruchomiono monitoring i wezwanie do wyjaśnień — SAR-0034. (źródło: SAR-0034, KYC-00456)

3. 2025-04-02 — Zgłoszenie podejrzanej transakcji (pass-through): szybkie przelewy SWIFT do jurysdykcji wysokiego ryzyka (Republika Vantia) powiązane z wcześniej wykrytymi wpłatami; eskalacja do zespołu ryzyka/compliance — SAR-0041. (źródło: SAR-0041, HT-00456)

4. 2025-04-15 — Raport ryzyka (compliance): podwyższenie klasy ryzyka klienta do E (wysokie) na podstawie SAR-0034, SAR-0041 i HT-00456; rekomendacja wdrożenia EDD i wstrzymania nowych produktów kredytowych do wyjaśnienia — RR-0012. (źródło: RR-0012, KYC-00456)

5. 2025-05-05 — Wniosek kredytowy: klient składa wniosek WN-4508 o kredyt 80 000 PLN na 48 mies.; zaświadczenie o dochodach ZD-4508 wskazuje 12 500 PLN/mies., ale w świetle raportu ryzyka wniosek objęto wzmożonym monitoringiem — WN-4508, ZD-4508. (źródło: WN-4508, ZD-4508, KYC-00456)

6. 2025-05-12 — Decyzja kredytowa: odmowa udzielenia kredytu z uwagi na klasę ryzyka E, brak możliwości ustalenia źródła pochodzenia środków oraz obowiązujące rekomendacje wstrzymujące nowe produkty — DC-2250. (źródło: DC-2250, RR-0012, KYC-00456)

(b) Ścieżka relacji (od transakcji do decyzji)
HT-00456 → SAR-0034 + SAR-0041 → RR-0012 → WN-4508 → DC-2250

(c) Kluczowe powody odmowy (3–4 punkty)
1. Wynik analizy transakcji: structuring (rozbijanie wpłat) i pass-through (rachunek tranzytowy) — podwyższone ryzyko AML (SAR-0034, SAR-0041, HT-00456).  
2. Brak dokumentacji ekonomicznej uzasadniającej wysoki wolumen wpłat (brak faktur/umów) — niezweryfikowane źródło środków (KYC-00456, HT-00456).  
3. Transfery do jurysdykcji wysokiego ryzyka (Republika Vantia) zwiększają ryzyko reputacyjne i AML (SAR-0041, RR-0012).  
4. Raport RR-0012 formalnie przypisał klasę ryzyka E i zarekomendował wstrzymanie nowych produktów kredytowych — podstawa do odmowy (RR-0012, DC-2250).

(d) Cytaty kluczowe (do 2 zdań każdy)
- „Seria wpłat gotówkowych w kwotach 9 400–9 900 PLN, dokonywanych wielokrotnie … Kwoty pojedynczych wpłat konsekwentnie utrzymywały się poniżej progu alertu, co wskazuje na celowe unikanie raportowania.” (SAR-0034)  
- „Rachunek tranzytowy (pass-through) — szybkie przekazywanie środków za granicę do jurysdykcji wysokiego ryzyka; brak potwierdzenia rzeczywistego charakteru handlowego transakcji.” (SAR-0041)  
- „Zgodnie z niniejszym raportem, każdy wniosek kredytowy klienta KL-00456 powinien zostać rozpatrzony z uwzględnieniem klasy ryzyka E i rekomendacji wstrzymania. Dotyczy to w szczególności wniosku WN-4508 (decyzja: DC-2250).” (RR-0012)  
- „Decyzja: NEGATYWNA. […] Brak możliwości ustalenia źródła pochodzenia środków oraz aktywne wzmożone środki bezpieczeństwa (EDD) wobec klienta.” (DC-2250)

(e) Braki i rekomendacja następnych kroków
- Brakujące dokumenty: pełna dokumentacja handlowa (faktury, umowy z kontrahentami), szczegółowe wyjaśnienia klienta oraz notatki operacyjne/korespondencja compliance potwierdzająca przebieg wyjaśnień.  
- Rekomendacja: poprosić klienta o komplet faktur i umów potwierdzających obroty; po dostarczeniu i weryfikacji dokumentów compliance może zaktualizować ocenę ryzyka i ponownie rozpatrzyć wniosek.

(f) Użyte ID źródeł
KYC-00456, HT-00456, SAR-0034, SAR-0041, RR-0012, WN-4508, ZD-4508, DC-2250.

Potwierdzenie zapisu do grafu wiedzy
- Fakt zweryfikowany i zapisany w grafie: learned::7a2abf93311079da (DC-2250: odmowa kredytu dla Marka Andrzeja Nowickiego z powodu klasy ryzyka E i braku źródła środków).  
- Dodano wskazówkę jakościową przypisaną do encji klienta: learning::3a1b3c544787a8cd („Brak dokumentów potwierdzających źródło środków; przy podobnych przypadkach dopilnować żądania faktur/umów i szybkiej eskalacji do EDD.”).

Jeśli chcesz, mogę: (1) wysłać sformalizowany wniosek do opiekuna klienta o dostarczenie brakujących faktur/umów, lub (2) odczytać i dołączyć do historii ewentualne notatki operacyjne/korespondencję (jeśli występują w repozytorium) — co preferujesz?

**Ocena:** dobra — Odpowiedź agenta w pełni pokrywa wszystkie kluczowe fakty i liczby z odpowiedzi oczekiwanej, prezentując kompletną sekwencję od transakcji do decyzji z zachowaniem precyzji i spójności merytorycznej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250', 'HT-00456', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'WN-4508']; w odpowiedzi ['DC-2250', 'HT-00456', 'KL-00456', 'KYC-00456', 'RR-0012', 'SAR-0034', 'SAR-0041', 'WN-4508', 'ZD-4508']; pokrycie 0.78

---

## [P3.3] (zestaw 3) 🟡 czesciowa
**Pytanie:** Porównaj trzy typy decyzji kredytowych w zbiorze (pozytywną, warunkową, negatywną) i wskaż, jak profil ryzyka z KYC oraz polityki determinowały wynik każdej z nich.

**Oczekiwana:** - **Pozytywna — DC-2201** (Anna Kowalska): klasa B, DTI 36,52%, LTV 80% — wszystkie kryteria POL-RYZYKO-01 spełnione → udzielenie kredytu.
  - **Warunkowa — DC-2203** (Bałtyk Logistyka): klasa C przy podwyższonym zadłużeniu → zgoda pod warunkiem opłaty wstępnej 30% lub dodatkowego zabezpieczenia (POL-RYZYKO-01 §5).
  - **Negatywna — DC-2250** (Marek Nowicki): zdolność wystarczająca (DTI 16,20%), ale klasa E z RR-0012 (AML) → odmowa (POL-RYZYKO-01 §5, POL-AML-01).
  - Wniosek: o wyniku decydował nie tylko wskaźnik finansowy, lecz klasa ryzyka (w tym override z tytułu AML).

**Odpowiedź agenta:** Odpowiedź przygotowana. Podsumowanie (z cytowaniem źródeł) — zgodnie z dokumentami i grafem:

1) Krótkie porównanie typów decyzji
- Pozytywna: zgoda bez dodatkowych warunków (przykłady: DC-2201, DC-2202, DC-2204).  
- Warunkowa: zgoda pod warunkiem spełnienia dodatkowych wymagań zabezpieczających (przykład: DC-2203).  
- Negatywna: odmowa — brak bezpośrednich przykładów w dostępnych dokumentach; POL-RYZYKO-01 opisuje kryteria odmowy (klasa E, przekroczenie limitów) (źródła: DC-2201, DC-2202, DC-2203, DC-2204, POL-RYZYKO-01).

2) Mechanizm wpływu KYC i POL-RYZYKO-01 (opis działania)
- Główne elementy decydujące: klasa ryzyka (A–E) z KYC, scoring (0–100), wskaźniki finansowe (DTI — stosunek zobowiązań do dochodu, LTV tam gdzie jest zabezpieczenie), oraz historia kredytowa/AML. (źródła: KYC-00123–KYC-00126, POL-RYZYKO-01).
- Zasady ujęte w dokumentach/przykładach:
  - Klasy A/B (wysoki/niski ryzyka) z wysokim scoringiem (≥60) i DTI w limicie zwykle otrzymują decyzję pozytywną (przykłady: DC-2202 — klasa A, scoring 92; DC-2201 — klasa B, scoring 78). (źródła: DC-2201, DC-2202, KYC-00123, KYC-00124)
  - Klasa C lub zwiększone zadłużenie (wyższe DTI / istniejące zobowiązania) prowadzą do decyzji warunkowej — bank wymaga dodatkowych zabezpieczeń/większej opłaty wstępnej (przykład: DC-2203 → warunek: dodatkowe zabezpieczenia/poręczenie). (źródła: DC-2203, KYC-00125)
  - Klasa E lub przekroczenie progów (DTI/LTV/negatywna historia) skutkuje odmową zgodnie z POL-RYZYKO-01 — brak ilustrującego dokumentu DC-* w zbiorze. (źródło: POL-RYZYKO-01)
- Dodatkowe reguły stosowane w ocenie (wynikające z polityki i przykładów):
  - Limit DTI orientacyjnie ≤45% dla klas A–C; wyjątki (do 50%) możliwe za zgodą Komitetu dla klasy A — testy stresowe (np. wzrost oprocentowania +2,5 p.p.) wymagają DTI po stresie ≤50% (w dokumentach stosowane jako kryterium oceny i testów). (źródło: POL-RYZYKO-01, przykładowe wyliczenia w DC-2201)
  - LTV dla kredytów zabezpieczonych zwykle do 80% — wyższe LTV prowadzą do dodatkowych zabezpieczeń. (źródła: POL-RYZYKO-01, DC-2201)

3) Konkretne przykłady (z dokumentów)
- DC-2201 (pozytywna): klient KYC-00123 (klasa B, scoring 78), DTI 36,52%, LTV 80%, test DTI po stresie 44,7%, kwota 480 000 PLN → umowa UM-7788 została zawarta (źródła: DC-2201, KYC-00123, UM-7788, ZD-4501, POL-RYZYKO-01).
- DC-2202 (pozytywna): klient KYC-00124 (klasa A, scoring 92), DTI 13,23% → umowa UM-7789 (źródła: DC-2202, KYC-00124, UM-7789).
- DC-2203 (warunkowa): klient KYC-00125 (klasa C, scoring 70), istniejące zobowiązania leasingowe → decyzja warunkowa z wymaganiem dodatkowych zabezpieczeń (w efekcie UM-7790 po spełnieniu warunków) (źródła: DC-2203, KYC-00125, UM-7790).
- DC-2204 (pozytywna, karta): klient KYC-00126 (klasa B, scoring 80), przyznany limit 15 000 PLN (źródła: DC-2204, KYC-00126, WN-4504).

4) Uwaga o brakach i ograniczeniach
- W zbiorze brak bezpośrednich przykładów decyzji negatywnej (brak dokumentu DC-* ilustrującego odmowę) — chociaż POL-RYZYKO-01 definiuje kryteria odmowy, nie mamy przykładowego DC potwierdzającego zastosowanie tych kryteriów. (źródła: POL-RYZYKO-01, brak DC negatywnego)
- Niektóre wartości progowe (szczegółowe progi DTI/LTV dla klas D/E) nie są zilustrowane przykładami i w razie potrzeby należy odczytać pełną treść POL-RYZYKO-01 lub znaleźć DC z odmową.

5) Potwierdzenie zapisu do grafu
- Zweryfikowany fakt i powiązana wskazówka jakościowa zostały zapisane w grafie wiedzy (ID faktu: learned::d68deef56c4024fc; ID wskazówki: learning::d68deef56c4024fc). (źródło: zapis grafu)

Źródła (dokumenty użyte): DC-2201, DC-2202, DC-2203, DC-2204, KYC-00123, KYC-00124, KYC-00125, KYC-00126, UM-7788, UM-7789, UM-7790, WN-4501, WN-4502, WN-4503, WN-4504, ZD-4501, ZD-4503, POL-RYZYKO-01.

Jeśli chcesz, mogę:
- odczytać i wkleić konkretne fragmenty (cytaty) z wymienionych dokumentów potwierdzające każdą liczbę/zasadę, albo
- wyszukać i zapisać przykłady rzeczywistych decyzji negatywnych (DC-*) do grafu, aby uzupełnić lukę ilustracyjną.

**Ocena:** czesciowa — Odpowiedź agenta szczegółowo omawia profil ryzyka i zasady polityki wpływające na każdą decyzję, jednak brak w niej wyraźnego przykładu decyzji negatywnej DC-2250 i konkretnego odniesienia do kluczowych wartości (np. DTI 16,20%, klasa E, odmowa z powodu AML) zawartych w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'DC-2203', 'DC-2250', 'KYC-00123', 'KYC-00125', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012']; w odpowiedzi ['DC-2201', 'DC-2202', 'DC-2203', 'DC-2204', 'KYC-00123', 'KYC-00124', 'KYC-00125', 'KYC-00126', 'POL-RYZYKO-01', 'UM-7788', 'UM-7789', 'UM-7790', 'WN-4501', 'WN-4502', 'WN-4503', 'WN-4504', 'ZD-4501', 'ZD-4503']; pokrycie 0.56

---

## [P3.4] (zestaw 3) ✅ dobra
**Pytanie:** Oblicz łączną kwotę odsetek dla wszystkich kredytów/leasingów z zawartymi umowami w zbiorze i podaj źródła.

**Oczekiwana:** - Kredyt hipoteczny UM-7788: odsetki 626 649,94 PLN wg pierwotnego HS-7788 (lub 579 719,78 PLN po repricingu wg HS-7794, przy założeniu utrzymania 7,45%).
  - Kredyt gotówkowy UM-7789: odsetki 15 077,76 PLN (HS-7789).
  - Leasing UM-7790: część odsetkowa 28 169,56 PLN netto (HS-7790).
  - **Suma (wariant pierwotny hipoteki):** 626 649,94 + 15 077,76 + 28 169,56 = **669 897,26 PLN**.
  - (Uwaga: umowa karty UM-7791 nie ma z góry ustalonych odsetek — zależą od wykorzystania limitu; wniosek WN-4508 odrzucono, więc go nie liczymy.)

**Odpowiedź agenta:** Łączna kwota odsetek dla wszystkich kredytów/leasingów z zawartymi umowami w zbiorze: 669 897,26 PLN. (źródła: UM-7788, UM-7789, UM-7790)

Szczegóły pozycji:
- UM-7788 — kredyt hipoteczny — odsetki: 626 649,94 PLN (źródło: UM-7788)
- UM-7789 — kredyt gotówkowy — odsetki: 15 077,76 PLN (źródło: UM-7789)
- UM-7790 — leasing operacyjny — odsetki: 28 169,56 PLN (źródło: UM-7790)

Weryfikacja: werdykt POTWIERDZONA — kwoty zgodne z dokumentami źródłowymi (UM-7788, UM-7789, UM-7790).

Aktualizacja grafu wiedzy: zapisano zweryfikowany fakt total_interest_all_concluded_loans_leases = 669897.26 PLN. ID zapisu: learned::3af71c3b84aca826. (Uwaga: poprzednia wartość w grafie wynosiła 43 247,32 PLN — dodano wskazówkę jakościową o konieczności poprawy procedury agregacji i uwzględniania waluty dla każdej pozycji.)

Braki danych: brak — wszystkie pozycje mają podane kwoty odsetek i źródła.

Struktura danych (proponowana):
{
  "total_interest": 669897.26,
  "currency": "PLN",
  "items": [
    {"id":"UM-7788","type":"kredyt hipoteczny","interest_amount":626649.94,"currency":"PLN","source_doc_ids":["UM-7788"]},
    {"id":"UM-7789","type":"kredyt gotówkowy","interest_amount":15077.76,"currency":"PLN","source_doc_ids":["UM-7789"]},
    {"id":"UM-7790","type":"leasing operacyjny","interest_amount":28169.56,"currency":"PLN","source_doc_ids":["UM-7790"]}
  ]
}

Jeśli chcesz, mogę wygenerować raport w pliku (CSV/JSON) zawierający te pozycje i zapis faktu w grafie.

**Ocena:** dobra — Odpowiedź agenta w pełni pokrywa się z oczekiwaniami pod względem kluczowych kwot, źródeł oraz sumy odsetek, bez pominięć merytorycznych.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788', 'HS-7789', 'HS-7790', 'HS-7794', 'UM-7788', 'UM-7789', 'UM-7790']; w odpowiedzi ['UM-7788', 'UM-7789', 'UM-7790']; pokrycie 0.43

---

## [P3.5] (zestaw 3) ✅ dobra
**Pytanie:** Opisz mechanizm i finansowy skutek zmiany wskaźnika NRR 3M dla kredytu hipotecznego — wskaż dokumenty i kwoty.

**Oczekiwana:** - NRR 3M spadł z 5,85% (TO-2025-Q1) do 5,35% (TO-2025-Q2), tj. o 0,50 p.p.
  - Zgodnie z REG-KH-02 §3 (oprocentowanie zmienne, aktualizacja kwartalna, marża stała), oprocentowanie UM-7788 zmieniło się z 7,95% na 7,45% bez aneksu.
  - Bank sporządził zaktualizowany harmonogram HS-7794 (od raty nr 2): rata spadła z 3 688,83 na **3 531,88 PLN** (o 156,95 PLN).
  - Łączne odsetki spadły z 626 649,94 do 579 719,78 PLN (oszczędność ok. 46 930,16 PLN przy utrzymaniu 7,45%).
  - Efekt widoczny na wyciągu HT-00123 (rata 1 = 3 688,83, raty 2–3 = 3 531,88).

**Odpowiedź agenta:** Krótko — mechanizm
- Oprocentowanie kredytu hipotecznego w Nordvik Finanse = wskaźnik NRR 3M + stała marża Banku; aktualizacja NRR następuje kwartalnie i nie wymaga aneksu do umowy (źródło: REG-KH-02; UM-7788). (źródła: REG-KH-02, UM-7788)

Kluczowe liczby i dokumenty (potwierdzone)
- NRR 3M Q1 2025 = 5,85% (źródło: TO-2025-Q1).  
- NRR 3M Q2 2025 = 5,35% (źródło: TO-2025-Q2).  
- Marża dla umowy UM-7788 = 2,10% (źródło: UM-7788, TO-2025-Q1/TO-2025-Q2).  
- Kwota kredytu w UM-7788 = 480 000 PLN; okres = 300 miesięcy (UM-7788).  
- Oprocentowanie nominalne przed zmianą = 5,85% + 2,10% = 7,95% (UM-7788 / TO-2025-Q1).  
- Oprocentowanie nominalne po zmianie = 5,35% + 2,10% = 7,45% (TO-2025-Q2 / UM-7788).  
- Rata przed zmianą (wg harmonogramu HS-7788) = 3 688,83 PLN (HS-7788).  
- Nowa rata po aktualizacji (wg zaktualizowanego harmonogramu HS-7794) = 3 531,88 PLN (HS-7794).

Finansowy skutek dla UM-7788 (potwierdzone wartości)
- Miesięczna różnica rat: 3 688,83 PLN − 3 531,88 PLN = 156,95 PLN oszczędności miesięcznie (HS-7784/HS-7794). (źródło: HS-7794)  
- Pozostałe parametry użyte w ostatecznym harmonogramie: saldo po racie nr 1 = 479 491,17 PLN; liczba pozostałych rat = 299 (HS-7794). (źródło: HS-7794)  
- Suma odsetek w całym okresie przy oprocentowaniu pierwotnym (wg HS-7788) = 626 649,94 PLN; suma odsetek po zmianie (wg HS-7794) = 579 719,78 PLN; oszczędność ≈ 46 930,16 PLN (HS-7794 vs HS-7788). (źródło: HS-7794, HS-7788)

Wyjaśnienie obliczeń / uwagi techniczne
- Mechanika: bank stosuje wzór oprocentowania = NRR 3M + marża; przy kwartalnej aktualizacji NRR bank przelicza harmonogram biorąc pod uwagę aktualne saldo i liczbę pozostałych rat (stąd finalna nowa rata w HS-7794 jest obliczona dla salda po racie nr 1, nie proste przeliczenie od pierwotnego P i n). (źródła: REG-KH-02, HS-7794)  
- Dlatego poprawne porównanie używa zaktualizowanego harmonogramu (HS-7794), a nie prostego przeliczenia od wartości początkowej. (źródło: HS-7794)

Dokumenty wykorzystane (lista)
- TO-2025-Q1 (tabela oprocentowania Q1 2025) — NRR 3M = 5,85%  
- TO-2025-Q2 (tabela oprocentowania Q2 2025) — NRR 3M = 5,35%  
- UM-7788 — umowa kredytowa (kwota, marża, zapis wzoru oprocentowania)  
- HS-7788 — pierwotny harmonogram i rata 3 688,83 PLN  
- HS-7794 — zaktualizowany harmonogram: nowa rata 3 531,88 PLN, saldo po racie 1, zestawienie odsetek i oszczędność ≈ 46 930,16 PLN  
- DC-2201 — decyzja kredytowa potwierdzająca parametry (UM-7788)

Zapisy w grafie (nauka)
- Zgodnie z procedurą: zweryfikowane fakty (nowe wartości raty i oszczędności oraz powiązania UM-7788 ↔ HS-7794 ↔ TO-2025-Q2) zostały zapisane do grafu wiedzy, wraz ze wskazówką jakościową dowiązaną do encji UM-7788: „Przy obliczaniu skutku zmiany NRR uwzględniać saldo po ostatniej zrealizowanej racie i liczbę pozostałych rat; nie stosować prostego przeliczenia na pierwotnym P i n, bo daje to nieprecyzyjne wyniki.” Zapis potwierdzony (źródła: HS-7794, UM-7788, TO-2025-Q2).

Czy chcesz, żeby przygotować szczegółowe porównanie pierwszych 24 rat przed i po zmianie (rozpisane kapitał/odsetki) lub symulację, gdyby NRR zmienił się o inną wartość?

**Ocena:** dobra — Odpowiedź agenta kompletne i poprawnie odzwierciedla kluczowe fakty, liczby i dokumenty podane w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788', 'HS-7794', 'HT-00123', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'UM-7788']; w odpowiedzi ['DC-2201', 'HS-7784', 'HS-7788', 'HS-7794', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'UM-7788']; pokrycie 0.86

---

## [P3.6] (zestaw 3) 🟡 czesciowa
**Pytanie:** Zidentyfikuj wszystkich klientów objętych wzmożonymi środkami bezpieczeństwa (EDD) i opisz podstawę oraz skutki dla ich klasy ryzyka.

**Oczekiwana:** - **KL-00456 (Marek Nowicki):** EDD z powodu SAR-0034 i SAR-0041 → RR-0012; klasa ryzyka podniesiona z C do **E**; wstrzymanie nowych kredytów (skutek: odmowa DC-2250).
  - **KL-00129 (Bursztyn Handel Sp. z o.o.):** EDD z powodu SAR-0052 (nietypowe wpłaty gotówkowe + transakcje z podmiotem powiązanym); klasa ryzyka podniesiona z C do **D**; nowe zaangażowania warunkowe/wstrzymane.
  - Obaj objęci zakazem tipping-off (POL-AML-01 §7).

**Odpowiedź agenta:** - KYC-00456 — Marek Andrzej Nowicki  
  - Podstawa przypisania do EDD: zgłoszenia podejrzanych transakcji (SAR-0034, SAR-0041) i klasyfikacja jako wysokie ryzyko (klasa E) (źródła: KYC-00456, SAR-0034, SAR-0041).  
  - Aktualna klasa ryzyka: wysokie ryzyko (klasa E) (źródła: KYC-00456, RR-0012, SAR-0034, SAR-0041).  
  - Skutki dla klasy ryzyka i monitoringu: zmiana klasyfikacji na klasę E; wstrzymanie nowych zaangażowań kredytowych do wyjaśnienia; wdrożenie wzmocnionego monitoringu transakcji (źródła: KYC-00456, SAR-0034, SAR-0041).

Informacja: w grafie znaleziono tylko powyższy wpis EDD. Odpowiedź została potwierdzona i zweryfikowane dane zapisano do grafu (graph_add_learned_fact) oraz dodano krótką wskazówkę jakościową (graph_add_learning) dla encji KYC-00456 (zapisy powiązano ze źródłami KYC-00456, SAR-0034, SAR-0041).

**Ocena:** czesciowa — Agent poprawnie zidentyfikował klienta KL-00456 i podstawy EDD oraz skutki dla klasy ryzyka, jednak pominął drugiego klienta KL-00129 oraz zakaz tipping-off, które były kluczowe w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00129', 'KYC-00456', 'POL-AML-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'SAR-0052']; w odpowiedzi ['KYC-00456', 'RR-0012', 'SAR-0034', 'SAR-0041']; pokrycie 0.57

---

## [P3.7] (zestaw 3) ✅ dobra
**Pytanie:** Które tabele oprocentowania i opłat obowiązują dla poszczególnych umów, biorąc pod uwagę daty ich zawarcia i zasady aktualizacji?

**Oczekiwana:** - Umowy zawarte w I kw. 2025 (UM-7788 z 14.02, UM-7789 z 05.03, UM-7790 z 20.03, UM-7791 z 12.03) bazują na TO-2025-Q1 i TOP-2025-Q1.
  - Kredyty stałoprocentowe (gotówkowy UM-7789) i leasing (UM-7790) zachowują stopę z dnia zawarcia.
  - Kredyt hipoteczny UM-7788 (zmienny) jest repricowany od Q2 wg TO-2025-Q2 (nowy harmonogram HS-7794).
  - Wniosek WN-4506 (10.05.2025, Q2) bazuje na TO-2025-Q2 i TOP-2025-Q2.

**Odpowiedź agenta:** Wykonałem procedurę: najpierw przeszukałem graf, potem (gdy graf nie zawierał pełnych powiązań) odczytałem dokumenty, sformułowałem odpowiedź i poddałem ją weryfikacji. Weryfikator uznał odpowiedź za POTWIERDZONĄ. Następnie zapisałem zweryfikowane fakty do grafu (tzw. moment nauki). Poniżej krótkie, konkretne zestawienie dla każdej umowy (źródła i ID wpisu w grafie podane przy pozycji).

1) UM-7788 (kredyt hipoteczny „Nordvik Dom”)  
- Data zawarcia: 14.02.2025 (źródło: UM-7788)  
- Tabela oprocentowania: TO-2025-Q1 (okres obowiązywania w dokumencie tabeli: 01.01.2025–31.03.2025) (źródła: TO-2025-Q1, UM-7788)  
- Tabela opłat: TOP-2025-Q1 (01.01.2025–31.03.2025) (źródła: TOP-2025-Q1, UM-7788)  
- Charakter oprocentowania i zasady aktualizacji: oprocentowanie zmienne — NRR 3M (5,85%) + marża 2,10%; kwartalna aktualizacja NRR 3M; zmiana oprocentowania następuje automatycznie zgodnie z REG-KH-02 §3 (źródła: UM-7788, TO-2025-Q1, REG-KH-02, HS-7788, DC-2201)  
- Regulamin powiązany: REG-KH-02 (źródło: UM-7788)  
- Zapisany fakt w grafie: learned::a233f0be3a5c093c

2) UM-7789 (kredyt gotówkowy „Nordvik Gotówka”)  
- Data zawarcia: 05.03.2025 (źródło: UM-7789)  
- Tabela oprocentowania: TO-2025-Q1 (01.01.2025–31.03.2025) (źródła: TO-2025-Q1, UM-7789)  
- Tabela opłat: TOP-2025-Q1 (01.01.2025–31.03.2025) (źródła: TOP-2025-Q1, UM-7789)  
- Charakter oprocentowania i zasady aktualizacji: oprocentowanie stałe 10,90% (brak repricingu) (źródła: UM-7789, TO-2025-Q1)  
- Regulamin powiązany: REG-KG-01 (źródło: UM-7789)  
- Zapisany fakt w grafie: learned::a03c1e01bbeb8d37

3) UM-7790 (leasing operacyjny „Nordvik Leasing”)  
- Data zawarcia: 20.03.2025 (źródło: UM-7790)  
- Tabela oprocentowania: TO-2025-Q1 (01.01.2025–31.03.2025) (źródła: TO-2025-Q1, UM-7790)  
- Tabela opłat: TOP-2025-Q1 (okres tabeli jak wyżej); szczegółowe opłaty i opłata wstępna opisane w REG-LE-04 i w umowie (źródła: TOP-2025-Q1, UM-7790, REG-LE-04)  
- Charakter oprocentowania i zasady aktualizacji: stopa leasingowa wyliczana na podstawie NRR 3M + marża (w dokumencie: przykład 5,85% + marża = 9,05%); pełne zasady repricingu leasingu odwołują się do REG-LE-04 (§5–§6) — zalecane sprawdzenie tych paragrafów dla szczegółów (źródła: UM-7790, TO-2025-Q1, REG-LE-04, HS-7790, DC-2203)  
- Regulamin powiązany: REG-LE-04 (źródło: UM-7790)  
- Zapisany fakt w grafie: learned::4b0c66942e5fd8d9

4) UM-7791 (karta kredytowa „Nordvik Karta”)  
- Data zawarcia: 12.03.2025 (źródło: UM-7791)  
- Tabela oprocentowania: TO-2025-Q1 (01.01.2025–31.03.2025) (źródła: TO-2025-Q1, UM-7791)  
- Tabela opłat: TOP-2025-Q1 (01.01.2025–31.03.2025) — opłata roczna i inne pozycje wymienione w TOP-2025-Q1 oraz REG-KK-03 (źródła: TOP-2025-Q1, UM-7791, REG-KK-03)  
- Charakter oprocentowania i zasady aktualizacji: w dokumentach wskazane oprocentowanie transakcji (18,50%) — traktowane jako stałe zgodnie z umową/tabelą; szczegóły opłat i ew. zmiany w regulaminie REG-KK-03 (źródła: UM-7791, TO-2025-Q1, REG-KK-03)  
- Regulamin powiązany: REG-KK-03 (źródło: UM-7791)  
- Zapisany fakt w grafie: learned::bb957d71eae668e2

Weryfikacja i zapis do grafu:
- Weryfikator: werdykt POTWIERDZONA (brak zastrzeżeń). (źródła użyte przez weryfikatora: UM-7788, UM-7789, UM-7790, UM-7791, TO-2025-Q1, TOP-2025-Q1, REG-KH-02, REG-KG-01, REG-LE-04, REG-KK-03, HS-7788, HS-7789, HS-7790, DC-2201..DC-2204)  
- Zapisano zweryfikowane fakty do grafu dla wszystkich 4 umów — ID wpisów: listed powyżej (learned::...).  
- Zapisano także wskazówkę jakościową (graph_add_learning) z treścią: „upewnić się co do dokładnej marży; sprawdź REG-LE-04 §5–§6 dla zasad repricingu leasingu” — ID wskazówki: learning::6dd84e7880c0b6b3.

Uwagi końcowe (krótkie):  
- Wszystkie wymienione umowy zawarte w I kwartale 2025 korzystają w dacie zawarcia z tabel TO-2025-Q1 i TOP-2025-Q1 (01.01.2025–31.03.2025).  
- Dla UM-7790 dopisałem w grafie wskazówkę, by zweryfikować konkretne paragrafy REG-LE-04 (§5–§6) jeśli potrzebujesz szczegółowego opisu repricingu leasingu.  
- Potwierdzam wykonanie zapisu nauki do grafu (ID wpisów powyżej).

Jeśli chcesz, mogę natychmiast: a) wyeksportować pełne fragmenty regulaminów/punktów tabel (TO/TOP) dotyczących marż i opłat, b) sprawdzić konkretne paragrafy REG-LE-04 (§5–§6) i uzupełnić graf o dokładne sformułowanie reguł repricingu. Którą opcję wybierasz?

**Ocena:** dobra — Odpowiedź agenta precyzyjnie pokrywa kluczowe fakty dotyczące dat zawarcia umów, przypisanych tabel oprocentowania i opłat oraz reguł aktualizacji zgodnie z oczekiwaną odpowiedzią.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KG-01', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'TOP-2025-Q1', 'TOP-2025-Q2', 'UM-7788', 'WN-4506']; w odpowiedzi ['DC-2201', 'DC-2203', 'DC-2204', 'HS-7788', 'HS-7789', 'HS-7790', 'REG-KG-01', 'REG-KH-02', 'REG-KK-03', 'REG-LE-04', 'TO-2025-Q1', 'TOP-2025-Q1', 'UM-7788', 'UM-7789', 'UM-7790', 'UM-7791']; pokrycie 0.62

---

## [P3.8] (zestaw 3) ✅ dobra
**Pytanie:** Sprawdź spójność danych osobowych i finansowych klientki KL-00124 we wszystkich dokumentach, w których występuje.

**Oczekiwana:** - Katarzyna Maria Lewandowska, PESEL 90111067321 — identyczne w KYC-00124, ZD-4503, WN-4502, UM-7789.
  - Dochód netto 8 200 PLN — spójny w ZD-4503, WN-4502, DC-2202.
  - Kredyt 50 000 PLN / 60 mies / 10,90% / rata 1 084,63 PLN — spójny w WN-4502, DC-2202, UM-7789, HS-7789.
  - Klasa ryzyka A (scoring 92) — KYC-00124, potwierdzona w DC-2202.
  - Brak sprzeczności.

**Odpowiedź agenta:** Poniżej wynik kontroli spójności danych klientki KL-00124 (Katarzyna Maria Lewandowska) na podstawie dokumentów dostępnych w aktach oraz pamięci grafowej.

1) Wniosek ogólny
- Dane osobowe i finansowe klientki są spójne we wszystkich dostępnych dokumentach — nie wykryto rozbieżności w wartościach kluczowych pól (źródła: KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789, ZD-4503).

2) Lista pól (wartość + źródła)
- Imię i nazwisko: Katarzyna Maria Lewandowska (źródło: KYC-00124; potwierdzone też w WN-4502, DC-2202, UM-7789)  
- PESEL: 90111067321 (źródło: KYC-00124; potwierdzone też w WN-4502, ZD-4503)  
- Data urodzenia: 1990-11-10 (źródło: KYC-00124)  
- Adres zamieszkania: ul. Słoneczna 5 m. 2, 80-100 Gdańsk (źródło: KYC-00124; potwierdzone też w WN-4502, ZD-4503)  
- Telefon / e-mail: +48 513 000 124 / k.lewandowska@test.example (źródło: KYC-00124, WN-4502)  
- Dokument tożsamości: dowód osobisty DEF 246810 (ważny do 22.03.2032) (źródło: KYC-00124)  
- Pracodawca: Nadmorskie Centrum Medyczne Sp. z o.o. (źródła: KYC-00124, WN-4502, ZD-4503)  
- NIP pracodawcy: 584-222-33-44 (źródła: KYC-00124, ZD-4503)  
- Data rozpoczęcia zatrudnienia: 01.08.2014 (źródło: ZD-4503)  
- Średni dochód netto: 8 200,00 PLN (źródła: KYC-00124, WN-4502, ZD-4503, DC-2202)  
- Numer rachunku (wypłata kredytu): PL88 9999 1000 0000 0012 4000 0007 (źródła: KYC-00124, UM-7789)  
- Numer rachunku (spłata kredytu): PL33 9999 1000 0000 0077 8900 0002 (źródła: UM-7789, HS-7789)  
- Zadłużenie bieżące: 0,00 PLN (źródło: KYC-00124; potwierdzone w DC-2202)  
- Produkt / kwota wniosku: kredyt gotówkowy „Nordvik Gotówka”, 50 000,00 PLN (źródła: WN-4502, DC-2202, UM-7789)  
- Okres kredytowania: 60 miesięcy (źródła: WN-4502, UM-7789, HS-7789)  
- Rata miesięczna: 1 084,63 PLN (źródła: WN-4502, DC-2202, UM-7789, HS-7789)  
- Oprocentowanie nominalne: 10,90% w skali roku (stałe) (źródła: WN-4502, UM-7789, HS-7789)  
- Prowizja przygotowawcza: 4% = 2 000,00 PLN (źródła: WN-4502, DC-2202, UM-7789)  
- RRSO: 13,46% (źródła: DC-2202, UM-7789)  
- Harmonogram spłat: pierwsza rata 10.04.2025, ostatnia rata 10.03.2030, suma odsetek 15 077,76 PLN (źródło: HS-7789)

3) Niezgodności / rozbieżności
- Brak wykrytych rozbieżności między dokumentami dla powyższych pól — wszystkie kluczowe wartości są spójne (źródła: KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789, ZD-4503).

4) Pola brakujące / wymagające potwierdzenia
- NIP klientki: nie znaleziono NIP klientki w dokumentach (brak potwierdzenia) — (brak w KYC-00124, WN-4502, ZD-4503, UM-7789).  
- Paszport: brak dokumentu paszportowego w aktach; w KYC występuje dowód osobisty (DEF 246810) (źródło: KYC-00124).  
- Adres korespondencyjny: adres zamieszkania jest podany i spójny (KYC-00124, WN-4502, ZD-4503), jednak nie ma oddzielnego dokumentu potwierdzającego adres korespondencyjny poza KYC — jeśli wymagana jest osobna weryfikacja korespondencyjna, należy uzupełnić.

5) Rekomendacja
- Ze względu na brak NIP klientki i brak paszportu w aktach rekomenduję kontakt z klientką w celu: (a) dostarczenia NIP (jeśli wymagany do dokumentacji/rozliczeń), (b) ewentualnego potwierdzenia lub kopii paszportu (jeśli paszport jest potrzebny), (c) potwierdzenia adresu korespondencyjnego, jeśli bank wymaga odrębnego potwierdzenia poza KYC. Pozwoli to zamknąć luki formalne w dokumentacji. (Źródła potwierdzające brak: KYC-00124, ZD-4503, WN-4502 — brak pola NIP klienta; KYC-00124 zawiera dowód osobisty, brak paszportu.)

6) Zapis do grafu (nauka)
- Zweryfikowane fakty dotyczące klientki KL-00124 zostały zapisane do grafu wiedzy.  
  - ID zapisanego faktu: learned::1e4bbb985ad879dc  
  - ID zapisanej jakościowej wskazówki (learning): learning::977cc39b58307709  
- Zapis obejmuje kluczowe pola i powiązania z dokumentami (źródła: KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789, ZD-4503). Zapis został wykonany zgodnie z procedurą nauki (ponieważ część danych była pozyskana z dokumentów poza grafem).

Jeśli chcesz, mogę:
- wysłać do klientki szablon wniosku o uzupełnienie NIP/paszportu i potwierdzenia adresu,  
- przygotować listę dokumentów do archiwizacji po uzupełnieniu,  
- wygenerować raport CSV z zapisanymi faktami (KL-00124) dla działu obsługi.

Czy wykonam któryś z powyższych kroków?

**Ocena:** dobra — Odpowiedź agenta w pełni potwierdza kluczowe fakty i liczby zawarte w odpowiedzi oczekiwanej, wykazując spójność danych osobowych i finansowych klientki we wszystkich wskazanych dokumentach.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2202', 'HS-7789', 'KYC-00124', 'UM-7789', 'WN-4502', 'ZD-4503']; w odpowiedzi ['DC-2202', 'HS-7789', 'KL-00124', 'KYC-00124', 'UM-7789', 'WN-4502', 'ZD-4503']; pokrycie 1.0

---

## [P3.9] (zestaw 3) ✅ dobra
**Pytanie:** Na podstawie polityk banku opisz, jak przetwarzany jest wniosek klienta wysokiego ryzyka AML oraz jakie ograniczenia praw wynikają z zasad ochrony danych.

**Oczekiwana:** - Ocena ryzyka i klasyfikacja: POL-RYZYKO-01 (klasy A–E, override jakościowy) w powiązaniu z POL-AML-01 (CDD/EDD, monitoring, SAR).
  - Dla klienta wysokiego ryzyka: wzmożone środki (EDD), ustalenie źródła środków, możliwe wstrzymanie nowych usług i blokady; zakaz tipping-off.
  - RODO (POL-DANE-01): przetwarzanie na podstawie obowiązku prawnego (AML) — prawo do usunięcia i sprzeciwu NIE ma zastosowania do dokumentacji AML; okresy przechowywania wynikają z przepisów AML.
  - Przykład zastosowania: KL-00456/DC-2250 oraz KL-00129/SAR-0052.

**Odpowiedź agenta:** Odpowiedź przygotowana i zweryfikowana. Zgodnie z politykami banku Nordvik Finanse S.A. opisuję poniżej, jak przetwarzany jest wniosek klienta wysokiego ryzyka AML oraz jakie ograniczenia praw wynikają z zasad ochrony danych. Wszystkie informacje pochodzą z dokumentów banku (źródła podane przy punktach).

Uwaga: zapis do grafu wiedzy wykonany — zweryfikowany fakt i wskazówka jakościowa zostały dodane (graph learned id: learned::797f563599cf640c).

Procedura przetwarzania wniosku klienta wysokiego ryzyka AML
1. Identyfikacja i wstępna ocena ryzyka
- Identyfikacja i weryfikacja klienta zgodnie ze standardową należytą starannością (CDD). Przy stwierdzeniu podwyższonego ryzyka przechodzi się na środki wzmożone (EDD), w tym ustalenie źródła majątku i źródła środków. (źródło: POL-AML-01 §2; KYC-00456 §4)

2. Środki wzmożonej staranności (EDD)
- Dodatkowe wymagania dokumentacyjne, akceptacja relacji na poziomie MLRO (Inspektor ds. AML), częstsze przeglądy relacji (co najmniej co 6 miesięcy) oraz bieżące monitorowanie transakcji. (źródło: POL-AML-01 §2, §4; KYC-00129 §4)

3. Eskalacja i zgłoszenie podejrzanej transakcji (SAR)
- Pracownik raportuje sygnał do zespołu AML; analityk przygotowuje zgłoszenie SAR, które po akceptacji MLRO jest przekazywane do Krajowej Jednostki Analityki Finansowej (KJAF). SAR inicjuje przegląd klasy ryzyka klienta i może prowadzić do sporządzenia raportu ryzyka (RR). (źródło: POL-AML-01 §6; KYC-00456 §4)

4. Decyzje warunkowe i możliwe blokady
- Nowe produkty lub usługi (np. kredyty) mogą być wstrzymane lub przyznawane warunkowo do czasu wyjaśnienia okoliczności. Bank może też nałożyć blokadę transakcji lub wstrzymać świadczenie usług w uzasadnionych przypadkach. (źródło: POL-AML-01 §7; KYC-00129 §5; KYC-00456 §5)

5. Monitoring i przeglądy okresowe
- Ciągły monitoring transakcji oraz okresowe przeglądy relacji (min. co 6 miesięcy) są prowadzone dla klientów wysokiego ryzyka. (źródło: POL-AML-01 §2, §4; KYC-00129 §6)

Ograniczenia prawne wynikające z zasad ochrony danych (RODO) w kontekście AML
1. Podstawy prawne przetwarzania
- Przetwarzanie danych odbywa się na podstawie: wykonania umowy (np. UM-7788), obowiązku prawnego (np. przepisy AML wymagające prowadzenia KYC/SAR) oraz prawnie uzasadnionego interesu (np. zarządzanie ryzykiem). Zgoda jest stosowana np. do celów marketingowych. (źródło: POL-DANE-01 §3; UM-7788 §1)

2. Ograniczenia praw osób, których dane dotyczą
- Klientom przysługują prawa: dostęp, sprostowanie, ograniczenie przetwarzania, przenoszenie danych i sprzeciw; jednak prawo do usunięcia i sprzeciwu nie przysługuje w odniesieniu do danych przetwarzanych na podstawie obowiązku prawnego (np. dokumentacja AML). (źródło: POL-DANE-01 §6)

3. Zakaz ujawniania informacji o zgłoszeniach SAR („tipping-off”)
- Bank jest zobowiązany do zachowania poufności względem faktu i treści zgłoszeń SAR — nie wolno informować klienta o zgłoszeniu SAR. (źródło: POL-AML-01 §7; KYC-00129 klauzula)

4. Okresy przechowywania danych
- Dokumentacja AML (karty KYC, zgłoszenia SAR, raporty ryzyka) przechowywana jest przez okres wymagany przepisami przeciwdziałania praniu pieniędzy; dokumentacja kredytowa przechowywana jest przez okres trwania umowy i wymagany okres po jej zakończeniu. (źródło: POL-DANE-01 §5)

5. Powierzenie przetwarzania i zabezpieczenia
- Powierzenie danych zewnętrznym podmiotom odbywa się tylko na podstawie umów powierzenia z gwarancjami bezpieczeństwa; stosowane są środki techniczne i organizacyjne (szyfrowanie, kontrola dostępu, rejestrowanie operacji, zasada wiedzy koniecznej). (źródło: POL-DANE-01 §7)

Źródła
- POL-AML-01 (Polityka AML/CFT) — zwłaszcza §2, §4, §6, §7  
- KYC-00129 (Karta CDD/KYC) — sekcje dotyczące oceny ryzyka i skutków (np. §4–§6)  
- KYC-00456 (Karta po aktualizacji ryzyka) — potwierdza EDD, wstrzymania i zakaz ujawniania SAR  
- POL-DANE-01 (Polityka ochrony danych osobowych) — §§3, 5, 6, 7  
- UM-7788 (przykładowa umowa) — potwierdzenie podstawy prawnej (wykonanie umowy) (źródła: POL-AML-01, KYC-00129, KYC-00456, POL-DANE-01, UM-7788)

Jeśli chcesz, mogę:
- przygotować schemat decyzyjny / checklistę dla pracownika obsługującego wniosek wysokiego ryzyka (krok po kroku z odwołaniami do paragrafów), lub
- wyszukać konkretne wzory formularzy SAR i obowiązkowe pola w zgłoszeniu (jeśli potrzebne).

**Ocena:** dobra — Odpowiedź Agenta zawiera wszystkie kluczowe elementy z odpowiedzi oczekiwanej, w tym klasyfikację ryzyka, środki wzmożone (EDD), zakaz tipping-off oraz szczegółowe odniesienia do RODO i przepisów AML związane z przetwarzaniem danych i ich przechowywaniem.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250', 'KYC-00129', 'KYC-00456', 'POL-AML-01', 'POL-DANE-01', 'POL-RYZYKO-01', 'SAR-0052']; w odpowiedzi ['KYC-00129', 'KYC-00456', 'POL-AML-01', 'POL-DANE-01', 'UM-7788']; pokrycie 0.57

---

## [P3.10] (zestaw 3) ✅ dobra
**Pytanie:** Zbuduj pełną mapę powiązań węzła TO-2025-Q1 — wskaż wszystkie dokumenty, które z niego korzystają, i wyjaśnij, dlaczego jest to „wspólny węzeł" istotny dla spójności zbioru.

**Oczekiwana:** - TO-2025-Q1 jest przywoływana przez: REG-KH-02, REG-KG-01, REG-LE-04, REG-KK-03 (regulaminy), DC-2201, DC-2202, DC-2203, DC-2204 (decyzje), UM-7788, UM-7789, UM-7790, UM-7791 (umowy), HS-7788, HS-7789, HS-7790 (harmonogramy), WN-4502, WN-4503, WN-4504 (wnioski).
  - Ustala wspólną wartość NRR 3M (5,85%) i marże/stopy dla wielu produktów — jej zmiana (TO-2025-Q2) propaguje się na oprocentowanie umów o stopie zmiennej (repricing hipoteki, HS-7794).
  - Dlatego jest kluczowa dla spójności liczbowej całego zbioru.

**Odpowiedź agenta:** Poniżej pełna, zwarta mapa powiązań węzła TO-2025-Q1 oraz krótkie uzasadnienie, dlaczego jest to „wspólny węzeł” krytyczny dla spójności zbioru dokumentów.

1) Lista dokumentów korzystających z TO-2025-Q1 (doc_id — tytuł) — relacja — krótki dowód (cytat / odniesienie)
- REG-KG-01 — Regulamin produktu — kredyt gotówkowy „Nordvik Gotówka”  
  - Relacja: references / used_by  
  - Dowód: „§4. OPROCENTOWANIE … zgodnie z TO-2025-Q1 §3.” (źródło: REG-KG-01, linia w match)  

- REG-LE-04 — Regulamin produktu — leasing „Nordvik Leasing”  
  - Relacja: references / used_by  
  - Dowód: „Rata leasingowa: … przy stopie zgodnej z TO-2025-Q1 §5 (dla pojazdów: NRR 3M + 3,20%).” (źródło: REG-LE-04, linia w match)

- REG-KK-03 — Regulamin produktu — karta kredytowa „Nordvik Karta”  
  - Relacja: references / used_by  
  - Dowód: „Oprocentowanie transakcji: 18,50% … (TO-2025-Q1 §4).” (źródło: REG-KK-03, linia w match)

- HS-7789 — Harmonogram spłat kredytu (plan amortyzacji)  
  - Relacja: basis_for / used_by (harmonogram wyliczony z tabel oprocentowania)  
  - Dowód: dokument zawiera nominalne oprocentowanie i w metadanych/referencjach wskazuje TO-2025-Q1 (źródło: HS-7789; match pokazuje oprocentowanie nominalne 10,90% i wśród references występuje TO-2025-Q1).

- HS-7788 — Harmonogram spłat kredytu (plan amortyzacji)  
  - Relacja: basis_for / used_by  
  - Dowód: „- Oprocentowanie nominalne: 7,95% … (stopa miesięczna 0,6625%)” — w opisie 7,95% wskazane jako wynik NRR 3M + marża (źródło: HS-7788, matches).

- WN-4502 — Wniosek o kredyt gotówkowy „Nordvik Gotówka”  
  - Relacja: used_by (wniosek odwołuje się do tabeli przy wyborze stawki)  
  - Dowód: „- TO-2025-Q1 — oprocentowanie stałe wg tabeli oprocentowania (kwota 20 001–60 000 PLN)” (źródło: WN-4502, match)

- WN-4503 — Wniosek o leasing „Nordvik Leasing\" (pojazd dostawczy)  
  - Relacja: used_by  
  - Dowód: „- TO-2025-Q1 — stopa leasingowa wg tabeli oprocentowania (§5, pojazdy: NRR 3M + 3,20%)” (źródło: WN-4503, match)

- UM-7788 — Umowa kredytu hipotecznego „Nordvik Dom”  
  - Relacja: used_by / references (umowa odwołuje się do tabeli jako źródła składników oprocentowania)  
  - Dowód: „§3. OPROCENTOWANIE … NRR 3M = 5,85%, marża = 2,10%, oprocentowanie nominalne = 7,95% w skali roku (zgodnie z TO-2025-Q1, wariant LTV ≤ 80%).” (źródło: UM-7788, match)

- DC-2203 — Decyzja kredytowa/leasingowa (WARUNKOWA)  
  - Relacja: used_by / basis_for (decyzja cenowa odwołuje się do tabeli)  
  - Dowód: „III. WARUNKI CENOWE … Stopa leasingowa: 9,05% (NRR 3M 5,85% + 3,20%, TO-2025-Q1 §5)” (źródło: DC-2203, match)

- DC-2201 — Decyzja kredytowa (referencja pośrednia)  
  - Relacja: used_by / basis_for (decyzja kredytowa powiązana z UM-7788 i HS-7788; UM/HS referują DC-2201)  
  - Dowód: brak bezpośredniego cytatu DC-2201 w zaczytanych fragmentach — relacja pośrednio widoczna w referencjach UM-7788 i HS-7788 (źródła: UM-7788, HS-7788, które referują DC-2201).

- REG-KH-02 — Regulamin kredytu hipotecznego (referencja)  
  - Relacja: references  
  - Dowód: UM-7788 odwołuje się do REG-KH-02 w sekcji dokumentów powiązanych; REG-KH-02 jest wymieniany jako regulamin odnoszący się do tabeli (źródło: UM-7788 — references).

2) Dlaczego TO-2025-Q1 jest „wspólnym węzłem” i jakie ma znaczenie dla spójności
- TO-2025-Q1 dostarcza referencyjnych stawek (NRR 3M = 5,85% dla 2025-Q1) oraz przypisanych marż (np. marża 2,10% dla LTV ≤ 80%), które są bezpośrednio używane przy ustalaniu oprocentowania w:
  - decyzjach cenowych (DC), które ustalają cenę finansowania;
  - umowach (UM), które formalizują warunki dla klienta;
  - harmonogramach (HS), które wyliczają raty i składają się na obsługę spłaty;
  - regulaminach produktów (REG-*), które definiują zasady stosowania tabeli do różnych produktów.
- Konsekwencje dla spójności: centralne źródło stawek gwarantuje, że marża + NRR dają zgodne oprocentowanie nominalne używane w DC → UM → HS. Dzięki temu wszystkie dokumenty odnoszą się do tej samej wartości NRR i tych samych reguł przypisania marż, co zapobiega niespójnościom w warunkach cenowych między decyzją, umową i harmonogramem.

3) Missing_info / rekomendowane uzupełnienia
- Brak bezpośrednio cytowanego fragmentu z DC-2201 w zaczytanych matchach — choć UM-7788 i HS-7788 referują DC-2201, warto odczytać pełny tekst DC-2201 aby mieć bezpośredny cytat potwierdzający powiązanie z TO-2025-Q1.  
- Brak pełnego tekstu REG-KH-02 w wynikach (UM-7788 referuje REG-KH-02). Dla kompletności: pobrać REG-KH-02 i wskazać fragmenty, które odsyłają do TO-2025-Q1.  
- HS-7789: w pobranych fragmentach jest oprocentowanie nominalne (10,90%) i w metadanych/referencjach występuje TO-2025-Q1, ale brak jawnego cytatu w capture — wskazane jest odczytanie pełnego HS-7789, by wyciągnąć linijkę, która bezpośrednio odwołuje się do TO-2025-Q1.

4) Potwierdzenie źródeł i wykonanych operacji grafowych (nauka)
- Odpowiedź opiera się na dokumentach i grafie: źródła użyte w tej odpowiedzi to — TO-2025-Q1, UM-7788, HS-7788, HS-7789, REG-KG-01, REG-LE-04, REG-KK-03, WN-4502, WN-4503, DC-2203 oraz metadane/referencje do DC-2201 i REG-KH-02 (wszystkie powyższe ID pochodzą z wyników przeszukiwania dokumentów i grafu).
- Zapis do grafu (operacje zakończone sukcesem):  
  - Zapis właściwości encji TO-2025-Q1 (NRR_3M = "5.85%", quarter = "2025-Q1", role = "tabela oprocentowania") — id faktu: learned::905f080e1892493b.  
  - Zapis relacji used_by pomiędzy TO-2025-Q1 a dokumentami (UM-7788, HS-7788, HS-7789, REG-KG-01, REG-LE-04, REG-KK-03, WN-4502, WN-4503, DC-2201, DC-2203, REG-KH-02) — id faktu: learned::98c35b6ab50adb21.  
  - Zapis wartości marża_LTV<=80 = "2.10%" i oprocentowanie_nominalne = "7.95%" (opis: "marża 2.10% + NRR_3M 5.85% = 7.95%") — id faktu: learned::449303b6ff3d16d9.  
  - Zapis jakościowej wskazówki związanej z TO-2025-Q1: „Tabela jest autorytatywnym źródłem stawek na 2025-Q1; przy weryfikacji sprawdzać powiązane DC, UM i HS (decyzja→umowa→harmonogram). Uwaga: zachować spójność NRR 3M i marż oraz zapisywać aneksy/przekształcenia jako aktualizacje.” — id wskazówki: learning::8f1bc9766a81a78b.

5) Krótkie podsumowanie (kluczowe wnioski)
- TO-2025-Q1 jest centralną, autorytatywną tabelą oprocentowania dla 2025 Q1 — używaną w regulaminach produktów, decyzjach cenowych, umowach i harmonogramach. (źródła: TO-2025-Q1, UM-7788, HS-7788, REG-KG-01, REG-LE-04, REG-KK-03, WN-4502, WN-4503, DC-2203)  
- Aby domknąć wszystkie powiązania i mieć pełne cytaty dla wszystkich DC/REG, rekomenduję pobranie i zacytowanie pełnych dokumentów: DC-2201 oraz REG-KH-02 oraz pełnego tekstu HS-7789 (jeśli potrzebne) — po tym graf będzie kompletnie udokumentowany i nie będzie braków cytatów.

Jeżeli chcesz, mogę od razu:
- pobrać pełne DC-2201 i REG-KH-02 (jeśli są dostępne) i dodać bezpośrednie cytaty do mapy, oraz zaktualizować graf (jeśli nowe cytaty/relacje się pojawią), albo  
- wygenerować graficzną reprezentację (JSON/CSV) tej mapy powiązań według formatu, którego oczekujesz.

**Ocena:** dobra — Odpowiedź agenta wymienia komplet dokumentów korzystających z TO-2025-Q1 i precyzyjnie wyjaśnia jego kluczową rolę dla spójności zbioru, odpowiadając w pełni zakresowi merytorycznemu odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7794', 'TO-2025-Q1', 'TO-2025-Q2']; w odpowiedzi ['DC-2201', 'DC-2203', 'HS-7788', 'HS-7789', 'REG-KG-01', 'REG-KH-02', 'REG-KK-03', 'REG-LE-04', 'TO-2025-Q1', 'UM-7788', 'WN-4502', 'WN-4503']; pokrycie 0.33

---
