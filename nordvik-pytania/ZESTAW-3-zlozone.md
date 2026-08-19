# ZESTAW 3 — pytania złożone (odpowiedź z wielu dokumentów)

Pytania, których odpowiedź jest **złożona** i wymaga syntezy informacji z **wielu
dokumentów**, często z obliczeniami, porównaniami i rozumowaniem. Test najtrudniejszy.

---

**P3.1.** Prześledź kompletny łańcuch kredytu hipotecznego Anny Kowalskiej — od profilu klienta do harmonogramu — i zweryfikuj spójność kluczowych liczb.
- **Oczekiwana odpowiedź (skrót):**
  - Łańcuch: KYC-00123 → WN-4501 → (załącznik ZD-4501) → DC-2201 → UM-7788 → HS-7788.
  - Klient klasy B (scoring 78), dochód netto 10 100 PLN (ZD-4501).
  - Kredyt 480 000 PLN, nieruchomość warta 600 000 PLN → **LTV 80%**; wkład własny 120 000 PLN.
  - Oprocentowanie 7,95% (NRR 3M 5,85% + marża 2,10%, TO-2025-Q1); **rata 3 688,83 PLN** na 300 mies.
  - **DTI 36,52%** (3 688,83 / 10 100) < limit 45% (POL-RYZYKO-01) → decyzja pozytywna.
  - Prowizja 9 600 PLN (2%, TOP-2025-Q1), RRSO 8,50%, suma odsetek 626 649,94 PLN.
  - Liczby są spójne w całym łańcuchu.
- **Dokumenty źródłowe:** KYC-00123, ZD-4501, WN-4501, DC-2201, UM-7788, HS-7788, POL-RYZYKO-01, REG-KH-02, TO-2025-Q1, TOP-2025-Q1

**P3.2.** Wyjaśnij, w jaki sposób działania compliance doprowadziły do odmowy kredytu Markowi Nowickiemu — od transakcji do decyzji. Wskaż całą sekwencję.
- **Oczekiwana odpowiedź (skrót):**
  - Rachunek firmowy (HT-00456) wykazał wpłaty gotówkowe rozbijane poniżej progu 15 000 PLN (structuring) i szybkie transfery ~464 950 PLN do Vantia (pass-through).
  - Powstały zgłoszenia SAR-0034 (structuring) i SAR-0041 (pass-through), oba na podstawie POL-AML-01.
  - Raport ryzyka RR-0012 zagregował oba SAR-y i rekomendował klasę E oraz wstrzymanie nowych kredytów.
  - Kartę KYC-00456 zaktualizowano do klasy E (WYSOKIE), wdrożono EDD.
  - Kolejny wniosek WN-4508 (kredyt 80 000 PLN) otrzymał decyzję **negatywną DC-2250** — mimo DTI 16,20% — z powodu klasy E i braku możliwości ustalenia źródła środków.
  - To pełna pętla zwrotna: transakcje → ryzyko → odmowa.
- **Dokumenty źródłowe:** HT-00456, SAR-0034, SAR-0041, POL-AML-01, RR-0012, KYC-00456, WN-4508, DC-2250, POL-RYZYKO-01

**P3.3.** Porównaj trzy typy decyzji kredytowych w zbiorze (pozytywną, warunkową, negatywną) i wskaż, jak profil ryzyka z KYC oraz polityki determinowały wynik każdej z nich.
- **Oczekiwana odpowiedź (skrót):**
  - **Pozytywna — DC-2201** (Anna Kowalska): klasa B, DTI 36,52%, LTV 80% — wszystkie kryteria POL-RYZYKO-01 spełnione → udzielenie kredytu.
  - **Warunkowa — DC-2203** (Bałtyk Logistyka): klasa C przy podwyższonym zadłużeniu → zgoda pod warunkiem opłaty wstępnej 30% lub dodatkowego zabezpieczenia (POL-RYZYKO-01 §5).
  - **Negatywna — DC-2250** (Marek Nowicki): zdolność wystarczająca (DTI 16,20%), ale klasa E z RR-0012 (AML) → odmowa (POL-RYZYKO-01 §5, POL-AML-01).
  - Wniosek: o wyniku decydował nie tylko wskaźnik finansowy, lecz klasa ryzyka (w tym override z tytułu AML).
