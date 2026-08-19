# Wyniki ewaluacji (self_learning_agents)

## [P1.1] (zestaw 1) ✅ dobra
**Pytanie:** Jaki jest numer PESEL (testowy) klientki Anny Katarzyny Kowalskiej?

**Oczekiwana:** 85072812345 (oznaczony jako testowy).

**Odpowiedź agenta:** Numer PESEL (testowy) klientki Anny Katarzyny Kowalskiej to 85072812345 (źródło: KYC-00123, WN-4501, UM-7788, ZD-4501). Zapisano ten zweryfikowany fakt w grafie wiedzy (ID: learned::be13f9f0aa32ad33).

**Ocena:** dobra — Odpowiedź agenta zawiera poprawny numer PESEL testowy klientki Anny Katarzyny Kowalskiej zgodny z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00123']; w odpowiedzi ['KYC-00123', 'UM-7788', 'WN-4501', 'ZD-4501']; pokrycie 1.0

---

## [P1.2] (zestaw 1) ✅ dobra
**Pytanie:** Na jaką kwotę opiewa kredyt hipoteczny w umowie UM-7788?

**Oczekiwana:** 480 000,00 PLN.

**Odpowiedź agenta:** Kwota kredytu hipotecznego w umowie UM-7788 wynosi 480 000,00 PLN (słownie: czterysta osiemdziesiąt tysięcy złotych). Źródła: UM-7788, DC-2201, HS-7788.

**Ocena:** dobra — Odpowiedź agenta podaje dokładnie tę samą kwotę kredytu hipotecznego co odpowiedź oczekiwana, włącznie z formatem i wartością liczbową.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['UM-7788']; w odpowiedzi ['DC-2201', 'HS-7788', 'UM-7788']; pokrycie 1.0

---

## [P1.3] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi miesięczna rata w harmonogramie HS-7788?

**Oczekiwana:** 3 688,83 PLN (300 rat annuitetowych).

**Odpowiedź agenta:** Miesięczna rata wynosi 3 688,83 PLN (źródło: HS-7788, UM-7788, DC-2201, TO-2025-Q1).

**Ocena:** dobra — Odpowiedź agenta podaje poprawną miesięczną ratę 3 688,83 PLN zgodnie z odpowiedzią oczekiwaną, a dodatkowe źródła nie wpływają na merytoryczną zgodność.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788']; w odpowiedzi ['DC-2201', 'HS-7788', 'TO-2025-Q1', 'UM-7788']; pokrycie 1.0

---

## [P1.4] (zestaw 1) ✅ dobra
**Pytanie:** Jaki jest maksymalny standardowy wskaźnik LTV według polityki ryzyka kredytowego?

**Oczekiwana:** 80% (standard; LTV 80–90% dopuszczalne wyjątkowo z dodatkowym zabezpieczeniem/ubezpieczeniem i wyższą marżą).

**Odpowiedź agenta:** Maksymalny standardowy wskaźnik LTV według polityki ryzyka kredytowego wynosi 80% (źródło: POL-RYZYKO-01).

**Ocena:** dobra — Odpowiedź agenta podaje poprawny maksymalny standardowy wskaźnik LTV jako 80%, zgodnie z oczekiwaniami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['POL-RYZYKO-01']; w odpowiedzi ['POL-RYZYKO-01']; pokrycie 1.0

---

## [P1.5] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi wartość wskaźnika NRR 3M w tabeli oprocentowania na I kwartał 2025?

**Oczekiwana:** 5,85% w skali roku.

**Odpowiedź agenta:** Wartość wskaźnika NRR 3M w tabeli oprocentowania na I kwartał 2025 wynosi 5,85% rocznie (źródło: TO-2025-Q1).

**Ocena:** dobra — Odpowiedź agenta poprawnie podaje wartość wskaźnika NRR 3M jako 5,85% rocznie, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['TO-2025-Q1']; w odpowiedzi ['TO-2025-Q1']; pokrycie 1.0

---

## [P1.6] (zestaw 1) ✅ dobra
**Pytanie:** Jaka jest stawka prowizji przygotowawczej dla kredytu hipotecznego w tabeli opłat Q1 2025?

**Oczekiwana:** 2,00% kwoty kredytu.

**Odpowiedź agenta:** Stawka prowizji przygotowawczej w tabeli opłat na I kwartał 2025 wynosi 2,00% kwoty kredytu. Dla przykładu, przy kredycie 480 000,00 PLN prowizja to 9 600,00 PLN (źródła: TOP-2025-Q1, UM-7788).

**Ocena:** dobra — Odpowiedź agenta poprawnie podaje stawkę prowizji przygotowawczej jako 2,00% kwoty kredytu zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['TOP-2025-Q1']; w odpowiedzi ['TOP-2025-Q1', 'UM-7788']; pokrycie 1.0

---

## [P1.7] (zestaw 1) ✅ dobra
**Pytanie:** Kto jest beneficjentem rzeczywistym (UBO) spółki „Bursztyn Handel Sp. z o.o."?

**Oczekiwana:** Andrzej Lewiński — 100% udziałów.

**Odpowiedź agenta:** Beneficjentem rzeczywistym (UBO) spółki "Bursztyn Handel Sp. z o.o." jest Andrzej Lewiński — posiada 100% udziałów (źródła: KYC-00129, SAR-0052).

Informacja została zweryfikowana i zapisana do grafu wiedzy (ID zapisanego faktu: learned::d2fa54c058a892ae). Uwaga: dokument UM-7788 nie zawierał tej informacji i nie był użyty jako potwierdzenie.

**Ocena:** dobra — Odpowiedź agenta zgadza się w kluczowych faktach i liczbach z odpowiedzią oczekiwaną, podając to samo nazwisko i procent udziałów.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j) → odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['KYC-00129']; w odpowiedzi ['KYC-00129', 'SAR-0052', 'UM-7788']; pokrycie 1.0

---

## [P1.8] (zestaw 1) ✅ dobra
**Pytanie:** Jakie rozstrzygnięcie zapadło w decyzji kredytowej DC-2250?

**Oczekiwana:** Decyzja NEGATYWNA (odmowa udzielenia kredytu gotówkowego).

**Odpowiedź agenta:** Decyzja kredytowa DC-2250 była negatywna (odmowa), podjęta 12 maja 2025 r. przez Komitet Kredytowy; przyczyny: klasa ryzyka E oraz brak możliwości ustalenia źródła środków; decyzja dotyczy wniosku WN-4508 klienta Marka Andrzeja Nowickiego. (źródło: graf DC-2250; zapis w grafie: learned::6e57d067ae74d073)

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe informacje oczekiwane w odpowiedzi, tzn. że decyzja była negatywna (odmowa udzielenia kredytu), a dodatkowo rozszerza ją o szczegóły, nie odbiegając od merytorycznej zgodności.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250']; w odpowiedzi ['DC-2250', 'WN-4508']; pokrycie 1.0

---

## [P1.9] (zestaw 1) ✅ dobra
**Pytanie:** Jaki limit kredytowy przyznano na karcie kredytowej w decyzji DC-2204?

**Oczekiwana:** 15 000,00 PLN.

**Odpowiedź agenta:** Limit kredytowy przyznany na karcie kredytowej w decyzji DC-2204 wynosi 15 000,00 PLN (źródło: DC-2204; potwierdzenie: UM-7791, WN-4504).

**Ocena:** dobra — Odpowiedź agenta podaje zgodną ze wzorem wartość limitu kredytowego 15 000,00 PLN, co odpowiada oczekiwanej odpowiedzi.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j) → odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['DC-2204']; w odpowiedzi ['DC-2204', 'UM-7791', 'WN-4504']; pokrycie 1.0

---

## [P1.10] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi minimalna kwota do zapłaty w cyklu rozliczeniowym karty kredytowej „Nordvik Karta"?

**Oczekiwana:** 5% zadłużenia, nie mniej niż 50 PLN.

**Odpowiedź agenta:** Minimalna kwota do zapłaty w cyklu rozliczeniowym karty kredytowej „Nordvik Karta” wynosi 5% salda zadłużenia, nie mniej niż 50 PLN (źródło: REG-KK-03).

**Ocena:** dobra — Odpowiedź agenta poprawnie podaje minimalną kwotę do zapłaty jako 5% zadłużenia, nie mniej niż 50 PLN, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KK-03']; w odpowiedzi ['REG-KK-03']; pokrycie 1.0

---

## [P1.11] (zestaw 1) ✅ dobra
**Pytanie:** Jak długi jest okres bezodsetkowy (grace period) karty kredytowej dla transakcji bezgotówkowych?

**Oczekiwana:** Do 56 dni (pod warunkiem spłaty całości zadłużenia w terminie).

**Odpowiedź agenta:** Okres bezodsetkowy (grace period) dla transakcji bezgotówkowych wynosi 56 dni. Warunek: spłata całego zadłużenia w terminie; niektóre transakcje mogą być wyłączone z tego okresu — sprawdź szczegóły w regulaminie karty (źródło: Regulamin_karty_kredytowej, Umowa_karta_kredytowa, T&C_karty_kredytowe, REG-KK-03).

Fakt został zapisany w grafie wiedzy (id: learned::93b811da6dd429fa).

**Ocena:** dobra — Odpowiedź agenta poprawnie podaje długość okresu bezodsetkowego do 56 dni oraz warunek całkowitej spłaty zadłużenia, dodatkowo wskazując na możliwe wyjątki, co nie przeczy informacji oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KK-03']; w odpowiedzi ['REG-KK-03']; pokrycie 1.0

---

## [P1.12] (zestaw 1) ✅ dobra
**Pytanie:** Do jakiego podmiotu i jakiej jurysdykcji trafiały przelewy zagraniczne z rachunku w historii transakcji HT-00456?

**Oczekiwana:** Do „Vantia Global Trade LLC" w Republice Vantia (jurysdykcja wysokiego ryzyka); łącznie ok. 464 950,00 PLN.

**Odpowiedź agenta:** Przelewy zagraniczne z rachunku HT-00456 były kierowane do podmiotu Vantia Global Trade LLC, z siedzibą w Republice Vantia; były to przelewy SWIFT dokonane w okresie 01.02.2025–31.03.2025 (źródło: HT-00456).

Zrealizowano pięć transferów o łącznej wartości 464 950,00 PLN; poszczególne kwoty: 88 000,00 PLN; 95 000,00 PLN; 92 500,00 PLN; 99 000,00 PLN; 90 450,00 PLN. Transfery następowały w ciągu 24–72 godzin od serii wpłat gotówkowych (źródło: HT-00456). Zweryfikowany fakt zapisano w grafie wiedzy (ID zapisu: learned::399d2799607adc62).

**Ocena:** dobra — Odpowiedź agenta jest zgodna z oczekiwaną co do podmiotu, jurysdykcji oraz łącznej kwoty przelewów zagranicznych z rachunku HT-00456.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HT-00456']; w odpowiedzi ['HT-00456']; pokrycie 1.0

---

## [P1.13] (zestaw 1) ✅ dobra
**Pytanie:** Jaki średni miesięczny dochód netto potwierdza zaświadczenie ZD-4503?

**Oczekiwana:** 8 200,00 PLN (klientka Katarzyna Lewandowska, Nadmorskie Centrum Medyczne Sp. z o.o.).

**Odpowiedź agenta:** Zaświadczenie ZD-4503 potwierdza średni miesięczny dochód netto w wysokości 8 200,00 PLN (źródła: ZD-4503; potwierdzenie w grafie: DC-2202).  
Weryfikacja: POTWIERDZONA — okres odniesienia: sierpień 2024–styczeń 2025; typ umowy: umowa o pracę na czas nieokreślony.  
Fakt zapisano w grafie wiedzy (ID wpisu: learned::ebb1b083a4b32342).

**Ocena:** dobra — Odpowiedź agenta zawiera poprawną kwotę 8 200,00 PLN i odnosi się do zaświadczenia ZD-4503, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['ZD-4503']; w odpowiedzi ['DC-2202', 'ZD-4503']; pokrycie 1.0

---

## [P1.14] (zestaw 1) 🟡 czesciowa
**Pytanie:** Ile wynosi wartość wykupu przedmiotu leasingu we wniosku WN-4503?

**Oczekiwana:** 1% wartości = 1 800,00 PLN netto.

**Odpowiedź agenta:** Wartość wykupu przedmiotu leasingu we wniosku WN-4503 wynosi 1 800,00 PLN (źródło: WN-4503).

--  
Zapisano potwierdzony fakt do grafu pamięci.

**Ocena:** czesciowa — Agent podał prawidłową kwotę 1 800,00 PLN, lecz nie uwzględnił, że wartość wykupu wynosi 1% wartości oraz nie wskazał, że jest to kwota netto.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['WN-4503']; w odpowiedzi ['WN-4503']; pokrycie 1.0

---

## [P1.15] (zestaw 1) ✅ dobra
**Pytanie:** Jaki wewnętrzny próg alertu dla wpłat gotówkowych określa polityka AML?

**Oczekiwana:** 15 000 PLN (rozbijanie wpłat poniżej progu = structuring).

**Odpowiedź agenta:** Wewnętrzny próg alertu dla wpłat gotówkowych określony w polityce AML wynosi 15 000 PLN (źródła: POL-AML-01, SAR-0034, HT-00456).

Zapis w grafie: learned::21a80bc32c3a7ea3 (wskazówka learning::21a80bc32c3a7ea3: „Rozbijanie wpłat tuż poniżej progu 15 000 PLN jest typologią podejrzaną — monitorować powiązane wpłaty”).

