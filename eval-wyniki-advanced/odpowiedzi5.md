# Wyniki ewaluacji (self_learning_agents)

## [P1.1] (zestaw 1) ✅ dobra
**Pytanie:** Jaki jest numer PESEL (testowy) klientki Anny Katarzyny Kowalskiej?

**Oczekiwana:** 85072812345 (oznaczony jako testowy).

**Odpowiedź agenta:** Numer PESEL (testowy) klientki Anna Katarzyna Kowalska to 85072812345 (źródło: graf wiedzy, potwierdzone dokumentem KYC-00123).

Zapis do grafu wiedzy wykonany: fakt PESEL=85072812345 zapisany (id faktu: learned::d59a300a865d547c) oraz wskazówka jakościowa dodana (id wskazówki: learning::d59a300a865d547c).

**Ocena:** dobra — Odpowiedź agenta zawiera poprawny numer PESEL zgodny z odpowiedzią oczekiwaną oraz jednoznacznie wskazuje, że jest to numer testowy.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00123']; w odpowiedzi ['KYC-00123']; pokrycie 1.0

---

## [P1.2] (zestaw 1) ✅ dobra
**Pytanie:** Na jaką kwotę opiewa kredyt hipoteczny w umowie UM-7788?

**Oczekiwana:** 480 000,00 PLN.

**Odpowiedź agenta:** Kwota kredytu hipotecznego w umowie UM-7788 wynosi 480 000,00 PLN (źródło: UM-7788).

Informuję też, że fakt ten pochodził z pamięci grafowej i został zweryfikowany oraz zapisany do grafu wiedzy (ID faktu: learned::40362ffccb37b257).

**Ocena:** dobra — Kwota kredytu hipotecznego podana przez agenta jest zgodna z oczekiwaną wartością 480 000,00 PLN.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['UM-7788']; w odpowiedzi ['UM-7788']; pokrycie 1.0

---

## [P1.3] (zestaw 1) 🟡 czesciowa
**Pytanie:** Ile wynosi miesięczna rata w harmonogramie HS-7788?

**Oczekiwana:** 3 688,83 PLN (300 rat annuitetowych).

**Odpowiedź agenta:** Krótko i rzeczowo:

- W oryginalnym harmonogramie HS-7788 miesięczna rata wynosi 3 688,83 PLN i jest ratą annuitetową (równe) — w dokumencie HS-7788 ta kwota jest podana dla rat nr 1–24 (źródło: HS-7788).  
- Uwaga: harmonogram został zaktualizowany dokumentem HS-7794, który zastępuje HS-7788 od raty nr 2 — od tej raty miesięczna rata wynosi 3 531,88 PLN (również annuitetowa) (źródło: HS-7794).

Zapis do grafu (nauka) został wykonany — dodano zweryfikowane fakty i wskazówkę jakościową:
- learned::87d5cd36c0c9db57 — HS-7794.monthly_installment_amount = "3531.88 PLN" (źródło: HS-7794)  
- learned::1f0ac9a01c7842a0 — HS-7794.effective_from_installment = "2" (źródło: HS-7794)  
- learned::4b46d569cc93a8aa — HS-7794.replaces = "HS-7788" (źródło: HS-7794)  
- learning::eedd6db85ed8653b — wskazówka jakościowa przypięta do HS-7788 (źródła: HS-7788, HS-7794)

Źródła: HS-7788, HS-7794.

**Ocena:** czesciowa — Odpowiedź agenta poprawnie podaje kwotę 3 688,83 PLN jako miesięczną ratę w harmonogramie HS-7788, ale dodatkowo wprowadza informację o aktualizacji, co wykracza poza oczekiwaną odpowiedź i może powodować niejednoznaczność.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788']; w odpowiedzi ['HS-7788', 'HS-7794']; pokrycie 1.0

---

## [P1.4] (zestaw 1) ✅ dobra
**Pytanie:** Jaki jest maksymalny standardowy wskaźnik LTV według polityki ryzyka kredytowego?

**Oczekiwana:** 80% (standard; LTV 80–90% dopuszczalne wyjątkowo z dodatkowym zabezpieczeniem/ubezpieczeniem i wyższą marżą).

**Odpowiedź agenta:** Maksymalny standardowy wskaźnik LTV według Polityki ryzyka kredytowego Nordvik Finanse S.A. wynosi 80% (źródło: POL-RYZYKO-01). Zapis do grafu wiedzy wykonany.

**Ocena:** dobra — Odpowiedź agenta prawidłowo podaje maksymalny standardowy wskaźnik LTV jako 80%, zgodnie z oczekiwaniami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['POL-RYZYKO-01']; w odpowiedzi ['POL-RYZYKO-01']; pokrycie 1.0

---

## [P1.5] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi wartość wskaźnika NRR 3M w tabeli oprocentowania na I kwartał 2025?

**Oczekiwana:** 5,85% w skali roku.

**Odpowiedź agenta:** Wskaźnik NRR 3M w tabeli oprocentowania na I kwartał 2025 wynosi 5,85% w skali roku (źródło: TO-2025-Q1).  
Graf wiedzy już zawierał tę informację (potwierdzenie: werdykt weryfikatora POTWIERDZONA); zapis nowego faktu do grafu nie był konieczny.

**Ocena:** dobra — Odpowiedź agenta poprawnie podaje wartość wskaźnika NRR 3M jako 5,85% w skali roku, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['TO-2025-Q1']; w odpowiedzi ['TO-2025-Q1']; pokrycie 1.0

---

## [P1.6] (zestaw 1) ✅ dobra
**Pytanie:** Jaka jest stawka prowizji przygotowawczej dla kredytu hipotecznego w tabeli opłat Q1 2025?

**Oczekiwana:** 2,00% kwoty kredytu.

**Odpowiedź agenta:** Stawka prowizji przygotowawczej dla kredytu hipotecznego w tabeli opłat Q1 2025 wynosi 2,00% (źródło: TO-2025-Q1). Weryfikacja potwierdziła tę wartość. Fakt był już w grafie, zapis do grafu nie był wymagany.

**Ocena:** dobra — Odpowiedź agenta zawiera dokładną stawkę prowizji przygotowawczej 2,00%, zgodną z oczekiwaną odpowiedzią.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['TOP-2025-Q1']; w odpowiedzi ['TO-2025-Q1']; pokrycie 0.0

---

## [P1.7] (zestaw 1) ✅ dobra
**Pytanie:** Kto jest beneficjentem rzeczywistym (UBO) spółki „Bursztyn Handel Sp. z o.o."?

**Oczekiwana:** Andrzej Lewiński — 100% udziałów.

**Odpowiedź agenta:** Beneficjentem rzeczywistym (UBO) spółki "Bursztyn Handel Sp. z o.o." jest Andrzej Lewiński — posiada 100% udziałów jako Beneficjent rzeczywisty (źródła: UM-7788, KYC-00129, KYC-00123). Informacja pobrana z grafu pamięci (zapis zweryfikowany i dopisany do grafu).

**Ocena:** dobra — Odpowiedź agenta jest zgodna merytorycznie z oczekiwaną, podając poprawne dane o beneficjencie rzeczywistym oraz procent udziałów.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00129']; w odpowiedzi ['KYC-00123', 'KYC-00129', 'UM-7788']; pokrycie 1.0

---

## [P1.8] (zestaw 1) ✅ dobra
**Pytanie:** Jakie rozstrzygnięcie zapadło w decyzji kredytowej DC-2250?

**Oczekiwana:** Decyzja NEGATYWNA (odmowa udzielenia kredytu gotówkowego).

**Odpowiedź agenta:** Decyzja DC-2250: odmowa udzielenia kredytu. Uzasadnienie: odmowa wynikała z wysokiego ryzyka AML (klasa E) i braku ustalenia źródła środków pomimo przeprowadzonego EDD; wnioskowana kwota 80 000 PLN, decyzja podjęta 12 maja 2025, mimo pozytywnej oceny zdolności finansowej. (źródło: DC-2250, WN-4508)

Zapis do grafu został wykonany — fakt zapisano jako learned::856faa944753faf0, a jakościowa wskazówka jako learning::fc96ee76240acf3b.

**Ocena:** dobra — Odpowiedź Agenta zgodnie wskazuje na negatywną decyzję kredytową (odmowa), co jest kluczowe i zgodne z oczekiwaną odpowiedzią, dodatkowo podając uzasadnienie i szczegóły nie naruszające zgodności merytorycznej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250']; w odpowiedzi ['DC-2250', 'WN-4508']; pokrycie 1.0

---

## [P1.9] (zestaw 1) ✅ dobra
**Pytanie:** Jaki limit kredytowy przyznano na karcie kredytowej w decyzji DC-2204?

**Oczekiwana:** 15 000,00 PLN.

**Odpowiedź agenta:** Przyznany limit kredytowy na karcie kredytowej w decyzji DC-2204: 15 000,00 PLN (źródła: DC-2204, UM-7791; dodatkowo REG-KK-03 opisuje zasady limitów).

Werdykt weryfikatora: POTWIERDZONA (DC-2204, UM-7791, REG-KK-03).

Zapis do grafu wykonany: fact_id = learned::c7f66b6b08ecf896, learning_id = learning::abf3b8edc75c74ef.

Uwaga: zgodnie z REG-KK-03 limit może być okresowo weryfikowany i zmieniany przez bank.

**Ocena:** dobra — Odpowiedź agenta zawiera poprawną wartość limitu 15 000,00 PLN zgodną z odpowiedzią oczekiwaną oraz dodatkowe informacje potwierdzające i wyjaśniające kontekst zmian limitu.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź

**Źródła:** oczekiwane ['DC-2204']; w odpowiedzi ['DC-2204', 'REG-KK-03', 'UM-7791']; pokrycie 1.0

---

## [P1.10] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi minimalna kwota do zapłaty w cyklu rozliczeniowym karty kredytowej „Nordvik Karta"?

**Oczekiwana:** 5% zadłużenia, nie mniej niż 50 PLN.

**Odpowiedź agenta:** Minimalna kwota do zapłaty w cyklu rozliczeniowym karty kredytowej „Nordvik Karta” wynosi 5% zadłużenia, nie mniej niż 50,00 PLN (źródła: REG-KK-03, UM-7791, DC-2204).

Zapis do grafu wykonany — fakt zapisano jako learned::85571e2ec66e38de.

**Ocena:** dobra — Odpowiedź agenta w pełni zgadza się z oczekiwaną co do minimalnej kwoty do zapłaty i wartości procentowej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j) → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['REG-KK-03']; w odpowiedzi ['DC-2204', 'REG-KK-03', 'UM-7791']; pokrycie 1.0

---

## [P1.11] (zestaw 1) ✅ dobra
**Pytanie:** Jak długi jest okres bezodsetkowy (grace period) karty kredytowej dla transakcji bezgotówkowych?

**Oczekiwana:** Do 56 dni (pod warunkiem spłaty całości zadłużenia w terminie).

**Odpowiedź agenta:** Okres bezodsetkowy (grace period) dla transakcji bezgotówkowych wynosi do 56 dni, pod warunkiem spłaty całego zadłużenia w terminie (źródło: REG-KK-03).  
Fakt został zapisany do grafu wiedzy (graph_add_learned_fact: true, źródło REG-KK-03); zapisana także krótka wskazówka jakościowa (learning_saved: true) — uwaga: wskazówka nie została automatycznie powiązana z istniejącym węzłem encji (proszę sprawdzić nazwę encji, jeśli wymagane jest ręczne powiązanie).

**Ocena:** dobra — Odpowiedź agenta zawiera kluczowe informacje zgodne z odpowiedzią oczekiwaną: okres bezodsetkowy wynosi do 56 dni pod warunkiem spłaty całego zadłużenia w terminie.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KK-03']; w odpowiedzi ['REG-KK-03']; pokrycie 1.0

---

## [P1.12] (zestaw 1) ✅ dobra
**Pytanie:** Do jakiego podmiotu i jakiej jurysdykcji trafiały przelewy zagraniczne z rachunku w historii transakcji HT-00456?

**Oczekiwana:** Do „Vantia Global Trade LLC" w Republice Vantia (jurysdykcja wysokiego ryzyka); łącznie ok. 464 950,00 PLN.

**Odpowiedź agenta:** Odpowiedź (zwięźle):

- Przelewy zagraniczne z rachunku HT-00456 trafiały do podmiotu: Vantia Global Trade LLC (beneficjent).
- Jurysdykcja: Republika Vantia (klasyfikowana jako jurysdykcja wysokiego ryzyka).
- Liczba przelewów: 5
- Łączna wartość: 464 950,00 PLN
- Okres transakcji z dokumentów: 2025-02-06 do 2025-03-25

Źródła: HT-00456, SAR-0041, RR-0012.

Status grafu: Fakt nie był wcześniej w grafie; został teraz zapisany jako learned::87514ac951873edb, a wskazówka jakościowa powiązana z rachunkiem HT-00456 zapisana jako learning::87514ac951873edb.

Jeśli chcesz, mogę teraz:
- wydobyć szczegóły poszczególnych przelewów (daty i kwoty poszczególnych 5 transakcji, numery SWIFT/transaction IDs jeśli są dostępne w dokumentach),
- lub przygotować krótkie podsumowanie AML z rekomendacjami (np. weryfikacja KYC beneficjenta, sprawdzenie komunikatów SWIFT/CSV).

**Ocena:** dobra — Odpowiedź agenta w pełni zgadza się z oczekiwaną pod względem kluczowych faktów: nazwy podmiotu, jurysdykcji oraz łącznej wartości przelewów.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HT-00456']; w odpowiedzi ['HT-00456', 'RR-0012', 'SAR-0041']; pokrycie 1.0

---

## [P1.13] (zestaw 1) ✅ dobra
**Pytanie:** Jaki średni miesięczny dochód netto potwierdza zaświadczenie ZD-4503?

**Oczekiwana:** 8 200,00 PLN (klientka Katarzyna Lewandowska, Nadmorskie Centrum Medyczne Sp. z o.o.).

**Odpowiedź agenta:** Średni miesięczny dochód netto potwierdzony w zaświadczeniu ZD-4503 wynosi 8 200,00 PLN (źródło: ZD-4503).

Zapis do grafu wiedzy wykonany: fakt zapisany jako learned::08ec0ea0dec6588a (źródło: ZD-4503).

**Ocena:** dobra — Odpowiedź agenta podaje prawidłową kwotę 8 200,00 PLN zgodnie z zaświadczeniem ZD-4503, co jest zgodne z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['ZD-4503']; w odpowiedzi ['ZD-4503']; pokrycie 1.0

---

## [P1.14] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi wartość wykupu przedmiotu leasingu we wniosku WN-4503?

**Oczekiwana:** 1% wartości = 1 800,00 PLN netto.

**Odpowiedź agenta:** Wartość wykupu przedmiotu leasingu we wniosku WN-4503 wynosi 1 800,00 PLN netto (co odpowiada 1% wartości netto przedmiotu: 180 000,00 PLN) (źródło: WN-4503).

