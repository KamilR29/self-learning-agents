# Nordvik Finanse S.A. — syntetyczny zbiór dokumentów (mapa zbioru)

> **Uwaga:** Wszystkie dane (osoby, PESEL, IBAN, adresy, kwoty, nazwy firm) są
> **całkowicie fikcyjne i testowe**. Nordvik Finanse S.A. to instytucja zmyślona
> na potrzeby testów agenta AI (multi-hop retrieval). Jakakolwiek zbieżność z
> rzeczywistymi podmiotami jest przypadkowa.

Docelowo zbiór liczy **50 dokumentów**. Poniżej pełna, planowana lista 50 ID z
typami i głównymi powiązaniami. Dokumenty oznaczone **[✔ PARTIA 1]** zostały już
wygenerowane (kompletny łańcuch nr 1 + węzły referencyjne). Pozostałe powstaną w
kolejnych partiach.

## Legenda schematu ID
`KL/KYC-00XXX` klient · `WN-XXXX` wniosek · `DC-XXXX` decyzja · `UM-XXXX` umowa ·
`HS-XXXX` harmonogram · `REG-[PRODUKT]-XX` regulamin · `TOP-YYYY-QX` tabela opłat ·
`TO-YYYY-QX` tabela oprocentowania · `POL-[OBSZAR]-XX` polityka · `SAR-XXXX` zgłoszenie AML ·
`RR-XXXX` raport ryzyka · `ZD-XXXX` zaświadczenie o dochodach · `HT-00XXX` historia transakcji.

## PARTIA 1 — łańcuch nr 1 (kredyt hipoteczny) + węzły referencyjne

| # | ID | Typ | Główne powiązania |
|---|----|-----|-------------------|
| 1/50 | KYC-00123 | Profil klienta / karta KYC (klient KL-00123) | ← WN-4501, DC-2201, UM-7788 |
| 2/50 | ZD-4501 | Zaświadczenie o dochodach | → KL-00123; załącznik do WN-4501 |
| 3/50 | WN-4501 | Wniosek — kredyt hipoteczny | → KL-00123, ZD-4501; ← DC-2201 |
| 4/50 | POL-RYZYKO-01 | Polityka ryzyka kredytowego | ← DC-2201, REG-KH-02 |
| 5/50 | REG-KH-02 | Regulamin kredytu hipotecznego „Nordvik Dom" | → POL-RYZYKO-01; ← DC-2201, UM-7788 |
| 6/50 | TO-2025-Q1 | Tabela oprocentowania Q1 2025 | ← UM-7788, DC-2201 |
| 7/50 | TOP-2025-Q1 | Tabela opłat i prowizji Q1 2025 | ← UM-7788 |
| 8/50 | DC-2201 | Decyzja kredytowa (pozytywna) | → WN-4501, KYC-00123, POL-RYZYKO-01, REG-KH-02, TO-2025-Q1 |
| 9/50 | UM-7788 | Umowa kredytu hipotecznego | → DC-2201, REG-KH-02, TO-2025-Q1, TOP-2025-Q1, KYC-00123 |
| 10/50 | HS-7788 | Harmonogram spłat | → UM-7788, TO-2025-Q1 |

**Łańcuch nr 1 (głębokość 6):**
`KL-00123 → WN-4501 → ZD-4501 → DC-2201 (→ POL-RYZYKO-01, REG-KH-02) → UM-7788 (→ TO-2025-Q1, TOP-2025-Q1) → HS-7788`

## PARTIA 2 — łańcuch nr 2 (compliance / relacja zwrotna) + węzły referencyjne