**Ocena:** dobra — Odpowiedź agenta poprawnie wskazuje próg 15 000 PLN oraz wspomina o rozbijaniu wpłat jako podejrzanej aktywności zgodnie z polityką AML.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['POL-AML-01']; w odpowiedzi ['HT-00456', 'POL-AML-01', 'SAR-0034']; pokrycie 1.0

---

## [P1.16] (zestaw 1) ✅ dobra
**Pytanie:** Jaka jest klasa ryzyka kredytowego klienta KL-00124 (Katarzyna Lewandowska)?

**Oczekiwana:** Klasa A (scoring 92/100), ryzyko niskie.

**Odpowiedź agenta:** Klasa ryzyka kredytowego klientki KL-00124 (Katarzyna Maria Lewandowska): A.

Szczegóły:
- Scoring: 92/100 (KYC-00124; potwierdzone w DC-2202).
- Wskaźnik DTI: 13,23% (DC-2202).
- Uzasadnienie: dokument DC-2202 i KYC-00124 przypisują klientce klasę A i scoring 92; zgodnie z POL-RYZYKO-01 klasa A odpowiada scoringowi 90–100, a DTI 13,23% mieści się w dopuszczalnym limicie dla klas A–C (≤45%).

Źródła i przeczytane dokumenty: DC-2202, KYC-00124, POL-RYZYKO-01 (dodatkowo sprawdzono: WN-4502, ZD-4503, UM-7789, TO-2025-Q1).

Fakt zapisano w grafie wiedzy: learned::743cced28bf7b344.

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe informacje z oczekiwanej odpowiedzi, tj. klasę A i scoring 92/100 wskazujące niskie ryzyko.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['KYC-00124']; w odpowiedzi ['DC-2202', 'KL-00124', 'KYC-00124', 'POL-RYZYKO-01', 'TO-2025-Q1', 'UM-7789', 'WN-4502', 'ZD-4503']; pokrycie 1.0

---

## [P1.17] (zestaw 1) ✅ dobra
**Pytanie:** Ile wynosi opłata roczna za kartę kredytową i kiedy jest znoszona?

**Oczekiwana:** 120,00 PLN; znoszona przy rocznym obrocie bezgotówkowym ≥ 12 000 PLN.

**Odpowiedź agenta:** Opłata roczna za kartę kredytową wynosi 120,00 PLN i jest znoszona, jeśli roczny obrót bezgotówkowy wynosi co najmniej 12 000,00 PLN (źródła: WN-4504, DC-2204).

**Ocena:** dobra — Odpowiedź agenta w pełni odpowiada wymaganiom merytorycznym podanym w odpowiedzi oczekiwanej, podając poprawną kwotę opłaty oraz warunek jej zniesienia.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['REG-KK-03', 'TOP-2025-Q1']; w odpowiedzi ['DC-2204', 'WN-4504']; pokrycie 0.0

---

## [P1.18] (zestaw 1) ❌ zla
**Pytanie:** Jakie oprocentowanie limitu w rachunku firmowym przyznano w decyzji DC-2205?

**Oczekiwana:** 12,50% w skali roku (zmienne); limit 50 000 PLN, prowizja za limit 1% rocznie = 500 PLN.

**Odpowiedź agenta:** Oprocentowanie limitu w rachunku firmowym przyznane w decyzji DC-2205 wynosi 1,00% kwoty limitu (źródło: DC-2205).

**Ocena:** zla — Odpowiedź agenta podaje prowizję 1% jako oprocentowanie limitu, co jest niezgodne z oczekiwaną informacją o oprocentowaniu 12,50% w skali roku; kluczowe dane o oprocentowaniu i limitach są niepoprawne lub pomieszane.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2205']; w odpowiedzi ['DC-2205']; pokrycie 1.0

---

## [P2.1] (zestaw 2) ✅ dobra
**Pytanie:** Czy rata w harmonogramie HS-7788 jest zgodna z kwotą kredytu i oprocentowaniem z umowy oraz tabeli oprocentowania?

**Oczekiwana:** Tak. Umowa UM-7788: 480 000 PLN na 300 mies.; oprocentowanie 7,95% = NRR 3M 5,85% + marża 2,10% (TO-2025-Q1); rata annuitetowa 3 688,83 PLN — zgodna z HS-7788.

**Odpowiedź agenta:** Krótka odpowiedź: Tak — rata w harmonogramie HS-7788 jest zgodna z kwotą kredytu i oprocentowaniem z umowy oraz tabeli oprocentowania.

Krótka kalkulacja (weryfikowalna):
- P = 480 000,00 PLN (kwota kredytu) (źródło: HS-7788, UM-7788)
- Oprocentowanie nominalne roczne = 7,95% = NRR 3M 5,85% + marża 2,10% (źródło: UM-7788, TO-2025-Q1)
- Stopa miesięczna i = 0,0795 / 12 ≈ 0,006625
- Liczba rat n = 300 (miesięcznych) (źródło: HS-7788, UM-7788)
- Wzór annuitetowy: R = P * (i*(1+i)^n) / ((1+i)^n - 1)
- Obliczenie: R ≈ 480000 * (0,006625*(1+0,006625)^300)/((1+0,006625)^300 -1) ≈ 3 688,83 PLN

Wniosek: Obliczona rata ≈ 3 688,83 PLN zgadza się z ratą podaną w harmonogramie HS-7788 i zapisaną w umowie. (źródło: HS-7788, UM-7788, TO-2025-Q1)

Zapis w pamięci grafowej: fakt i wskazówka jakościowa zostały zapisane w grafie dla HS-7788 (ID faktu i wskazówki dostępne w grafie).

**Ocena:** dobra — Odpowiedź agenta poprawnie potwierdza zgodność raty z kwotą i oprocentowaniem z umowy oraz tabeli, precyzyjnie podając wszystkie kluczowe dane i przeprowadzając prawidłową kalkulację raty annuitetowej zgodną z oczekiwaniami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788', 'TO-2025-Q1', 'UM-7788']; w odpowiedzi ['HS-7788', 'TO-2025-Q1', 'UM-7788']; pokrycie 1.0

---

## [P2.2] (zestaw 2) ✅ dobra
**Pytanie:** Na podstawie której decyzji zawarto umowę UM-7788 i jaki wskaźnik DTI przyjęto w tej decyzji?

**Oczekiwana:** Decyzja DC-2201 (pozytywna); DTI = 36,52% (rata 3 688,83 / dochód netto 10 100).

**Odpowiedź agenta:** Umowa UM-7788 została zawarta na podstawie decyzji DC-2201. W decyzji DC-2201 przyjęto wskaźnik DTI na poziomie 36,52% (źródła: DC-2201, UM-7788; dodatkowo ZD-4501 potwierdza dochód użyty w obliczeniu DTI).

**Ocena:** dobra — Odpowiedź agenta poprawnie wskazuje decyzję DC-2201 i właściwy wskaźnik DTI 36,52%, zgodnie z oczekiwaną odpowiedzią.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['DC-2201', 'UM-7788']; w odpowiedzi ['DC-2201', 'UM-7788', 'ZD-4501']; pokrycie 1.0

---

## [P2.3] (zestaw 2) ✅ dobra
**Pytanie:** Dlaczego wniosek WN-4508 został odrzucony, skoro klient miał wystarczającą zdolność kredytową?

**Oczekiwana:** Decyzja DC-2250 była negatywna nie z powodu zdolności (DTI 16,20% — akceptowalne), lecz z powodu klasy ryzyka E nadanej w raporcie RR-0012 na podstawie zgłoszeń SAR-0034 i SAR-0041 oraz braku możliwości ustalenia źródła środków (AML).

**Odpowiedź agenta:** W skrócie: Wniosek WN-4508 został odrzucony nie z powodu braku zdolności kredytowej, ale z powodu nadania klientowi (KL-00456) klasy ryzyka E oraz niemożności ustalenia źródeł pochodzenia środków. Klasa E oznacza wysokie ryzyko AML/reputacyjne i zgodnie z politykami banku (POL-AML-01, POL-RYZYKO-01) skutkuje odmową udzielenia nowych produktów kredytowych mimo pozytywnej oceny zdolności. Innymi słowy: wynik finansowy (zdolność) jest tylko jednym z kryteriów; ryzyko zgodności i reputacji może przeważyć i uniemożliwić przyznanie kredytu.

Źródła: DC-2250, RR-0012, KYC-00456 (oraz powiązane polityki: POL-AML-01, POL-RYZYKO-01).

**Ocena:** dobra — Odpowiedź agenta w pełni pokrywa kluczowe fakty oczekiwane: negatywna decyzja nie ze względu na zdolność kredytową (DTI 16,20%), lecz przez klasę ryzyka E oraz brak możliwości ustalenia źródła środków, uwzględniając odpowiednie raporty i polityki.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250', 'RR-0012', 'WN-4508']; w odpowiedzi ['DC-2250', 'KL-00456', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012', 'WN-4508']; pokrycie 1.0

---

## [P2.4] (zestaw 2) 🟡 czesciowa
**Pytanie:** Który regulamin i którą politykę powołuje decyzja kredytowa DC-2201?

**Oczekiwana:** Regulamin kredytu hipotecznego REG-KH-02 oraz Politykę ryzyka kredytowego POL-RYZYKO-01 (dodatkowo tabelę TO-2025-Q1 dla parametrów cenowych).

**Odpowiedź agenta:** Decyzja kredytowa DC-2201 powołuje:
- Regulamin Produktu Kredytowego KH (REG-KH-02) (źródło: DC-2201),
- Politykę ryzyka kredytowego (POL-RYZYKO-01) (źródło: DC-2201).

**Ocena:** czesciowa — Agent poprawnie wskazał regulamin i politykę, ale pominął tabelę TO-2025-Q1 wymienioną w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'POL-RYZYKO-01', 'REG-KH-02']; w odpowiedzi ['DC-2201', 'POL-RYZYKO-01', 'REG-KH-02']; pokrycie 1.0

---

## [P2.5] (zestaw 2) ✅ dobra
**Pytanie:** Jakie warunki postawiła decyzja warunkowa DC-2203 i w jaki sposób zostały spełnione w umowie leasingu UM-7790?

**Oczekiwana:** DC-2203 wymagała albo podwyższenia opłaty wstępnej do 30%, albo dodatkowego zabezpieczenia. W UM-7790 klient wybrał drugi wariant: ustanowił poręczenie cywilne Tomasza Górskiego oraz weksel własny in blanco, zachowując opłatę wstępną 20% (36 000 PLN); dostarczył też zaświadczenia ZUS/US.

**Odpowiedź agenta:** Oto krótkie podsumowanie — jakie warunki postawiła decyzja warunkowa DC-2203 i jak każdy z nich został spełniony w umowie leasingu UM-7790.

Warunki z DC-2203 (termin spełnienia: do 02.04.2025)
1. Podwyższenie opłaty wstępnej z 20% do 30% LUB ustanowienie dodatkowego zabezpieczenia: poręczenie cywilne Tomasza Górskiego oraz weksel własny in blanco ze deklaracją wekslową. (źródło: DC-2203)  
2. Dostarczenie zaświadczeń o niezaleganiu wobec ZUS i US (nie starszych niż 30 dni). (źródło: DC-2203)  
3. Zawarcie umowy ubezpieczenia przedmiotu (AC/OC) z cesją na Finansującego przed wydaniem pojazdu. (źródło: DC-2203)

Sposób spełnienia warunków w UM-7790
1. Zabezpieczenia zamiast podwyższenia opłaty: w UM-7790 wybrano wariant z dodatkowymi zabezpieczeniami — poręczenie cywilne Tomasza Górskiego oraz weksel własny in blanco z deklaracją wekslową; opłata wstępna pozostała 20% (36 000,00 PLN). (źródła: UM-7790 §1, §6; por. DC-2203)  
2. Zaświadczenia o niezaleganiu: dokumenty potwierdzające brak zaległości wobec ZUS i US zostały dostarczone (data w aktach: 2025-03-14) i zostały odnotowane w UM-7790. (źródła: UM-7790 §1; DC-2203)  
3. Ubezpieczenie z cesją: UM-7790 przewiduje obowiązek zawarcia i utrzymania ubezpieczenia AC/OC z cesją na Finansującego przed wydaniem przedmiotu leasingu. (źródła: UM-7790 §5; DC-2203)

Werdykt weryfikatora: POTWIERDZONA — wszystkie wymienione warunki DC-2203 mają bezpośrednie potwierdzenie w UM-7790 (weryfikacja: DC-2203, UM-7790; dodatkowo HS-7790 jako załącznik/harmonogram).  

Dodatkowo: zapisano zweryfikowany fakt w grafie wiedzy (id: learned::f6a571021221d564) oraz dodano wskazówkę jakościową do encji DC-2203 (id: learning::92c4ccf705cfe70c).  

Źródła: DC-2203; UM-7790 (§1, §5, §6); HS-7790 (załącznik).

**Ocena:** dobra — Odpowiedź agenta w pełni pokrywa kluczowe warunki z DC-2203 oraz sposób ich spełnienia w UM-7790, zgodnie z oczekiwaniami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2203', 'UM-7790']; w odpowiedzi ['DC-2203', 'HS-7790', 'UM-7790']; pokrycie 1.0

---

## [P2.6] (zestaw 2) ✅ dobra
**Pytanie:** Jak zmieniła się rata kredytu hipotecznego UM-7788 po zmianie wskaźnika i co było przyczyną?