Potwierdzam zapis do grafu wiedzy — dodano fakty: „Wartość wykupu 1 800,00 PLN netto (WN-4503)”, „Wartość wykupu procentowo 1% (WN-4503)” oraz „Wartość netto przedmiotu 180 000,00 PLN (WN-4503)”.

**Ocena:** dobra — Odpowiedź agenta jest zgodna merytorycznie z oczekiwaną, podając wartość wykupu jako 1 800,00 PLN netto odpowiadającą 1% wartości przedmiotu leasingu.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['WN-4503']; w odpowiedzi ['WN-4503']; pokrycie 1.0

---

## [P1.15] (zestaw 1) ✅ dobra
**Pytanie:** Jaki wewnętrzny próg alertu dla wpłat gotówkowych określa polityka AML?

**Oczekiwana:** 15 000 PLN (rozbijanie wpłat poniżej progu = structuring).

**Odpowiedź agenta:** Wewnętrzny próg alertu dla wpłat gotówkowych w polityce AML Nordvik Finanse S.A. wynosi 15 000 PLN. (źródło: POL-AML-01)

Dodatkowe informacje z dokumentu:
- Próg dotyczy wpłat gotówkowych ogółem; rozbijanie wpłat tuż poniżej progu (structuring/smurfing) jest traktowane jako typologia podejrzana (źródło: POL-AML-01, §4).
- Istnieje także odrębny próg raportowania transakcji ponadprogowych: równowartość 15 000 EUR (jednorazowo lub jako powiązane) — to próg regulacyjny, nie wewnętrzny alert w PLN (źródło: POL-AML-01, §4).
- Dokument nie wyszczególnia wyjątków dotyczących rodzaju klientów (np. instytucjonalni) ani szczególnych typów wpłat.

Zapis do grafu wiedzy:
- Zweryfikowany fakt zapisałem do grafu: learned::0e2ed37d3a7c61f3 (próg 15 000 PLN oraz informacja o structuring) i dodałem wskazówkę jakościową learning::3cce19c7a5b66697 dotyczącą rozróżnienia progów i sprawdzania wyjątków. (źródło zapisu: POL-AML-01)

Jeśli chcesz, mogę przytoczyć dokładne cytaty z §4 POL-AML-01 lub sprawdzić, czy w innych dokumentach (procedury oddziałowe/operacyjne) są dodatkowe wyjątki.

**Ocena:** dobra — Odpowiedź agenta poprawnie podaje wewnętrzny próg alertu 15 000 PLN oraz wyjaśnia, że rozbijanie wpłat poniżej progu jest traktowane jako structuring, zgodnie z oczekiwaniami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j) → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['POL-AML-01']; w odpowiedzi ['POL-AML-01']; pokrycie 1.0

---

## [P1.16] (zestaw 1) ✅ dobra
**Pytanie:** Jaka jest klasa ryzyka kredytowego klienta KL-00124 (Katarzyna Lewandowska)?

**Oczekiwana:** Klasa A (scoring 92/100), ryzyko niskie.

**Odpowiedź agenta:** Klasa ryzyka kredytowego klienta KL-00124 (Katarzyna Lewandowska) to: A.

Fakty potwierdzone:
- Klasa ryzyka: A (źródła: KYC-00124, DC-2202, graf:KL-00124)  
- Scoring: 92/100 (źródła: KYC-00124, DC-2202)  
- DTI: 13,23% (źródło: DC-2202)

Weryfikator: POTWIERDZONA (potwierdzenie w dokumentach KYC-00124 i DC-2202).

Zapis do grafu (nauka) wykonany:
- Dodane zweryfikowane fakty: learned::aef54edda199069f, learned::166fcb87c03fc715, learned::3aec9d1099f20a3d
- Dodana wskazówka jakościowa (learning): learning::d016e02fb5eafa97

Jeśli chcesz, mogę otworzyć i pokazać fragmenty dokumentów KYC-00124 i DC-2202.

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe informacje: klasę A oraz scoring 92/100, zgodne z odpowiedzią oczekiwaną, mimo że nie wymienia bezpośrednio klasy ryzyka jako 'niskie'.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00124']; w odpowiedzi ['DC-2202', 'KL-00124', 'KYC-00124']; pokrycie 1.0

---

## [P1.17] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi opłata roczna za kartę kredytową i kiedy jest znoszona?

**Oczekiwana:** 120,00 PLN; znoszona przy rocznym obrocie bezgotówkowym ≥ 12 000 PLN.

**Odpowiedź agenta:** Opłata roczna za kartę kredytową: 120,00 PLN.  
Opłata jest znoszona, gdy roczny obrót bezgotówkowy na karcie wynosi co najmniej 12 000,00 PLN. (źródło: TOP-2025-Q1)

Weryfikacja: informacja POTWIERDZONA.  
Zapis do grafu wykonano — fakt zapisany jako learned::e225f27afe3d16a3, a wskazówka jakościowa jako learning::e225f27afe3d16a3.  
(Uwaga: wcześniejsze wpisy w grafie wskazywały REGULAMIN_KART i TARYFA_OPŁAT jako źródła; weryfikacja ujednoliciła źródło na TOP-2025-Q1.)

**Ocena:** dobra — Odpowiedź agenta jest w pełni zgodna z odpowiedzią oczekiwaną, podając tę samą kwotę opłaty oraz warunek jej zniesienia przy rocznym obrocie bezgotówkowym ≥ 12 000 PLN.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KK-03', 'TOP-2025-Q1']; w odpowiedzi ['TOP-2025-Q1']; pokrycie 0.5

---

## [P1.18] (zestaw 1) 🟡 czesciowa
**Pytanie:** Jakie oprocentowanie limitu w rachunku firmowym przyznano w decyzji DC-2205?

**Oczekiwana:** 12,50% w skali roku (zmienne); limit 50 000 PLN, prowizja za limit 1% rocznie = 500 PLN.

**Odpowiedź agenta:** Oprocentowanie limitu w rachunku firmowym przyznane w decyzji DC-2205 wynosi 12,50% w skali roku i jest oprocentowaniem zmiennym (źródło: DC-2205).

Zapis do grafu: fakt ten już istniał w grafie (DC-2205) — nie dodano nowego zapisu.

**Ocena:** czesciowa — Agent podał prawidłowe oprocentowanie i jego zmienny charakter, ale pominął informację o limicie 50 000 PLN oraz prowizji 1% rocznie.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['DC-2205']; w odpowiedzi ['DC-2205']; pokrycie 1.0

---

## [P2.1] (zestaw 2) ✅ dobra
**Pytanie:** Czy rata w harmonogramie HS-7788 jest zgodna z kwotą kredytu i oprocentowaniem z umowy oraz tabeli oprocentowania?

**Oczekiwana:** Tak. Umowa UM-7788: 480 000 PLN na 300 mies.; oprocentowanie 7,95% = NRR 3M 5,85% + marża 2,10% (TO-2025-Q1); rata annuitetowa 3 688,83 PLN — zgodna z HS-7788.

**Odpowiedź agenta:** Tak — rata 3 688,83 PLN w harmonogramie HS-7788 jest zgodna z kwotą kredytu 480 000,00 PLN oraz oprocentowaniem 7,95% p.a. (NRR 3M 5,85% + marża 2,10%) przy metodzie annuitetowej. Uzasadnienie: UM-7788 i TO-2025-Q1 wskazują oprocentowanie 7,95% rocznie (miesięczna stopa 7,95%/12 ≈ 0,6625%) i okres 300 miesięcy, a HS-7788 podaje ratę 3 688,83 PLN (ostatnia rata 3 688,84 PLN z powodu zaokrągleń) — zgodność obliczeń annuitetowych została potwierdzona (źródła: HS-7788, UM-7788, TO-2025-Q1). Weryfikator ocenił odpowiedź jako POTWIERDZONĄ. Zapis do grafu: fakt dodany (learned::eb1a7267ba428f15) i wskazówka jakościowa przypisana do HS-7788 (learning::e7f355de507fe5ed).

**Ocena:** dobra — Odpowiedź agenta w pełni potwierdza zgodność raty z kwotą, oprocentowaniem i okresem z umowy oraz tabeli oprocentowania podanymi w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788', 'TO-2025-Q1', 'UM-7788']; w odpowiedzi ['HS-7788', 'TO-2025-Q1', 'UM-7788']; pokrycie 1.0

---

## [P2.2] (zestaw 2) ✅ dobra
**Pytanie:** Na podstawie której decyzji zawarto umowę UM-7788 i jaki wskaźnik DTI przyjęto w tej decyzji?

**Oczekiwana:** Decyzja DC-2201 (pozytywna); DTI = 36,52% (rata 3 688,83 / dochód netto 10 100).

**Odpowiedź agenta:** Umowę UM-7788 zawarto na podstawie decyzji DC-2201; w tej decyzji przyjęto wskaźnik DTI = 36,52% (źródła: UM-7788, DC-2201).

Zapis do grafu wiedzy wykonano: learned::a7f3fcd2715a72ef. Weryfikator: POTWIERDZONA (evidence: UM-7788, DC-2201).

**Ocena:** dobra — Odpowiedź agenta zawiera poprawne informacje dotyczące decyzji DC-2201 oraz wskaźnika DTI 36,52%, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'UM-7788']; w odpowiedzi ['DC-2201', 'UM-7788']; pokrycie 1.0

---

## [P2.3] (zestaw 2) ✅ dobra
**Pytanie:** Dlaczego wniosek WN-4508 został odrzucony, skoro klient miał wystarczającą zdolność kredytową?

**Oczekiwana:** Decyzja DC-2250 była negatywna nie z powodu zdolności (DTI 16,20% — akceptowalne), lecz z powodu klasy ryzyka E nadanej w raporcie RR-0012 na podstawie zgłoszeń SAR-0034 i SAR-0041 oraz braku możliwości ustalenia źródła środków (AML).

**Odpowiedź agenta:** Krótko i rzeczowo — powód odrzucenia:

- Główny powód: wysoka klasa ryzyka AML (klasa E) i brak możliwości wiarygodnego ustalenia źródła pochodzenia środków; klient był objęty wzmożonym monitoringiem (EDD) i w raporcie RR-0012 wystąpiły zgłoszenia podejrzanych transakcji (m.in. structuring i pass‑through). To spowodowało negatywną decyzję pomimo pozytywnej oceny finansowej. (źródło: DC-2250, KYC-00456)

Uzupełniające fakty potwierdzające, że zdolność była wystarczająca, ale nie decydująca:
- Dochód netto użyty do oceny: 12 500,00 PLN (średni); DTI: 16,20% (poniżej limitu 45%). (źródło: WN-4508, ZD-4508)
- Scoring finansowy: 66/100, z jednakową korektą jakościową z tytułu ryzyka AML. (źródło: KYC-00456)
- Decyzja DC-2250 explicite wskazuje rekomendację wstrzymania nowych produktów kredytowych do czasu wyjaśnienia ryzyka. (źródło: DC-2250)

W skrócie: zdolność kredytowa klienta była wystarczająca, ale bank odmówił z powodu ryzyka AML i niemożności zweryfikowania źródeł środków — ryzyko to miało priorytet wobec czysto finansowych kryteriów. (źródła: DC-2250, KYC-00456, WN-4508, ZD-4508)

Zapis do grafu zostanie wykonany: nie — informacja o przyczynie odrzucenia (wysokie ryzyko AML i brak ustalenia źródła środków) już znajdowała się w grafie wiedzy.

**Ocena:** dobra — Odpowiedź agenta zgodnie odzwierciedla kluczowe fakty z odpowiedzi oczekiwanej, wskazując na ryzyko AML klasy E, zgłoszenia w raporcie RR-0012 oraz brak możliwości ustalenia źródła środków jako przyczynę odrzucenia, mimo wystarczającej zdolności kredytowej klienta (DTI 16,20%).

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['DC-2250', 'RR-0012', 'WN-4508']; w odpowiedzi ['DC-2250', 'KYC-00456', 'RR-0012', 'WN-4508', 'ZD-4508']; pokrycie 1.0

---

## [P2.4] (zestaw 2) 🟡 czesciowa
**Pytanie:** Który regulamin i którą politykę powołuje decyzja kredytowa DC-2201?

**Oczekiwana:** Regulamin kredytu hipotecznego REG-KH-02 oraz Politykę ryzyka kredytowego POL-RYZYKO-01 (dodatkowo tabelę TO-2025-Q1 dla parametrów cenowych).

**Odpowiedź agenta:** Decyzja kredytowa DC-2201 odwołuje się do regulaminu REG-KH-02 oraz do polityki POL-RYZYKO-01 (źródło: DC-2201).  
Zapis do grafu został już uwzględniony (fakt pochodzi z DC-2201).

**Ocena:** czesciowa — Agent podał poprawne regulamin i politykę, ale pominął tabelę TO-2025-Q1 wymienioną w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['DC-2201', 'POL-RYZYKO-01', 'REG-KH-02']; w odpowiedzi ['DC-2201', 'POL-RYZYKO-01', 'REG-KH-02']; pokrycie 1.0

---

## [P2.5] (zestaw 2) 🟡 czesciowa
**Pytanie:** Jakie warunki postawiła decyzja warunkowa DC-2203 i w jaki sposób zostały spełnione w umowie leasingu UM-7790?

**Oczekiwana:** DC-2203 wymagała albo podwyższenia opłaty wstępnej do 30%, albo dodatkowego zabezpieczenia. W UM-7790 klient wybrał drugi wariant: ustanowił poręczenie cywilne Tomasza Górskiego oraz weksel własny in blanco, zachowując opłatę wstępną 20% (36 000 PLN); dostarczył też zaświadczenia ZUS/US.

**Odpowiedź agenta:** Oto krótkie i rzeczowe podsumowanie.

Warunki postawione w decyzji warunkowej DC-2203 oraz sposób ich spełnienia w umowie leasingu UM-7790:

1. Poręczenie cywilne Tomasza Górskiego — poręczenie zostało przedstawione i zaakceptowane (źródła: DC-2203, UM-7790).  
2. Weksel własny in blanco z deklaracją wekslową — weksel dołączony do umowy (źródła: DC-2203, UM-7790).  
3. Zaświadczenia o niezaleganiu wobec ZUS i US (stan na 2025-03-14) — zaświadczenia potwierdzają brak zaległości na wskazaną datę (źródła: DC-2203, UM-7790).  
4. Umowa ubezpieczenia AC/OC z cesją na Finansującego — umowa ubezpieczenia zawarta zgodnie z wymogami, z cesją na Finansującego (źródła: DC-2203, UM-7790).

Weryfikacja: werdykt — POTWIERDZONA (wszystkie powyższe warunki są potwierdzone w dokumentacji: DC-2203 i UM-7790).

Zapis do grafu wiedzy (nauka): potwierdzone informacje zostały zapisane w grafie. Fakt zapisany jako learned::fa4be41a23b7300d; dodatkowa jakościowa wskazówka zapisana jako learning::9ecc718389f08dd3.  

Brak brakujących detali zgłoszonych podczas weryfikacji. Jeśli chcesz, mogę odczytać konkretne fragmenty UM-7790 (sekcje/klauzule) potwierdzające każdy punkt.