| # | ID | Typ | Główne powiązania |
|---|----|-----|-------------------|
| 11/50 | KYC-00456 | Profil klienta / KYC (klient KL-00456) — po aktualizacji ryzyka | ← HT-00456, SAR-0034, SAR-0041, RR-0012, WN-4508, DC-2250 |
| 12/50 | POL-AML-01 | Polityka AML/CFT | ← SAR-0034, SAR-0041, RR-0012, DC-2250 |
| 13/50 | REG-KG-01 | Regulamin kredytu gotówkowego „Nordvik Gotówka" | → TO-2025-Q1, TOP-2025-Q1; ← WN-4508, DC-2250 |
| 14/50 | HT-00456 | Historia transakcji (rachunek firmowy) | → KL-00456; ← SAR-0034, SAR-0041, RR-0012 |
| 15/50 | SAR-0034 | Zgłoszenie SAR (structuring) | → HT-00456, POL-AML-01, KYC-00456 |
| 16/50 | SAR-0041 | Zgłoszenie SAR (pass-through) | → HT-00456, POL-AML-01, SAR-0034 |
| 17/50 | RR-0012 | Raport ryzyka klienta | → SAR-0034, SAR-0041, HT-00456, POL-AML-01, POL-RYZYKO-01, KYC-00456 |
| 18/50 | ZD-4508 | Zaświadczenie o dochodach z działalności | → KL-00456; załącznik do WN-4508 |
| 19/50 | WN-4508 | Wniosek — kredyt gotówkowy | → KL-00456, ZD-4508, REG-KG-01, TO-2025-Q1, TOP-2025-Q1 |
| 20/50 | DC-2250 | Decyzja kredytowa (NEGATYWNA) | → WN-4508, KYC-00456, RR-0012, POL-AML-01, POL-RYZYKO-01 |

**Łańcuch nr 2 (głębokość 6, z relacją zwrotną):**
`HT-00456 → SAR-0034 + SAR-0041 (→ POL-AML-01) → RR-0012 → aktualizacja KYC-00456 (ryzyko → WYSOKIE, klasa E) → WN-4508 → DC-2250 (NEGATYWNA)`

Relacja zwrotna: zgłoszenia SAR i raport ryzyka podwyższają klasę ryzyka klienta
(KYC-00456), co bezpośrednio powoduje odmowę w kolejnej decyzji kredytowej (DC-2250)
mimo wystarczającej zdolności finansowej (DTI 16,20%).

## PARTIA 3 — łańcuch nr 3 (gotówkowy, pozytywny) i łańcuch nr 4 (leasing, warunkowy)

| # | ID | Typ | Główne powiązania |
|---|----|-----|-------------------|
| 21/50 | KYC-00124 | Profil klienta / KYC (klient KL-00124) | ← WN-4502, DC-2202, UM-7789 |
| 22/50 | ZD-4503 | Zaświadczenie o dochodach | → KL-00124; załącznik do WN-4502 |
| 23/50 | WN-4502 | Wniosek — kredyt gotówkowy | → KL-00124, ZD-4503, REG-KG-01, TO-2025-Q1, TOP-2025-Q1 |
| 24/50 | DC-2202 | Decyzja kredytowa (POZYTYWNA) | → WN-4502, KYC-00124, POL-RYZYKO-01, REG-KG-01, TO-2025-Q1 |
| 25/50 | UM-7789 | Umowa kredytu gotówkowego | → DC-2202, REG-KG-01, TO-2025-Q1, TOP-2025-Q1, KYC-00124 |
| 26/50 | HS-7789 | Harmonogram spłat | → UM-7789, TO-2025-Q1 |
| 27/50 | REG-LE-04 | Regulamin leasingu „Nordvik Leasing" | → TO-2025-Q1, TOP-2025-Q1, POL-RYZYKO-01; ← WN-4503, DC-2203 |
| 28/50 | KYC-00125 | Profil klienta / KYC (klient instytucjonalny KL-00125) | ← WN-4503, DC-2203 |
| 29/50 | WN-4503 | Wniosek — leasing pojazdu | → KL-00125, REG-LE-04, TO-2025-Q1, TOP-2025-Q1 |
| 30/50 | DC-2203 | Decyzja leasingowa (WARUNKOWA) | → WN-4503, KYC-00125, POL-RYZYKO-01, REG-LE-04, TO-2025-Q1 |

**Łańcuch nr 3 (głębokość 6, decyzja pozytywna):**
`KL-00124 → WN-4502 → ZD-4503 → DC-2202 (→ POL-RYZYKO-01, REG-KG-01) → UM-7789 (→ TO-2025-Q1, TOP-2025-Q1) → HS-7789`