**Oczekiwana:** Rata spadła z 3 688,83 PLN na 3 531,88 PLN, ponieważ NRR 3M spadł z 5,85% (TO-2025-Q1) do 5,35% (TO-2025-Q2), co przy marży 2,10% dało oprocentowanie 7,45% zamiast 7,95%. Nowy harmonogram to HS-7794 (obowiązuje od raty nr 2).

**Odpowiedź agenta:** Rata kredytu hipotecznego UM-7788 zmniejszyła się z 3 688,83 PLN do 3 531,88 PLN (spadek o 156,95 PLN). Przyczyną była obniżka oprocentowania z 7,95% do 7,45% w wyniku spadku wskaźnika NRR 3M (repricing) — zmiana zaczęła obowiązywać od raty nr 2 zgodnie z HS-7794. (źródło: UM-7788, HS-7794, TO-2025-Q1)

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe fakty i liczby zgodne z odpowiedzią oczekiwaną, w tym zmianę raty, wskaźnika, oprocentowania oraz numer nowego harmonogramu.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7794', 'REG-KH-02', 'TO-2025-Q2', 'UM-7788']; w odpowiedzi ['HS-7794', 'TO-2025-Q1', 'UM-7788']; pokrycie 0.5

---

## [P2.7] (zestaw 2) ✅ dobra
**Pytanie:** Którego klienta i na podstawie jakich zgłoszeń przeklasyfikowano do najwyższej klasy ryzyka (E)?

**Oczekiwana:** Klienta KL-00456 (Marek Nowicki, JDG „MN Trade"). Podstawa: zgłoszenia SAR-0034 (structuring) i SAR-0041 (pass-through) → raport ryzyka RR-0012 → aktualizacja karty KYC-00456 do klasy E.

**Odpowiedź agenta:** Krótko i rzeczowo:

- Klient: KL-00456 — Marek Andrzej Nowicki (brak sprzeczności w dokumentach) (źródło: KYC-00456).  
- Data przeklasyfikowania: 2025-04-16 (źródło: KYC-00456).  
- Podstawa przeklasyfikowania (główne zgłoszenia/raporty):
  - SAR-0034 — zgłoszenie podejrzanej transakcji (structuring) (źródło: SAR-0034, powołane w KYC-00456).  
  - SAR-0041 — zgłoszenie podejrzanej transakcji (pass‑through) (źródło: SAR-0041, powołane w KYC-00456).  
  - RR-0012 — raport ryzyka rekomendujący przeklasyfikowanie i wdrożenie EDD (źródło: RR-0012, powołane w KYC-00456).  
  - Aktualizacja KYC: KYC-00456 — wpis o nadpisaniu klasy na E i wdrożeniu środków (EDD) oraz wstrzymaniu nowych produktów (źródło: KYC-00456).
- Dokumenty powiązane (wymienione w KYC-00456): HT-00456 (historia transakcji), WN-4508 (wniosek), DC-2250 (decyzja kredytowa), POL-AML-01 (polityka AML), POL-RYZYKO-01 (polityka ryzyka — definicja klasy E i zasady rewizji) (źródła: KYC-00456, POL-RYZYKO-01).
- Skutki/uwagi: wdrożono wzmożone środki kontroli (EDD) i wstrzymano oferowanie nowych produktów kredytowych do wyjaśnienia (źródło: KYC-00456, RR-0012, POL-RYZYKO-01).
- Weryfikacja i zapis: informacja została zweryfikowana w dokumentach i zapisana do grafu wiedzy (fact_id: learned::1a29ef1b5ba4fba3; learning_id: learning::1a29ef1b5ba4fba3).  

Główne źródła: KYC-00456, SAR-0034, SAR-0041, RR-0012, POL-RYZYKO-01.

**Ocena:** dobra — Odpowiedź agenta zawiera kompletną i zgodną merytorycznie informację o kliencie KL-00456, podstawie przeklasyfikowania na klasę E (zgłoszenia SAR-0034 i SAR-0041 oraz raport RR-0012) oraz aktualizacji KYC-00456, zgodnie z oczekiwaniami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00456', 'RR-0012', 'SAR-0034', 'SAR-0041']; w odpowiedzi ['DC-2250', 'HT-00456', 'KL-00456', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'WN-4508']; pokrycie 1.0

---

## [P2.8] (zestaw 2) 🟡 czesciowa
**Pytanie:** Jaka jest relacja między zaświadczeniem ZD-4501, wnioskiem WN-4501 i decyzją DC-2201?

**Oczekiwana:** ZD-4501 jest załącznikiem nr 1 do wniosku WN-4501 i potwierdza dochód netto 10 100 PLN; ten dochód został użyty w decyzji DC-2201 do wyliczenia wskaźnika DTI (36,52%).

**Odpowiedź agenta:** Krótko i rzeczowo:

- ZD-4501 to zaświadczenie o dochodach klienta i jest załącznikiem nr 1 do wniosku kredytowego WN-4501 (źródło: ZD-4501, WN-4501).  
- Dochód z ZD-4501 został użyty w wyliczeniu wskaźnika DTI, który był brany pod uwagę w decyzji kredytowej DC-2201 (źródło: ZD-4501, DC-2201).  
- DC-2201 to decyzja rozstrzygająca o wniosku WN-4501 — decyzja wykorzystuje informacje zawarte we WN-4501 i w załącznikach (w tym ZD-4501) (źródło: WN-4501, DC-2201).

Dodatkowo: powyższe trzy relacje zostały zapisane w grafie wiedzy jako zweryfikowane fakty (id: learned::15f914b6f7ae3ddf, learned::c7253e2c6880d583, learned::b59fff8653f26485).

**Ocena:** czesciowa — Odpowiedź agenta prawidłowo opisuje relacje między dokumentami i ich funkcje, jednak nie podaje konkretnej kwoty dochodu netto (10 100 PLN) ani wartości wskaźnika DTI (36,52%), które są kluczowe w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'WN-4501', 'ZD-4501']; w odpowiedzi ['DC-2201', 'WN-4501', 'ZD-4501']; pokrycie 1.0

---

## [P2.9] (zestaw 2) ✅ dobra
**Pytanie:** Ile wynosi rata leasingowa netto i brutto oraz z czego wynika różnica?

**Oczekiwana:** Rata netto 3 586,87 PLN, brutto 4 411,85 PLN; różnica to VAT 23% doliczany do raty leasingu.

**Odpowiedź agenta:** 1) Rata leasingowa:
- Netto: 3 586,87 PLN (źródło: UM-7790).
- Brutto: 4 411,85 PLN (źródło: UM-7790).

2) Skąd wynika różnica:
- Różnica wynika z naliczonego podatku VAT 23% (regulacja i praktyka naliczania VAT w umowach leasingowych) (źródło: REG-LE-04; potwierdzenie kwot w UM-7790).

3) Dodatkowe informacje istotne dla rat:
- Termin płatności: do 25. dnia każdego miesiąca (źródło: UM-7790).
- Liczba rat w harmonogramie: 48 rat; suma opłat leasingowych netto: 172 169,56 PLN (źródło: HS-7790).

Użyte źródła: [UM-7790, HS-7790, REG-LE-04].

(Uwaga: odpowiedź oparta wyłącznie na dokumentach powiązanych z tą transakcją.)

**Ocena:** dobra — Odpowiedź agenta zawiera prawidłowe kwoty rat netto i brutto oraz wyjaśnia, że różnica wynika z podatku VAT 23%, co jest zgodne z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['HS-7790', 'UM-7790']; w odpowiedzi ['HS-7790', 'REG-LE-04', 'UM-7790']; pokrycie 1.0

---

## [P2.10] (zestaw 2) ✅ dobra
**Pytanie:** Czy profil ryzyka klienta KL-00124 jest zgodny z pozytywnym rozstrzygnięciem decyzji DC-2202?

**Oczekiwana:** Tak. KYC-00124: klasa A, scoring 92/100, brak zobowiązań; DC-2202: DTI 13,23%, spełnione kryteria POL-RYZYKO-01 — decyzja pozytywna spójna z profilem.

**Odpowiedź agenta:** Podsumowanie kluczowych danych: klasa ryzyka A (najniższe ryzyko); scoring kredytowy 92/100; DTI 13,23%. Decyzja DC-2202 z 25.02.2025 jest pozytywna i odwołuje się do zgodności z polityką ryzyka oraz pozytywnej oceny profilu klienta.

Konkluzja: TAK — profil ryzyka klienta KL-00124 jest zgodny z pozytywnym rozstrzygnięciem decyzji DC-2202, ponieważ KYC wskazuje klasę A i scoring 92/100, a DC-2202 potwierdza DTI 13,23% i pozytywny wynik decyzji (spełnienie kryteriów polityki ryzyka).

Źródła: KYC-00124, DC-2202.

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe dane i poprawnie potwierdza zgodność profilu ryzyka klienta z pozytywną decyzją DC-2202, zgodnie z odpowiedzią oczekiwaną.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach

**Źródła:** oczekiwane ['DC-2202', 'KYC-00124', 'POL-RYZYKO-01']; w odpowiedzi ['DC-2202', 'KL-00124', 'KYC-00124']; pokrycie 0.67

---

## [P2.11] (zestaw 2) ✅ dobra
**Pytanie:** Kto jest kredytobiorcą w umowie UM-7789, jaki jest cel kredytu i na jaki rachunek następuje spłata?

**Oczekiwana:** Katarzyna Maria Lewandowska (KL-00124); cel: remont mieszkania; rachunek spłaty (testowy) PL33 9999 1000 0000 0077 8900 0002.

**Odpowiedź agenta:** Kredytobiorcą w umowie UM-7789 jest Katarzyna Maria Lewandowska (źródło: UM-7789, §1).  
Celem kredytu jest remont mieszkania (źródło: UM-7789, §1).  
Spłata kredytu następuje na rachunek PL33 9999 1000 0000 0077 8900 0002 (źródło: UM-7789, §2 ust. 3).

Fakty zostały zapisane w grafie wiedzy powiązanym z dokumentem UM-7789 (źródło zapisu: UM-7789).

**Ocena:** dobra — Odpowiedź agenta jest w pełni zgodna merytorycznie z oczekiwaną, podając poprawnego kredytobiorcę, cel kredytu oraz numer rachunku spłaty.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00124', 'UM-7789']; w odpowiedzi ['UM-7789']; pokrycie 0.5

---

## [P2.12] (zestaw 2) 🟡 czesciowa
**Pytanie:** Które oprocentowanie zastosowano w kredycie gotówkowym z wniosku WN-4506 i skąd ono pochodzi?

**Oczekiwana:** 10,90% stałe (przedział 20 001–60 000 PLN) — z tabeli TO-2025-Q2 (wniosek złożony w Q2 2025). Rata 980,74 PLN dla 30 000 PLN na 36 mies.

**Odpowiedź agenta:** Odpowiedź: W kredycie gotówkowym z wniosku WN-4506 zastosowano oprocentowanie stałe 10,90% w skali roku. Pochodzi ono z tabeli oprocentowania TO-2025-Q2 (§3) dla przedziału kwot 20 001–60 000 PLN (wnioskowana kwota 30 000 PLN). (Źródła: WN-4506, TO-2025-Q2; por. także TO-2025-Q1)

Cytowane fragmenty / fakty:
- {fact: "wniosek: oprocentowanie stałe 10,90% w skali roku (kwota 20 001–60 000 PLN)", source_doc_id: "WN-4506"}
- {fact: "tabela TO-2025-Q2 §3: oprocentowanie stałe 10,90% dla 20 001–60 000 PLN", source_doc_id: "TO-2025-Q2"}
- {fact: "TO-2025-Q1 potwierdza ten przedział/stopę w poprzednim kwartale (dla porównania)", source_doc_id: "TO-2025-Q1"}

Dodatkowo: Zweryfikowałem informację i zapisałem zweryfikowany fakt oraz krótką wskazówkę jakościową do grafu wiedzy (encja WN-4506) — wniosek odnosi się do TO-2025-Q2, nie do TO-2025-Q1. Jeśli chcesz, mogę przesłać pełne cytaty z dokumentów.

**Ocena:** czesciowa — Agent poprawnie wskazał oprocentowanie 10,90% stałe oraz jego pochodzenie z tabeli TO-2025-Q2 dla przedziału 20 001–60 000 PLN, jednak pominął informację o racie 980,74 PLN dla 30 000 PLN na 36 miesięcy, która była wymagana w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → odpytuję pamięć GRAFOWĄ (Neo4j) → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['DC-2206', 'TO-2025-Q2', 'WN-4506']; w odpowiedzi ['TO-2025-Q1', 'TO-2025-Q2', 'WN-4506']; pokrycie 0.67

---

## [P2.13] (zestaw 2) ✅ dobra
**Pytanie:** Czym różnią się dwie historie transakcji (HT-00123 i HT-00456) i jakie skutki compliance z nich wynikły?

**Oczekiwana:** HT-00123 (KL-00123) to normalny profil detaliczny (wynagrodzenie, spłata raty, wydatki bytowe) — brak przesłanek AML. HT-00456 (KL-00456) wykazuje structuring i transfery pass-through do jurysdykcji wysokiego ryzyka — skutkuje zgłoszeniami SAR-0034/0041.

**Odpowiedź agenta:** Krótko: HT-00123 to typowa historia rachunku detalicznego z regularnymi wpływami wynagrodzenia i spłatami kredytu hipotecznego, bez przesłanek AML. HT-00456 to historia rachunku firmowego JDG „MN Trade” z masowymi wpłatami gotówkowymi rozbijanymi poniżej progów i szybkimi transferami zagranicznymi do jurysdykcji wysokiego ryzyka — stwierdzono istotne podejrzenia AML i podjęto działania compliance.