**Ocena:** czesciowa — Odpowiedź agenta wymienia dodatkowy warunek (umowę ubezpieczenia) i nie wspomina o alternatywie podwyższenia opłaty wstępnej do 30%, a także nie podaje kwoty 20% (36 000 PLN) opłaty wstępnej, co było kluczowym elementem odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź

**Źródła:** oczekiwane ['DC-2203', 'UM-7790']; w odpowiedzi ['DC-2203', 'UM-7790']; pokrycie 1.0

---

## [P2.6] (zestaw 2) ✅ dobra
**Pytanie:** Jak zmieniła się rata kredytu hipotecznego UM-7788 po zmianie wskaźnika i co było przyczyną?

**Oczekiwana:** Rata spadła z 3 688,83 PLN na 3 531,88 PLN, ponieważ NRR 3M spadł z 5,85% (TO-2025-Q1) do 5,35% (TO-2025-Q2), co przy marży 2,10% dało oprocentowanie 7,45% zamiast 7,95%. Nowy harmonogram to HS-7794 (obowiązuje od raty nr 2).

**Odpowiedź agenta:** Krótko: Rata kredytu hipotecznego UM-7788 zmniejszyła się z 3 688,83 PLN do 3 531,88 PLN (obniżka o 156,95 PLN). Przyczyną był spadek wskaźnika NRR 3M z 5,85% do 5,35%, co obniżyło oprocentowanie kredytu z 7,95% do 7,45% (repricing automatyczny zgodnie z zasadami dla stopy zmiennej). (źródła: HS-7788, HS-7794, TO-2025-Q1/TO-2025-Q2, REG-KH-02)

Szczegóły i źródła:
- Poprzednia rata (przed repricingiem): 3 688,83 PLN (HS-7788; uwaga: ostatnia rata nr 300 = 3 688,84 PLN) — źródło: HS-7788.  
- Nowa rata po aktualizacji: 3 531,88 PLN (harmonogram po repricingu) — źródło: HS-7794.  
- Różnica: obniżka o 156,95 PLN (wyliczenie z HS-7788 i HS-7794).  
- Powód: NRR 3M spadł z 5,85% (wartość poprzednia) do 5,35% (TO-2025-Q2), co przy marży 2,10% obniżyło oprocentowanie z 7,95% do 7,45% — źródła: TO-2025-Q1/TO-2025-Q2, HS-7794.  
- Repricing nastąpił automatycznie zgodnie z zasadami oprocentowania zmiennego (REG-KH-02 / postanowienia TO-2025-Qx) — źródła: TO-2025-Q1/TO-2025-Q2, REG-KH-02.

Zapis w grafie wiedzy (wykonany):
Zgodnie z procedurą, zweryfikowane fakty dotyczące UM-7788 zostały zapisane do grafu:
1) aktualna rata 3 531,88 PLN (źródło: HS-7794),  
2) poprzednia rata 3 688,83 PLN (źródło: HS-7788),  
3) zmiana: obniżka 156,95 PLN (HS-7788 + HS-7794),  
4) NRR 3M = 5,35% (powołanie na TO-2025-Q2 / HS-7794),  
5) oprocentowanie zmienione z 7,95% na 7,45% (HS-7788, HS-7794).

Weryfikacja: końcowy werdykt fact-checkera — POTWIERDZONA (źródła: HS-7788, HS-7794, TO-2025-Q1/TO-2025-Q2, REG-KH-02).

Jeśli chcesz, mogę przesłać fragmenty dokumentów (cytaty) potwierdzające poszczególne liczby lub pokazać harmonogram po repricingu (HS-7794).

**Ocena:** dobra — Odpowiedź agenta w pełni zgadza się merytorycznie z odpowiedzią oczekiwaną, podając te same kluczowe liczby i przyczynę zmiany raty.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j) → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['HS-7794', 'REG-KH-02', 'TO-2025-Q2', 'UM-7788']; w odpowiedzi ['HS-7788', 'HS-7794', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'TO-2025-Qx', 'UM-7788']; pokrycie 1.0

---

## [P2.7] (zestaw 2) 🟡 czesciowa
**Pytanie:** Którego klienta i na podstawie jakich zgłoszeń przeklasyfikowano do najwyższej klasy ryzyka (E)?

**Oczekiwana:** Klienta KL-00456 (Marek Nowicki, JDG „MN Trade"). Podstawa: zgłoszenia SAR-0034 (structuring) i SAR-0041 (pass-through) → raport ryzyka RR-0012 → aktualizacja karty KYC-00456 do klasy E.

**Odpowiedź agenta:** - KL-00456 (Marek Andrzej Nowicki) — podstawy: SAR-0034, SAR-0041, RR-0012 — data: 2025-04-16 — (źródła: SAR-0034, SAR-0041, RR-0012, KYC-00456)

Weryfikacja: POTWIERDZONA (źródło potwierdzenia: KYC-00456).  
Zapis do grafu wykonany: learned::1f15381cc106fc7f.

**Ocena:** czesciowa — Agent poprawnie wskazał klienta i zgłoszenia, ale podał inne imię oraz nie wspomniał o aktualizacji karty KYC do klasy E, co jest kluczowe.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00456', 'RR-0012', 'SAR-0034', 'SAR-0041']; w odpowiedzi ['KL-00456', 'KYC-00456', 'RR-0012', 'SAR-0034', 'SAR-0041']; pokrycie 1.0

---

## [P2.8] (zestaw 2) ✅ dobra
**Pytanie:** Jaka jest relacja między zaświadczeniem ZD-4501, wnioskiem WN-4501 i decyzją DC-2201?

**Oczekiwana:** ZD-4501 jest załącznikiem nr 1 do wniosku WN-4501 i potwierdza dochód netto 10 100 PLN; ten dochód został użyty w decyzji DC-2201 do wyliczenia wskaźnika DTI (36,52%).

**Odpowiedź agenta:** Odpowiedź (zwięźle):

Na podstawie grafu: ZD-4501 jest załącznikiem do wniosku WN-4501; decyzja DC-2201 dotyczy wniosku WN-4501 i bazuje na danych z ZD-4501 (m.in. dochód użyty do obliczenia wskaźnika DTI). (źródło: ZD-4501, WN-4501, DC-2201)

Relacje:
- ZD-4501 — załącznik → WN-4501 (rola: załącznik nr 1) (źródło: ZD-4501, WN-4501)
- DC-2201 — decyzja dotycząca → WN-4501 (rola: decyzja rozstrzygająca) (źródło: DC-2201, WN-4501)
- DC-2201 — bazuje na danych z → ZD-4501 (dochód wykorzystany do obliczenia DTI) (źródło: DC-2201, ZD-4501)

Powiązane dodatkowe dokumenty: TO-2025-Q1, REG-KH-02, POL-RYZYKO-01 (wskazane w DC-2201 jako dokumenty powiązane). (źródło: DC-2201)

Pola grafu wykorzystane: nodes: ZD-4501, WN-4501, DC-2201; relation types: "załącza"/"załącznik", "wydana zgodnie z"/"decyzja dotycząca", "bazuje na"/"wykorzystane_dane". Odpowiedź zweryfikowana jako POTWIERDZONA i zapisana w grafie.

**Ocena:** dobra — Odpowiedź agenta poprawnie wskazuje, że ZD-4501 jest załącznikiem nr 1 do wniosku WN-4501 oraz że decyzja DC-2201 bazuje na danych z ZD-4501, w tym na dochodzie użytym do obliczenia wskaźnika DTI; jedynie nie podano konkretnej wartości dochodu netto i wskaźnika DTI, które były w odpowiedzi oczekiwanej, jednak kluczowa relacja została zachowana.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['DC-2201', 'WN-4501', 'ZD-4501']; w odpowiedzi ['DC-2201', 'POL-RYZYKO-01', 'REG-KH-02', 'TO-2025-Q1', 'WN-4501', 'ZD-4501']; pokrycie 1.0

---

## [P2.9] (zestaw 2) ✅ dobra
**Pytanie:** Ile wynosi rata leasingowa netto i brutto oraz z czego wynika różnica?

**Oczekiwana:** Rata netto 3 586,87 PLN, brutto 4 411,85 PLN; różnica to VAT 23% doliczany do raty leasingu.

**Odpowiedź agenta:** Rata leasingowa netto: 3 586,87 PLN.  
Rata leasingowa brutto: 4 411,85 PLN.  
Kwota VAT (różnica): 824,98 PLN (stawka 23%).

Różnica wynika z doliczenia podatku VAT zgodnie z formułą: Rata brutto = Rata netto + (Rata netto × VAT%). (źródła: HS-7790, UM-7790, REG-LE-04)

Fakt został zapisany do grafu wiedzy (ID: learned::cc09f6035b4c603b) i dopisano krótką wskazówkę jakościową dotycząca konieczności sprawdzania HS/UM dla konkretnych kwot, zamiast polegania tylko na regulaminie.

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe fakty i liczby zgodne z odpowiedzią oczekiwaną, dokładnie wyjaśniając źródło różnicy jako VAT 23%.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j) → odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź

**Źródła:** oczekiwane ['HS-7790', 'UM-7790']; w odpowiedzi ['HS-7790', 'REG-LE-04', 'UM-7790']; pokrycie 1.0

---

## [P2.10] (zestaw 2) ✅ dobra
**Pytanie:** Czy profil ryzyka klienta KL-00124 jest zgodny z pozytywnym rozstrzygnięciem decyzji DC-2202?

**Oczekiwana:** Tak. KYC-00124: klasa A, scoring 92/100, brak zobowiązań; DC-2202: DTI 13,23%, spełnione kryteria POL-RYZYKO-01 — decyzja pozytywna spójna z profilem.

**Odpowiedź agenta:** Tak — profil ryzyka klienta KL-00124 jest zgodny z pozytywnym rozstrzygnięciem decyzji DC-2202; decyzja potwierdza klasę A, scoring 92 i DTI 13,23% jako spełniające wymogi (źródło: DC-2202). 

Zapis do grafu: fakt o zgodności KL-00124 z DC-2202 został zapisany w grafie (status: saved).

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe fakty i liczby zgodne z odpowiedzią oczekiwaną, potwierdzając klasę A, scoring 92 oraz DTI 13,23% i zgodność profilu z decyzją DC-2202.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2202', 'KYC-00124', 'POL-RYZYKO-01']; w odpowiedzi ['DC-2202', 'KL-00124']; pokrycie 0.33

---

## [P2.11] (zestaw 2) ✅ dobra
**Pytanie:** Kto jest kredytobiorcą w umowie UM-7789, jaki jest cel kredytu i na jaki rachunek następuje spłata?

**Oczekiwana:** Katarzyna Maria Lewandowska (KL-00124); cel: remont mieszkania; rachunek spłaty (testowy) PL33 9999 1000 0000 0077 8900 0002.

**Odpowiedź agenta:** Kredytobiorcą w umowie UM-7789 jest Katarzyna Maria Lewandowska (PESEL 90111067321, ul. Słoneczna 5 m.2, 80-100 Gdańsk). Celem kredytu jest remont mieszkania. Spłata kredytu następuje na rachunek PL33 9999 1000 0000 0077 8900 0002 należący do Katarzyny Marii Lewandowskiej (źródło: UM-7789, KYC-00124, HS-7789).

Informuję także, że powyższy fakt został zapisany do grafu wiedzy (UM-7789; źródła: UM-7789, KYC-00124, HS-7789).

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe informacje oczekiwane: poprawnego kredytobiorcę, cel kredytu oraz rachunek spłaty zgodny z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00124', 'UM-7789']; w odpowiedzi ['HS-7789', 'KYC-00124', 'UM-7789']; pokrycie 1.0

---

## [P2.12] (zestaw 2) ✅ dobra
**Pytanie:** Które oprocentowanie zastosowano w kredycie gotówkowym z wniosku WN-4506 i skąd ono pochodzi?

**Oczekiwana:** 10,90% stałe (przedział 20 001–60 000 PLN) — z tabeli TO-2025-Q2 (wniosek złożony w Q2 2025). Rata 980,74 PLN dla 30 000 PLN na 36 mies.

**Odpowiedź agenta:** Oprocentowanie stałe 10,90% zastosowano w kredycie gotówkowym z wniosku WN-4506. Pochodzi ono z warunków samego wniosku oraz z tabeli oprocentowania TO-2025-Q2 i jest potwierdzone decyzją kredytową DC-2206 (źródła: WN-4506, TO-2025-Q2, DC-2206).

Weryfikator: POTWIERDZONA.  
Zapis do grafu: zweryfikowany fakt dodany (id: learned::ebc57649a3b3646d).

**Ocena:** dobra — Odpowiedź agenta prawidłowo wskazuje oprocentowanie 10,90% stałe oraz źródło – tabelę TO-2025-Q2 i sam wniosek, zgodnie z odpowiedzią oczekiwaną, dodatkowo podając potwierdzenie decyzją kredytową, co nie stoi w sprzeczności z wymaganiami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2206', 'TO-2025-Q2', 'WN-4506']; w odpowiedzi ['DC-2206', 'TO-2025-Q2', 'WN-4506']; pokrycie 1.0

---

## [P2.13] (zestaw 2) ✅ dobra
**Pytanie:** Czym różnią się dwie historie transakcji (HT-00123 i HT-00456) i jakie skutki compliance z nich wynikły?

**Oczekiwana:** HT-00123 (KL-00123) to normalny profil detaliczny (wynagrodzenie, spłata raty, wydatki bytowe) — brak przesłanek AML. HT-00456 (KL-00456) wykazuje structuring i transfery pass-through do jurysdykcji wysokiego ryzyka — skutkuje zgłoszeniami SAR-0034/0041.

**Odpowiedź agenta:** Odpowiedź przygotowana. Weryfikator potwierdził poprawność i brak braków; poniżej krótkie podsumowanie (źródła w nawiasach):

1) Główne różnice:
- HT-00123: klient detaliczny, transakcje krajowe, brak structuringu i pass-through, brak zgłoszeń SAR (źródła: HT-00123, UM-7788).  
- HT-00456: zgłoszenia SAR dotyczące structuringu i pass-through, wystawiono raport ryzyka wskazujący wysokie ryzyko (klasa E) (źródła: HT-00456, SAR-0034, SAR-0041, RR-0012).

2) Skutki compliance dla HT-00123:
- Brak działań nadzwyczajnych — brak nieprawidłowości AML i SAR; standardowe monitorowanie i spłaty rat z umowy UM-7788 (źródła: HT-00123, UM-7788).

3) Skutki compliance dla HT-00456:
- Wygenerowano raport RR-0012 z rekomendacjami: reklasyfikacja do klasy E (wysokie ryzyko), wdrożenie EDD, wstrzymanie nowych produktów kredytowych oraz rozważenie zakończenia relacji (źródła: HT-00456, SAR-0034, SAR-0041, RR-0012).

Dodatkowo informuję, że odpowiedź została zapisana do grafu wiedzy jako nowy zweryfikowany fakt (nauka): porównanie i konsekwencje compliance dla HT-00123 vs HT-00456 (entry powiązany z HT-00123 i HT-00456).

