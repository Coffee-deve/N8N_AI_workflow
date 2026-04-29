README: System automatyzacji obsługi zgłoszeń (AI-Powered Workflow)
Ten projekt to prototyp systemu automatyzacji w n8n, który segreguje przychodzące zgłoszenia klientów, analizuje je przy pomocy modelu AI (Gemini) i podejmuje odpowiednie akcje w zależności od priorytetu.

Jak uruchomić rozwiązanie
Import workflow: Zaimportuj dostarczony plik .json do swojej instancji n8n.

Konfiguracja poświadczeń (Credentials):

Google Sheets: Utwórz poświadczenia Google Sheets OAuth2 API. Upewnij się, że Twoje konto Google ma dostęp do API arkuszy i odpowiednie uprawnienia (scopes).

Gmail: Skonfiguruj poświadczenia Gmail OAuth2 API. Jest to wymagane do wysyłki powiadomień.

Google Gemini: Skonfiguruj węzeł Google Gemini Chat Model, wklejając swój klucz API wygenerowany w Google AI Studio.

Dostosowanie arkusza:

Workflow jest wstępnie skonfigurowany pod konkretny ID arkusza Google Sheets. Pamiętaj, aby w węzłach "Google Sheets" zmienić ID arkusza (documentId) na własny dokument, do którego masz dostęp.

Uruchomienie:

Workflow jest skonfigurowany do uruchomienia ręcznego (Manual Trigger).

Po kliknięciu "Execute Workflow", system najpierw sprawdzi strukturę arkusza, a następnie wygeneruje 5 testowych zgłoszeń, przeanalizuje je przez AI, zapisze wyniki w arkuszu oraz wyśle e-mail w przypadku priorytetu "Wysoki".

Nieoczywiste wymagania i uwagi
Uprawnienia Google OAuth2: Najczęstszym problemem przy uruchamianiu węzłów Google jest brak odpowiednich zakresów (scopes) w konsoli Google Cloud. Upewnij się, że podczas tworzenia poświadczeń w n8n dodałeś uprawnienia zarówno do Spreadsheets, jak i Gmail.

Struktura danych w arkuszu: Workflow zakłada, że arkusz jest pusty lub posiada określoną strukturę nagłówków. Węzeł "Code to initialize the table" zapewnia bazową strukturę, ale jeśli arkusz nie jest czysty, może dojść do błędów przy dopisywaniu danych.

Limity API: Użycie modelu Gemini wiąże się z limitami zapytań (Rate Limits). Jeśli planujesz przetwarzać setki zgłoszeń naraz, upewnij się, że Twój plan w Google AI Studio na to pozwala.

Wysyłka e-mail: Węzeł Gmail wymaga, aby Twoje konto było skonfigurowane tak, aby n8n mogło wysyłać maile w Twoim imieniu (często wymaga to dodania adresu e-mail jako "Test user" w konsoli Google Cloud, jeśli aplikacja nie została zweryfikowana).