1) Kluczowe różnice
   - Profil klienta: klient indywidualny Anna K. Kowalska (rachunek osobisty) vs. JDG „MN Trade” (rachunek firmowy) (źródła: HT-00123; HT-00456).
   - Typ i skala transakcji: regularne wpływy wynagrodzeń i zwykłe wydatki vs. setki tysięcy PLN w gotówce (liczne wpłaty 9 400–9 900 PLN) oraz szybkie przelewy zagraniczne (źródło: HT-00456).
   - Ryzyko AML: HT-00123 — brak przesłanek do zgłoszenia; HT-00456 — structuring (rozbijanie wpłat) i funkcja „pass-through” wobec odbiorcy w jurysdykcji wysokiego ryzyka (źródła: HT-00123; HT-00456).

2) Skutki compliance wynikające z każdej historii
   - HT-00123: brak zgłoszeń SAR i brak rekomendacji działań AML (źródło: HT-00123).
   - HT-00456: złożono zgłoszenia podejrzanych transakcji SAR-0034 (structuring) i SAR-0041 (transfery pass-through); przeprowadzono przegląd ryzyka RR-0012, który uznał klienta za wysokie ryzyko i zawiera rekomendacje dalszych działań (źródła: SAR-0034; SAR-0041; RR-0012).

3) Konsekwencje dla obsługi klienta / produktów
   - HT-00123: kontynuacja standardowej obsługi, bez EDD ani ograniczeń produktowych (źródło: HT-00123).
   - HT-00456: wdrożenie wzmożonych środków bezpieczeństwa (EDD), wezwania do dokumentacji źródeł środków, rekomendacje wstrzymania nowych produktów kredytowych i możliwość ograniczenia/zakńczenia relacji; działania te wpływają też na rozpatrywanie wniosków kredytowych (DC-2250 powiązane z oceną RR-0012) (źródła: RR-0012; KYC-00456; DC-2250).

Wykorzystane źródła: HT-00123; HT-00456; SAR-0034; SAR-0041; RR-0012; KYC-00456; DC-2250; POL-AML-01.

Jeśli chcesz, mogę przygotować krótkie streszczenie dla zespołu AML (np. do SAR/monitoringu) albo wyciągnięte wykresy czasowe przepływów z HT-00456.

**Ocena:** dobra — Odpowiedź agenta dokładnie odwzorowuje kluczowe fakty i liczby z oczekiwanej odpowiedzi, uwzględniając różnice w profilach, typach transakcji oraz skutki compliance, w tym konkretne zgłoszenia SAR oraz działania EDD.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HT-00123', 'HT-00456', 'SAR-0034', 'SAR-0041']; w odpowiedzi ['DC-2250', 'HT-00123', 'HT-00456', 'KYC-00456', 'POL-AML-01', 'RR-0012', 'SAR-0034', 'SAR-0041']; pokrycie 1.0

---

## [P2.14] (zestaw 2) ✅ dobra
**Pytanie:** Jakie zabezpieczenia ustanowiono dla kredytu hipotecznego UM-7788 i jak mają się one do wymogów polityki ryzyka?

**Oczekiwana:** Hipoteka umowna do 720 000 PLN (150% kwoty), cesja z polisy ubezpieczenia nieruchomości, ubezpieczenie pomostowe do wpisu hipoteki — zgodne z wymogiem zabezpieczenia hipotecznego z POL-RYZYKO-01 §4.

**Odpowiedź agenta:** Podsumowanie ustanowionych zabezpieczeń i ich zgodności z POL-RYZYKO-01:

1) Ustanowione zabezpieczenia
- Hipoteka umowna na nieruchomości (KW GD1Y/00099999/9) do kwoty 720 000,00 PLN (tj. 150% kwoty kredytu). (źródło: UM-7788 §6; DC-2201 V.2; WN-4501)  
- Cesja praw z polisy ubezpieczenia nieruchomości (ubezpieczenie od ognia i zdarzeń losowych) na rzecz Banku. (źródło: UM-7788 §6; DC-2201 V.3; REG-KH-02 §7)  
- Ubezpieczenie pomostowe obowiązujące do dnia prawomocnego wpisu hipoteki (do czasu wpisu obowiązek ubezpieczenia pomostowego). (źródło: UM-7788 §6; DC-2201 V.4; REG-KH-02 §7)  
- Brak poręczycieli w dostępnych dokumentach (UM-7788, DC-2201, WN-4501). (źródło: UM-7788; DC-2201)

2) Zgodność z polityką ryzyka POL-RYZYKO-01
- Zabezpieczenia wymienione powyżej odpowiadają wymaganiom POL-RYZYKO-01 (w szczególności obowiązek hipoteki wpisanej/wniosku o wpis oraz cesji z polisy, zastępcze ubezpieczenie pomostowe do wpisu). Decyzja kredytowa DC-2201 i regulamin REG-KH-02 potwierdzają stosowanie kryteriów polityki ryzyka i warunki uruchomienia zgodne z POL-RYZYKO-01. (źródło: DC-2201; REG-KH-02; POL-RYZYKO-01)
- Na podstawie dokumentów: ocena zgodności = zgodne / spełnione warunki proceduralne. (źródło: DC-2201; UM-7788; REG-KH-02)

3) Braki / istotne zastrzeżenia (co nie jest potwierdzone w dostępnych dokumentach)
- Brak w dokumentach numeru polisy ubezpieczeniowej oraz szczegółowej sumy ubezpieczenia (numer polisy/kwota nie znalezione). (źródło: UM-7788; WN-4501; DC-2201)  
- Brak bezpośredniego potwierdzenia prawomocnego wpisu hipoteki w księdze wieczystej (widoczne są wymogi i wniosek o wpis, nie ma w materiałach finalnego wypisu/poświadczenia wpisu). (źródło: UM-7788; DC-2201; WN-4501)

4) Rekomendowane dalsze kroki (opcjonalne)
- Pozyskanie kopii polisy ubezpieczeniowej z numerem polisy i sumą ubezpieczenia oraz dokumentu potwierdzającego cesję praw.  
- Uzyskanie wypisu/odpisu z księgi wieczystej potwierdzającego prawomocny wpis hipoteki (ew. akt notarialny ustanowienia hipoteki / potwierdzenie z sądu/EGiB).

Zapis w grafie: powyższe zweryfikowane fakty dotyczące UM-7788 zostały dopisane do grafu wiedzy (hipoteka 720 000 PLN, cesja polisy, ubezpieczenie pomostowe, brak poręczycieli oraz brak potwierdzeń numeru polisy i wpisu KW). (źródła użyte: UM-7788, DC-2201, WN-4501, REG-KH-02, POL-RYZYKO-01)

Jeśli chcesz, mogę teraz poszukać dokumentów potwierdzających numer polisy i/lub wypis z księgi wieczystej.

**Ocena:** dobra — Odpowiedź agenta poprawnie identyfikuje wszystkie kluczowe zabezpieczenia (hipoteka do 720 000 PLN/150% kwoty, cesja polisy, ubezpieczenie pomostowe) i potwierdza ich zgodność z polityką ryzyka, dodatkowo uwzględniając braki formalne, które nie były wymagane w odpowiedzi oczekiwanej.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['POL-RYZYKO-01', 'UM-7788']; w odpowiedzi ['DC-2201', 'POL-RYZYKO-01', 'REG-KH-02', 'UM-7788', 'WN-4501']; pokrycie 1.0

---

## [P3.1] (zestaw 3) 🟡 czesciowa
**Pytanie:** Prześledź kompletny łańcuch kredytu hipotecznego Anny Kowalskiej — od profilu klienta do harmonogramu — i zweryfikuj spójność kluczowych liczb.

**Oczekiwana:** - Łańcuch: KYC-00123 → WN-4501 → (załącznik ZD-4501) → DC-2201 → UM-7788 → HS-7788.
  - Klient klasy B (scoring 78), dochód netto 10 100 PLN (ZD-4501).
  - Kredyt 480 000 PLN, nieruchomość warta 600 000 PLN → **LTV 80%**; wkład własny 120 000 PLN.
  - Oprocentowanie 7,95% (NRR 3M 5,85% + marża 2,10%, TO-2025-Q1); **rata 3 688,83 PLN** na 300 mies.
  - **DTI 36,52%** (3 688,83 / 10 100) < limit 45% (POL-RYZYKO-01) → decyzja pozytywna.
  - Prowizja 9 600 PLN (2%, TOP-2025-Q1), RRSO 8,50%, suma odsetek 626 649,94 PLN.
  - Liczby są spójne w całym łańcuchu.

**Odpowiedź agenta:** Wykonałem analizę całego łańcucha dokumentów (KYC → WN → DC → UM → HS) dotyczącego kredytu Anny Kowalskiej i zweryfikowałem spójność kluczowych liczb. Poniżej podsumowanie (źródła w nawiasach).

1) Powiązane dokumenty (łańcuch)
- ZD-4501 — zaświadczenie o zatrudnieniu i dochodzie (KYC) (ZD-4501).  
- WN-4501 — wniosek kredytowy (WN) (WN-4501).  
- DC-2201 — decyzja kredytowa (DC) (DC-2201).  
- UM-7788 — umowa kredytu (UM) (UM-7788).  
- HS-7794 — harmonogram spłat po aktualizacji (HS) (HS-7794).  
- REG-KH-02 — regulamin produktu (REG-KH-02).

2) Kluczowe liczby i daty (wartość — źródło)
- Kwota kredytu: 480 000,00 PLN (WN-4501; DC-2201; UM-7788).  
- Okres kredytowania: 300 miesięcy (25 lat) (WN-4501; DC-2201; UM-7788; HS-7794).  
- Oprocentowanie przed aktualizacją: 7,95% = NRR 3M 5,85% + marża 2,10% (DC-2201; UM-7788).  
- Rata przed aktualizacją: 3 688,83 PLN, rata annuitetowa (DC-2201; UM-7788).  
- Prowizja przygotowawcza: 2,00% = 9 600,00 PLN (DC-2201; UM-7788; REG-KH-02).  
- Data uruchomienia kredytu: 20.02.2025 (UM-7788).  
- Pierwsza rata wg umowy (UM): 15.03.2025 (UM-7788).  
- Zmiana wskaźnika w harmonogramie (HS): nowe NRR 3M = 5,35% → nowe oprocentowanie 7,45% (HS-7794).  
- Nowa rata od raty nr 2 (po aktualizacji): 3 531,88 PLN (HS-7794).  
- Pierwsza rata wg zaktualizowanego HS: 15.04.2025; ostatnia rata: 15.02.2050; liczba pozostałych rat po aktualizacji: 299 (HS-7794).

3) Ocena spójności
- Zgodności między WN, DC i UM: parametry podstawowe (kwota 480 000 PLN, okres 300 mies., oprocentowanie jako suma NRR+marża 7,95%, rata 3 688,83 PLN, prowizja 9 600 PLN) są spójne i potwierdzone w WN-4501, DC-2201 i UM-7788. (WN-4501; DC-2201; UM-7788)  
- Repricing / aktualizacja oprocentowania: HS-7794 dokumentuje obniżkę NRR 3M do 5,35% → nowe oprocentowanie 7,45% i obniżenie raty do 3 531,88 PLN od raty nr 2; takie działanie jest zgodne z zasadą zmiennego oprocentowania jako sumy NRR+marża i kwartalną aktualizacją bez aneksu (REG-KH-02). (HS-7794; REG-KH-02)  
- Zmiana daty pierwszej raty — niejasność / rozbieżność: UM wskazuje pierwszą ratę 15.03.2025 (UM-7788), natomiast HS po aktualizacji podaje "pierwsza rata wg nowego harmonogramu" 15.04.2025 (HS-7794). Równocześnie HS informuje, że nowa rata obowiązuje od raty nr 2. Konieczne do wyjaśnienia: czy rata z 15.03.2025 (wg umowy) pozostaje w mocy jako rata nr 1 (a HS zmienia ratę od nr 2 i przesuwa termin kolejnych rat), czy harmonogram został operacyjnie przesunięty i pierwsza rata w praktyce będzie 15.04.2025. To jest jedyna istotna niejasność wymagająca potwierdzenia operacyjnego. (UM-7788; HS-7794)  
- Inne elementy: liczby kapitałowe/pozostały kapitał po pierwszej racie (np. „pozostały kapitał 479 491,17 PLN”) występowały w alternatywnym podsumowaniu HS — jeśli potrzebne, mogę wyciągnąć szczegółową pozycję kapitał/odsetki dla raty nr 1 z HS-7794; na razie kluczowe wartości i ich zmiana są udokumentowane. (HS-7794)

4) Działania wykonane w pamięci grafu (aby przyspieszyć przyszłe zapytania)
- Zapisano zweryfikowane fakty dotyczące kredytu (kwota, okres, oprocentowanie początkowe i po repricingu, raty, prowizja, daty) oraz krótką wskazówkę dotyczącą rozbieżności dat. Zapisane identyfikatory wpisów w grafie:
  - saved_fact_ids: learned::c7050bd4788f54e7, learned::ae292555bd747b55, learned::07165a01c8b1bd63, learned::9e8540be69c07433, learned::d093c03bf17b61ba, learned::cd150a009f9e437d, learned::c20f460b795702b9, learned::a41e247c0789df02  
  - learning (wskazówka): learning::2f9f55854733c246