**Ocena:** dobra — Odpowiedź agenta dokładnie odzwierciedla kluczowe fakty i skutki compliance zgodnie z odpowiedzią oczekiwaną, uwzględniając brak przesłanek AML w HT-00123 oraz structuring i pass-through wraz ze zgłoszeniami SAR w HT-00456.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['HT-00123', 'HT-00456', 'SAR-0034', 'SAR-0041']; w odpowiedzi ['HT-00123', 'HT-00456', 'RR-0012', 'SAR-0034', 'SAR-0041', 'UM-7788']; pokrycie 1.0

---

## [P2.14] (zestaw 2) ✅ dobra
**Pytanie:** Jakie zabezpieczenia ustanowiono dla kredytu hipotecznego UM-7788 i jak mają się one do wymogów polityki ryzyka?

**Oczekiwana:** Hipoteka umowna do 720 000 PLN (150% kwoty), cesja z polisy ubezpieczenia nieruchomości, ubezpieczenie pomostowe do wpisu hipoteki — zgodne z wymogiem zabezpieczenia hipotecznego z POL-RYZYKO-01 §4.

**Odpowiedź agenta:** Odpowiedź (zwięźle):

1) Ustanowione zabezpieczenia
- Hipoteka umowna do kwoty 720 000,00 PLN (150% kwoty kredytu) na nieruchomości wpisanej w KW GD1Y/00099999/9 (ul. Morska 22 m.5, Gdynia). (źródło: UM-7788, DC-2201)  
- Cesja praw z polisy ubezpieczenia nieruchomości od ognia i zdarzeń losowych na rzecz banku. (źródło: UM-7788, DC-2201)  
- Ubezpieczenie pomostowe obowiązujące do dnia prawomocnego wpisu hipoteki (obejmuje okres między uruchomieniem kredytu a wpisem hipoteki). (źródło: UM-7788, DC-2201)  
- Brak poręczeń wymienionych jako zabezpieczenie w dokumentacji UM-7788/DC-2201. (źródło: UM-7788, DC-2201)

2) Kluczowe liczby związane z zabezpieczeniem
- Kwota kredytu: 480 000,00 PLN; wartość nieruchomości: 600 000,00 PLN → LTV ≈ 80%. (źródło: UM-7788, DC-2201)  

3) Zgodność z polityką ryzyka (POL-RYZYKO-01)
- Zabezpieczenia (hipoteka przewyższająca kwotę kredytu, cesja polisy, ubezpieczenie pomostowe) oraz LTV ≈ 80% są zgodne z wymogami polityki ryzyka wskazanymi w POL-RYZYKO-01 (zgodność potwierdzona w dokumentacji decyzji kredytowej). (źródło: DC-2201; powiązanie z POL-RYZYKO-01 w grafie)  
- Profil klienta (KYC: klasa B, scoring 78/100) jest akceptowalny w świetle decyzji kredytowej i polityki ryzyka. (źródło: KYC-00123, DC-2201)

4) Krótkie podsumowanie oceny
- Zabezpieczenia są kompletne i wystarczające w świetle dokumentów: hipoteka + cesja polisy + ubezpieczenie pomostowe zapewniają ochronę banku; LTV mieści się w przyjętych limitach polityki ryzyka. (źródła: UM-7788, DC-2201, KYC-00123)

5) Zapis do grafu (potwierdzenie nauki)
Na podstawie przeglądu dokumentów zapisano/uzupełniono w grafie następujące zweryfikowane fakty dotyczące UM-7788:
- nominalne oprocentowanie początkowe 7,95% (NRR 3M 5,85% + marża 2,10%) — źródła: UM-7788, TO-2025-Q1, DC-2201;  
- zmiana oprocentowania od 01.04.2025 na 7,45% (NRR 3M 5,35% + marża 2,10%) oraz nowa rata od 15.04.2025 = 3 531,88 PLN — źródło: HS-7794;  
- prowizja przygotowawcza 2% = 9 600 PLN oraz opłata za wycenę 500 PLN — źródła: UM-7788, TOP-2025-Q1, DC-2201;  
- RRSO 8,50%; całkowite odsetki 626 649,94 PLN; całkowity koszt 636 749,94 PLN; daty zawarcia/uruchomienia i pierwszej raty (14.02.2025, 20.02.2025, 15.03.2025) — źródło: UM-7788, HS-7788.  
Dodatkowo w grafie dodano krótką wskazówkę jakościową przypisaną do UM-7788: uwaga o wcześniejszym braku danych o oprocentowaniu i aktualizacjach rat oraz konieczności uwzględniania kosztów (prowizje, RRSO) i kwartalnych zmian NRR. (Zapis wykonany — fakt nauki został dokonany).

6) Źródła (wybrane)
UM-7788, DC-2201, HS-7788, HS-7794, TO-2025-Q1, KYC-00123, TOP-2025-Q1.

Jeśli chcesz, mogę przesłać krótką listę kontrolną dokumentów i konkretnych paragrafów (np. punktów umowy) lub wygenerować jednozdaniowe potwierdzenie zgodności dla raportu compliance.

**Ocena:** dobra — Odpowiedź agenta zawiera kompletne i zgodne z oczekiwaniami informacje dotyczące ustanowionych zabezpieczeń (hipoteka umowna do 720 000 PLN, cesja polisy, ubezpieczenie pomostowe) oraz potwierdza ich zgodność z wymogami polityki ryzyka POL-RYZYKO-01 §4.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź

**Źródła:** oczekiwane ['POL-RYZYKO-01', 'UM-7788']; w odpowiedzi ['DC-2201', 'HS-7788', 'HS-7794', 'KYC-00123', 'POL-RYZYKO-01', 'TO-2025-Q1', 'TOP-2025-Q1', 'UM-7788']; pokrycie 1.0

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

**Odpowiedź agenta:** Oto zwięzłe, weryfikowane podsumowanie kompletnego łańcucha kredytu hipotecznego Anny Kowalskiej oraz status zapisu do grafu.

1) Powiązane dokumenty (pełny łańcuch)
- KYC: KYC-00123 (profil klienta)  
- WN (wniosek): WN-4501  
- DC (decyzja kredytowa): DC-2201  
- UM (umowa kredytu): UM-7788  
- HS (harmonogram spłat, załącznik): HS-7788

2) Kluczowe liczby / fakty (źródła)
- PESEL klientki: 85072812345 (KYC-00123; potwierdzone też we WN-4501, UM-7788).  
- Kwota kredytu: 480 000,00 PLN (WN-4501; DC-2201; UM-7788; HS-7788).  
- Okres kredytowania: 300 miesięcy (25 lat) (WN-4501; DC-2201; UM-7788; HS-7788).  
- Rodzaj rat: równe (annuitetowe) (WN-4501; DC-2201; UM-7788; HS-7788).  
- Oprocentowanie: zmienne — NRR 3M 5,85% + marża 2,10% = 7,95% nominalne (DC-2201; UM-7788; HS-7788).  
- Rata miesięczna: 3 688,83 PLN (HS-7788; DC-2201; UM-7788). Ostatnia rata: 3 688,84 PLN (drobna korekta) (HS-7788).  
- Prowizja przygotowawcza: 2,00% = 9 600,00 PLN (DC-2201; UM-7788).  
- Opłata za wycenę: 500,00 PLN (UM-7788).  
- Data uruchomienia: 20.02.2025 (UM-7788).  
- Pierwsza rata (termin): 15.03.2025 (HS-7788).  
Źródła: KYC-00123, WN-4501, DC-2201, UM-7788, HS-7788.

3) Spójność i niezgodności
- Werdykt weryfikatora: POTWIERDZONA — wszystkie kluczowe wartości mają pokrycie w dokumentach i są spójne między sobą. (weryfikacja: KYC-00123, WN-4501, DC-2201, UM-7788, HS-7788)  
- Nie wykryto rozbieżności między wnioskiem → decyzją → umową → harmonogramem dotyczącymi kwoty, okresu, rodzaju rat, oprocentowania, prowizji ani wysokości raty.  
- Uwaga: harmonogram zawiera korektę ostatniej raty o 0,01 PLN (ostatnia rata 3 688,84 PLN) — zgodne z HS-7788.

4) Braki / uwagi proceduralne
- Początkowo graf nie zawierał numeru PESEL — PESEL został potwierdzony w dokumentach i dopisany do grafu (zapisałem ten fakt). Po tej aktualizacji nie ma braków ważnych dla analizy finansowej łańcucha.

5) Zapis do grafu (moment nauki) — wykonane
- Zapisano fakt PESEL klienta (85072812345) powiązany z encją Anna Kowalska / KYC-00123 / UM-7788 — id zapisu: learned::a1079d2dd4aed576.  
- Zapisano fakt parametrów kredytu (kwota, okres, raty, oprocentowanie rozbite na NRR+marża, rata, prowizja, opłaty, daty, HS-7788 jako załącznik) — id zapisu: learned::209fe4cb9976c15a.  
- Dodano wskazówkę jakościową powiązaną z KYC-00123 (o konieczności synchronizacji PESEL z dokumentami i uwadze na oznaczenia typu "PESEL (TESTOWY)") — id zapisu: learning::8ab4a3725de051c7.

6) Krótkie podsumowanie
Łańcuch kredytowy Anny Kowalskiej (KYC-00123 → WN-4501 → DC-2201 → UM-7788 → HS-7788) jest kompletny i spójny pod względem wszystkich kluczowych liczb i terminów. W grafie uzupełniono brakujący PESEL i zapisano zweryfikowane parametry kredytu (widoczne w grafie pod podanymi id).

Jeśli chcesz, mogę:
- dostarczyć bezpośrednie cytaty (fragmenty) z konkretnych sekcji dokumentów (podaj które dokumenty/sekcje chcesz zobaczyć dokładniej),  
- wygenerować CSV z harmonogramem rat (pierwsze 24 + ostatnie 3) z HS-7788.

**Ocena:** dobra — Odpowiedź agenta pokrywa kompletność i spójność kluczowych liczb oraz identyfikuje pełny łańcuch dokumentów zgodnie z odpowiedzią oczekiwaną, zawierając właściwe wartości kwoty kredytu, oprocentowania, raty, prowizji i okresu.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'HS-7788', 'KYC-00123', 'POL-RYZYKO-01', 'REG-KH-02', 'TO-2025-Q1', 'TOP-2025-Q1', 'UM-7788', 'WN-4501', 'ZD-4501']; w odpowiedzi ['DC-2201', 'HS-7788', 'KYC-00123', 'UM-7788', 'WN-4501']; pokrycie 0.5

---

## [P3.2] (zestaw 3) ✅ dobra
**Pytanie:** Wyjaśnij, w jaki sposób działania compliance doprowadziły do odmowy kredytu Markowi Nowickiemu — od transakcji do decyzji. Wskaż całą sekwencję.

**Oczekiwana:** - Rachunek firmowy (HT-00456) wykazał wpłaty gotówkowe rozbijane poniżej progu 15 000 PLN (structuring) i szybkie transfery ~464 950 PLN do Vantia (pass-through).
  - Powstały zgłoszenia SAR-0034 (structuring) i SAR-0041 (pass-through), oba na podstawie POL-AML-01.
  - Raport ryzyka RR-0012 zagregował oba SAR-y i rekomendował klasę E oraz wstrzymanie nowych kredytów.
  - Kartę KYC-00456 zaktualizowano do klasy E (WYSOKIE), wdrożono EDD.
  - Kolejny wniosek WN-4508 (kredyt 80 000 PLN) otrzymał decyzję **negatywną DC-2250** — mimo DTI 16,20% — z powodu klasy E i braku możliwości ustalenia źródła środków.
  - To pełna pętla zwrotna: transakcje → ryzyko → odmowa.

**Odpowiedź agenta:** Poniżej wyjaśnienie sekwencji — krok po kroku — w jaki sposób działania compliance doprowadziły do odmowy kredytu Markowi Nowickiemu. Odpowiedź oparta wyłącznie na dokumentach: WN-4508, DC-2250, KYC-00456, SAR-0034, SAR-0041, HT-00456.

Sekwencja przyczynowo-skutkowa:
1. Nieprawidłowe wzorce transakcyjne na rachunku firmowym:
   - Analiza historii transakcji HT-00456 (01.02.2025–31.03.2025) wykazała 54 wpłaty gotówkowe łącznie 478 800 PLN realizowane w kwotach 9 400–9 900 PLN (tuż poniżej wewnętrznego progu alertu 15 000 PLN) oraz duże transfery zagraniczne do jurysdykcji wysokiego ryzyka (464 950 PLN). Brak faktur i dokumentacji handlowej uzasadniającej obroty. (źródło: HT-00456, KYC-00456)

2. Wydanie zgłoszeń transakcji podejrzanych (SAR):
   - Na podstawie powyższych anomalii sporządzono SAR-0034 (typologia: structuring / rozbijanie wpłat) oraz SAR-0041 (typologia: pass-through / rachunek tranzytowy). Zgłoszenia rekomendowały wzmożone monitorowanie, eskalację i dalsze działania analityczne. (źródło: SAR-0034, SAR-0041, HT-00456)

3. Wzmożone środki bezpieczeństwa i podniesienie kategorii ryzyka:
   - Departament Zgodności wdrożył wzmożone środki (EDD) i przeprowadził przegląd profilu klienta. W wyniku analizy nadano klientowi klasę ryzyka E (wysokie), wskazując na znaczące ryzyko AML oraz brak wystarczającej dokumentacji źródła środków (KYC-00456, RR-0012 powiązany). (źródło: KYC-00456, SAR-0034, SAR-0041)

4. Wpływ na ocenę wniosku kredytowego:
   - Wniosek kredytowy WN-4508 trafił do oceny już przy obowiązujących wskazaniach compliance (klient objęty wzmożonym monitoringiem, aktywny raport ryzyka). Departament Zgodności przekazał opinię do Komitetu Kredytowego, wskazując na ryzyko wynikające z SAR i braku dokumentacji źródła środków. (źródło: WN-4508, KYC-00456, SAR-0034, SAR-0041)

5. Decyzja odmowna:
   - Komitet kredytowy, powołując się na polityki bankowe (POL-AML-01, POL-RYZYKO-01) oraz na fakt, że nie udało się ustalić źródła środków pomimo wezwań i wdrożonych EDD, podjął decyzję o odmowie udzielenia kredytu (DC-2250). W uzasadnieniu wskazano: klasa ryzyka E, brak możliwości ustalenia źródła środków oraz obowiązujące restrykcje co do udzielania nowych produktów klientom o takim profilu. (źródło: DC-2250, WN-4508, KYC-00456)

Krótko: wykryte w HT-00456 wzory wskazujące na structuring i pass-through → złożenie SAR-0034 i SAR-0041 → nadanie klasy ryzyka E i wdrożenie EDD w KYC-00456 → opinia compliance przekazana przy ocenie wniosku WN-4508 → odmowa kredytu DC-2250 z powodu braku możliwości ustalenia źródła środków i wysokiego ryzyka AML.