**Łańcuch nr 4 (głębokość 4, decyzja warunkowa):**
`KL-00125 → WN-4503 (→ REG-LE-04) → DC-2203 (→ POL-RYZYKO-01, TO-2025-Q1) [warunki: opłata wstępna 30% albo poręczenie właściciela + weksel]`

## PARTIA 4 — domknięcie leasingu (łańcuch 4) + karta kredytowa (łańcuch 5) + konto firmowe (łańcuch 6)

| # | ID | Typ | Główne powiązania |
|---|----|-----|-------------------|
| 31/50 | REG-KK-03 | Regulamin karty kredytowej „Nordvik Karta" | → TO-2025-Q1, TOP-2025-Q1, POL-RYZYKO-01; ← WN-4504, DC-2204 |
| 32/50 | UM-7790 | Umowa leasingu operacyjnego | → DC-2203, WN-4503, REG-LE-04, TO-2025-Q1, KYC-00125 |
| 33/50 | HS-7790 | Harmonogram opłat leasingowych | → UM-7790, TO-2025-Q1 |
| 34/50 | KYC-00126 | Profil klienta / KYC (klient KL-00126) | ← WN-4504, DC-2204, UM-7791 |
| 35/50 | WN-4504 | Wniosek — karta kredytowa | → KL-00126, REG-KK-03, TO-2025-Q1, TOP-2025-Q1 |
| 36/50 | DC-2204 | Decyzja kredytowa (POZYTYWNA, karta) | → WN-4504, KYC-00126, POL-RYZYKO-01, REG-KK-03, TO-2025-Q1 |
| 37/50 | UM-7791 | Umowa o kartę kredytową | → DC-2204, REG-KK-03, TO-2025-Q1, TOP-2025-Q1, KYC-00126 |
| 38/50 | KYC-00127 | Profil klienta / KYC (klient instytucjonalny KL-00127) | ← WN-4505, DC-2205 |
| 39/50 | WN-4505 | Wniosek — konto firmowe + limit w rachunku | → KL-00127, TOP-2025-Q1, POL-RYZYKO-01 |
| 40/50 | DC-2205 | Decyzja kredytowa (POZYTYWNA, limit w rachunku) | → WN-4505, KYC-00127, POL-RYZYKO-01, TOP-2025-Q1 |

**Łańcuch nr 4 — DOMKNIĘTY (głębokość 6):**
`KL-00125 → WN-4503 (→ REG-LE-04) → DC-2203 → UM-7790 (→ TO-2025-Q1) → HS-7790`
(warunki DC-2203 spełnione: poręczenie właściciela + weksel, opłata wstępna 20%)

**Łańcuch nr 5 — karta kredytowa (głębokość 4, decyzja pozytywna):**
`KL-00126 → WN-4504 (→ REG-KK-03) → DC-2204 → UM-7791 (→ TO-2025-Q1, TOP-2025-Q1)`

**Łańcuch nr 6 — konto firmowe z limitem (głębokość 3, decyzja pozytywna):**
`KL-00127 → WN-4505 → DC-2205 (→ POL-RYZYKO-01, TOP-2025-Q1)`

## PARTIA 5 (KOŃCOWA) — nowy kwartał, repricing hipoteki, ostatni klienci i SAR