5) Rekomendacja / następne kroki (jeśli chcesz)
- Jeśli chcesz pełnej eliminacji niejasności: poprosić dział operacji/kredytów o potwierdzenie, czy pierwsza rata pozostaje 15.03.2025 (UM) i że zmiana z HS dotyczy raty nr 2 (czy też HS przesunął rzeczywisty termin pierwszej raty na 15.04.2025). Źródłem tej weryfikacji powinna być notatka operacyjna/zmiana harmonogramu lub akceptacja aneksu (jeśli istnieje).

Podsumowanie: łańcuch dokumentów jest kompletny i liczbowo spójny w większości punktów; jedyna istotna niejasność dotyczy terminu/zakresu wejścia w życie zmian harmonogramu (data pierwszej raty/przejście na nową ratę) i wymaga krótkiego potwierdzenia operacyjnego. (Źródła: ZD-4501, WN-4501, DC-2201, UM-7788, HS-7794, REG-KH-02).

Jeśli chcesz, mogę:
- wyodrębnić szczegółowe pozycje harmonogramu dla pierwszych 3 rat z HS-7794 (kapitał/odsetki), albo  
- przygotować treść zapytania do działu operacji/kredytów w celu doprecyzowania daty pierwszej raty. Którą opcję wybierasz?

**Ocena:** czesciowa — Agent poprawnie zidentyfikował i zweryfikował większość kluczowych liczb i dokumentów, ale wprowadził rozbieżność co do harmonogramu (HS-7794 vs HS-7788) oraz nie podał LTV i DTI, które są kluczowe dla kompletności zgodności z oczekiwaną odpowiedzią.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'HS-7788', 'KYC-00123', 'POL-RYZYKO-01', 'REG-KH-02', 'TO-2025-Q1', 'TOP-2025-Q1', 'UM-7788', 'WN-4501', 'ZD-4501']; w odpowiedzi ['DC-2201', 'HS-7794', 'REG-KH-02', 'UM-7788', 'WN-4501', 'ZD-4501']; pokrycie 0.5

---

## [P3.2] (zestaw 3) 🟡 czesciowa
**Pytanie:** Wyjaśnij, w jaki sposób działania compliance doprowadziły do odmowy kredytu Markowi Nowickiemu — od transakcji do decyzji. Wskaż całą sekwencję.

**Oczekiwana:** - Rachunek firmowy (HT-00456) wykazał wpłaty gotówkowe rozbijane poniżej progu 15 000 PLN (structuring) i szybkie transfery ~464 950 PLN do Vantia (pass-through).
  - Powstały zgłoszenia SAR-0034 (structuring) i SAR-0041 (pass-through), oba na podstawie POL-AML-01.
  - Raport ryzyka RR-0012 zagregował oba SAR-y i rekomendował klasę E oraz wstrzymanie nowych kredytów.
  - Kartę KYC-00456 zaktualizowano do klasy E (WYSOKIE), wdrożono EDD.
  - Kolejny wniosek WN-4508 (kredyt 80 000 PLN) otrzymał decyzję **negatywną DC-2250** — mimo DTI 16,20% — z powodu klasy E i braku możliwości ustalenia źródła środków.
  - To pełna pętla zwrotna: transakcje → ryzyko → odmowa.

**Odpowiedź agenta:** Poniżej przedstawiam sekwencję działań (od transakcji/wniosku do decyzji) wyjaśniającą, dlaczego wniosek kredytowy Marka Nowickiego został odrzucony przez compliance. Wszystkie stwierdzenia opierają się na dokumentach: WN-4508, RR-0012, DC-2250.

Sekwencja krok po kroku:
1. Złożenie wniosku: Marek Nowicki złożył wniosek kredytowy (WN-4508). (źródło: WN-4508)
2. Weryfikacja finansowa: Bank przeprowadził ocenę zdolności kredytowej; wyniki finansowe klienta (dochód, DTI) spełniały kryteria banku. (źródła: WN-4508, DC-2250)
3. Analiza ryzyka/AML: Departament Ryzyka / Zgodności sporządził raport ryzyka (RR-0012), który wskazał wysokie ryzyko AML (klasa E), w tym podejrzenia o structuring i pass-through oraz brak udokumentowanego źródła środków. (źródło: RR-0012)
4. Rekomendacja compliance: Na podstawie raportu RR-0012 Departament Zgodności zarekomendował wstrzymanie udzielania produktu do czasu wyjaśnienia oraz uznał, że ryzyko jest nieakceptowalne w obecnym stanie. (źródło: RR-0012)
5. Decyzja kredytowa: Komitet Kredytowy, uwzględniając opinię compliance i raport ryzyka, podjął decyzję negatywną (DC-2250) — odmowa kredytu mimo spełnienia kryteriów zdolnościowych. (źródła: DC-2250, RR-0012, WN-4508)
6. Informacja dla klienta: Klient otrzymał informację o odmowie z ogólnym wskazaniem przyczyn związanych z oceną ryzyka i wymogami zgodności (źródło: DC-2250).

Podsumowanie: Odmowa wynikała z wysokiego ryzyka AML (klasa E) oraz braku możliwości ustalenia źródła środków stwierdzonych w raporcie RR-0012; były to przesłanki decydujące mimo pozytywnej oceny zdolności finansowej (WN-4508, RR-0012, DC-2250).

Zapis w grafie: Fakt przyczyny odmowy został zapisany w grafie wiedzy i powiązany z dokumentami WN-4508, RR-0012, DC-2250 (id learned::99380c05ff2255c5).

Jeśli chcesz, mogę:
- rozwinąć szczegóły raportu RR-0012 (konkretne obserwacje wskazujące na structuring / pass-through),
- udostępnić fragmenty decyzji DC-2250 z uzasadnieniem (jeśli poufność na to pozwala).

**Ocena:** czesciowa — Odpowiedź agenta poprawnie opisuje główną sekwencję od wniosku do odmowy i wskazuje kluczowe dokumenty, jednak pomija konkretne szczegóły transakcji (wpłaty poniżej progu, kwotę transferów, kody SAR) oraz aktualizację KYC i wdrożenie EDD, które są istotne w oczekiwanej odpowiedzi.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250', 'HT-00456', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'WN-4508']; w odpowiedzi ['DC-2250', 'RR-0012', 'WN-4508']; pokrycie 0.33

---

## [P3.3] (zestaw 3) 🟡 czesciowa
**Pytanie:** Porównaj trzy typy decyzji kredytowych w zbiorze (pozytywną, warunkową, negatywną) i wskaż, jak profil ryzyka z KYC oraz polityki determinowały wynik każdej z nich.

**Oczekiwana:** - **Pozytywna — DC-2201** (Anna Kowalska): klasa B, DTI 36,52%, LTV 80% — wszystkie kryteria POL-RYZYKO-01 spełnione → udzielenie kredytu.
  - **Warunkowa — DC-2203** (Bałtyk Logistyka): klasa C przy podwyższonym zadłużeniu → zgoda pod warunkiem opłaty wstępnej 30% lub dodatkowego zabezpieczenia (POL-RYZYKO-01 §5).
  - **Negatywna — DC-2250** (Marek Nowicki): zdolność wystarczająca (DTI 16,20%), ale klasa E z RR-0012 (AML) → odmowa (POL-RYZYKO-01 §5, POL-AML-01).
  - Wniosek: o wyniku decydował nie tylko wskaźnik finansowy, lecz klasa ryzyka (w tym override z tytułu AML).

**Odpowiedź agenta:** Poniżej krótkie porównanie trzech typów decyzji oraz wskazanie, które elementy profilu KYC i które polityki determinowały wynik każdej z nich. Wszystkie wnioski oparte wyłącznie na danych z grafu i repozytorium (podaję źródła).

1) Decyzja pozytywna — DC-2202
- Kluczowe elementy KYC, które zadecydowały:
  - klasa ryzyka A, scoring 92/100; niski wskaźnik DTI (13,23%); dochód potwierdzony (8 200 PLN/mies., ZD-4503); zatrudnienie na etat — stabilny profil finansowy → niski risk premium (źródło: KYC-00124, ZD-4503).  
- Polityki/regularia i ich wpływ:
  - POL-RYZYKO-01 i regulamin produktu kredytowego (REG-KG-01) potwierdziły, że parametry klienta mieszczą się w akceptowalnych limitach (stąd decyzja bez warunków) (źródło: DC-2202, POL-RYZYKO-01, REG-KG-01, TO-2025-Q1).  
- Efekt: kredyt udzielony bez dodatkowych zabezpieczeń; umowa powiązana UM-7789 (źródło: DC-2202, UM-7789).

2) Decyzja warunkowa — DC-2203
- Kluczowe elementy KYC:
  - decyzja wskazuje wyższe ryzyko klienta powiązanego z KYC-00125 (profil wymagający korekt zabezpieczeń) — szczegóły KYC-00125 nie były udostępnione do pełnego odczytu, więc nie wszystkie pola KYC można zweryfikować (źródło: DC-2203; brak dostępu do treści KYC-00125).  
- Polityki/regularia i ich wpływ:
  - POL-RYZYKO-01 i regulamin/leasing (REG-LE-04) wymagały zaostrzenia zabezpieczeń lub dodatkowych warunków przy wyższym ryzyku (stąd warunki wymienione w decyzji) (źródło: DC-2203, POL-RYZYKO-01, REG-LE-04, TO-2025-Q1).  
- Warunki postawione klientowi:
  - np. podwyższenie opłaty wstępnej do 30% lub ustanowienie dodatkowego zabezpieczenia; dostarczenie zaświadczeń ZUS/US; ubezpieczenie z cesją — warunki służą kompensacji zwiększonego ryzyka (źródło: DC-2203, UM-7790).

3) Decyzja negatywna — DC-2250
- Kluczowe elementy KYC:
  - decyzja przypisana do KYC-00456 i uzasadniona klasą ryzyka E, brakiem możliwości wiarygodnego ustalenia źródła środków oraz (w rezultacie) wysokim DTI/niestabilnym profilem dochodowym — stąd odmowa (uwaga: treść KYC-00456 nie była w pełni dostępna do odczytu przy ekstrakcji) (źródło: DC-2250, powiązanie: KYC-00456).  
- Polityki/regularia i ich wpływ:
  - POL-AML-01 (kontrola źródeł środków), POL-RYZYKO-01 i odpowiedni regulamin produktu (REG-KG-01) były podstawą formalnego zakazu finansowania w takich przypadkach — polityki wymagają odmowy, gdy źródło środków nie jest potwierdzone lub ryzyko jest zbyt wysokie (źródło: DC-2250, POL-AML-01, POL-RYZYKO-01, REG-KG-01).  
- Efekt: odmowa bez warunków łagodzących (źródło: DC-2250).

Syntetyczne wnioski / obszary ryzyka
- Stabilny dochód, wysoki scoring i niski DTI (KYC) prowadzą zwykle do decyzji pozytywnej; polityki ryzyka potwierdzają tę ścieżkę (np. DC-2202: KYC-00124, POL-RYZYKO-01).  
- Przy średnim scoringu/niestabilnym dochodzie bank preferuje decyzję warunkową (z dodatkowymi zabezpieczeniami) — polityki wymuszają kompensujące warunki (np. DC-2203: warunki zabezpieczające, POL-RYZYKO-01, REG-LE-04).  
- Brak potwierdzenia źródła środków i wysoka ocena ryzyka (klasa E) prowadzą do automatycznej odmowy zgodnie z politykami AML i polityką ryzyka (np. DC-2250: POL-AML-01, POL-RYZYKO-01).  

Uwaga dotycząca weryfikacji danych
- Dla DC-2202 mamy pełne pola KYC i potwierdzenia dochodu (KYC-00124, ZD-4503, UM-7789, POL-RYZYKO-01).  
- Treści KYC powiązane z DC-2203 (KYC-00125) oraz DC-2250 (KYC-00456) nie były w pełni dostępne do odczytu podczas ekstrakcji — opis warunków i przyczyn decyzji pochodzi z treści decyzji (DC-2203, DC-2250) i cytowanych polityk, ale szczegółowe pola KYC (np. pełne wartości DTI/scoring) wymagają odczytu tych KYC dla kompletnej weryfikacji (źródła do uzupełnienia: KYC-00125, KYC-00456).  

Źródła (wybrane z grafu/repozytorium): DC-2202, KYC-00124, ZD-4503, UM-7789, POL-RYZYKO-01, REG-KG-01, TO-2025-Q1; DC-2203, UM-7790, REG-LE-04, POL-RYZYKO-01; DC-2250, POL-AML-01, POL-RYZYKO-01.  

Jeśli chcesz, mogę:
- odczytać/zaimportować brakujące KYC (KYC-00125, KYC-00456) i ponownie potwierdzić szczegóły; lub
- przygotować tabelaryczne porównanie liczbowych wskaźników (scoring, DTI, dochód) dla wszystkich trzech przypadków — jeśli udostępnisz brakujące pliki KYC.

**Ocena:** czesciowa — Agent prawidłowo opisał wpływ profilu ryzyka KYC i polityk na decyzje kredytowe, ale użył innych ID decyzji i wartości (np. DC-2202 zamiast DC-2201) oraz podał niekompletne lub różne dane liczbowo (DTI, klasy ryzyka) w porównaniu z oczekiwaną odpowiedzią.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach → niepotwierdzone/niepełne → KOLEJNA RUNDA szukania w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2201', 'DC-2203', 'DC-2250', 'KYC-00123', 'KYC-00125', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'RR-0012']; w odpowiedzi ['DC-2202', 'DC-2203', 'DC-2250', 'KYC-00124', 'KYC-00125', 'KYC-00456', 'POL-AML-01', 'POL-RYZYKO-01', 'REG-KG-01', 'REG-LE-04', 'TO-2025-Q1', 'UM-7789', 'UM-7790', 'ZD-4503']; pokrycie 0.67