Dokumenty źródłowe (użyte przy powyższym wyjaśnieniu):
WN-4508, DC-2250, KYC-00456, SAR-0034, SAR-0041, HT-00456.

Dodatkowo: zapis do grafu wiedzy wykonany
- Fakt z opisem powyższej sekwencji zapisano w grafie jako learned::c1f76768d91af957 (encja KL-00456).
- Dodano wskazówkę jakościową dla encji KL-00456 jako learning::56455b99036ba2f4.
Potwierdzam, że wiedza ta została zapisana w grafie zgodnie z procedurą nauki.

**Ocena:** dobra — Odpowiedź agenta wiernie odzwierciedla kluczowe fakty, liczby i sekwencję przedstawioną w odpowiedzi oczekiwanej, zachowując pełną spójność merytoryczną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250', 'HT-00456', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'WN-4508']; w odpowiedzi ['DC-2250', 'HT-00456', 'KL-00456', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'WN-4508']; pokrycie 1.0

---

## [P3.3] (zestaw 3) 🟡 czesciowa
**Pytanie:** Porównaj trzy typy decyzji kredytowych w zbiorze (pozytywną, warunkową, negatywną) i wskaż, jak profil ryzyka z KYC oraz polityki determinowały wynik każdej z nich.

**Oczekiwana:** - **Pozytywna — DC-2201** (Anna Kowalska): klasa B, DTI 36,52%, LTV 80% — wszystkie kryteria POL-RYZYKO-01 spełnione → udzielenie kredytu.
  - **Warunkowa — DC-2203** (Bałtyk Logistyka): klasa C przy podwyższonym zadłużeniu → zgoda pod warunkiem opłaty wstępnej 30% lub dodatkowego zabezpieczenia (POL-RYZYKO-01 §5).
  - **Negatywna — DC-2250** (Marek Nowicki): zdolność wystarczająca (DTI 16,20%), ale klasa E z RR-0012 (AML) → odmowa (POL-RYZYKO-01 §5, POL-AML-01).
  - Wniosek: o wyniku decydował nie tylko wskaźnik finansowy, lecz klasa ryzyka (w tym override z tytułu AML).

**Odpowiedź agenta:** Porównanie trzech typów decyzji kredytowych oraz wpływ profilu ryzyka i polityk

Pozytywna decyzja kredytowa
- ID decyzji: DC-2202 (źródło: DC-2202)  
- Dokumenty KYC: KYC-00124; powiązane: WN-4502, ZD-4503 (źródła: KYC-00124, WN-4502, ZD-4503)  
- Kluczowe liczby: scoring 92; DTI 13,23%; klasa ryzyka A (źródła: KYC-00124, DC-2202)  
- Zastosowane polityki: POL-RYZYKO-01 (kryteria klas A–C, DTI ≤45%, scoring ≥60), REG-KG-01, TO-2025-Q1, UM-7789 (źródła: POL-RYZYKO-01, REG-KG-01, TO-2025-Q1, UM-7789)  
- Wyjaśnienie: Wysoki scoring (92) i niski DTI (13,23%) kwalifikowały klienta do klasy A zgodnie z POL-RYZYKO-01, co bez dodatkowych warunków doprowadziło do decyzji pozytywnej (źródła: DC-2202, POL-RYZYKO-01).

Warunkowa decyzja kredytowa
- ID decyzji: DC-2203 (źródło: DC-2203)  
- Dokumenty KYC: KYC-00125; powiązane: WN-4503 (źródła: KYC-00125, WN-4503)  
- Kluczowe liczby: scoring 70; klasa ryzyka C (źródło: KYC-00125, DC-2203)  
- Zastosowane polityki: POL-RYZYKO-01 (warunkowe decyzje dla klas C–D), REG-LE-04, TO-2025-Q1 (źródła: POL-RYZYKO-01, REG-LE-04, TO-2025-Q1)  
- Wyjaśnienie: Klient klasy C (scoring 70) spełniał warunkowe kryteria (POL-RYZYKO-01); aby obniżyć ryzyko wymuszono warunki (np. podwyższenie opłaty wstępnej 20%→30% lub dodatkowe zabezpieczenie, dostarczenie ZUS/US, cesja ubezpieczenia), co umożliwiło pozytywną decyzję pod warunkiem ich spełnienia (źródło: DC-2203, POL-RYZYKO-01).

Negatywna decyzja kredytowa
- ID decyzji: DC-2250 (źródło: DC-2250)  
- Dokumenty KYC: KYC-00456; dodatkowo raport RR-0012 (źródła: KYC-00456, RR-0012)  
- Kluczowe liczby: scoring 66, ale override do klasy ryzyka E; DTI 16,20% (źródła: KYC-00456, RR-0012, DC-2250)  
- Zastosowane polityki: POL-RYZYKO-01 (negatywna gdy klasa E lub nieusuwalne ryzyka), POL-AML-01 (EDD, wstrzymanie/odmowa przy wysokim ryzyku AML), REG-KG-01 (źródła: POL-RYZYKO-01, POL-AML-01, REG-KG-01)  
- Wyjaśnienie: Mimo umiarkowanego DTI, klient otrzymał override do klasy E z powodu sygnałów AML i braku możliwości ustalenia źródła środków (RR-0012); zgodnie z POL-RYZYKO-01 i POL-AML-01 rekomendacja wstrzymania/odmowy doprowadziła do decyzji negatywnej (źródła: DC-2250, RR-0012, POL-RYZYKO-01, POL-AML-01).

Notatka o zapisie do grafu
- Zapisano do grafu trzy zweryfikowane fakty dotyczące DC-2202, DC-2203 i DC-2250 oraz dodano do grafu trzy jakościowe wskazówki powiązane z encjami decyzji (potwierdzenie zapisu w grafie: DC-2202, DC-2203, DC-2250).

Źródła: DC-2202, DC-2203, DC-2250, KYC-00124, KYC-00125, KYC-00456, RR-0012, POL-RYZYKO-01, POL-AML-01, REG-KG-01, REG-LE-04, TO-2025-Q1, UM-7789, WN-4502, WN-4503, ZD-4503, ZD-4508.

**Ocena:** czesciowa — Odpowiedź agenta poprawnie klasyfikuje decyzje i odnosi się do profilu ryzyka oraz polityk, jednak niezgodności w ID pozytywnej decyzji (DC-2202 zamiast DC-2201) oraz inne wartości DTI i scoringów różnią się od oczekiwanych, co obniża zgodność merytoryczną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'DC-2203', 'DC-2250', 'KYC-00123', 'KYC-00125', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012']; w odpowiedzi ['DC-2202', 'DC-2203', 'DC-2250', 'KYC-00124', 'KYC-00125', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'REG-KG-01', 'REG-LE-04', 'RR-0012', 'TO-2025-Q1', 'UM-7789', 'WN-4502', 'WN-4503', 'ZD-4503', 'ZD-4508']; pokrycie 0.78

---

## [P3.4] (zestaw 3) ✅ dobra
**Pytanie:** Oblicz łączną kwotę odsetek dla wszystkich kredytów/leasingów z zawartymi umowami w zbiorze i podaj źródła.

**Oczekiwana:** - Kredyt hipoteczny UM-7788: odsetki 626 649,94 PLN wg pierwotnego HS-7788 (lub 579 719,78 PLN po repricingu wg HS-7794, przy założeniu utrzymania 7,45%).
  - Kredyt gotówkowy UM-7789: odsetki 15 077,76 PLN (HS-7789).
  - Leasing UM-7790: część odsetkowa 28 169,56 PLN netto (HS-7790).
  - **Suma (wariant pierwotny hipoteki):** 626 649,94 + 15 077,76 + 28 169,56 = **669 897,26 PLN**.
  - (Uwaga: umowa karty UM-7791 nie ma z góry ustalonych odsetek — zależą od wykorzystania limitu; wniosek WN-4508 odrzucono, więc go nie liczymy.)

**Odpowiedź agenta:** Odpowiedź — lista umów z odsetkami (kwoty zgodne z dokumentami):

1) UM-7790 — leasing — 28 169,56 PLN (źródła: UM-7790, HS-7790, TO-2025-Q1, DC-2203)  
2) UM-7788 — kredyt hipoteczny — 626 649,94 PLN (źródła: UM-7788, HS-7788, TO-2025-Q1, DC-2201)  
3) UM-7789 — kredyt gotówkowy — 15 077,76 PLN (źródła: UM-7789, HS-7789, TO-2025-Q1, DC-2202)

Łączna kwota odsetek dla wszystkich kredytów/leasingów: 669 897,26 PLN.

Kompletność danych: wszystkie wymienione pozycje mają complete_data = yes (dane wystarczające do obliczenia odsetek).

Wykorzystane dokumenty (pełna lista źródeł): UM-7790, HS-7790, UM-7788, HS-7788, UM-7789, HS-7789, TO-2025-Q1, DC-2201, DC-2202, DC-2203.

Weryfikacja: propozycja została sprawdzona i zweryfikowana jako POTWIERDZONA (verifier).

Zapis do grafu (nauka): zweryfikowane fakty zostały zapisane do grafu wiedzy:
- UM-7788: total_interest = 626649.94 PLN (id zapisu: learned::9ed3019d50ce91dd)  
- UM-7789: total_interest = 15077.76 PLN (id zapisu: learned::3c5739a65a5cbfd3)  
- Fakt zbiorczy signed_agreements_total_interest = 669897.26 PLN (id zapisu: learned::b3828430f2650bc4)

Jeśli chcesz, mogę wygenerować szczegółowe wyciągi/harmonogramy (wiersz po wierszu) z dokumentów HS-* dla każdej umowy.

**Ocena:** dobra — Odpowiedź agenta jest kompletna i merytorycznie zgodna z oczekiwaną, ze wszystkimi kluczowymi kwotami i źródłami poprawnie wskazanymi oraz sumą odsetek zgodną z wariantem pierwotnym. 

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788', 'HS-7789', 'HS-7790', 'HS-7794', 'UM-7788', 'UM-7789', 'UM-7790']; w odpowiedzi ['DC-2201', 'DC-2202', 'DC-2203', 'HS-7788', 'HS-7789', 'HS-7790', 'TO-2025-Q1', 'UM-7788', 'UM-7789', 'UM-7790']; pokrycie 0.86

---

## [P3.5] (zestaw 3) ✅ dobra
**Pytanie:** Opisz mechanizm i finansowy skutek zmiany wskaźnika NRR 3M dla kredytu hipotecznego — wskaż dokumenty i kwoty.

**Oczekiwana:** - NRR 3M spadł z 5,85% (TO-2025-Q1) do 5,35% (TO-2025-Q2), tj. o 0,50 p.p.
  - Zgodnie z REG-KH-02 §3 (oprocentowanie zmienne, aktualizacja kwartalna, marża stała), oprocentowanie UM-7788 zmieniło się z 7,95% na 7,45% bez aneksu.
  - Bank sporządził zaktualizowany harmonogram HS-7794 (od raty nr 2): rata spadła z 3 688,83 na **3 531,88 PLN** (o 156,95 PLN).
  - Łączne odsetki spadły z 626 649,94 do 579 719,78 PLN (oszczędność ok. 46 930,16 PLN przy utrzymaniu 7,45%).
  - Efekt widoczny na wyciągu HT-00123 (rata 1 = 3 688,83, raty 2–3 = 3 531,88).

**Odpowiedź agenta:** Oto zwięzłe wyjaśnienie mechanizmu i konkretnego skutku finansowego zmiany NRR 3M na przykładzie dokumentów banku Nordvik.

1) Mechanizm (jak NRR 3M wpływa na oprocentowanie)
- Oprocentowanie zmienne kredytu = NRR 3M + marża banku (marża jest stała dla umowy). (źródło: REG-KH-02 §3.1; TO-2025-Q1 §1–§2)  
- Aktualizacja wartości NRR 3M jest kwartalna; zmiana NRR 3M powoduje automatyczną aktualizację oprocentowania według obowiązującej tabeli TO bez wymogu aneksu do umowy. (źródło: REG-KH-02 §3.3; TO-2025-Q1 §7; TO-2025-Q2 §7)

2) Konkretny finansowy skutek — przykład (umowa UM-7788 / decyzja DC-2201)
Dane wyjściowe: kwota kredytu 480 000 PLN, okres 300 mies., marża 2,10% (LTV ≤ 80%). (źródło: DC-2201; UM-7788)

- Stan przed (I kw. 2025):  
  - NRR 3M = 5,85% → oprocentowanie nominalne = 5,85% + 2,10% = 7,95%. (źródło: TO-2025-Q1; UM-7788)  
  - miesięczna rata annuitetowa wg harmonogramu HS-7788: 3 688,83 PLN. (źródło: HS-7788; UM-7788)

- Stan po zmianie (II kw. 2025):  
  - NRR 3M = 5,35% → oprocentowanie nominalne = 5,35% + 2,10% = 7,45%. (źródło: TO-2025-Q2)  
  - zaktualizowany harmonogram HS-7794: rata zmieniona do 3 531,88 PLN (od wskazanej daty/raty). (źródło: HS-7794)

- Różnica i skutek:  
  - Różnica miesięczna raty: 3 688,83 PLN − 3 531,88 PLN = 156,95 PLN mniej miesięcznie. (źródło: HS-7788; HS-7794)  
  - Szacowana łączna oszczędność na odsetkach przy założeniu utrzymania nowych warunków do końca okresu: ~46 930,16 PLN (wartość podana w HS-7794). (źródło: HS-7794)

3) Daty/efektywność zmiany
- Nowe oprocentowanie i harmonogram obowiązują zgodnie z zapisami tabeli TO i harmonogramem (przykładowo HS-7794 wskazuje pierwszą ratę wg nowego harmonogramu 15.04.2025). (źródło: TO-2025-Q2; HS-7794)

4) Źródła (dokumenty cytowane powyżej)
- TO-2025-Q1, TO-2025-Q2, REG-KH-02, UM-7788, HS-7788, HS-7794, DC-2201.

Weryfikacja i zapis do grafu
- Odpowiedź została zweryfikowana jako POTWIERDZONA przez weryfikatora.  
- Zapis do grafu wiedzy (graph_add_learned_fact) oraz dodanie jakościowej wskazówki (graph_add_learning) zostały wykonane dla encji „NRR 3M” i „oprocentowanie zmienne”, z powiązaniem źródeł: TO-2025-Q1, TO-2025-Q2, REG-KH-02, UM-7788, HS-7788, HS-7794, DC-2201.

Jeśli chcesz, mogę: (a) pokazać fragmenty dokumentów zawierające cytowane liczby (linie z plików), (b) policzyć dokładne oszczędności przy alternatywnym horyzoncie lub zmiennej liczbie rat, albo (c) porównać scenariusze z innymi wartościami NRR 3M.

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe fakty i liczby zgodne z odpowiedzią oczekiwaną, włącznie z dokumentami, wartościami NRR 3M, oprocentowaniem, kwotami rat i oszczędnościami na odsetkach.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788', 'HS-7794', 'HT-00123', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'UM-7788']; w odpowiedzi ['DC-2201', 'HS-7788', 'HS-7794', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'UM-7788']; pokrycie 0.86