- **Dokumenty źródłowe:** DC-2201, DC-2203, DC-2250, KYC-00123, KYC-00125, KYC-00456, RR-0012, POL-RYZYKO-01, POL-AML-01

**P3.4.** Oblicz łączną kwotę odsetek dla wszystkich kredytów/leasingów z zawartymi umowami w zbiorze i podaj źródła.
- **Oczekiwana odpowiedź:**
  - Kredyt hipoteczny UM-7788: odsetki 626 649,94 PLN wg pierwotnego HS-7788 (lub 579 719,78 PLN po repricingu wg HS-7794, przy założeniu utrzymania 7,45%).
  - Kredyt gotówkowy UM-7789: odsetki 15 077,76 PLN (HS-7789).
  - Leasing UM-7790: część odsetkowa 28 169,56 PLN netto (HS-7790).
  - **Suma (wariant pierwotny hipoteki):** 626 649,94 + 15 077,76 + 28 169,56 = **669 897,26 PLN**.
  - (Uwaga: umowa karty UM-7791 nie ma z góry ustalonych odsetek — zależą od wykorzystania limitu; wniosek WN-4508 odrzucono, więc go nie liczymy.)
- **Dokumenty źródłowe:** UM-7788/HS-7788/HS-7794, UM-7789/HS-7789, UM-7790/HS-7790

**P3.5.** Opisz mechanizm i finansowy skutek zmiany wskaźnika NRR 3M dla kredytu hipotecznego — wskaż dokumenty i kwoty.
- **Oczekiwana odpowiedź (skrót):**
  - NRR 3M spadł z 5,85% (TO-2025-Q1) do 5,35% (TO-2025-Q2), tj. o 0,50 p.p.
  - Zgodnie z REG-KH-02 §3 (oprocentowanie zmienne, aktualizacja kwartalna, marża stała), oprocentowanie UM-7788 zmieniło się z 7,95% na 7,45% bez aneksu.
  - Bank sporządził zaktualizowany harmonogram HS-7794 (od raty nr 2): rata spadła z 3 688,83 na **3 531,88 PLN** (o 156,95 PLN).
  - Łączne odsetki spadły z 626 649,94 do 579 719,78 PLN (oszczędność ok. 46 930,16 PLN przy utrzymaniu 7,45%).
  - Efekt widoczny na wyciągu HT-00123 (rata 1 = 3 688,83, raty 2–3 = 3 531,88).
- **Dokumenty źródłowe:** TO-2025-Q1, TO-2025-Q2, REG-KH-02, UM-7788, HS-7788, HS-7794, HT-00123

**P3.6.** Zidentyfikuj wszystkich klientów objętych wzmożonymi środkami bezpieczeństwa (EDD) i opisz podstawę oraz skutki dla ich klasy ryzyka.
- **Oczekiwana odpowiedź:**
  - **KL-00456 (Marek Nowicki):** EDD z powodu SAR-0034 i SAR-0041 → RR-0012; klasa ryzyka podniesiona z C do **E**; wstrzymanie nowych kredytów (skutek: odmowa DC-2250).
  - **KL-00129 (Bursztyn Handel Sp. z o.o.):** EDD z powodu SAR-0052 (nietypowe wpłaty gotówkowe + transakcje z podmiotem powiązanym); klasa ryzyka podniesiona z C do **D**; nowe zaangażowania warunkowe/wstrzymane.
  - Obaj objęci zakazem tipping-off (POL-AML-01 §7).
- **Dokumenty źródłowe:** KYC-00456, SAR-0034, SAR-0041, RR-0012, KYC-00129, SAR-0052, POL-AML-01