---

## [P3.4] (zestaw 3) ❌ zla
**Pytanie:** Oblicz łączną kwotę odsetek dla wszystkich kredytów/leasingów z zawartymi umowami w zbiorze i podaj źródła.

**Oczekiwana:** - Kredyt hipoteczny UM-7788: odsetki 626 649,94 PLN wg pierwotnego HS-7788 (lub 579 719,78 PLN po repricingu wg HS-7794, przy założeniu utrzymania 7,45%).
  - Kredyt gotówkowy UM-7789: odsetki 15 077,76 PLN (HS-7789).
  - Leasing UM-7790: część odsetkowa 28 169,56 PLN netto (HS-7790).
  - **Suma (wariant pierwotny hipoteki):** 626 649,94 + 15 077,76 + 28 169,56 = **669 897,26 PLN**.
  - (Uwaga: umowa karty UM-7791 nie ma z góry ustalonych odsetek — zależą od wykorzystania limitu; wniosek WN-4508 odrzucono, więc go nie liczymy.)

**Odpowiedź agenta:** Wykonałem analizę grafu i dokumentów.

Podsumowanie (krótko):
- Łączna kwota odsetek dla wszystkich umów ze statusem „zawarta”: 28 169,56 PLN.

Rozbicie:
- UM-7790 (leasing): 28 169,56 PLN (źródło: UM-7790, HS-7790).

Pełna lista dokumentów źródłowych: UM-7790, HS-7790, DC-2203, WN-4503, TO-2025-Q1.

Weryfikacja: wynik POTWIERDZONY (weryfikator potwierdził zgodność kwoty z dokumentami). Jeśli chcesz, mogę teraz zapisać tę zweryfikowaną faktografię do grafu wiedzy, aby przyspieszyć przyszłe zapytania.

**Ocena:** zla — Agent podał tylko odsetki z leasingu UM-7790, ignorując odsetki z kredytów hipotecznego UM-7788 i gotówkowego UM-7789 oraz prawidłową sumę wymaganych wartości.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['HS-7788', 'HS-7789', 'HS-7790', 'HS-7794', 'UM-7788', 'UM-7789', 'UM-7790']; w odpowiedzi ['DC-2203', 'HS-7790', 'TO-2025-Q1', 'UM-7790', 'WN-4503']; pokrycie 0.29

---

## [P3.5] (zestaw 3) ✅ dobra
**Pytanie:** Opisz mechanizm i finansowy skutek zmiany wskaźnika NRR 3M dla kredytu hipotecznego — wskaż dokumenty i kwoty.

**Oczekiwana:** - NRR 3M spadł z 5,85% (TO-2025-Q1) do 5,35% (TO-2025-Q2), tj. o 0,50 p.p.
  - Zgodnie z REG-KH-02 §3 (oprocentowanie zmienne, aktualizacja kwartalna, marża stała), oprocentowanie UM-7788 zmieniło się z 7,95% na 7,45% bez aneksu.
  - Bank sporządził zaktualizowany harmonogram HS-7794 (od raty nr 2): rata spadła z 3 688,83 na **3 531,88 PLN** (o 156,95 PLN).
  - Łączne odsetki spadły z 626 649,94 do 579 719,78 PLN (oszczędność ok. 46 930,16 PLN przy utrzymaniu 7,45%).
  - Efekt widoczny na wyciągu HT-00123 (rata 1 = 3 688,83, raty 2–3 = 3 531,88).

**Odpowiedź agenta:** Oto zwięzłe wyjaśnienie mechanizmu oraz finansowego skutku zmiany NRR 3M wraz ze wskazaniem dokumentów i kwot (wszystko oparte wyłącznie na danych z grafu i dokumentów):

1) Mechanizm
- Oprocentowanie kredytu hipotecznego jest indeksowane wzorem: oprocentowanie = NRR 3M + marża banku (źródło: TO-2025-Q1).  
- Gdy NRR 3M się zmienia, oprocentowanie jest korygowane automatycznie zgodnie z powyższą regułą; zmiana ta następnie wpływa na wysokość rat kapitałowo-odsetkowych zgodnie z harmonogramem spłaty (źródła: TO-2025-Q1, UM-7788, HS-7794).

2) Konkretny finansowy skutek (przykład UM-7788)
- NRR 3M: 5,85% (I kwartał 2025) → 5,35% (II kwartał 2025), spadek o 0,50 punktu procentowego (źródło: TO-2025-Q1).  
- W umowie UM-7788 oprocentowanie zmieniło się z 7,95% na 7,45% (różnica 0,50 p.p.), zgodnie z regułą indeksacji (źródła: UM-7788, HS-7794).  
- Miesięczna rata kredytu została obniżona z 3 688,83 PLN do 3 531,88 PLN (zmiana obowiązuje od kwietnia 2025, harmonogram HS-7794) (źródła: UM-7788, HS-7794).

3) Wnioski praktyczne
- Zmiana NRR 3M o 0,50 p.p. przełożyła się bezpośrednio na obniżenie oprocentowania o 0,50 p.p. i obniżenie miesięcznej raty w przykładowej umowie UM-7788 o 156,95 PLN miesięcznie (różnica: 3 688,83 − 3 531,88 PLN) (źródła: TO-2025-Q1, UM-7788, HS-7794).  
- Przy ocenie wpływu zmian wskaźnika zawsze sprawdzać: aktualną wartość NRR dla odpowiednich kwartałów (TO-2025-Q1), zapis umowy kredytowej określający marżę i mechanizm repricingu (UM-*), oraz odpowiadający harmonogram/anksy (HS-*) (źródła: TO-2025-Q1, UM-7788, HS-7794).

Źródła:
- TO-2025-Q1 (wartości NRR 3M: 5,85% → 5,35%)  
- UM-7788 (warunki umowy, zmiana oprocentowania 7,95% → 7,45%)  
- HS-7794 (harmonogram: rata 3 688,83 PLN → 3 531,88 PLN, zmiana od kwietnia 2025)

Jeśli chcesz, mogę:
- pokazać fragmenty konkretnych zapisów z wymienionych dokumentów (TO-2025-Q1, UM-7788, HS-7794),  
- policzyć wpływ zmiany NRR na ratę dla innej umowy (podaj ID umowy lub parametry: kwota, pozostały okres, marża).

**Ocena:** dobra — Odpowiedź agenta zawiera wszystkie kluczowe dane i kwoty zgodne z oczekiwaną, w tym spadek NRR 3M, zmianę oprocentowania, raty i odniesienia do właściwych dokumentów.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7788', 'HS-7794', 'HT-00123', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'UM-7788']; w odpowiedzi ['HS-7794', 'TO-2025-Q1', 'UM-7788']; pokrycie 0.43

---

## [P3.6] (zestaw 3) 🟡 czesciowa
**Pytanie:** Zidentyfikuj wszystkich klientów objętych wzmożonymi środkami bezpieczeństwa (EDD) i opisz podstawę oraz skutki dla ich klasy ryzyka.

**Oczekiwana:** - **KL-00456 (Marek Nowicki):** EDD z powodu SAR-0034 i SAR-0041 → RR-0012; klasa ryzyka podniesiona z C do **E**; wstrzymanie nowych kredytów (skutek: odmowa DC-2250).
  - **KL-00129 (Bursztyn Handel Sp. z o.o.):** EDD z powodu SAR-0052 (nietypowe wpłaty gotówkowe + transakcje z podmiotem powiązanym); klasa ryzyka podniesiona z C do **D**; nowe zaangażowania warunkowe/wstrzymane.
  - Obaj objęci zakazem tipping-off (POL-AML-01 §7).

**Odpowiedź agenta:** Poniżej zwięzły raport — wszelkie informacje są potwierdzone w grafie i dokumentach wskazanych przy każdym punkcie.

1) Marek Andrzej Nowicki, JDG „MN Trade”
   - Identyfikator: KYC-00456
   - Podstawa objęcia EDD: zgłoszenia podejrzanych transakcji SAR-0034 i SAR-0041; rekomendacja z raportu ryzyka RR-0012
   - Aktualna klasa ryzyka: E (WYSOKIE)
   - Skutki dla klasy ryzyka: wstrzymanie nowych zaangażeń kredytowych do czasu wyjaśnienia sytuacji; obowiązek prowadzenia wzmożonego (wzmocnionego) monitoringu transakcji; możliwe dodatkowe ograniczenia zgodnie z POL-AML-01
   - Źródła: KYC-00456, RR-0012, SAR-0034, SAR-0041, HT-00456, POL-AML-01, WN-4508
   - Zapis w grafie: fakt EDD zapisany (id faktu: learned::2c1c0a2a2ac7cca0)

Jeśli chcesz, mogę:
- wygenerować szczegółowy przegląd dokumentów (wyciągi z KYC-00456, fragmenty RR-0012 i SAR-0034/0041),
- lub przeszukać graf ponownie pod kątem innych klientów EDD (szersze kryteria).

**Ocena:** czesciowa — Agent poprawnie zidentyfikował klienta KL-00456 i opisał podstawę oraz skutki EDD, lecz pominął klienta KL-00129 oraz informacje o zakazie tipping-off dla obydwu klientów.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['KYC-00129', 'KYC-00456', 'POL-AML-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'SAR-0052']; w odpowiedzi ['HT-00456', 'KYC-00456', 'POL-AML-01', 'RR-0012', 'SAR-0034', 'SAR-0041', 'WN-4508']; pokrycie 0.71

---

## [P3.7] (zestaw 3) ✅ dobra
**Pytanie:** Które tabele oprocentowania i opłat obowiązują dla poszczególnych umów, biorąc pod uwagę daty ich zawarcia i zasady aktualizacji?

**Oczekiwana:** - Umowy zawarte w I kw. 2025 (UM-7788 z 14.02, UM-7789 z 05.03, UM-7790 z 20.03, UM-7791 z 12.03) bazują na TO-2025-Q1 i TOP-2025-Q1.
  - Kredyty stałoprocentowe (gotówkowy UM-7789) i leasing (UM-7790) zachowują stopę z dnia zawarcia.
  - Kredyt hipoteczny UM-7788 (zmienny) jest repricowany od Q2 wg TO-2025-Q2 (nowy harmonogram HS-7794).
  - Wniosek WN-4506 (10.05.2025, Q2) bazuje na TO-2025-Q2 i TOP-2025-Q2.

**Odpowiedź agenta:** Rozpoczynam analizę zgodnie z procedurą (graf → dokumenty → answerer → verifier). Poniżej finalna, zweryfikowana odpowiedź.

1) UM-7788 (kredyt hipoteczny)
- Data zawarcia: 14.02.2025 (źródło: UM-7788)
- Tabela oprocentowania obowiązująca na dzień zawarcia:
  - TO-2025-Q1 (okres obowiązywania: 01.01.2025–31.03.2025). Oprocentowanie zmienne na dzień zawarcia: 7,95% = NRR 3M (5,85%) + marża 2,10% (źródła: UM-7788, TO-2025-Q1).
- Tabela opłat/prowizji powiązana:
  - TOP-2025-Q1 (okres: I kwartał 2025) — stosowana na dzień zawarcia (źródło: UM-7788, TOP-2025-Q1).
- Zasady aktualizacji:
  - Oprocentowanie zmienne; kwartalna aktualizacja wg wskaźnika NRR 3M, marża pozostaje stała; aktualizacja następuje automatycznie bez konieczności aneksu (REG-KH-02 §3, TO-2025-Q2 odwołuje się do tej zasady) (źródła: REG-KH-02, TO-2025-Q2, HS-7794).
- Uwagi o brakach: brak (werdykt: POTWIERDZONA).

2) UM-7790 (leasing operacyjny)
- Data zawarcia: 20.03.2025 (źródło: UM-7790)
- Tabela oprocentowania obowiązująca na dzień zawarcia:
  - TO-2025-Q1 (01.01.2025–31.03.2025). Stopa leasingowa stosowana na zawarcie: 9,05% = NRR 3M (5,85%) + 3,20% (źródła: UM-7790, TO-2025-Q1).
- Tabela opłat/prowizji powiązana:
  - Brak wyraźnie wskazanej tabeli OP/TOP w dokumentach powiązanych z UM-7790; opłaty regulowane są warunkami umowy i regulaminem REG-LE-04 (źródła: UM-7790, REG-LE-04). 
- Zasady aktualizacji:
  - W dokumentach związanych z UM-7790 nie ma jednoznacznej klauzuli o automatycznej kwartalnej aktualizacji oprocentowania ani o konieczności aneksu; umowa i decyzja stosują stopę z TO-2025-Q1 na dzień zawarcia, bez zapisu o automatycznym repricingu (źródła: UM-7790, DC-2203). 
- Uwagi o brakach: brak wyraźnej informacji o tabeli opłat/prowizji (brak OP/TOP powiązanego) oraz brak klauzuli opisującej mechanizm aktualizacji wprost — wymagane dalsze sprawdzenie, jeśli konieczne szczegóły proceduralne (np. czy repricing leasingu następuje według odrębnego regulaminu).