---

## [P3.6] (zestaw 3) ✅ dobra
**Pytanie:** Zidentyfikuj wszystkich klientów objętych wzmożonymi środkami bezpieczeństwa (EDD) i opisz podstawę oraz skutki dla ich klasy ryzyka.

**Oczekiwana:** - **KL-00456 (Marek Nowicki):** EDD z powodu SAR-0034 i SAR-0041 → RR-0012; klasa ryzyka podniesiona z C do **E**; wstrzymanie nowych kredytów (skutek: odmowa DC-2250).
  - **KL-00129 (Bursztyn Handel Sp. z o.o.):** EDD z powodu SAR-0052 (nietypowe wpłaty gotówkowe + transakcje z podmiotem powiązanym); klasa ryzyka podniesiona z C do **D**; nowe zaangażowania warunkowe/wstrzymane.
  - Obaj objęci zakazem tipping-off (POL-AML-01 §7).

**Odpowiedź agenta:** Poniżej lista klientów zidentyfikowanych w grafie i dokumentach jako objęci wzmożonymi środkami bezpieczeństwa (EDD), z podaniem podstawy, skutków oraz brakujących danych. Zapis do grafu został wykonany — potwierdzenia zapisu: learned::988a02c1fecd1e2c (KL-00456), learned::e5fb75312334720f; wskazówki jakościowe: learning::1065b10d7b141765 (KL-00456), learning::a68c0f5093d61c7c (KL-00129).

[
  {
    "client_id": "KL-00456",
    "name": "Marek Andrzej Nowicki",
    "edd_flag": true,
    "edd_basis": [
      "SAR-0034 (structuring)",
      "SAR-0041 (pass-through)",
      "Rekomendacje z raportu ryzyka RR-0012",
      "Wysoki wolumen obrotów gotówkowych nieuzasadniony dokumentacją (KYC-00456)"
    ],
    "impacts": [
      "Podwyższenie klasy ryzyka do E (WYSOKIE)",
      "Wstrzymanie nowych zaangażowań kredytowych do czasu wyjaśnienia",
      "Wzmożony monitoring transakcji/rachunku",
      "Wymóg udokumentowania tytułu i źródła środków",
      "Tipping-off (zakaz ujawniania informacji klientowi)"
    ],
    "sources_in_graph": [
      "KYC-00456",
      "SAR-0034",
      "SAR-0041",
      "RR-0012",
      "POL-AML-01"
    ],
    "complete": false,
    "missing_fields": [
      "dokładna data objęcia EDD (edd_date)",
      "decyzja RM/Compliance potwierdzająca wdrożenie EDD (decision_id)",
      "szczegóły działań wykonanych w ramach EDD (actions_taken) — np. wezwania, kontrole, wyniki wyjaśnień",
      "status relacji/konkluzja (relationship_status) — czy relacja zakończona/utrzymana",
      "ew. notatki z monitoringu po wdrożeniu EDD (monitoring_logs)"
    ]
  },
  {
    "client_id": "KL-00129",
    "name": "Bursztyn Handel Sp. z o.o.",
    "edd_flag": true,
    "edd_basis": [
      "SAR-0052 dotyczące nietypowych wpłat gotówkowych i transakcji z podmiotem powiązanym",
      "Wskazanie w KYC-00129 odnoszące się do nietypowości transakcji"
    ],
    "impacts": [
      "Aktualizacja klasy ryzyka do D (PODWYŻSZONE)",
      "Wstrzymanie nowych zaangażowań kredytowych do czasu wyjaśnienia",
      "Wzmożony monitoring rachunku",
      "Wezwanie klienta o udokumentowanie tytułu i źródła środków",
      "Tipping-off (zakaz ujawniania informacji klientowi)"
    ],
    "sources_in_graph": [
      "KYC-00129",
      "SAR-0052",
      "POL-AML-01",
      "POL-RYZYKO-01"
    ],
    "complete": false,
    "missing_fields": [
      "dokładna data objęcia EDD (edd_date)",
      "decyzja RM/Compliance potwierdzająca wdrożenie EDD (decision_id)",
      "szczegóły działań wykonanych w ramach EDD (actions_taken)",
      "status relacji/konkluzja (relationship_status)",
      "ew. dokumentacja dostarczona przez klienta po wezwaniu (verification_docs)"
    ]
  }
]

Weryfikacja:
- Odpowiedź została zweryfikowana wobec dokumentów źródłowych: KYC-00456, SAR-0034, SAR-0041, RR-0012, KYC-00129, SAR-0052, POL-AML-01, POL-RYZYKO-01 — werdykt: POTWIERDZONA.

Zapis w grafie:
- Zweryfikowane fakty dotyczące obu klientów zostały zapisane do grafu (learned::988a02c1fecd1e2c dla KL-00456; learned::e5fb75312334720f dla KL-00129).
- Dodano jakościowe wskazówki (learning::1065b10d7b141765 dla KL-00456; learning::a68c0f5093d61c7c dla KL-00129), wskazujące brakujące pola do uzupełnienia przy przyszłych analizach.

Jeśli chcesz, mogę:
- Wyciągnąć pełne fragmenty tekstu (cytaty) z dokumentów KYC/SAR (podaj które) i dołączyć je do raportu.
- Wyszukać decyzje RM/Compliance, monitoring logs lub dokumenty weryfikacyjne dla tych klientów (jeśli istnieją) i zaktualizować wpisy w grafie.
- Wygenerować krótkie instrukcje działania dla COMPLIANCE na podstawie brakujących pól.

**Ocena:** dobra — Odpowiedź Agenta w pełni zgodna merytorycznie z oczekiwaną, poprawnie identyfikuje klientów, podstawy EDD, skutki oraz klasy ryzyka, z dodatkowymi szczegółami i potwierdzeniem źródeł.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00129', 'KYC-00456', 'POL-AML-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'SAR-0052']; w odpowiedzi ['KL-00129', 'KL-00456', 'KYC-00129', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'SAR-0052']; pokrycie 1.0

---

## [P3.7] (zestaw 3) 🟡 czesciowa
**Pytanie:** Które tabele oprocentowania i opłat obowiązują dla poszczególnych umów, biorąc pod uwagę daty ich zawarcia i zasady aktualizacji?

**Oczekiwana:** - Umowy zawarte w I kw. 2025 (UM-7788 z 14.02, UM-7789 z 05.03, UM-7790 z 20.03, UM-7791 z 12.03) bazują na TO-2025-Q1 i TOP-2025-Q1.
  - Kredyty stałoprocentowe (gotówkowy UM-7789) i leasing (UM-7790) zachowują stopę z dnia zawarcia.
  - Kredyt hipoteczny UM-7788 (zmienny) jest repricowany od Q2 wg TO-2025-Q2 (nowy harmonogram HS-7794).
  - Wniosek WN-4506 (10.05.2025, Q2) bazuje na TO-2025-Q2 i TOP-2025-Q2.

**Odpowiedź agenta:** [
  {
    "umowa_id": "UM-7788",
    "data_zawarcia": "2025-02-14",
    "tabela_oprocentowania": {
      "id": "TO-2025-Q1",
      "data_wejscia": "2025-01-01",
      "regula_aktualizacji": "Oprocentowanie zmienne = NRR 3M (5,85%) + marża Banku (2,10%). Zmiana wartości NRR 3M w kolejnych kwartałach powoduje zmianę oprocentowania bez konieczności aneksu (REG-KH-02 §3); aktualizacja kwartalna; marża stała.",
      "zrodla": ["DC-2201", "REG-KH-02", "TO-2025-Q1", "HS-7788"]
    },
    "tabela_oplat": {
      "id": "TOP-2025-Q1",
      "data_wejscia": "2025-01-01",
      "regula_aktualizacji": "Opłaty i prowizje zgodnie z REG-KH-02 i TOP-2025-Q1; prowizja przygotowawcza jednorazowa 2,00% przy uruchomieniu.",
      "zrodla": ["DC-2201", "REG-KH-02", "TOP-2025-Q1", "HS-7788"]
    }
  },
  {
    "umowa_id": "UM-7789",
    "data_zawarcia": "2025-03-05",
    "tabela_oprocentowania": {
      "id": "TO-2025-Q1",
      "data_wejscia": "2025-01-01",
      "regula_aktualizacji": "Oprocentowanie stałe (10,90%) zgodnie z TO-2025-Q1 §3 — brak zmian w okresie kredytowania.",
      "zrodla": ["DC-2202", "REG-KG-01", "TO-2025-Q1", "HS-7789"]
    },
    "tabela_oplat": {
      "id": "TOP-2025-Q1",
      "data_wejscia": "2025-01-01",
      "regula_aktualizacji": "Opłaty i prowizje zgodnie z REG-KG-01 i TOP-2025-Q1; wcześniejsza spłata bez opłat (REG-KG-01 §7, TOP-2025-Q1 §2).",
      "zrodla": ["DC-2202", "REG-KG-01", "TOP-2025-Q1", "HS-7789"]
    }
  },
  {
    "umowa_id": "UM-7790",
    "data_zawarcia": "2025-03-20",
    "tabela_oprocentowania": {
      "id": "TO-2025-Q1",
      "data_wejscia": "2025-01-01",
      "regula_aktualizacji": "Stopa leasingowa = NRR 3M (5,85%) + marża 3,20% (łącznie 9,05%). Szczegóły dotyczące zasad stosowania w REG-LE-04; zmiany NRR wpływają na stopę zgodnie z regulaminem.",
      "zrodla": ["DC-2203", "REG-LE-04", "TO-2025-Q1", "HS-7790"]
    },
    "tabela_oplat": {
      "id": null,
      "data_wejscia": null,
      "regula_aktualizacji": "Brak informacji o tabeli opłat w dokumentach powiązanych z UM-7790 — wymagane dodatkowe źródło (np. odwołanie w WN-4503 lub oddzielna tabela opłat).",
      "zrodla": []
    }
  },
  {
    "umowa_id": "UM-7791",
    "data_zawarcia": "2025-03-12",
    "tabela_oprocentowania": {
      "id": "TO-2025-Q1",
      "data_wejscia": "2025-01-01",
      "regula_aktualizacji": "Oprocentowanie transakcji 18,50% r/r, stopa zmienna (nie wyższa niż odsetki maksymalne) zgodnie z regulaminem karty (REG-KK-03) i TO-2025-Q1.",
      "zrodla": ["DC-2204", "REG-KK-03", "TO-2025-Q1"]
    },
    "tabela_oplat": {
      "id": "TOP-2025-Q1",
      "data_wejscia": "2025-01-01",
      "regula_aktualizacji": "Opłata roczna za kartę 120,00 PLN; zniesienie przy rocznym obrocie ≥ 12 000 PLN; opłaty zgodnie z TOP-2025-Q1 §3 i REG-KK-03.",
      "zrodla": ["DC-2204", "REG-KK-03", "TOP-2025-Q1"]
    }
  }
]

Podsumowanie (3 zdania):
Dla UM-7788, UM-7789 i UM-7791 obowiązują tabele TO-2025-Q1 (oprocentowanie) i TOP-2025-Q1 (opłaty) z regułami aktualizacji określonymi w przypisanych regulaminach (REG-KH-02, REG-KG-01, REG-KK-03). UM-7790 ma przypisaną tabelę oprocentowania TO-2025-Q1 (stopa leasingowa oparta na NRR 3M + marża), lecz w dokumentacji powiązanej nie znaleziono odniesienia do tabeli opłat — wymagana jest dodatkowa weryfikacja (np. WN-4503). Wszystkie powyższe dane zostały zweryfikowane w dokumentach (źródła wymienione przy każdej umowie) i zapisane do grafu: dodano/ zaktualizowano fakty dla UM-7788, UM-7789, UM-7790, UM-7791 oraz dołączono krótkie wskazówki jakościowe wskazujące uzupełnione pola i brakującą tabelę opłat dla UM-7790.

**Ocena:** czesciowa — Odpowiedź agenta szczegółowo opisuje tabele TO-2025-Q1 i TOP-2025-Q1 dla umów z Q1 2025 oraz brak tabeli opłat dla UM-7790, ale pomija repricing kredytu hipotecznego UM-7788 od Q2 2025 zgodnie z harmonogramem HS-7794, co jest kluczowym faktem oczekiwanym w odpowiedzi.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KG-01', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'TOP-2025-Q1', 'TOP-2025-Q2', 'UM-7788', 'WN-4506']; w odpowiedzi ['DC-2201', 'DC-2202', 'DC-2203', 'DC-2204', 'HS-7788', 'HS-7789', 'HS-7790', 'REG-KG-01', 'REG-KH-02', 'REG-KK-03', 'REG-LE-04', 'TO-2025-Q1', 'TOP-2025-Q1', 'UM-7788', 'UM-7789', 'UM-7790', 'UM-7791', 'WN-4503']; pokrycie 0.62

---

## [P3.8] (zestaw 3) 🟡 czesciowa
**Pytanie:** Sprawdź spójność danych osobowych i finansowych klientki KL-00124 we wszystkich dokumentach, w których występuje.

**Oczekiwana:** - Katarzyna Maria Lewandowska, PESEL 90111067321 — identyczne w KYC-00124, ZD-4503, WN-4502, UM-7789.
  - Dochód netto 8 200 PLN — spójny w ZD-4503, WN-4502, DC-2202.
  - Kredyt 50 000 PLN / 60 mies / 10,90% / rata 1 084,63 PLN — spójny w WN-4502, DC-2202, UM-7789, HS-7789.
  - Klasa ryzyka A (scoring 92) — KYC-00124, potwierdzona w DC-2202.
  - Brak sprzeczności.

**Odpowiedź agenta:** Podsumowanie (krótkie)
- Dane klientki KL-00124 (Katarzyna Maria Lewandowska) są ogólnie spójne: imię i nazwisko, PESEL (90111067321), adres zamieszkania (ul. Słoneczna 5 m. 2, 80-100 Gdańsk), pracodawca, dochód netto oraz parametry kredytu (kwota, okres, oprocentowanie, prowizja, rata) zgadzają się między dokumentami KYC-00124, WN-4502, DC-2202, UM-7789 i HS-7789. (źródła: KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789)

Zidentyfikowane niezgodności i braki (dokładnie)
- Braki pól (nieobecne w niektórych dokumentach)
  - Adres korespondencyjny: brak wartości we wszystkich dokumentach (KYC ma adres zamieszkania, ale adres korespondencyjny jest pusty). (KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789)
  - PESEL: podany w KYC-00124, WN-4502 i UM-7789, ale brak pola PESEL w DC-2202 i HS-7789 (opisane jako brak w ekstrakcie). (KYC-00124, WN-4502, UM-7789 vs DC-2202, HS-7789)
  - Stanowisko (dokładne): podane tylko w KYC-00124 ("pielęgniarka koordynująca"); we WN-4502 jest pracodawca, ale brak wyszczególnionego stanowiska. (KYC-00124 vs WN-4502)
  - Informacje o paszporcie: brak (dokument tożsamości występuje tylko jako dowód osobisty w KYC-00124). (KYC-00124 i pozostałe)
  - NIP klienta: nie był dostępny w grafie początkowym; KYC-00124 zawiera „NIP TESTOWY” w treści, ale NIP nie był ujednolicony w grafie. (KYC-00124 / graf)