| # | ID | Typ | Główne powiązania |
|---|----|-----|-------------------|
| 41/50 | TO-2025-Q2 | Tabela oprocentowania Q2 2025 (NRR 3M → 5,35%) | → TO-2025-Q1; ← HS-7794, UM-7788, WN-4506, DC-2206 |
| 42/50 | TOP-2025-Q2 | Tabela opłat i prowizji Q2 2025 | → TOP-2025-Q1; ← WN-4506, DC-2206 |
| 43/50 | POL-DANE-01 | Polityka ochrony danych osobowych (RODO) | ← regulaminy i karty KYC |
| 44/50 | HT-00123 | Historia transakcji (rachunek osobisty KL-00123) | → KL-00123, UM-7788, HS-7788, HS-7794 |
| 45/50 | HS-7794 | Zaktualizowany harmonogram hipoteki (po zmianie NRR 3M) | → UM-7788, HS-7788, TO-2025-Q2, REG-KH-02 |
| 46/50 | KYC-00128 | Profil klienta / KYC (klient KL-00128) | ← WN-4506, DC-2206 |
| 47/50 | WN-4506 | Wniosek — kredyt gotówkowy | → KL-00128, REG-KG-01, TO-2025-Q2, TOP-2025-Q2 |
| 48/50 | DC-2206 | Decyzja kredytowa (POZYTYWNA) | → WN-4506, KYC-00128, POL-RYZYKO-01, REG-KG-01, TO-2025-Q2 |
| 49/50 | KYC-00129 | Profil klienta / KYC (klient instytucjonalny KL-00129, monitorowany) | ← SAR-0052 |
| 50/50 | SAR-0052 | Zgłoszenie SAR (wpłaty gotówkowe / podmiot powiązany) | → KYC-00129, POL-AML-01 |

**Łańcuch nr 7 — repricing hipoteki (relacja zwrotna, między-kwartalna):**
`TO-2025-Q2 (NRR 3M 5,85% → 5,35%) → REG-KH-02 §3 → UM-7788 → HS-7794 (nowa rata 3 531,88; zastępuje HS-7788 od raty 2)` — widoczne także w HT-00123.

**Łańcuch nr 8 — kredyt gotówkowy nowego klienta (decyzja pozytywna):**
`KL-00128 → WN-4506 (→ REG-KG-01, TO-2025-Q2) → DC-2206`

**Łańcuch nr 9 — compliance (relacja zwrotna):**
`SAR-0052 (→ POL-AML-01) → aktualizacja KYC-00129 (ryzyko → PODWYŻSZONE, klasa D, EDD)`

## STATUS ZBIORU: KOMPLETNY — 50/50 dokumentów

Podsumowanie typów (zgodność ze strukturą docelową):
- Klienci/KYC: 8 (KYC-00123, 124, 125, 126, 127, 128, 129, 456)
- Wnioski: 6 (WN-4501, 4502, 4503, 4504, 4505, 4506, 4508 → 7)
- Decyzje: 7 (DC-2201, 2202, 2203, 2204, 2205, 2206, 2250) — pozytywne, warunkowa, negatywna
- Umowy: 4 (UM-7788, 7789, 7790, 7791)
- Harmonogramy: 4 (HS-7788, 7789, 7790, 7794)
- Zaświadczenia: 3 (ZD-4501, 4503, 4508)
- Compliance: 3× SAR (0034, 0041, 0052) + 1× RR (0012)
- Referencyjne: 4 regulaminy (REG-KH-02, KG-01, LE-04, KK-03), 2 tabele oprocentowania (TO-2025-Q1/Q2), 2 tabele opłat (TOP-2025-Q1/Q2), 3 polityki (POL-RYZYKO-01, AML-01, DANE-01), 2 historie transakcji (HT-00123, 00456)

## Mapa relacji (PARTIA 1)

| ID źródłowe | Typ relacji | ID docelowe |
|-------------|-------------|-------------|
| WN-4501 | dotyczy klienta | KL-00123 (KYC-00123) |
| WN-4501 | ma załącznik | ZD-4501 |
| ZD-4501 | dotyczy klienta | KL-00123 |
| DC-2201 | rozstrzyga wniosek | WN-4501 |
| DC-2201 | ocenia profil | KYC-00123 |
| DC-2201 | stosuje politykę | POL-RYZYKO-01 |
| DC-2201 | powołuje regulamin | REG-KH-02 |
| DC-2201 | powołuje warunki cenowe | TO-2025-Q1 |
| REG-KH-02 | odsyła do polityki | POL-RYZYKO-01 |
| UM-7788 | realizuje decyzję | DC-2201 |
| UM-7788 | inkorporuje regulamin | REG-KH-02 |
| UM-7788 | stosuje oprocentowanie | TO-2025-Q1 |
| UM-7788 | stosuje opłaty | TOP-2025-Q1 |
| UM-7788 | zawarta z klientem | KYC-00123 |
| HS-7788 | wykonuje umowę | UM-7788 |
| HS-7788 | oparty o oprocentowanie | TO-2025-Q1 |