3) UM-7789 (kredyt gotówkowy)
- Data zawarcia: 05.03.2025 (źródło: UM-7789)
- Tabela oprocentowania obowiązująca na dzień zawarcia:
  - TO-2025-Q1 (01.01.2025–31.03.2025). Oprocentowanie stałe przy zawarciu: 10,90% (zgodnie z TO-2025-Q1 §3 i UM-7789 §3) (źródła: UM-7789, TO-2025-Q1).
- Tabela opłat/prowizji powiązana:
  - TOP-2025-Q1 (I kwartał 2025) — prowizje i opłaty stosowane na dzień zawarcia (źródła: UM-7789, TOP-2025-Q1).
- Zasady aktualizacji:
  - Oprocentowanie stałe: zapis umowny, że oprocentowanie stałe nie ulega zmianie przez cały okres kredytowania (UM-7789 §3). Regulaminy powiązane (REG-KG-01) i TOP-2025-Q1 potwierdzają brak bieżących zmian oprocentowania (źródła: UM-7789, REG-KG-01).
- Uwagi o brakach: brak.

Źródła wykorzystane (dokumenty): UM-7788, TO-2025-Q1, TO-2025-Q2, TOP-2025-Q1, UM-7790, REG-LE-04, DC-2203, UM-7789, REG-KG-01, HS-7788, HS-7794, HS-7790.

Jeśli chcesz, mogę:
- wyciągnąć i wkleić konkretne cytaty (fragmenty §) z wymienionych dokumentów; 
- sprawdzić, czy dla UM-7790 istnieje ukryta tabela opłat w innych dokumentach (przeszukać katalog OP-, TOP- dodatkowo); 
- przygotować tabelaryczne zestawienie dla raportu compliance.

**Ocena:** dobra — Odpowiedź agenta w pełni odpowiada oczekiwanym kluczowym faktom dotyczącym tabel oprocentowania i opłat oraz zasad aktualizacji dla poszczególnych umów wraz z odniesieniem do odpowiednich dokumentów i dat.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach

**Źródła:** oczekiwane ['REG-KG-01', 'REG-KH-02', 'TO-2025-Q1', 'TO-2025-Q2', 'TOP-2025-Q1', 'TOP-2025-Q2', 'UM-7788', 'WN-4506']; w odpowiedzi ['DC-2203', 'HS-7788', 'HS-7790', 'HS-7794', 'REG-KG-01', 'REG-KH-02', 'REG-LE-04', 'TO-2025-Q1', 'TO-2025-Q2', 'TOP-2025-Q1', 'UM-7788', 'UM-7789', 'UM-7790']; pokrycie 0.75

---

## [P3.8] (zestaw 3) ✅ dobra
**Pytanie:** Sprawdź spójność danych osobowych i finansowych klientki KL-00124 we wszystkich dokumentach, w których występuje.

**Oczekiwana:** - Katarzyna Maria Lewandowska, PESEL 90111067321 — identyczne w KYC-00124, ZD-4503, WN-4502, UM-7789.
  - Dochód netto 8 200 PLN — spójny w ZD-4503, WN-4502, DC-2202.
  - Kredyt 50 000 PLN / 60 mies / 10,90% / rata 1 084,63 PLN — spójny w WN-4502, DC-2202, UM-7789, HS-7789.
  - Klasa ryzyka A (scoring 92) — KYC-00124, potwierdzona w DC-2202.
  - Brak sprzeczności.

**Odpowiedź agenta:** Wykonałem analizę i weryfikację spójności danych klientki KL-00124 zgodnie z procedurą. Podsumowanie:

Lista dokumentów i kluczowe pola (skrót)
- KYC-00124 (Karta KYC / CDD)
  - Dane osobowe: Katarzyna Maria Lewandowska; PESEL 90111067321; ur. 1990-11-10, Gdańsk; adres zamieszkania: ul. Słoneczna 5 m.2, 80-100 Gdańsk; dowód: DEF 246810 (ważny do 2032-03-22); zamężna (rozdzielność majątkowa); tel. +48 513 000 124; e-mail k.lewandowska@test.example.
  - Dane finansowe: dochód netto 8 200,00 PLN (średnio), brak zobowiązań wskazanych.

- WN-4502 (Wniosek kredytowy „Nordvik Gotówka”)
  - Dane osobowe: tożsame z KYC-00124.
  - Dane finansowe: kwota 50 000,00 PLN; okres 60 mies.; oprocentowanie nominalne stałe 10,90% ; rata 1 084,63 PLN; prowizja 4% = 2 000,00 PLN; dochód netto 8 200,00 PLN; DTI 13,23%; cel: remont mieszkania.

- DC-2202 (Decyzja kredytowa)
  - Dane osobowe: zgodne z KYC/WN.
  - Dane finansowe: kwota 50 000,00 PLN; okres 60 mies.; oprocentowanie 10,90%; rata 1 084,63 PLN; prowizja 2 000,00 PLN; RRSO 13,46%; DTI 13,23%; scoring 92/100; profil ryzyka A; decyzja: pozytywna. Dochód 8 200 PLN potwierdzony zaświadczeniem ZD-4503.

- UM-7789 (Umowa kredytowa)
  - Dane osobowe: zgodne z KYC.
  - Dane finansowe: kwota 50 000,00 PLN; okres 60 mies.; oprocentowanie 10,90% stałe; rata 1 084,63 PLN; prowizja 2 000,00 PLN; RRSO 13,46%; całkowity koszt kredytu 17 077,76 PLN; uruchomienie 07.03.2025; załącznik HS-7789 z harmonogramem.

- ZD-4503 (Zaświadczenie o dochodach)
  - Dane osobowe: zgodne z KYC.
  - Dane finansowe: pracodawca Nadmorskie Centrum Medyczne Sp. z o.o. (NIP 584-222-33-44); umowa o pracę na czas nieokreślony; średni dochód netto 8 200,00 PLN (6 mies.); ważne do 12.03.2025.

- HS-7789 (Harmonogram spłat)
  - Dane finansowe: kwota 50 000,00 PLN; 60 rat annuitetowych po 1 084,63 PLN; pierwsza rata 10.04.2025, ostatnia 10.03.2030; szczegóły rozkładu kapitału/odsetek; konto spłaty podane.

Braki / pola nieznalezione
- Brak adresu korespondencyjnego (nie występuje w przeglądanych dokumentach).
- Brak NIP klientki (w dokumentach jest NIP pracodawcy, nie NIP osobisty).
- Brak informacji o paszporcie (dostępny tylko dowód osobisty).
- Brak rozbieżności co do kluczowych pól — inne ewentualne pola drugorzędne (np. numer dowodu poza KYC, dane osób na utrzymaniu) są albo nieistotne lub niepełne.

Ocena spójności
- Ogólna ocena: SPÓJNE i POTWIERDZONE.
  - Dane osobowe (imię, nazwisko, PESEL, data urodzenia, adres zamieszkania, dowód, status zatrudnienia) są zgodne we wszystkich dokumentach.
  - Dane finansowe (kwota kredytu, okres, oprocentowanie nominalne, rata, prowizja, RRSO, dochód, DTI, scoring, terminy spłat) są zgodne i wzajemnie potwierdzone (WN-4502, DC-2202, UM-7789, HS-7789, ZD-4503).

Działania wykonane / zapis w grafie
- Zweryfikowane fakty zostały zapisane do grafu wiedzy jako nauczone (dla encji KL-00124): dane osobowe, dane kredytowe, dochody, ryzyko/ scoring, harmonogram i lista braków (adres_korespondencyjny, nip_klienta, paszport). Wpisy pochodzą z dokumentów: KYC-00124, WN-4502, DC-2202, UM-7789, ZD-4503, HS-7789.
- Weryfikator ocenił odpowiedź jako POTWIERDZONĄ.

Źródła
- KYC-00124, WN-4502, DC-2202, UM-7789, ZD-4503, HS-7789.

Jeżeli chcesz, mogę:
- dopisać brakujący adres korespondencyjny/NIP klientki (jeśli podasz źródło),
- wygenerować raport PDF z cytowaniem źródeł,
- sprawdzić, czy w innych systemach (np. historia transakcji) nie ma dodatkowych zobowiązań klientki.

**Ocena:** dobra — Odpowiedź agenta w pełni pokrywa się merytorycznie z odpowiedzią oczekiwaną, potwierdzając zgodność kluczowych danych osobowych i finansowych klientki w wymienionych dokumentach.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2202', 'HS-7789', 'KYC-00124', 'UM-7789', 'WN-4502', 'ZD-4503']; w odpowiedzi ['DC-2202', 'HS-7789', 'KL-00124', 'KYC-00124', 'UM-7789', 'WN-4502', 'ZD-4503']; pokrycie 1.0

---

## [P3.9] (zestaw 3) ✅ dobra
**Pytanie:** Na podstawie polityk banku opisz, jak przetwarzany jest wniosek klienta wysokiego ryzyka AML oraz jakie ograniczenia praw wynikają z zasad ochrony danych.

**Oczekiwana:** - Ocena ryzyka i klasyfikacja: POL-RYZYKO-01 (klasy A–E, override jakościowy) w powiązaniu z POL-AML-01 (CDD/EDD, monitoring, SAR).
  - Dla klienta wysokiego ryzyka: wzmożone środki (EDD), ustalenie źródła środków, możliwe wstrzymanie nowych usług i blokady; zakaz tipping-off.
  - RODO (POL-DANE-01): przetwarzanie na podstawie obowiązku prawnego (AML) — prawo do usunięcia i sprzeciwu NIE ma zastosowania do dokumentacji AML; okresy przechowywania wynikają z przepisów AML.
  - Przykład zastosowania: KL-00456/DC-2250 oraz KL-00129/SAR-0052.

**Odpowiedź agenta:** Odpowiedź przygotowana i zweryfikowana — poniżej końcowe, potwierdzone streszczenie zgodnie z politykami banku.

Wstęp
- Wniosek klienta zaklasyfikowanego jako wysokie ryzyko AML jest przetwarzany według procedur AML banku, które obejmują identyfikację i weryfikację, wzmożone środki należytej staranności (EDD), monitorowanie transakcji, zgłaszanie podejrzanych operacji oraz decyzje na poziomie MLRO. Przetwarzanie danych odbywa się w ramach obowiązku prawnego, przy jednoczesnym stosowaniu zasad ochrony danych (źródła: POL-AML-01; KYC-00456; SAR-0034; POL-DANE-01; RR-0012).

Kroki przetwarzania (etapy)
1. Identyfikacja i ocena ryzyka
   - Przeprowadzenie standardowego CDD (identyfikacja klienta i beneficjenta rzeczywistego) i ocena ryzyka wg kryteriów klient/produkt/kanal/geografia (POL-AML-01 §2–§3; KYC-00456 §1, §4).
2. Reklasyfikacja i zastosowanie EDD
   - Klient sklasyfikowany jako wysokie ryzyko otrzymuje wzmożone środki należytej staranności (EDD): dodatkowe ustalenie źródła majątku/środków, zbieranie dokumentów, częstsze przeglądy (np. co 6 miesięcy) i akceptacja działań przez MLRO (POL-AML-01 §2; KYC-00456 §4).
3. Monitorowanie transakcji i wykrywanie typologii
   - Automatyczne i ręczne monitorowanie pod kątem typologii (np. structuring) oraz progów raportowych (informacje w POL-AML-01 i SAR-0034) (POL-AML-01 §4–§5; SAR-0034).
4. Wezwanie do udokumentowania źródła środków
   - W razie podejrzeń bank wzywa klienta do dostarczenia dokumentów potwierdzających źródło środków (wzór wezwania / praktyka opisana w SAR-0034 i KYC-00456 §7) (SAR-0034 §5; KYC-00456 §7).
5. Zgłoszenie podejrzanej transakcji (SAR)
   - Pracownik zgłasza sygnał do zespołu AML; analityk przygotowuje SAR, który wymaga akceptacji MLRO i jest przekazywany do KJAF (POL-AML-01 §6; SAR-0034).
6. Działania zaradcze i ograniczenia usług
   - Na podstawie raportu ryzyka (RR-0012) możliwa jest reklasyfikacja (np. do klasy E), wstrzymanie przyznawania nowych produktów/świadczenia usług do czasu wyjaśnienia oraz blokada transakcji, jeśli uzasadnione (RR-0012 §3–§4; POL-AML-01 §7).
7. Zakaz tipping-off
   - Bank nie ujawnia klientowi informacji o zgłoszeniu SAR ani o prowadzonych postępowaniach (zakaz „tipping-off”) (POL-AML-01 §7).

Ograniczenia prawne — ochrona danych (RODO)
- Podstawa przetwarzania: obowiązek prawny
  - Dane związane z AML są przetwarzane na podstawie obowiązku prawnego, co uprawnia bank do ich przetwarzania nawet gdy klient żąda usunięcia czy wnosi sprzeciw (POL-DANE-01 §3, §6).
- Prawa klienta i ich ograniczenia
  - Klient ma prawa: dostęp do danych, sprostowanie, ograniczenie przetwarzania, przenoszenie danych oraz sprzeciw — ale prawa te mogą być ograniczone, gdy przetwarzanie jest konieczne ze względu na obowiązki AML (POL-DANE-01 §5–§6).
  - Prawo do usunięcia (art. 17 RODO) jest wyłączone w zakresie danych przetwarzanych ze względu na obowiązek prawny AML (POL-DANE-01 §6).
