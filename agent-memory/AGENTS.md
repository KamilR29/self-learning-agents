# Pamięć agenta — PLAYBOOK (strategie, nie fakty)

To jest pamięć PROCEDURALNA. Fakty (np. kwoty, PESEL) trafiają do grafu wiedzy.
Tutaj zapisujesz WSKAZÓWKI, JAK skuteczniej odpowiadać, aby kolejne pytania szły
lepiej: od czego zaczynać dla danego typu pytania, co zadziałało, co nie,
które podejście/wywołania pomagają, na co uważać.

## O systemie
- Odpowiadam na pytania o dokumenty fikcyjnego banku Nordvik Finanse.
- Fakty opieram na dokumentach/grafie i cytuję ID źródeł.

## Wskazówki (uczą się z każdą interakcją)
- W przypadku pytań o kompletny łańcuch kredytu hipotecznego zawsze szczegółowo przeszukuj dokumenty KYC, wniosku, decyzji, umowy i harmonogramu, zwracając uwagę na wszystkie kluczowe liczby: kwotę, okres, oprocentowanie, prowizję i harmonogram rat.
- Weryfikuj zgodność oprocentowania i prowizji z aktualnymi obowiązującymi wzorcami oraz regulaminami banku.
- W przypadku feedbacku o braku kluczowych liczb w odpowiedzi, natychmiast wyszukuj je i uzupełniaj graf o precyzyjne dane liczbowe oraz dopisuj wskazówki jakościowe dotyczące spójności oraz ryzyka zmian.
- Nie odpowiadaj ponownie na pytanie, jeżeli oceniono odpowiedź jako złą z powodu braku danych, tylko wykonaj kompletne uzupełnienie danych i wskazówek w grafie.

(pusto — dopisywane automatycznie po każdym pytaniu; przykłady: „Pytania o łańcuch
hipoteczny: śledź KYC→WN→ZD→DC→UM→HS; HS-7794 to repricing HS-7788, nie sprzeczność”)
- Wartość wskaźnika NRR 3M w tabeli oprocentowania na I kwartał 2025 wynosi 5,85% i powinna być uwzględniana w odpowiedziach na pytania dotyczące tego wskaźnika.
- Oprocentowanie zmienne w kredytach hipotecznych jest sumą NRR 3M i marży wyznaczonej zgodnie z tabelą oprocentowania.
- Aktualizacja wskaźnika NRR 3M nie wymaga aneksu do umowy, następuje automatycznie wg warunków tabeli TO-2025-Q1.
- Zawsze zaczynaj od zidentyfikowania powiązanych dokumentów umowy i decyzji w grafie relacji, aby szybko ustalić podstawę prawną i kluczowe wskaźniki finansowe.
- Zawsze zaczynaj od szczegółowego porównania kluczowych elementów obu historii transakcji, uwzględniając powiązane dokumenty finansowe i compliance, aby uniknąć pominięcia istotnych danych liczbowych i kontekstowych.
- Zawsze zaczynaj od sprawdzenia dokumentów KYC i decyzji kredytowych powiązanych z danym klientem, a następnie wykorzystaj graf powiązań, aby zweryfikować informacje o klasie ryzyka w dokumentach polityk ryzyka i raportach.
- Zawsze zaczynaj od porównania kluczowych dokumentów historii transakcji w formie grafu, aby szybko zidentyfikować różnice i powiązane skutki compliance.
- Zawsze zaczynaj od bezpośredniego dokumentu wymienionego w pytaniu (tu ZD-4503) i wykorzystaj powiązany graf dokumentów, aby szybko zidentyfikować kluczowe informacje o specyficznych danych finansowych.
- Zawsze zaczynaj od zidentyfikowania i przeanalizowania dokumentu decyzji warunkowej oraz powiązanego umowy, korzystając z grafu powiązań, aby szybko odnaleźć i zweryfikować warunki oraz ich spełnienie.
- W przypadku pytań o zgodność profilu ryzyka klienta z decyzją kredytową, UWZGLĘDNIAJ KONKRETNE DANE z KYC i DC, w szczególności klasyfikację ryzyka, scoring kredytowy oraz wskaźnik DTI i spełnienie kryteriów POL-RYZYKO-01.
  - Dla pytań o zgodność profilu z decyzją zawsze uwzględniać scoring i stan zobowiązań; jeśli brak w grafie to dodać scoring i zobowiązania z DC/KYC.
Dla HS-7788 zweryfikowano zgodność raty annuitetowej (3 688,83 PLN) z UM-7788 i TO-2025-Q1; przy obliczeniach użyto miesięcznej stopy 0,0795/12.
- Feedback: odpowiedź dotycząca DC-2201 oceniona jako częściowa z powodu pominięcia TO-2025-Q1; procedura nauki: zapisz brakujący fakt do grafu i dodaj wskazówkę jakościową.
- W przypadku kompletnego łańcucha hipotecznego zawsze uwzględniać w odpowiedzi profil klienta (klasa, scoring, dochód) oraz wyliczone wskaźniki LTV i DTI; jeśli DTI nie jest jawnie podane, policzyć DTI_inclusive jako stosunek raty nowego kredytu do dochodu i zapisać do grafu.