## Mapa relacji (PARTIA 2)

| ID źródłowe | Typ relacji | ID docelowe |
|-------------|-------------|-------------|
| HT-00456 | dotyczy klienta | KL-00456 (KYC-00456) |
| SAR-0034 | zgłasza transakcje z | HT-00456 |
| SAR-0034 | stosuje politykę | POL-AML-01 |
| SAR-0034 | dotyczy klienta | KYC-00456 |
| SAR-0041 | zgłasza transakcje z | HT-00456 |
| SAR-0041 | stosuje politykę | POL-AML-01 |
| SAR-0041 | powiązane ze zgłoszeniem | SAR-0034 |
| RR-0012 | agreguje zgłoszenie | SAR-0034 |
| RR-0012 | agreguje zgłoszenie | SAR-0041 |
| RR-0012 | analizuje transakcje | HT-00456 |
| RR-0012 | rekomenduje reklasyfikację | KYC-00456 |
| RR-0012 | stosuje politykę ryzyka | POL-RYZYKO-01 |
| KYC-00456 | zaktualizowany przez | RR-0012 |
| ZD-4508 | dotyczy klienta | KL-00456 |
| WN-4508 | ma załącznik | ZD-4508 |
| WN-4508 | dotyczy produktu | REG-KG-01 |
| WN-4508 | stosuje oprocentowanie | TO-2025-Q1 |
| WN-4508 | stosuje opłaty | TOP-2025-Q1 |
| DC-2250 | rozstrzyga wniosek | WN-4508 |
| DC-2250 | ocenia profil | KYC-00456 |
| DC-2250 | opiera się na raporcie | RR-0012 |
| DC-2250 | stosuje politykę AML | POL-AML-01 |
| DC-2250 | stosuje politykę ryzyka | POL-RYZYKO-01 |

## Mapa relacji (PARTIA 3)

| ID źródłowe | Typ relacji | ID docelowe |
|-------------|-------------|-------------|
| ZD-4503 | dotyczy klienta | KL-00124 |
| WN-4502 | dotyczy klienta | KL-00124 (KYC-00124) |
| WN-4502 | ma załącznik | ZD-4503 |
| WN-4502 | dotyczy produktu | REG-KG-01 |
| WN-4502 | stosuje oprocentowanie | TO-2025-Q1 |
| WN-4502 | stosuje opłaty | TOP-2025-Q1 |
| DC-2202 | rozstrzyga wniosek | WN-4502 |
| DC-2202 | ocenia profil | KYC-00124 |
| DC-2202 | stosuje politykę ryzyka | POL-RYZYKO-01 |
| UM-7789 | realizuje decyzję | DC-2202 |
| UM-7789 | inkorporuje regulamin | REG-KG-01 |
| UM-7789 | stosuje oprocentowanie | TO-2025-Q1 |
| UM-7789 | stosuje opłaty | TOP-2025-Q1 |
| UM-7789 | zawarta z klientem | KYC-00124 |
| HS-7789 | wykonuje umowę | UM-7789 |
| HS-7789 | oparty o oprocentowanie | TO-2025-Q1 |
| REG-LE-04 | odsyła do oprocentowania | TO-2025-Q1 |
| REG-LE-04 | odsyła do polityki | POL-RYZYKO-01 |
| WN-4503 | dotyczy klienta | KL-00125 (KYC-00125) |
| WN-4503 | dotyczy produktu | REG-LE-04 |
| WN-4503 | stosuje oprocentowanie | TO-2025-Q1 |
| DC-2203 | rozstrzyga wniosek | WN-4503 |
| DC-2203 | ocenia profil | KYC-00125 |
| DC-2203 | stosuje politykę ryzyka | POL-RYZYKO-01 |
| DC-2203 | powołuje regulamin | REG-LE-04 |