- Spójność finansowa (brak rozbieżności liczbowych)
  - Kwota kredytu (50 000,00 PLN), okres (60 miesięcy), oprocentowanie (stałe 10,90% p.a.), prowizja (4% = 2 000,00 PLN) i rata (1 084,63 PLN) są zgodne we wszystkich dokumentach. (WN-4502, DC-2202, UM-7789, HS-7789)
  - Dochód netto miesięczny 8 200,00 PLN jest konsekwentnie raportowany (KYC-00124, WN-4502, DC-2202).
- Uwaga dotycząca identyfikatorów w dokumentach: numer dowodu osobistego (DEF 246810) występuje w KYC-00124; inne dokumenty nie podają numeru dowodu w ekstrakcie. (KYC-00124 vs WN-4502/DC-2202/UM-7789/HS-7789)

Zalecane kroki / proponowane korekty
1. Uzupełnić / potwierdzić z klientką:
   - adres korespondencyjny (jeśli różny od adresu zamieszkania) i zaktualizować we wszystkich dokumentach i w grafie;
   - czy posiada paszport (jeżeli ma być rejestrowany) oraz ewentualny numer paszportu;
   - NIP (jeśli wymagany do rejestrów) — potwierdzić i ujednolicić w grafie/dokumentach.
2. Dopisać/zweryfikować PESEL w dokumentach decyzyjnych i harmonogramie (DC-2202, HS-7789) albo dodać adnotację o powiązaniu z profilem KYC (aby wszystkie dokumenty miały jednoznaczny identyfikator klienta).
3. Uzupełnić stanowisko pracy w WN-4502 (skrócone/niepełne) na zgodne z KYC-00124 („pielęgniarka koordynująca”) lub potwierdzić aktualny tytuł/zatrudnienie z pracodawcą.
4. Wprowadzić porządkowanie dokumentacji: upewnić się, że numer dowodu/rejestr identyfikatorów jest dostępny w dokumentach decyzyjnych lub że dokumenty powołują się jednoznacznie na profil KYC (np. KL-00124), by uniknąć braków identyfikacyjnych przy audycie.
5. Po potwierdzeniu powyższych danych z klientką zaktualizować dokumenty i graf wiedzy (graf został już uzupełniony o kluczowe fakty — patrz potwierdzenie poniżej).

Potwierdzenie zapisu do grafu (learning)
- Zapisano do grafu zweryfikowane fakty dotyczące KL-00124 oraz dodano jakościową wskazówkę o brakujących polach. Zapis obejmuje m.in.: pełne imię i nazwisko, PESEL, datę urodzenia, adres zamieszkania, numer dowodu osobistego i datę ważności, pracodawcę, stanowisko, dochód netto, DTI oraz parametry kredytu (kwota, okres, oprocentowanie, prowizja, rata) oraz listę powiązanych dokumentów. Dodano wskazówkę: „Graf początkowo brakował pól adres korespondencyjny, NIP klienta i informacji o paszporcie. Przy zapisie zweryfikowano i uzupełniono pola personalne i finansowe. Uwaga: PESEL i numer dowodu występują w różnych dokumentach; przyszłe sprawdzenia powinny potwierdzić obecność PESEL we wszystkich dokumentach decyzyjnych i harmonogramie spłat.” (operacja zapisu wykonana w grafie; źródła: KYC-00124, WN-4502, DC-2202, UM-7789, HS-7789)

Pełna lista źródeł cytowanych
- KYC-00124
- WN-4502
- DC-2202
- UM-7789
- HS-7789

metadata
{
  "facts": {
    "id": "KL-00124",
    "name": "Katarzyna Maria Lewandowska",
    "documents": [
      "KYC-00124",
      "WN-4502",
      "DC-2202",
      "UM-7789",
      "HS-7789"
    ]
  },
  "documents": {
    "KYC-00124": {
      "pełne_imię_i_nazwisko": "Katarzyna Maria Lewandowska",
      "PESEL": "90111067321",
      "data_urodzenia": "10.11.1990",
      "adres_zamieszkania": "ul. Słoneczna 5 m. 2, 80-100 Gdańsk",
      "adres_korespondencyjny": null,
      "typ_i_numer_dokumentu_tożsamości": "dowód osobisty DEF 246810",
      "zatrudnienie": {
        "pracodawca": "Nadmorskie Centrum Medyczne Sp. z o.o.",
        "stanowisko": "pielęgniarka koordynująca"
      },
      "dochód_netto_miesięczny": "8 200,00 PLN",
      "inne_źródła_dochodu": "oszczędności",
      "DTI": null,
      "kwota_kredytu": null,
      "okres": null,
      "oprocentowanie_marża": null,
      "prowizja": null,
      "rata_miesięczna": null,
      "source_text_snippet": "Imię i nazwisko: Katarzyna Maria Lewandowska\n- PESEL (TESTOWY): 90111067321\n- Data i miejsce urodzenia: 10.11.1990, Gdańsk\n- Dokument tożsamości: dowód osobisty DEF 246810 (TESTOWY), ważny do 22.03.2032\n- Adres: ul. Słoneczna 5 m. 2, 80-100 Gdańsk\n- Status zatrudnienia: umowa o pracę na czas nieokreślony\n- Pracodawca: \"Nadmorskie Centrum Medyczne Sp. z o.o.\" (NIP TESTOWY 584-222-33-44)\n- Stanowisko: pielęgniarka koordynująca; zatrudniona od 01.08.2014\n- Średni miesięczny dochód netto (6 mies.): 8 200,00 PLN\n- Deklarowane źródło majątku: wynagrodzenie ze stosunku pracy, oszczędności"
    },
    "WN-4502": {
      "pełne_imię_i_nazwisko": "Katarzyna Maria Lewandowska",
      "PESEL": "90111067321",
      "data_urodzenia": null,
      "adres_zamieszkania": "ul. Słoneczna 5 m. 2, 80-100 Gdańsk",
      "adres_korespondencyjny": null,
      "typ_i_numer_dokumentu_tożsamości": null,
      "zatrudnienie": {
        "pracodawca": "Nadmorskie Centrum Medyczne Sp. z o.o.",
        "stanowisko": null
      },
      "dochód_netto_miesięczny": "8 200,00 PLN",
      "inne_źródła_dochodu": null,
      "DTI": "13,23%",
      "kwota_kredytu": "50 000,00 PLN",
      "okres": "60 miesięcy",
      "oprocentowanie_marża": "stałe 10,90% w skali roku",
      "prowizja": "4,00% = 2 000,00 PLN",
      "rata_miesięczna": "1 084,63 PLN",
      "source_text_snippet": "Imię i nazwisko: Katarzyna Maria Lewandowska\n- PESEL (TESTOWY): 90111067321\n- Adres: ul. Słoneczna 5 m. 2, 80-100 Gdańsk\n- Źródło dochodu: umowa o pracę na czas nieokreślony (Nadmorskie Centrum Medyczne Sp. z o.o.)\n- Średni miesięczny dochód netto: 8 200,00 PLN (potwierdzony ZD-4503)\n- Wskaźnik DTI (indykatywnie): 1 084,63 / 8 200,00 = 13,23%\n- Wnioskowana kwota: 50 000,00 PLN\n- Okres: 60 miesięcy\n- Oprocentowanie: stałe 10,90% w skali roku\n- Rata: 1 084,63 PLN\n- Prowizja przygotowawcza: 4,00% = 2 000,00 PLN"
    },
    "DC-2202": {
      "pełne_imię_i_nazwisko": "Katarzyna Maria Lewandowska",
      "PESEL": null,
      "data_urodzenia": null,
      "adres_zamieszkania": null,
      "adres_korespondencyjny": null,
      "typ_i_numer_dokumentu_tożsamości": null,
      "zatrudnienie": null,
      "dochód_netto_miesięczny": "8 200,00 PLN",
      "inne_źródła_dochodu": null,
      "DTI": "13,23%",
      "kwota_kredytu": "50 000,00 PLN",
      "okres": "60 miesięcy",
      "oprocentowanie_marża": "stałe 10,90%",
      "prowizja": "4,00% = 2 000,00 PLN",
      "rata_miesięczna": "1 084,63 PLN",
      "source_text_snippet": "Klient: KL-00124 (Katarzyna Maria Lewandowska)\nKwota kredytu: 50 000,00 PLN\nOkres: 60 miesięcy\nOprocentowanie: stałe 10,90% w skali roku\nRata annuitetowa: 1 084,63 PLN\nProwizja przygotowawcza: 4,00% = 2 000,00 PLN\nDochód netto (ZD-4503): 8 200,00 PLN/mies.\nWskaźnik DTI: 13,23%"
    },
    "UM-7789": {
      "pełne_imię_i_nazwisko": "Katarzyna Maria Lewandowska",
      "PESEL": "90111067321",
      "data_urodzenia": null,
      "adres_zamieszkania": "ul. Słoneczna 5 m. 2, 80-100 Gdańsk",
      "adres_korespondencyjny": null,
      "typ_i_numer_dokumentu_tożsamości": null,
      "zatrudnienie": null,
      "dochód_netto_miesięczny": null,
      "inne_źródła_dochodu": null,
      "DTI": null,
      "kwota_kredytu": "50 000,00 PLN",
      "okres": "60 miesięcy",
      "oprocentowanie_marża": "stała stopa procentowa 10,90%",
      "prowizja": "4,00% = 2 000,00 PLN",
      "rata_miesięczna": "1 084,63 PLN",
      "source_text_snippet": "Katarzyną Marią Lewandowską, PESEL (TESTOWY) 90111067321, zam. ul. Słoneczna 5 m. 2, 80-100 Gdańsk\nKredyt gotówkowy „Nordvik Gotówka\" w kwocie 50 000,00 PLN\nOkres kredytowania: 60 miesięcy\nOprocentowanie stałe 10,90%\nProwizja przygotowawcza: 4,00% kwoty kredytu = 2 000,00 PLN\nKredyt spłacany jest w 60 równych ratach po 1 084,63 PLN"
    },
    "HS-7789": {
      "pełne_imię_i_nazwisko": "Katarzyna Maria Lewandowska",
      "PESEL": null,
      "data_urodzenia": null,
      "adres_zamieszkania": null,
      "adres_korespondencyjny": null,
      "typ_i_numer_dokumentu_tożsamości": null,
      "zatrudnienie": null,
      "dochód_netto_miesięczny": null,
      "inne_źródła_dochodu": null,
      "DTI": null,
      "kwota_kredytu": "50 000,00 PLN",
      "okres": "60 miesięcy",
      "oprocentowanie_marża": "stałe 10,90%",
      "prowizja": null,
      "rata_miesięczna": "1 084,63 PLN",
      "source_text_snippet": "HARMONOGRAM SPŁAT\nKwota kredytu: 50 000,00 PLN\nOprocentowanie nominalne: 10,90% w skali roku, STAŁE\nLiczba rat: 60\nWysokość raty: 1 084,63 PLN\nPierwsza rata: 10.04.2025 | Ostatnia rata: 10.03.2030"
    }
  },
  "inconsistencies": [
    "Adres korespondencyjny nie występuje we wszystkich dokumentach.",
    "PESEL jest podany w dokumentach KYC-00124, WN-4502, UM-7789; brak pola PESEL w DC-2202 i HS-7789.",
    "Stanowisko pracy jest podane tylko w dokumencie KYC-00124 (pielęgniarka koordynująca); WN-4502 podaje pracodawcę, ale brak stanowiska.",
    "W dokumentach brak informacji o paszporcie (występuje tylko dowód osobisty w KYC-00124).",
    "Parametry kredytu (kwota 50 000 PLN, okres 60 miesięcy, oprocentowanie 10,90%, prowizja 4%, rata 1 084,63 PLN) są spójne między dokumentami."
  ]
}

**Ocena:** czesciowa — Odpowiedź agenta uwzględnia wszystkie kluczowe dane osobowe i finansowe oraz wskazuje na szczegóły spójności i braki, ale w porównaniu z oczekiwaną nie zawiera informacji o klasie ryzyka A (scoring 92), która jest wymagana; pozostałe dane są zgodne i szczegółowo omówione.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2202', 'HS-7789', 'KYC-00124', 'UM-7789', 'WN-4502', 'ZD-4503']; w odpowiedzi ['DC-2202', 'HS-7789', 'KL-00124', 'KYC-00124', 'UM-7789', 'WN-4502', 'ZD-4503']; pokrycie 1.0

---

## [P3.9] (zestaw 3) ✅ dobra
**Pytanie:** Na podstawie polityk banku opisz, jak przetwarzany jest wniosek klienta wysokiego ryzyka AML oraz jakie ograniczenia praw wynikają z zasad ochrony danych.

**Oczekiwana:** - Ocena ryzyka i klasyfikacja: POL-RYZYKO-01 (klasy A–E, override jakościowy) w powiązaniu z POL-AML-01 (CDD/EDD, monitoring, SAR).
  - Dla klienta wysokiego ryzyka: wzmożone środki (EDD), ustalenie źródła środków, możliwe wstrzymanie nowych usług i blokady; zakaz tipping-off.
  - RODO (POL-DANE-01): przetwarzanie na podstawie obowiązku prawnego (AML) — prawo do usunięcia i sprzeciwu NIE ma zastosowania do dokumentacji AML; okresy przechowywania wynikają z przepisów AML.
  - Przykład zastosowania: KL-00456/DC-2250 oraz KL-00129/SAR-0052.

**Odpowiedź agenta:** Oto zwięzłe podsumowanie — wyłącznie na podstawie polityk i dokumentów banku.

Jak przetwarzany jest wniosek klienta sklasyfikowanego jako wysokie ryzyko AML
- Identyfikacja i weryfikacja (CDD): w pierwszym kroku przeprowadzana jest pełna identyfikacja klienta i beneficjenta rzeczywistego. (źródło: POL-AML-01 §2; KYC-00456 §1)  
- Wzmożone środki należytej staranności (EDD): dla klientów wysokiego ryzyka stosuje się EDD — m.in. dodatkowe ustalenie źródła majątku i środków, akceptacja na poziomie MLRO, bieżące monitorowanie transakcji i częstsze przeglądy (co najmniej co 6 miesięcy). (źródło: POL-AML-01 §2)  
- Zgłaszanie podejrzeń (SAR): przy podejrzeniu prania pieniędzy pracownik przekazuje sygnał do zespołu AML; analityk przygotowuje zgłoszenie SAR, MLRO akceptuje i kieruje zgłoszenie do KJAF. Może być też sporządzony raport ryzyka (RR). (źródło: POL-AML-01 §6; KYC-00456 §4)  
- Zakaz ujawniania (tipping-off) i środki zabezpieczające: bank nie ujawnia klientowi faktu zgłoszenia SAR; może zablokować transakcje lub wstrzymać świadczenie nowych usług (w tym udzielanie produktów kredytowych) do wyjaśnienia. (źródło: POL-AML-01 §7; KYC-00456 §5)  
- Skutki operacyjne: przy wysokim ryzyku możliwe wstrzymanie udzielania nowych produktów kredytowych i okresowy przegląd klasy ryzyka. (źródło: KYC-00456 §5)