- Zasada minimalizacji i zasady bezpieczeństwa
  - Bank zbiera i przetwarza wyłącznie dane niezbędne do celów AML (zasada minimalizacji) oraz stosuje środki techniczne i organizacyjne (szyfrowanie, kontrola dostępu, rejestrowanie operacji, zasada „wiedzy koniecznej”) (POL-DANE-01 §4–§7).
- Obowiązki w przypadku naruszeń
  - Bank rejestruje incydenty bezpieczeństwa i zgłasza naruszenia odpowiednim organom; przy wysokim ryzyku informuje osoby, których dane dotyczą (POL-DANE-01 §8).

Przechowywanie i archiwizacja
- Dokumentacja AML (karty KYC, SAR, raporty ryzyka) przechowywana jest przez okres wymagany przepisami prawa o przeciwdziałaniu praniu pieniędzy; polityki i procedury podlegają corocznemu przeglądowi (POL-AML-01 §8; POL-DANE-01 §5, §9).
- Uwaga: w dostępnych dokumentach brak szczegółowych, technicznych specyfikacji dotyczących systemów archiwizacji (konkretne systemy, formaty, terminy retencji w latach nieopisane w pełni) — to pozostaje luka dokumentacyjna (KYC-00456; POL-DANE-01).

Źródła (cytowane dokumenty)
- POL-AML-01 (Polityka AML/CFT)
- SAR-0034 (wzory/opracowania zgłoszeń podejrzanych)
- POL-DANE-01 (Polityka ochrony danych osobowych / RODO)
- KYC-00456 (Karta KYC / procedury po reklasyfikacji)
- RR-0012 (Raport ryzyka klienta)

Uwagi końcowe
- Odpowiedź oparta jest wyłącznie na powyższych politykach i dokumentach wewnętrznych; werdykt weryfikatora: POTWIERDZONA (brak rozbieżności między dokumentami a powyższym opisem). Jeśli chcesz, mogę: 1) dostarczyć wzór wezwania klienta (pełny tekst z SAR-0034), 2) wyszukać i dołączyć konkretne zapisy prawne krajowe/ustawowe powiązane z obowiązkiem zgłaszania SAR, lub 3) spróbować uzupełnić brakujące specyfikacje techniczne (należałoby przeszukać repozytoria IT/OPS banku).

**Ocena:** dobra — Odpowiedź Agenta kompleksowo i zgodnie z oczekiwaniami opisuje przetwarzanie wniosku wysokiego ryzyka AML oraz uwzględnia wymogi ochrony danych i zakaz tipping-off, zgodnie z kluczowymi politykami i przykładami.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['DC-2250', 'KYC-00129', 'KYC-00456', 'POL-AML-01', 'POL-DANE-01', 'POL-RYZYKO-01', 'SAR-0052']; w odpowiedzi ['KYC-00456', 'POL-AML-01', 'POL-DANE-01', 'RR-0012', 'SAR-0034']; pokrycie 0.43

---

## [P3.10] (zestaw 3) 🟡 czesciowa
**Pytanie:** Zbuduj pełną mapę powiązań węzła TO-2025-Q1 — wskaż wszystkie dokumenty, które z niego korzystają, i wyjaśnij, dlaczego jest to „wspólny węzeł" istotny dla spójności zbioru.

**Oczekiwana:** - TO-2025-Q1 jest przywoływana przez: REG-KH-02, REG-KG-01, REG-LE-04, REG-KK-03 (regulaminy), DC-2201, DC-2202, DC-2203, DC-2204 (decyzje), UM-7788, UM-7789, UM-7790, UM-7791 (umowy), HS-7788, HS-7789, HS-7790 (harmonogramy), WN-4502, WN-4503, WN-4504 (wnioski).
  - Ustala wspólną wartość NRR 3M (5,85%) i marże/stopy dla wielu produktów — jej zmiana (TO-2025-Q2) propaguje się na oprocentowanie umów o stopie zmiennej (repricing hipoteki, HS-7794).
  - Dlatego jest kluczowa dla spójności liczbowej całego zbioru.

**Odpowiedź agenta:** Oto pełna mapa powiązań węzła TO-2025-Q1, oparta na grafie i dokumentach wskazanych w zadaniu.

1) Lista dokumentów powołujących się na TO-2025-Q1 (ID + typ)
- DC-2201 (decyzja/ dokument decyzji) (źródło: graf)  
- DC-2202 (decyzja/ dokument decyzji) (źródło: graf)  
- WN-4504 (wniosek kredytowy) (źródło: graf)  
- WN-4508 (wniosek kredytowy) (źródło: graf, REG-KG-01)  
- POL-RYZYKO-01 (polityka ryzyka) (źródło: graf)  
- REG-LE-04 (regulamin / regulacja prawna) (źródło: graf)  
- UM-7788 (umowa kredytu hipotecznego) (źródło: UM-7788, graf)  
- UM-7789 (umowa kredytu gotówkowego) (źródło: UM-7789, graf)  
- HS-7788 (harmonogram spłat, załącznik do UM-7788) (źródło: UM-7788, graf)  
- HS-7789 (harmonogram spłat, załącznik do UM-7789) (źródło: UM-7789, graf)  
- TOP-2025-Q1 (tabela opłat/prowizji / dokument powiązany) (źródło: graf)  
- REG-KH-02 (regulamin produktu kredytu hipotecznego) (źródło: REG-KH-02)  
- REG-KG-01 (regulamin produktu kredytu gotówkowego) (źródło: REG-KG-01)

2) Krótki opis relacji każdego dokumentu do TO-2025-Q1 (1–2 zdania każdy)
- DC-2201 / DC-2202: decyzje kredytowe powołują wartości i reguły z TO-2025-Q1 jako podstawę do określenia warunków oprocentowania (źródło: graf).  
- WN-4504 / WN-4508: wnioski kredytowe wykorzystują parametry z TO-2025-Q1 do określenia proponowanych stawek/opcji produktowych (źródło: graf).  
- POL-RYZYKO-01: polityka ryzyka odnosi się do wskaźników i progu wymagań, które są powiązane z wartościami i klasyfikacją z TO-2025-Q1 (źródło: graf).  
- REG-LE-04: regulacja prawna wskazuje TO-2025-Q1 jako obowiązującą tabelę odniesienia dla naliczeń określonych w przepisach wewnętrznych (źródło: graf).  
- UM-7788: umowa hipoteczna odwołuje się bezpośrednio do TO-2025-Q1 dla ustalenia NRR 3M i obliczenia oprocentowania zmiennego (NRR 3M + marża) (źródło: UM-7788, REG-KH-02).  
- UM-7789: umowa gotówkowa odwołuje się do TO-2025-Q1 dla ustalenia stopy stałej kredytu określonej w tabeli (źródło: UM-7789, REG-KG-01).  
- HS-7788 / HS-7789: harmonogramy spłat są powiązane z umowami, a więc pośrednio z parametrami oprocentowania pochodzącymi z TO-2025-Q1 (źródło: UM-7788, UM-7789).  
- TOP-2025-Q1: dokument zbiorczy (tabela opłat/prowizji) współdzieli strukturę odniesień z TO-2025-Q1 i jest stosowany wspólnie z nim przy kalkulacji kosztów (źródło: graf).  
- REG-KH-02: regulamin kredytu hipotecznego opisuje regułę: oprocentowanie = NRR 3M + marża oraz że NRR 3M określa tabela TO-2025-Q1 (źródło: REG-KH-02).  
- REG-KG-01: regulamin kredytu gotówkowego odsyła do TO-2025-Q1 dla stawek stałego oprocentowania oraz podaje sposób odniesienia do tabeli (źródło: REG-KG-01).

3) Kluczowe atrybuty powiązane z TO-2025-Q1 (wartości i reguły)
- Wartość NRR 3M dla I kwartału 2025: 5,85% (explicitnie cytowane w UM-7788 jako NRR 3M = 5,85%) (źródło: UM-7788).  
- Przykładowa marża użyta w UM-7788: 2,10% (UM-7788) — razem daje oprocentowanie nominalne 7,95% (źródło: UM-7788).  
- Przykładowa stopa stała w UM-7789: 10,90% (UM-7789).  
- Reguła naliczania oprocentowania zmiennego: oprocentowanie = NRR 3M + marża; aktualizacja kwartalna wg wartości NRR z ostatniego dnia roboczego poprzedniego kwartału; zmiana NRR nie wymaga aneksu (źródło: REG-KH-02, UM-7788).  
- Reguły i odwołania do TO-2025-Q1 dla opłat/prowizji są skonsolidowane z TOP-2025-Q1 (źródło: graf, REG-KG-01).

4) Dlaczego TO-2025-Q1 jest „wspólnym węzłem” istotnym dla spójności zbioru (3–5 punktów)
- Centralne odniesienie finansowe: TO-2025-Q1 dostarcza referencyjne stawki (NRR, stopy stałe), które są wykorzystywane przez umowy, decyzje i wnioski; bez jednego źródła odniesienia spójność stawek byłaby zagrożona (źródła: UM-7788, UM-7789, REG-KH-02).  
- Standaryzacja zasad wyliczeń: reguła „oprocentowanie = NRR 3M + marża” i kwartalna aktualizacja definiowana w regulaminach zapewnia jednolity mechanizm aktualizacji stawek w całym zbiorze dokumentów (źródło: REG-KH-02).  
- Powiązanie procesowe: TO-2025-Q1 łączy etapy procesów kredytowych — wniosek → decyzja → umowa → harmonogram — zapewniając, że te dokumenty odnoszą się do tej samej definicji stawek (źródła: graf, UM-7788).  
- Konsystencja regulacyjna i ryzyka: polityki i regulaminy (POL-RYZYKO-01, REG-LE-04, REG-KH-02, REG-KG-01) powołują się na TO-2025-Q1, co ułatwia zgodność z wewnętrznymi zasadami i oceną ryzyka (źródła: graf, REG-KH-02).  
- Użyteczność analityczna: scentralizowane dane (NRR, stopy, marże) w jednym węźle upraszczają raportowanie, audyt i kontrolę jakości danych finansowych (źródła: UM-7788, UM-7789, TOP-2025-Q1).

5) Luki i rekomendacje do grafu
- Luka: brak jednoznacznie wskazanych dat obowiązywania tabeli TO-2025-Q1 oraz dat fixingów NRR w dostępnych fragmentach (brak w UM-7788/REG-KH-02 fragmentu z datą początku obowiązywania tabeli) (źródła: UM-7788, REG-KH-02 — brak dat).  
- Rekomendacja: dodać do grafu atrybuty czasowe dla TO-2025-Q1 — data początku obowiązywania tabeli, data źródłowego fixing'u NRR (np. data ostatniego dnia roboczego poprzedniego kwartału) oraz powiązania czasowe (valid_from/valid_to) do dokumentów umownych i decyzji, które używają danej wersji tabeli (zalecane źródła do uzupełnienia: TO-2025-Q1, DC-2201, DC-2202, UM-7788, UM-7789).

Weryfikacja i zapis do grafu
- Proponowana mapa powiązań została zweryfikowana (weryfikator: POTWIERDZONA) w oparciu o graf i fragmenty dokumentów (werdykt: POTWIERDZONA).  
- Zweryfikowany fakt i wskazówka jakościowa zostały zapisane do grafu (ID zapisu faktu: learned::adda85b4a38df5b2; ID zapisu wskazówki: learning::adda85b4a38df5b2).

Cytowane źródła
- Graf relacji (połączenia węzła TO-2025-Q1): DC-2201, DC-2202, WN-4504, WN-4508, POL-RYZYKO-01, REG-LE-04, UM-7788, UM-7789, HS-7788, HS-7789, TOP-2025-Q1, REG-KH-02, REG-KG-01  
- Dokumenty (fragmenty): REG-KH-02 (§3), REG-KG-01 (§4), UM-7788 (§3 — NRR 3M = 5,85%, marża = 2,10%), UM-7789 (§3 — oprocentowanie stałe = 10,90%).

Jeżeli chcesz, mogę:
- wyeksportować mapę powiązań w formacie CSV/JSON (lista relacji i atrybutów),  
- przeszukać TO-2025-Q1 w poszukiwaniu dat obowiązywania i szczegółów fixingów oraz dodać je do grafu.

**Ocena:** czesciowa — Agent poprawnie wskazał większość dokumentów przywołujących TO-2025-Q1 i omówił jego kluczową rolę dla spójności zbioru, lecz lista dokumentów zawiera dodatkowe pozycje nieobecne w odpowiedzi oczekiwanej (np. POL-RYZYKO-01, WN-4508, TOP-2025-Q1) oraz pomija kilka dokumentów obecnych w odpowiedzi oczekiwanej (np. DC-2203, DC-2204, UM-7790, UM-7791, HS-7790, WN-4502, WN-4503), co częściowo obniża zgodność merytoryczną mapy powiązań.

**Zdarzenia:** odpytuję pamięć GRAFOWĄ (Neo4j) → nie znaleziono w pamięci/grafie → przeszukuję DOKUMENTY → formułuję odpowiedź → WERYFIKUJĘ odpowiedź w dokumentach → odpytuję pamięć GRAFOWĄ (Neo4j)

**Źródła:** oczekiwane ['HS-7794', 'TO-2025-Q1', 'TO-2025-Q2']; w odpowiedzi ['DC-2201', 'DC-2202', 'HS-7788', 'HS-7789', 'POL-RYZYKO-01', 'REG-KG-01', 'REG-KH-02', 'REG-LE-04', 'TO-2025-Q1', 'TOP-2025-Q1', 'UM-7788', 'UM-7789', 'WN-4504', 'WN-4508']; pokrycie 0.33

---