## Mapa relacji (PARTIA 4)

| ID źródłowe | Typ relacji | ID docelowe |
|-------------|-------------|-------------|
| REG-KK-03 | odsyła do oprocentowania | TO-2025-Q1 |
| REG-KK-03 | odsyła do opłat | TOP-2025-Q1 |
| REG-KK-03 | odsyła do polityki | POL-RYZYKO-01 |
| UM-7790 | realizuje decyzję | DC-2203 |
| UM-7790 | dotyczy przedmiotu z | WN-4503 |
| UM-7790 | inkorporuje regulamin | REG-LE-04 |
| UM-7790 | stosuje oprocentowanie | TO-2025-Q1 |
| UM-7790 | zawarta z klientem | KYC-00125 |
| HS-7790 | wykonuje umowę | UM-7790 |
| HS-7790 | oparty o oprocentowanie | TO-2025-Q1 |
| WN-4504 | dotyczy klienta | KL-00126 (KYC-00126) |
| WN-4504 | dotyczy produktu | REG-KK-03 |
| WN-4504 | stosuje oprocentowanie | TO-2025-Q1 |
| WN-4504 | stosuje opłaty | TOP-2025-Q1 |
| DC-2204 | rozstrzyga wniosek | WN-4504 |
| DC-2204 | ocenia profil | KYC-00126 |
| DC-2204 | stosuje politykę ryzyka | POL-RYZYKO-01 |
| DC-2204 | powołuje regulamin | REG-KK-03 |
| UM-7791 | realizuje decyzję | DC-2204 |
| UM-7791 | inkorporuje regulamin | REG-KK-03 |
| UM-7791 | stosuje oprocentowanie | TO-2025-Q1 |
| UM-7791 | stosuje opłaty | TOP-2025-Q1 |
| UM-7791 | zawarta z klientem | KYC-00126 |
| WN-4505 | dotyczy klienta | KL-00127 (KYC-00127) |
| WN-4505 | stosuje opłaty | TOP-2025-Q1 |
| DC-2205 | rozstrzyga wniosek | WN-4505 |
| DC-2205 | ocenia profil | KYC-00127 |
| DC-2205 | stosuje politykę ryzyka | POL-RYZYKO-01 |

## Mapa relacji (PARTIA 5)

| ID źródłowe | Typ relacji | ID docelowe |
|-------------|-------------|-------------|
| TO-2025-Q2 | zastępuje tabelę | TO-2025-Q1 |
| TOP-2025-Q2 | zastępuje tabelę | TOP-2025-Q1 |
| HS-7794 | aktualizuje harmonogram | HS-7788 |
| HS-7794 | wykonuje umowę | UM-7788 |
| HS-7794 | oparty o oprocentowanie | TO-2025-Q2 |
| HS-7794 | zgodny z regulaminem | REG-KH-02 |
| HT-00123 | dotyczy klienta | KL-00123 (KYC-00123) |
| HT-00123 | pokazuje spłaty umowy | UM-7788 |
| HT-00123 | kwoty zgodne z harmonogramem | HS-7788 |
| HT-00123 | kwoty zgodne z harmonogramem | HS-7794 |
| WN-4506 | dotyczy klienta | KL-00128 (KYC-00128) |
| WN-4506 | dotyczy produktu | REG-KG-01 |
| WN-4506 | stosuje oprocentowanie | TO-2025-Q2 |
| WN-4506 | stosuje opłaty | TOP-2025-Q2 |
| DC-2206 | rozstrzyga wniosek | WN-4506 |
| DC-2206 | ocenia profil | KYC-00128 |
| DC-2206 | stosuje politykę ryzyka | POL-RYZYKO-01 |
| DC-2206 | powołuje regulamin | REG-KG-01 |
| SAR-0052 | dotyczy klienta | KYC-00129 |
| SAR-0052 | stosuje politykę | POL-AML-01 |
| KYC-00129 | zaktualizowany przez | SAR-0052 |
| POL-DANE-01 | reguluje przetwarzanie w | REG-KH-02, REG-KG-01, REG-KK-03, REG-LE-04 |