**P3.7.** Które tabele oprocentowania i opłat obowiązują dla poszczególnych umów, biorąc pod uwagę daty ich zawarcia i zasady aktualizacji?
- **Oczekiwana odpowiedź (skrót):**
  - Umowy zawarte w I kw. 2025 (UM-7788 z 14.02, UM-7789 z 05.03, UM-7790 z 20.03, UM-7791 z 12.03) bazują na TO-2025-Q1 i TOP-2025-Q1.
  - Kredyty stałoprocentowe (gotówkowy UM-7789) i leasing (UM-7790) zachowują stopę z dnia zawarcia.
  - Kredyt hipoteczny UM-7788 (zmienny) jest repricowany od Q2 wg TO-2025-Q2 (nowy harmonogram HS-7794).
  - Wniosek WN-4506 (10.05.2025, Q2) bazuje na TO-2025-Q2 i TOP-2025-Q2.
- **Dokumenty źródłowe:** UM-7788/7789/7790/7791, WN-4506, TO-2025-Q1, TO-2025-Q2, TOP-2025-Q1, TOP-2025-Q2, REG-KH-02, REG-KG-01

**P3.8.** Sprawdź spójność danych osobowych i finansowych klientki KL-00124 we wszystkich dokumentach, w których występuje.
- **Oczekiwana odpowiedź:**
  - Katarzyna Maria Lewandowska, PESEL 90111067321 — identyczne w KYC-00124, ZD-4503, WN-4502, UM-7789.
  - Dochód netto 8 200 PLN — spójny w ZD-4503, WN-4502, DC-2202.
  - Kredyt 50 000 PLN / 60 mies / 10,90% / rata 1 084,63 PLN — spójny w WN-4502, DC-2202, UM-7789, HS-7789.
  - Klasa ryzyka A (scoring 92) — KYC-00124, potwierdzona w DC-2202.
  - Brak sprzeczności.
- **Dokumenty źródłowe:** KYC-00124, ZD-4503, WN-4502, DC-2202, UM-7789, HS-7789

**P3.9.** Na podstawie polityk banku opisz, jak przetwarzany jest wniosek klienta wysokiego ryzyka AML oraz jakie ograniczenia praw wynikają z zasad ochrony danych.
- **Oczekiwana odpowiedź (skrót):**
  - Ocena ryzyka i klasyfikacja: POL-RYZYKO-01 (klasy A–E, override jakościowy) w powiązaniu z POL-AML-01 (CDD/EDD, monitoring, SAR).
  - Dla klienta wysokiego ryzyka: wzmożone środki (EDD), ustalenie źródła środków, możliwe wstrzymanie nowych usług i blokady; zakaz tipping-off.
  - RODO (POL-DANE-01): przetwarzanie na podstawie obowiązku prawnego (AML) — prawo do usunięcia i sprzeciwu NIE ma zastosowania do dokumentacji AML; okresy przechowywania wynikają z przepisów AML.
  - Przykład zastosowania: KL-00456/DC-2250 oraz KL-00129/SAR-0052.
- **Dokumenty źródłowe:** POL-RYZYKO-01, POL-AML-01, POL-DANE-01, KYC-00456, DC-2250, KYC-00129, SAR-0052

**P3.10.** Zbuduj pełną mapę powiązań węzła TO-2025-Q1 — wskaż wszystkie dokumenty, które z niego korzystają, i wyjaśnij, dlaczego jest to „wspólny węzeł" istotny dla spójności zbioru.
- **Oczekiwana odpowiedź (skrót):**
  - TO-2025-Q1 jest przywoływana przez: REG-KH-02, REG-KG-01, REG-LE-04, REG-KK-03 (regulaminy), DC-2201, DC-2202, DC-2203, DC-2204 (decyzje), UM-7788, UM-7789, UM-7790, UM-7791 (umowy), HS-7788, HS-7789, HS-7790 (harmonogramy), WN-4502, WN-4503, WN-4504 (wnioski).
  - Ustala wspólną wartość NRR 3M (5,85%) i marże/stopy dla wielu produktów — jej zmiana (TO-2025-Q2) propaguje się na oprocentowanie umów o stopie zmiennej (repricing hipoteki, HS-7794).
  - Dlatego jest kluczowa dla spójności liczbowej całego zbioru.
- **Dokumenty źródłowe:** TO-2025-Q1 (+ dokumenty wymienione powyżej), TO-2025-Q2, HS-7794