Ograniczenia praw wynikające z zasad ochrony danych (RODO / polityka ochrony danych)
- Zasada minimalizacji: bank przetwarza tylko dane niezbędne do celów oceny ryzyka i realizacji obowiązków prawnych (np. dokumentacja AML, KYC). (źródło: POL-DANE-01 §4)  
- Podstawy prawne: przetwarzanie w zakresie AML opiera się głównie na obowiązku prawnym oraz — tam, gdzie stosowne — na wykonaniu umowy; zgoda nie zastępuje obowiązku przetwarzania dla celów AML. (źródło: POL-DANE-01 §3)  
- Prawa osób: klient ma prawa dostępu, sprostowania, ograniczenia przetwarzania, przenoszenia danych i wniesienia sprzeciwu, ale prawo do usunięcia i sprzeciwu nie ma zastosowania do danych przetwarzanych na podstawie obowiązku prawnego (np. dokumentacja AML). Wnioski rozpatrywane są w terminie miesiąca. (źródło: POL-DANE-01 §6)  
- Okresy przechowywania: dokumentacja AML/KYC przechowywana jest przez okres wymagany przepisami AML; dokumentacja kredytowa przez okres trwania umowy i wymagany okres po jej zakończeniu. (źródło: POL-DANE-01 §5)  
- Naruszenia danych: naruszenia rejestrowane i — jeśli wymagane — zgłaszane organowi nadzorczemu w ciągu 72 godzin; w razie wysokiego ryzyka informuje się też osoby, których dane dotyczą. (źródło: POL-DANE-01 §8)

Wnioski praktyczne
- Procedura łączy wzmożone kontrole AML z ograniczeniami RODO: bank może zbierać i przechowywać dodatkowe dane niezbędne do EDD (na podstawie obowiązku prawnego), lecz musi stosować zasadę minimalizacji, respektować prawa osób tam, gdzie to możliwe, i przestrzegać zasad raportowania naruszeń oraz zakazu tipping-off. (źródła: POL-AML-01, POL-DANE-01, KYC-00456)

Weryfikacja i zapis do grafu wiedzy
- Weryfikator ocenił powyższe stwierdzenia jako: POTWIERDZONA (źródła: POL-AML-01, POL-DANE-01, KYC-00456).  
- Fakt i wskazówka jakościowa zostały zapisane do grafu wiedzy. ID zapisanego faktu: learned::ac9ddfd9dc201e9d; ID zapisu wskazówki jakościowej: learning::ac9ddfd9dc201e9d. Dzięki temu następnym razem informacje będą dostępne bez ponownego czytania dokumentów.

Źródła (dokumenty użyte): POL-AML-01, POL-DANE-01 (POL-RODO), KYC-00456.  

Jeżeli chcesz, mogę rozwinąć procedurę krok po kroku z cytatami paragrafów lub przygotować checklistę wymogów dokumentacyjnych dla EDD.

**Ocena:** dobra — Odpowiedź agenta w pełni pokrywa kluczowe elementy oczekiwane, tj. proces EDD, zakaz tipping-off, podstawy prawne RODO oraz ograniczenia prawne dotyczące danych AML, zgodnie z politykami banku.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250', 'KYC-00129', 'KYC-00456', 'POL-AML-01', 'POL-DANE-01', 'POL-RYZYKO-01', 'SAR-0052']; w odpowiedzi ['KYC-00456', 'POL-AML-01', 'POL-DANE-01']; pokrycie 0.43

---

## [P3.10] (zestaw 3) ✅ dobra
**Pytanie:** Zbuduj pełną mapę powiązań węzła TO-2025-Q1 — wskaż wszystkie dokumenty, które z niego korzystają, i wyjaśnij, dlaczego jest to „wspólny węzeł" istotny dla spójności zbioru.

**Oczekiwana:** - TO-2025-Q1 jest przywoływana przez: REG-KH-02, REG-KG-01, REG-LE-04, REG-KK-03 (regulaminy), DC-2201, DC-2202, DC-2203, DC-2204 (decyzje), UM-7788, UM-7789, UM-7790, UM-7791 (umowy), HS-7788, HS-7789, HS-7790 (harmonogramy), WN-4502, WN-4503, WN-4504 (wnioski).
  - Ustala wspólną wartość NRR 3M (5,85%) i marże/stopy dla wielu produktów — jej zmiana (TO-2025-Q2) propaguje się na oprocentowanie umów o stopie zmiennej (repricing hipoteki, HS-7794).
  - Dlatego jest kluczowa dla spójności liczbowej całego zbioru.

**Odpowiedź agenta:** Oto pełna mapa powiązań węzła TO-2025-Q1 w formacie JSON (źródło: pamięć grafowa — wpisy grafu wskazane poniżej).

JSON:
{
  "direct_refs": [
    {"doc_id": "REG-KH-02", "relation_type": "references", "note": "Regulamin kredytu hipotecznego odnosi się do tabeli w zakresie oprocentowania."},
    {"doc_id": "UM-7791", "relation_type": "uses table", "note": "Umowa korzysta z oprocentowania według tej tabeli."},
    {"doc_id": "UM-7790", "relation_type": "uses table", "note": "Umowa korzysta z oprocentowania według tej tabeli."},
    {"doc_id": "UM-7789", "relation_type": "uses table", "note": "Umowa korzysta z oprocentowania według tej tabeli."},
    {"doc_id": "UM-7788", "relation_type": "uses table", "note": "Umowa stosuje wartość NRR 3M i marżę z tabeli."},
    {"doc_id": "HS-7790", "relation_type": "has schedule", "note": "Harmonogram spłat oparty na oprocentowaniu z tabeli."},
    {"doc_id": "REG-KG-01", "relation_type": "references", "note": "Regulamin kredytu gotówkowego odnosi się do oprocentowania z tabeli."},
    {"doc_id": "DC-2204", "relation_type": "uses table", "note": "Decyzja kredytowa określa cenę kredytu według tej tabeli."},
    {"doc_id": "DC-2203", "relation_type": "uses table", "note": "Decyzja kredytowa wykorzystuje oprocentowanie z tabeli."},
    {"doc_id": "WN-4504", "relation_type": "uses rate table", "note": "Wniosek kredytowy odnosi się do tej tabeli."},
    {"doc_id": "DC-2202", "relation_type": "uses table", "note": "Decyzja kredytowa oparta na oprocentowaniu z tabeli."},
    {"doc_id": "POL-RYZYKO-01", "relation_type": "applies policy", "note": "Polityka ryzyka stosuje dane z tabeli oprocentowania."},
    {"doc_id": "POL-AML-01", "relation_type": "applies policy", "note": "Polityka AML odnosi się do tabeli jako części procedur."},
    {"doc_id": "Wniosek kredytowy", "relation_type": "uses rate table", "note": "Wniosek wykorzystuje dane z tabeli oprocentowania."},
    {"doc_id": "REG-LE-04", "relation_type": "references", "note": "Regulamin leasingu odnosi się do tabeli."},
    {"doc_id": "Nordvik Karta", "relation_type": "references", "note": "Karta kredytowa zdefiniowana zgodnie z oprocentowaniem tabeli."},
    {"doc_id": "Marek Nowicki", "relation_type": "governed by", "note": "Decyzje klienta powiązane z warunkami tabeli."},
    {"doc_id": "HS-7788", "relation_type": "has schedule", "note": "Harmonogram spłat kredytu zależny od oprocentowania w tabeli."},
    {"doc_id": "TO-2025-Q1", "relation_type": "self-reference", "note": "Jest to tabela oprocentowania I kwartału 2025."}
  ],
  "indirect_refs": [
    {"doc_id": "POL-RYZYKO-01", "via": ["REG-KH-02"], "relation_chain": ["REG-KH-02 -> TO-2025-Q1"], "note": "Polityka ryzyka odnosi się do regulaminu, który wprost korzysta z tabeli."},
    {"doc_id": "REG-KH-02", "via": ["TO-2025-Q1"], "relation_chain": ["REG-KH-02 -> TO-2025-Q1"], "note": "Regulamin bezpośrednio odnosi się do tabeli."},
    {"doc_id": "POL-AML-01", "via": ["REG-KH-02"], "relation_chain": ["POL-AML-01 -> REG-KH-02 -> TO-2025-Q1"], "note": "Polityka AML odwołuje się do regulaminu korzystającego z tabeli."},
    {"doc_id": "REG-KG-01", "via": ["TO-2025-Q1"], "relation_chain": ["REG-KG-01 -> TO-2025-Q1"], "note": "Regulamin kredytu gotówkowego powołuje się na tabelę oprocentowania."},
    {"doc_id": "TOP-2025-Q1", "via": ["TO-2025-Q1"], "relation_chain": ["TOP-2025-Q1 -> TO-2025-Q1"], "note": "Inny dokument tabeli korzysta ze wspólnych danych."},
    {"doc_id": "TO-2025-Q2", "via": ["TO-2025-Q1"], "relation_chain": ["TO-2025-Q2 -> TO-2025-Q1"], "note": "Następna tabela kwartałowa odwołuje się do poprzedniej."},
    {"doc_id": "Wniosek kredytowy", "via": ["TO-2025-Q1"], "relation_chain": ["Wniosek kredytowy -> TO-2025-Q1"], "note": "Wniosek korzysta z ustaleń tabeli."},
    {"doc_id": "DC-2202", "via": ["TO-2025-Q1"], "relation_chain": ["DC-2202 -> TO-2025-Q1"], "note": "Decyzja kredytowa w oparciu o tabelę."},
    {"doc_id": "WN-4504", "via": ["TO-2025-Q1"], "relation_chain": ["WN-4504 -> TO-2025-Q1"], "note": "Wniosek kredytowy powiązany z tabelą."},
    {"doc_id": "REG-LE-04", "via": ["TO-2025-Q1"], "relation_chain": ["REG-LE-04 -> TO-2025-Q1"], "note": "Regulamin leasingu stosuje dane z tabeli."},
    {"doc_id": "Nordvik Karta", "via": ["TO-2025-Q1"], "relation_chain": ["Nordvik Karta -> TO-2025-Q1"], "note": "Specyfikacja karty kredytowej oparta na tabeli."},
    {"doc_id": "Marek Nowicki", "via": ["TO-2025-Q1"], "relation_chain": ["Marek Nowicki -> TO-2025-Q1"], "note": "Decyzje klienta uzależnione od danych tabeli."},
    {"doc_id": "HS-7788", "via": ["TO-2025-Q1"], "relation_chain": ["HS-7788 -> TO-2025-Q1"], "note": "Harmonogram spłat związany z tabelą."},
    {"doc_id": "Harmonogram spłat kredytu (plan amortyzacji)", "via": ["HS-7788"], "relation_chain": ["Harmonogram spłat kredytu -> HS-7788 -> TO-2025-Q1"], "note": "Plan amortyzacji pośrednio zależny od tabeli."},
    {"doc_id": "wniosek klienta", "via": ["Wniosek kredytowy"], "relation_chain": ["wniosek klienta -> Wniosek kredytowy -> TO-2025-Q1"], "note": "Wniosek klienta pośrednio korzysta z tabeli."},
    {"doc_id": "Umowa kredytu hipotecznego „Nordvik Dom\"", "via": ["UM-7788"], "relation_chain": ["Umowa kredytu hipotecznego -> UM-7788 -> TO-2025-Q1"], "note": "Umowa kredytu hipotecznego korzysta z wartości tabeli."},
    {"doc_id": "Umowa kredytu gotówkowego „Nordvik Gotówka\"", "via": ["UM-7790"], "relation_chain": ["Umowa kredytu gotówkowego -> UM-7790 -> TO-2025-Q1"], "note": "Umowa kredytu gotówkowego odwołuje się do tabeli."}
  ],
  "relations_summary": [
    "references",
    "uses table",
    "governed by",
    "applies policy",
    "has schedule",
    "uses rate table"
  ],
  "explanation": "TO-2025-Q1 jest wspólnym węzłem, ponieważ łączy różne dokumenty i polityki, zapewniając spójność w odniesieniu do tabel oprocentowania oraz regulacji, co jest kluczowe dla zarządzania ryzykiem kredytowym i polityką kredytową."
}

Krótka synteza (2–4 zdania):
TO-2025-Q1 (tabela oprocentowania I kw. 2025) jest bezpośrednio wykorzystywana przez regulaminy (REG-KH-02, REG-KG-01), umowy (UM-7788, UM-7789, UM-7790, UM-7791), decyzje kredytowe (DC-2202, DC-2203, DC-2204), harmonogramy (HS-7788, HS-7790) oraz polityki (POL-RYZYKO-01, POL-AML-01) — zob. direct_refs i indirect_refs powyżej (źródła: REG-KH-02, UM-7788, UM-7790, UM-7789, UM-7791, HS-7790, HS-7788, DC-2202, DC-2203, DC-2204, POL-RYZYKO-01, POL-AML-01, WN-4504, REG-LE-04, Nordvik Karta). Dzięki temu węzeł zapewnia spójność oprocentowania i odniesień regulacyjnych w całym zbiorze dokumentów, co jest istotne dla jednolitego stosowania warunków kredytowych i zarządzania ryzykiem (źródło: TO-2025-Q1 i powiązania w grafie).

Weryfikacja i zapis do grafu:
- Weryfikator ocenił przygotowaną mapę jako POTWIERDZONĄ (wszystkie wymienione powiązania są obecne w pamięci grafowej).
- Ponieważ wszystkie potrzebne fakty były już dostępne w grafie (nie wykonywałem wyszukiwania w dokumentach), nie zapisywałem nowych faktów do grafu. Jeśli życzysz sobie, mogę wykonać dodatkowy zapis/udokumentowanie lub dodać jakościowe wskazówki (graph_add_learning) dla TO-2025-Q1 — daj znać.

Jeżeli chcesz, mogę teraz:
- wygenerować diagram grafu (lista powiązań w formacie DOT) albo
- przejść do odczytania treści poszczególnych dokumentów (np. UM-7788, DC-2202, HS-7788) aby rozwinąć szczegóły liczbowo-prawne powiązań.

**Ocena:** dobra — Odpowiedź agenta prawidłowo wskazuje wszystkie kluczowe dokumenty korzystające z węzła TO-2025-Q1 i wyjaśnia jego rolę jako wspólnego, spójnego węzła zgodnie z oczekiwaniami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['HS-7794', 'TO-2025-Q1', 'TO-2025-Q2']; w odpowiedzi ['DC-2202', 'DC-2203', 'DC-2204', 'HS-7788', 'HS-7790', 'POL-AML-01', 'POL-RYZYKO-01', 'REG-KG-01', 'REG-KH-02', 'REG-LE-04', 'TO-2025-Q1', 'TO-2025-Q2', 'TOP-2025-Q1', 'UM-7788', 'UM-7789', 'UM-7790', 'UM-7791', 'WN-4504']; pokrycie 0.67

---
