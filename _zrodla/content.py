# -*- coding: utf-8 -*-
# Teksty strony mikosokphoto.pl w 6 językach. Firma, adres, NIP, e-mail i telefon są wspólne.

COMPANY = "Mikołaj Sokołowski MikoSokPhoto"
NIP = "8641840005"
EMAIL = "mikosokphoto@gmail.com"
PHONE_HREF = "+48604927086"
PHONE = "+48 604 927 086"
STREET = "ul. Meissnera 6/76"
CITY = "31-457 Kraków"

LANGS = ["pl", "en", "de", "es", "fr", "uk"]
LANG_LABEL = {"pl": "PL", "en": "EN", "de": "DE", "es": "ES", "fr": "FR", "uk": "UA"}
LANG_NAME = {"pl": "Polski", "en": "English", "de": "Deutsch", "es": "Español", "fr": "Français", "uk": "Українська"}

M = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
APPPRIV = 'href="pediatria-leki-prywatnosc.html"'

T = {}

# ---------------------------------------------------------------- POLSKI
T["pl"] = dict(
    nav=["Start", "Pediatria LEKI", "Kontakt", "Polityka prywatności"],
    lang_aria="Język",
    home_title="MikoSokPhoto – Mikołaj Sokołowski",
    home_desc="MikoSokPhoto Mikołaj Sokołowski – Kraków. Dane firmy i kontakt.",
    home_sub="Mikołaj Sokołowski · Kraków",
    logo_alt="Logo MikoSokPhoto",
    contact_title="Kontakt – MikoSokPhoto",
    contact_desc="Dane kontaktowe firmy MikoSokPhoto Mikołaj Sokołowski, Kraków.",
    contact_h1="Kontakt",
    labels=["Firma", "Adres", "NIP", "E-mail", "Telefon"],
    country="Polska",
    priv_title="Polityka prywatności – MikoSokPhoto",
    priv_desc="Polityka prywatności strony i aplikacji MikoSokPhoto.",
    priv_h1="Polityka prywatności",
    priv_date="Obowiązuje od 12 listopada 2026 r.",
    priv=[
        ("1. Administrator danych", f"Administratorem danych osobowych jest Mikołaj Sokołowski, prowadzący działalność gospodarczą pod firmą {COMPANY}, {STREET}, {CITY}, NIP {NIP}. Kontakt w sprawach danych osobowych: {M}."),
        ("2. Zakres polityki", "Polityka dotyczy strony internetowej mikosokphoto.pl oraz aplikacji mobilnych publikowanych przez MikoSokPhoto w sklepie Google Play."),
        ("3. Strona internetowa", "Strona nie używa plików cookies, narzędzi analitycznych ani formularzy. Strona jest hostowana w usłudze GitHub Pages (GitHub, Inc.), która może automatycznie rejestrować techniczne dane połączenia, np. adres IP, w celu zapewnienia bezpieczeństwa i działania usługi. Zasady przetwarzania tych danych przez GitHub opisuje polityka prywatności GitHub."),
        ("4. Kontakt e-mail i telefoniczny", "Jeśli skontaktujesz się z nami e-mailem lub telefonicznie, przetwarzamy dane podane w wiadomości (np. imię, adres e-mail, numer telefonu, treść) wyłącznie w celu odpowiedzi i obsługi sprawy, na podstawie art. 6 ust. 1 lit. f RODO (prawnie uzasadniony interes). Dane przechowujemy przez czas potrzebny do obsługi sprawy, a następnie przez okres przedawnienia ewentualnych roszczeń."),
        ("5. Aplikacje mobilne", f"Aplikacje MikoSokPhoto nie wymagają zakładania konta i nie zbierają danych osobowych, o ile opis danej aplikacji nie stanowi inaczej. Dane wprowadzane do aplikacji przechowywane są lokalnie na urządzeniu użytkownika i nie są przesyłane do administratora. Uprawnienia, o które prosi aplikacja, są wykorzystywane wyłącznie do realizacji jej funkcji. Jeżeli konkretna aplikacja przetwarza dodatkowe dane, informacja o tym znajduje się w tej polityce oraz w sekcji „Bezpieczeństwo danych” na jej stronie w Google Play. Aplikacja Pediatria LEKI ma własną, szczegółową <a {APPPRIV}>politykę prywatności</a>."),
        ("6. Odbiorcy danych", "Dane nie są sprzedawane ani udostępniane podmiotom trzecim w celach marketingowych. Mogą być przekazywane jedynie dostawcom usług technicznych (np. hosting, poczta e-mail) w zakresie niezbędnym do ich świadczenia lub organom uprawnionym na podstawie przepisów prawa."),
        ("7. Twoje prawa", f"Masz prawo do dostępu do swoich danych, ich sprostowania, usunięcia, ograniczenia przetwarzania, przenoszenia danych oraz wniesienia sprzeciwu. Przysługuje Ci także prawo wniesienia skargi do Prezesa Urzędu Ochrony Danych Osobowych (ul. Stawki 2, 00-193 Warszawa). W celu skorzystania z praw napisz na {M}."),
        ("8. Zmiany polityki", "Polityka może być aktualizowana, np. w związku z publikacją nowych aplikacji. Aktualna wersja jest zawsze dostępna na tej stronie."),
    ],
    app_title="Pediatria LEKI – MikoSokPhoto",
    app_desc="Pediatria LEKI – aplikacja szkoleniowa do szybkiego przeliczania dawek leków w pediatrycznych symulacjach medycznych na kursach.",
    app_lead="Aplikacja szkoleniowa do szybkiego przeliczania dawek leków w scenariuszach pediatrycznej symulacji medycznej.",
    app_notice="<strong>Tylko do nauki i symulacji.</strong> Aplikacja służy do ćwiczeń na przypadkach szkoleniowych podczas kursów pediatrycznych. Nie jest przeznaczona do podejmowania decyzji dotyczących rzeczywistych pacjentów i nie została zwalidowana do zastosowań klinicznych.",
    app_sections=[
        ("Do czego służy", [
            "Pediatria LEKI powstała z myślą o kursach i zajęciach symulacyjnych z ratownictwa pediatrycznego. Pozwala uczestnikom i instruktorom w kilka sekund przeliczyć dawki leków, przepływy we wlewach i rozmiary sprzętu dla dziecka lub noworodka z danego scenariusza, tak aby w trakcie ćwiczenia skupić się na postępowaniu, a po nim na omówieniu wyników.",
            "Wystarczy wpisać dane przypadku, a aplikacja pokaże obliczone dawki, rozmiary sprzętu i wartości referencyjne do porównania z decyzjami podjętymi w symulacji."]),
        ("Jak działa", [
            ("Dane przypadku", "masa wpisana ręcznie, szacowana z wieku lub odczytana z długości ciała na taśmie Broselow. Osobny tryb noworodka: masa w gramach, wiek ciążowy i wiek w dniach."),
            ("Szybkie dawki leków", "kafelki z obliczonymi dawkami pogrupowane w zakładki (RKO, ból, oddech, inne), panel RSI z lekami do intubacji oraz szczegóły każdego leku ze schematami dawkowania i źródłami. Aplikacja ostrzega, gdy lek nie jest przeznaczony dla danego wieku lub brakuje danych do obliczenia."),
            ("Parametry życiowe", "normy dla wieku, a u noworodków centyle HR, RR, SBP i MAP."),
            ("Drogi oddechowe i resuscytacja", "rozmiar i głębokość wprowadzenia rurki, energia defibrylacji, proporcje RKO oraz startowe ustawienia respiratora po ROSC."),
            ("Kalkulatory", "pompa infuzyjna (stężenie i prędkość w ml/h) oraz „Przelicz Dawkę” dla dowolnego leku."),
            ("Własny katalog leków", "instruktor może dodać własne leki i kategorie, przypiąć je do szybkich dawek i przenieść katalog na inne urządzenie za pomocą pliku kopii."),
            ("Metodyka, wzory i źródła", "opis sposobu liczenia i źródeł danych (m.in. ChPL, ERC, UK-WHO), przydatny przy omawianiu scenariusza.")]),
        ("Prywatność i działanie offline", [
            f"Aplikacja działa w całości na urządzeniu: bez konta, bez internetu, bez reklam i analityki. Dane przypadku nie są zapisywane ani przesyłane. W ćwiczeniach należy używać wyłącznie danych fikcyjnych. Szczegóły: <a {APPPRIV}>polityka prywatności Pediatria LEKI</a>."]),
        ("Dla kogo", [
            "Dla uczestników i instruktorów kursów pediatrycznych, studentów oraz personelu medycznego ćwiczącego scenariusze symulacyjne. Aplikacja nie jest przeznaczona dla dzieci."]),
        ("Dostępność", [
            "Aplikacja na Androida (wkrótce w Google Play) oraz wersja uruchamiana w przeglądarce. Dostępne języki: polski, angielski, niemiecki, hiszpański, francuski i ukraiński."]),
    ],
    ap_title="Polityka prywatności – Pediatria LEKI",
    ap_desc="Polityka prywatności aplikacji Pediatria LEKI (pl.pediatrialeki.mobile).",
    ap_h1="Polityka prywatności — Pediatria LEKI",
    ap_version="Wersja z 9 listopada 2026 · aplikacja na Androida",
    ap=[
        ("Aplikacja nie zbiera i nie przesyła danych", "Pediatria LEKI działa w całości na urządzeniu: nie wymaga konta, nie korzysta z internetu (nie ma uprawnienia dostępu do sieci), nie zawiera reklam, analityki ani narzędzi śledzących. Wydawca nie otrzymuje żadnych danych osobowych ani danych o zdrowiu."),
        ("Dane przypadku", "Masa, wiek, data urodzenia, wiek ciążowy i długość ciała służą wyłącznie do obliczeń widocznych na ekranie. Nie są zapisywane — znikają po wybraniu „Nowy przypadek” albo po zamknięciu aplikacji. W ćwiczeniach używaj danych fikcyjnych. Nie wpisuj danych osobowych rzeczywistych pacjentów, także w polach tekstowych katalogu."),
        ("Co zostaje na urządzeniu", "W pamięci aplikacji zapisywane są tylko: wybrany język, rozmiar tekstu, własny katalog leków (jeśli go utworzysz) oraz kolejność sortowania katalogu. Dane te nie opuszczają urządzenia i nie trafiają do kopii zapasowej Androida. Odinstalowanie aplikacji lub wyczyszczenie jej danych usuwa je trwale."),
        ("Kopia katalogu w pliku", "Plik kopii powstaje tylko po wybraniu „Zapisz kopię do pliku” i zapisuje się w miejscu wskazanym w systemowym oknie zapisu. Wczytanie kopii odczytuje wyłącznie plik wskazany przez użytkownika. O dalszym losie pliku (przesłanie, usunięcie) decyduje użytkownik."),
        ("Linki do źródeł", "Odnośniki do ChPL, wytycznych i publikacji otwierają się w zewnętrznej przeglądarce. Od tej chwili obowiązują zasady prywatności odwiedzanej strony."),
        ("Uprawnienia i odbiorcy", "Aplikacja nie prosi o żadne uprawnienia systemowe i nie przekazuje danych podmiotom trzecim. Jest przeznaczona do ćwiczeń dla personelu medycznego, nie dla dzieci."),
        ("Zmiany i kontakt", "Nowa wersja polityki pojawi się w aplikacji i pod tym adresem, wraz z datą."),
    ],
    ap_publisher="Wydawca", ap_contact="kontakt",
)

# ---------------------------------------------------------------- ENGLISH
T["en"] = dict(
    nav=["Home", "Pediatria LEKI", "Contact", "Privacy policy"],
    lang_aria="Language",
    home_title="MikoSokPhoto – Mikołaj Sokołowski",
    home_desc="MikoSokPhoto Mikołaj Sokołowski – Kraków, Poland. Company details and contact.",
    home_sub="Mikołaj Sokołowski · Kraków, Poland",
    logo_alt="MikoSokPhoto logo",
    contact_title="Contact – MikoSokPhoto",
    contact_desc="Contact details of MikoSokPhoto Mikołaj Sokołowski, Kraków, Poland.",
    contact_h1="Contact",
    labels=["Company", "Address", "Tax ID (NIP)", "Email", "Phone"],
    country="Poland",
    priv_title="Privacy policy – MikoSokPhoto",
    priv_desc="Privacy policy of the MikoSokPhoto website and apps.",
    priv_h1="Privacy policy",
    priv_date="Effective from 12 November 2026.",
    priv=[
        ("1. Data controller", f"The controller of personal data is Mikołaj Sokołowski, running a business under the name {COMPANY}, {STREET}, {CITY}, Poland, tax ID (NIP) {NIP}. Contact for data protection matters: {M}."),
        ("2. Scope", "This policy covers the website mikosokphoto.pl and the mobile apps published by MikoSokPhoto on Google Play."),
        ("3. Website", "The website does not use cookies, analytics tools or forms. It is hosted on GitHub Pages (GitHub, Inc.), which may automatically log technical connection data, such as IP addresses, to keep the service secure and running. GitHub's processing of this data is described in the GitHub privacy statement."),
        ("4. Email and phone contact", "If you contact us by email or phone, we process the data you provide (e.g. name, email address, phone number, message content) only to reply and handle your matter, on the basis of Art. 6(1)(f) GDPR (legitimate interest). We keep the data for as long as needed to handle the matter and then for the limitation period of any claims."),
        ("5. Mobile apps", f"MikoSokPhoto apps do not require an account and do not collect personal data unless the description of a given app states otherwise. Data entered into the apps is stored locally on the user's device and is not sent to the controller. Any permissions an app requests are used only for its features. If a specific app processes additional data, this is described in this policy and in the “Data safety” section of its Google Play listing. The Pediatria LEKI app has its own detailed <a {APPPRIV}>privacy policy</a>."),
        ("6. Recipients", "Data is not sold or shared with third parties for marketing purposes. It may only be passed to technical service providers (e.g. hosting, email) to the extent necessary to provide their services, or to authorities entitled to it by law."),
        ("7. Your rights", f"You have the right to access, rectify and erase your data, to restrict processing, to data portability and to object. You also have the right to lodge a complaint with the Polish supervisory authority, the President of the Personal Data Protection Office (UODO, ul. Stawki 2, 00-193 Warsaw). To exercise your rights, write to {M}."),
        ("8. Changes", "This policy may be updated, for example when new apps are published. The current version is always available on this page."),
    ],
    app_title="Pediatria LEKI – MikoSokPhoto",
    app_desc="Pediatria LEKI – a training app for fast drug dose calculations in paediatric medical simulation courses.",
    app_lead="A training app for fast drug dose calculations in paediatric medical simulation scenarios.",
    app_notice="<strong>For learning and simulation only.</strong> The app is intended for practising training cases during paediatric courses. It is not intended for making decisions about real patients and has not been validated for clinical use.",
    app_sections=[
        ("What it is for", [
            "Pediatria LEKI was created for paediatric emergency care courses and simulation sessions. It lets participants and instructors calculate drug doses, infusion rates and equipment sizes for the child or newborn in a scenario within seconds, so they can focus on management during the exercise and on reviewing the results afterwards.",
            "Enter the case data and the app shows the calculated doses, equipment sizes and reference values to compare with the decisions made during the simulation."]),
        ("How it works", [
            ("Case data", "weight entered manually, estimated from age or read from body length on a Broselow tape. A separate newborn mode with weight in grams, gestational age and age in days."),
            ("Quick drug doses", "tiles with calculated doses grouped into tabs (CPR, pain, breathing, other), an RSI panel with intubation drugs, and details of each drug with dosing regimens and sources. The app warns when a drug is not intended for the given age or when data needed for the calculation is missing."),
            ("Vital signs", "age-specific normal ranges and, for newborns, HR, RR, SBP and MAP centiles."),
            ("Airway and resuscitation", "tube size and insertion depth, defibrillation energy, CPR ratios and initial ventilator settings after ROSC."),
            ("Calculators", "infusion pump (concentration and rate in ml/h) and “Recalculate dose” for any drug."),
            ("Custom drug catalogue", "instructors can add their own drugs and categories, pin them to quick doses and move the catalogue to another device using a backup file."),
            ("Methodology, formulas and sources", "how the calculations are made and where the data comes from (incl. SmPC, ERC, UK-WHO), useful when debriefing a scenario.")]),
        ("Privacy and offline use", [
            f"The app runs entirely on the device: no account, no internet, no ads or analytics. Case data is neither saved nor sent anywhere. Use only fictional data in exercises. Details: <a {APPPRIV}>Pediatria LEKI privacy policy</a>."]),
        ("Who it is for", [
            "Participants and instructors of paediatric courses, students and medical staff practising simulation scenarios. The app is not intended for children."]),
        ("Availability", [
            "Android app (coming soon to Google Play) and a version that runs in the browser. Languages: Polish, English, German, Spanish, French and Ukrainian."]),
    ],
    ap_title="Privacy policy – Pediatria LEKI",
    ap_desc="Privacy policy of the Pediatria LEKI app (pl.pediatrialeki.mobile).",
    ap_h1="Privacy policy — Pediatria LEKI",
    ap_version="Version of 9 November 2026 · Android app",
    ap=[
        ("The app does not collect or transmit data", "Pediatria LEKI runs entirely on the device: it does not require an account, does not use the internet (it has no network access permission) and contains no ads, analytics or tracking tools. The publisher receives no personal data or health data."),
        ("Case data", "Weight, age, date of birth, gestational age and body length are used only for the calculations shown on screen. They are not saved — they disappear after choosing “New case” or closing the app. Use fictional data in exercises. Do not enter personal data of real patients, including in the catalogue text fields."),
        ("What stays on the device", "The app stores only: the selected language, text size, your custom drug catalogue (if you create one) and the catalogue sort order. This data never leaves the device and is not included in Android backups. Uninstalling the app or clearing its data deletes it permanently."),
        ("Catalogue backup file", "A backup file is created only when you choose “Save backup to file” and is saved in the location you pick in the system save dialog. Loading a backup reads only the file you select. What happens to the file afterwards (sharing, deleting) is up to you."),
        ("Links to sources", "Links to SmPCs, guidelines and publications open in an external browser. From then on, the privacy policy of the visited website applies."),
        ("Permissions and recipients", "The app does not request any system permissions and does not share data with third parties. It is intended for training medical staff, not for children."),
        ("Changes and contact", "A new version of this policy will appear in the app and at this address, together with its date."),
    ],
    ap_publisher="Publisher", ap_contact="contact",
)

# ---------------------------------------------------------------- DEUTSCH
T["de"] = dict(
    nav=["Start", "Pediatria LEKI", "Kontakt", "Datenschutz"],
    lang_aria="Sprache",
    home_title="MikoSokPhoto – Mikołaj Sokołowski",
    home_desc="MikoSokPhoto Mikołaj Sokołowski – Krakau, Polen. Unternehmensdaten und Kontakt.",
    home_sub="Mikołaj Sokołowski · Krakau, Polen",
    logo_alt="Logo MikoSokPhoto",
    contact_title="Kontakt – MikoSokPhoto",
    contact_desc="Kontaktdaten von MikoSokPhoto Mikołaj Sokołowski, Krakau, Polen.",
    contact_h1="Kontakt",
    labels=["Unternehmen", "Anschrift", "Steuernummer (NIP)", "E-Mail", "Telefon"],
    country="Polen",
    priv_title="Datenschutzerklärung – MikoSokPhoto",
    priv_desc="Datenschutzerklärung der Website und der Apps von MikoSokPhoto.",
    priv_h1="Datenschutzerklärung",
    priv_date="Gültig ab 12. November 2026.",
    priv=[
        ("1. Verantwortlicher", f"Verantwortlicher für die personenbezogenen Daten ist Mikołaj Sokołowski, der ein Gewerbe unter der Firma {COMPANY}, {STREET}, {CITY}, Polen, Steuernummer (NIP) {NIP} betreibt. Kontakt in Datenschutzfragen: {M}."),
        ("2. Geltungsbereich", "Diese Erklärung gilt für die Website mikosokphoto.pl und die von MikoSokPhoto bei Google Play veröffentlichten mobilen Apps."),
        ("3. Website", "Die Website verwendet keine Cookies, keine Analysewerkzeuge und keine Formulare. Sie wird bei GitHub Pages (GitHub, Inc.) gehostet; dabei können technische Verbindungsdaten wie IP-Adressen automatisch protokolliert werden, um Sicherheit und Betrieb des Dienstes zu gewährleisten. Die Verarbeitung dieser Daten durch GitHub ist in der Datenschutzerklärung von GitHub beschrieben."),
        ("4. Kontakt per E-Mail und Telefon", "Wenn Sie uns per E-Mail oder Telefon kontaktieren, verarbeiten wir die von Ihnen mitgeteilten Daten (z. B. Name, E-Mail-Adresse, Telefonnummer, Inhalt der Nachricht) ausschließlich zur Beantwortung und Bearbeitung Ihres Anliegens auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse). Wir speichern die Daten so lange, wie es für die Bearbeitung erforderlich ist, und anschließend für die Dauer der Verjährungsfrist etwaiger Ansprüche."),
        ("5. Mobile Apps", f"Die Apps von MikoSokPhoto erfordern kein Benutzerkonto und erheben keine personenbezogenen Daten, sofern in der Beschreibung der jeweiligen App nichts anderes angegeben ist. In die Apps eingegebene Daten werden lokal auf dem Gerät gespeichert und nicht an den Verantwortlichen übermittelt. Angeforderte Berechtigungen werden nur für die Funktionen der App genutzt. Verarbeitet eine App weitere Daten, ist dies in dieser Erklärung und im Abschnitt „Datensicherheit“ ihres Eintrags bei Google Play beschrieben. Die App Pediatria LEKI hat eine eigene, ausführliche <a {APPPRIV}>Datenschutzerklärung</a>."),
        ("6. Empfänger", "Daten werden weder verkauft noch zu Marketingzwecken an Dritte weitergegeben. Sie können nur an technische Dienstleister (z. B. Hosting, E-Mail) im erforderlichen Umfang oder an gesetzlich berechtigte Behörden übermittelt werden."),
        ("7. Ihre Rechte", f"Sie haben das Recht auf Auskunft, Berichtigung und Löschung Ihrer Daten, auf Einschränkung der Verarbeitung, auf Datenübertragbarkeit und auf Widerspruch. Außerdem können Sie Beschwerde bei der polnischen Aufsichtsbehörde einlegen, dem Präsidenten des Amtes für Datenschutz (UODO, ul. Stawki 2, 00-193 Warschau). Zur Ausübung Ihrer Rechte schreiben Sie an {M}."),
        ("8. Änderungen", "Diese Erklärung kann aktualisiert werden, z. B. bei der Veröffentlichung neuer Apps. Die aktuelle Fassung ist stets auf dieser Seite verfügbar."),
    ],
    app_title="Pediatria LEKI – MikoSokPhoto",
    app_desc="Pediatria LEKI – Trainings-App zur schnellen Berechnung von Medikamentendosen in pädiatrischen Simulationskursen.",
    app_lead="Trainings-App zur schnellen Berechnung von Medikamentendosen in pädiatrischen medizinischen Simulationsszenarien.",
    app_notice="<strong>Nur für Ausbildung und Simulation.</strong> Die App dient dem Üben an Trainingsfällen in pädiatrischen Kursen. Sie ist nicht für Entscheidungen über echte Patienten bestimmt und wurde nicht für den klinischen Einsatz validiert.",
    app_sections=[
        ("Wofür sie gedacht ist", [
            "Pediatria LEKI wurde für Kurse und Simulationstrainings in der pädiatrischen Notfallmedizin entwickelt. Teilnehmende und Ausbildende können damit in Sekunden Medikamentendosen, Infusionsraten und Ausrüstungsgrößen für das Kind oder Neugeborene im Szenario berechnen – so bleibt der Fokus während der Übung auf dem Vorgehen und danach auf der Nachbesprechung.",
            "Nach Eingabe der Falldaten zeigt die App berechnete Dosen, Ausrüstungsgrößen und Referenzwerte, die mit den Entscheidungen in der Simulation verglichen werden können."]),
        ("So funktioniert es", [
            ("Falldaten", "Gewicht manuell eingegeben, aus dem Alter geschätzt oder anhand der Körperlänge auf dem Broselow-Band abgelesen. Eigener Neugeborenen-Modus mit Gewicht in Gramm, Gestationsalter und Alter in Tagen."),
            ("Schnelle Dosierungen", "Kacheln mit berechneten Dosen, gruppiert in Registerkarten (Reanimation, Schmerz, Atmung, Sonstiges), ein RSI-Bereich mit Intubationsmedikamenten sowie Details zu jedem Medikament mit Dosierungsschemata und Quellen. Die App warnt, wenn ein Medikament für das Alter nicht vorgesehen ist oder Daten für die Berechnung fehlen."),
            ("Vitalparameter", "altersabhängige Normwerte, bei Neugeborenen Perzentilen für HF, AF, SBP und MAD."),
            ("Atemweg und Reanimation", "Tubusgröße und Einführtiefe, Defibrillationsenergie, CPR-Verhältnisse und Anfangseinstellungen des Beatmungsgeräts nach ROSC."),
            ("Rechner", "Infusionspumpe (Konzentration und Rate in ml/h) sowie „Dosis umrechnen“ für beliebige Medikamente."),
            ("Eigener Medikamentenkatalog", "Ausbildende können eigene Medikamente und Kategorien anlegen, sie an die Schnelldosierungen anheften und den Katalog per Sicherungsdatei auf ein anderes Gerät übertragen."),
            ("Methodik, Formeln und Quellen", "Beschreibung der Berechnungen und Datenquellen (u. a. Fachinformationen, ERC, UK-WHO), hilfreich bei der Nachbesprechung.")]),
        ("Datenschutz und Offline-Betrieb", [
            f"Die App läuft vollständig auf dem Gerät: kein Konto, kein Internet, keine Werbung und keine Analyse. Falldaten werden weder gespeichert noch übertragen. Verwenden Sie in Übungen nur fiktive Daten. Details: <a {APPPRIV}>Datenschutzerklärung Pediatria LEKI</a>."]),
        ("Für wen", [
            "Für Teilnehmende und Ausbildende pädiatrischer Kurse, Studierende und medizinisches Personal, das Simulationsszenarien übt. Die App ist nicht für Kinder bestimmt."]),
        ("Verfügbarkeit", [
            "Android-App (demnächst bei Google Play) und eine Version für den Browser. Sprachen: Polnisch, Englisch, Deutsch, Spanisch, Französisch und Ukrainisch."]),
    ],
    ap_title="Datenschutzerklärung – Pediatria LEKI",
    ap_desc="Datenschutzerklärung der App Pediatria LEKI (pl.pediatrialeki.mobile).",
    ap_h1="Datenschutzerklärung — Pediatria LEKI",
    ap_version="Fassung vom 9. November 2026 · Android-App",
    ap=[
        ("Die App erhebt und übermittelt keine Daten", "Pediatria LEKI läuft vollständig auf dem Gerät: Sie erfordert kein Konto, nutzt kein Internet (sie hat keine Berechtigung für Netzwerkzugriff) und enthält keine Werbung, Analyse- oder Tracking-Werkzeuge. Der Herausgeber erhält keine personenbezogenen Daten und keine Gesundheitsdaten."),
        ("Falldaten", "Gewicht, Alter, Geburtsdatum, Gestationsalter und Körperlänge dienen ausschließlich den auf dem Bildschirm angezeigten Berechnungen. Sie werden nicht gespeichert – sie verschwinden nach „Neuer Fall“ oder beim Schließen der App. Verwenden Sie in Übungen fiktive Daten. Geben Sie keine personenbezogenen Daten echter Patienten ein, auch nicht in Textfeldern des Katalogs."),
        ("Was auf dem Gerät bleibt", "Gespeichert werden nur: die gewählte Sprache, die Textgröße, Ihr eigener Medikamentenkatalog (falls angelegt) und die Sortierreihenfolge des Katalogs. Diese Daten verlassen das Gerät nicht und sind nicht Teil der Android-Sicherung. Deinstallation oder Löschen der App-Daten entfernt sie dauerhaft."),
        ("Katalogsicherung als Datei", "Eine Sicherungsdatei entsteht nur, wenn Sie „Sicherung in Datei speichern“ wählen, und wird an dem im Systemdialog gewählten Ort gespeichert. Beim Laden wird nur die von Ihnen gewählte Datei gelesen. Was danach mit der Datei geschieht (Weitergabe, Löschen), entscheiden Sie."),
        ("Links zu Quellen", "Links zu Fachinformationen, Leitlinien und Publikationen öffnen sich in einem externen Browser. Ab dann gilt die Datenschutzerklärung der besuchten Website."),
        ("Berechtigungen und Empfänger", "Die App fordert keine Systemberechtigungen an und gibt keine Daten an Dritte weiter. Sie ist für das Training von medizinischem Personal bestimmt, nicht für Kinder."),
        ("Änderungen und Kontakt", "Eine neue Fassung dieser Erklärung erscheint in der App und unter dieser Adresse, jeweils mit Datum."),
    ],
    ap_publisher="Herausgeber", ap_contact="Kontakt",
)

# ---------------------------------------------------------------- ESPAÑOL
T["es"] = dict(
    nav=["Inicio", "Pediatria LEKI", "Contacto", "Privacidad"],
    lang_aria="Idioma",
    home_title="MikoSokPhoto – Mikołaj Sokołowski",
    home_desc="MikoSokPhoto Mikołaj Sokołowski – Cracovia, Polonia. Datos de la empresa y contacto.",
    home_sub="Mikołaj Sokołowski · Cracovia, Polonia",
    logo_alt="Logotipo de MikoSokPhoto",
    contact_title="Contacto – MikoSokPhoto",
    contact_desc="Datos de contacto de MikoSokPhoto Mikołaj Sokołowski, Cracovia, Polonia.",
    contact_h1="Contacto",
    labels=["Empresa", "Dirección", "N.º fiscal (NIP)", "Correo electrónico", "Teléfono"],
    country="Polonia",
    priv_title="Política de privacidad – MikoSokPhoto",
    priv_desc="Política de privacidad del sitio web y de las aplicaciones de MikoSokPhoto.",
    priv_h1="Política de privacidad",
    priv_date="Vigente desde el 12 de noviembre de 2026.",
    priv=[
        ("1. Responsable del tratamiento", f"El responsable del tratamiento de los datos personales es Mikołaj Sokołowski, que ejerce su actividad empresarial bajo el nombre {COMPANY}, {STREET}, {CITY}, Polonia, n.º fiscal (NIP) {NIP}. Contacto para cuestiones de protección de datos: {M}."),
        ("2. Ámbito", "Esta política se aplica al sitio web mikosokphoto.pl y a las aplicaciones móviles publicadas por MikoSokPhoto en Google Play."),
        ("3. Sitio web", "El sitio web no utiliza cookies, herramientas de análisis ni formularios. Está alojado en GitHub Pages (GitHub, Inc.), que puede registrar automáticamente datos técnicos de conexión, como la dirección IP, para garantizar la seguridad y el funcionamiento del servicio. El tratamiento de estos datos por parte de GitHub se describe en su declaración de privacidad."),
        ("4. Contacto por correo electrónico y teléfono", "Si nos contacta por correo electrónico o por teléfono, tratamos los datos que nos facilite (p. ej., nombre, correo electrónico, número de teléfono, contenido del mensaje) únicamente para responder y gestionar su consulta, con base en el art. 6.1.f del RGPD (interés legítimo). Conservamos los datos durante el tiempo necesario para gestionar la consulta y, después, durante el plazo de prescripción de posibles reclamaciones."),
        ("5. Aplicaciones móviles", f"Las aplicaciones de MikoSokPhoto no requieren cuenta y no recopilan datos personales, salvo que la descripción de una aplicación concreta indique lo contrario. Los datos introducidos en las aplicaciones se guardan localmente en el dispositivo del usuario y no se envían al responsable. Los permisos que solicita una aplicación se usan solo para sus funciones. Si una aplicación trata datos adicionales, se indica en esta política y en la sección «Seguridad de los datos» de su ficha en Google Play. La aplicación Pediatria LEKI tiene su propia <a {APPPRIV}>política de privacidad</a> detallada."),
        ("6. Destinatarios", "Los datos no se venden ni se ceden a terceros con fines de marketing. Solo pueden transmitirse a proveedores de servicios técnicos (p. ej., alojamiento, correo electrónico) en la medida necesaria o a las autoridades facultadas por ley."),
        ("7. Sus derechos", f"Tiene derecho a acceder a sus datos, rectificarlos, suprimirlos, limitar su tratamiento, a la portabilidad y a oponerse al tratamiento. También puede presentar una reclamación ante la autoridad de control polaca, el Presidente de la Oficina de Protección de Datos Personales (UODO, ul. Stawki 2, 00-193 Varsovia). Para ejercer sus derechos, escriba a {M}."),
        ("8. Cambios", "Esta política puede actualizarse, por ejemplo, al publicar nuevas aplicaciones. La versión vigente está siempre disponible en esta página."),
    ],
    app_title="Pediatria LEKI – MikoSokPhoto",
    app_desc="Pediatria LEKI – aplicación formativa para calcular rápidamente dosis de fármacos en cursos de simulación médica pediátrica.",
    app_lead="Aplicación formativa para calcular rápidamente dosis de fármacos en escenarios de simulación médica pediátrica.",
    app_notice="<strong>Solo para formación y simulación.</strong> La aplicación sirve para practicar con casos formativos en cursos pediátricos. No está destinada a tomar decisiones sobre pacientes reales y no ha sido validada para uso clínico.",
    app_sections=[
        ("Para qué sirve", [
            "Pediatria LEKI se creó pensando en los cursos y sesiones de simulación de emergencias pediátricas. Permite a participantes e instructores calcular en segundos las dosis de fármacos, los ritmos de perfusión y los tamaños del material para el niño o recién nacido del escenario, de modo que durante el ejercicio puedan centrarse en la actuación y, después, en el análisis de los resultados.",
            "Basta con introducir los datos del caso y la aplicación muestra las dosis calculadas, los tamaños del material y los valores de referencia para compararlos con las decisiones tomadas en la simulación."]),
        ("Cómo funciona", [
            ("Datos del caso", "peso introducido manualmente, estimado a partir de la edad o leído según la talla en la cinta de Broselow. Modo neonatal independiente con peso en gramos, edad gestacional y edad en días."),
            ("Dosis rápidas", "fichas con las dosis calculadas agrupadas en pestañas (RCP, dolor, respiración, otros), un panel de secuencia rápida de intubación (SRI) y la ficha de cada fármaco con pautas de dosificación y fuentes. La aplicación avisa cuando un fármaco no está indicado para esa edad o faltan datos para el cálculo."),
            ("Constantes vitales", "valores normales según la edad y, en recién nacidos, percentiles de FC, FR, PAS y PAM."),
            ("Vía aérea y reanimación", "tamaño y profundidad de inserción del tubo, energía de desfibrilación, relaciones de RCP y ajustes iniciales del respirador tras la RCE."),
            ("Calculadoras", "bomba de perfusión (concentración y velocidad en ml/h) y «Recalcular dosis» para cualquier fármaco."),
            ("Catálogo propio de fármacos", "el instructor puede añadir sus propios fármacos y categorías, fijarlos en las dosis rápidas y trasladar el catálogo a otro dispositivo mediante un archivo de copia."),
            ("Metodología, fórmulas y fuentes", "descripción de los cálculos y de las fuentes de datos (p. ej., fichas técnicas, ERC, UK-WHO), útil en el debriefing del escenario.")]),
        ("Privacidad y funcionamiento sin conexión", [
            f"La aplicación funciona íntegramente en el dispositivo: sin cuenta, sin internet, sin anuncios ni análisis. Los datos del caso no se guardan ni se envían. En los ejercicios deben usarse solo datos ficticios. Más información: <a {APPPRIV}>política de privacidad de Pediatria LEKI</a>."]),
        ("Para quién", [
            "Para participantes e instructores de cursos pediátricos, estudiantes y personal sanitario que practica escenarios de simulación. La aplicación no está destinada a niños."]),
        ("Disponibilidad", [
            "Aplicación para Android (próximamente en Google Play) y versión que se ejecuta en el navegador. Idiomas: polaco, inglés, alemán, español, francés y ucraniano."]),
    ],
    ap_title="Política de privacidad – Pediatria LEKI",
    ap_desc="Política de privacidad de la aplicación Pediatria LEKI (pl.pediatrialeki.mobile).",
    ap_h1="Política de privacidad — Pediatria LEKI",
    ap_version="Versión del 9 de noviembre de 2026 · aplicación para Android",
    ap=[
        ("La aplicación no recopila ni transmite datos", "Pediatria LEKI funciona íntegramente en el dispositivo: no requiere cuenta, no usa internet (no tiene permiso de acceso a la red) y no contiene anuncios, herramientas de análisis ni de seguimiento. El editor no recibe ningún dato personal ni de salud."),
        ("Datos del caso", "El peso, la edad, la fecha de nacimiento, la edad gestacional y la talla se usan únicamente para los cálculos que se muestran en pantalla. No se guardan: desaparecen al elegir «Nuevo caso» o al cerrar la aplicación. Use datos ficticios en los ejercicios. No introduzca datos personales de pacientes reales, tampoco en los campos de texto del catálogo."),
        ("Qué se queda en el dispositivo", "La aplicación solo guarda: el idioma elegido, el tamaño del texto, su catálogo propio de fármacos (si lo crea) y el orden del catálogo. Estos datos no salen del dispositivo ni se incluyen en la copia de seguridad de Android. Desinstalar la aplicación o borrar sus datos los elimina de forma permanente."),
        ("Copia del catálogo en archivo", "El archivo de copia solo se crea al elegir «Guardar copia en archivo» y se guarda en la ubicación indicada en el diálogo del sistema. Al cargar una copia solo se lee el archivo que usted selecciona. Lo que ocurra después con el archivo (compartirlo, borrarlo) lo decide usted."),
        ("Enlaces a fuentes", "Los enlaces a fichas técnicas, guías y publicaciones se abren en un navegador externo. A partir de ese momento se aplica la política de privacidad del sitio visitado."),
        ("Permisos y destinatarios", "La aplicación no solicita permisos del sistema ni cede datos a terceros. Está destinada a la formación de personal sanitario, no a niños."),
        ("Cambios y contacto", "Las nuevas versiones de esta política aparecerán en la aplicación y en esta dirección, con su fecha."),
    ],
    ap_publisher="Editor", ap_contact="contacto",
)

# ---------------------------------------------------------------- FRANÇAIS
T["fr"] = dict(
    nav=["Accueil", "Pediatria LEKI", "Contact", "Confidentialité"],
    lang_aria="Langue",
    home_title="MikoSokPhoto – Mikołaj Sokołowski",
    home_desc="MikoSokPhoto Mikołaj Sokołowski – Cracovie, Pologne. Informations sur l’entreprise et contact.",
    home_sub="Mikołaj Sokołowski · Cracovie, Pologne",
    logo_alt="Logo MikoSokPhoto",
    contact_title="Contact – MikoSokPhoto",
    contact_desc="Coordonnées de MikoSokPhoto Mikołaj Sokołowski, Cracovie, Pologne.",
    contact_h1="Contact",
    labels=["Entreprise", "Adresse", "N° fiscal (NIP)", "E-mail", "Téléphone"],
    country="Pologne",
    priv_title="Politique de confidentialité – MikoSokPhoto",
    priv_desc="Politique de confidentialité du site et des applications MikoSokPhoto.",
    priv_h1="Politique de confidentialité",
    priv_date="En vigueur depuis le 12 novembre 2026.",
    priv=[
        ("1. Responsable du traitement", f"Le responsable du traitement des données personnelles est Mikołaj Sokołowski, exerçant une activité commerciale sous le nom {COMPANY}, {STREET}, {CITY}, Pologne, n° fiscal (NIP) {NIP}. Contact pour toute question relative aux données personnelles : {M}."),
        ("2. Champ d’application", "Cette politique s’applique au site mikosokphoto.pl et aux applications mobiles publiées par MikoSokPhoto sur Google Play."),
        ("3. Site web", "Le site n’utilise ni cookies, ni outils d’analyse, ni formulaires. Il est hébergé sur GitHub Pages (GitHub, Inc.), qui peut enregistrer automatiquement des données techniques de connexion, comme l’adresse IP, afin d’assurer la sécurité et le fonctionnement du service. Le traitement de ces données par GitHub est décrit dans la déclaration de confidentialité de GitHub."),
        ("4. Contact par e-mail et par téléphone", "Si vous nous contactez par e-mail ou par téléphone, nous traitons les données fournies (p. ex. nom, adresse e-mail, numéro de téléphone, contenu du message) uniquement pour vous répondre et traiter votre demande, sur la base de l’art. 6, par. 1, point f) du RGPD (intérêt légitime). Nous conservons ces données le temps nécessaire au traitement de la demande, puis pendant le délai de prescription des éventuelles réclamations."),
        ("5. Applications mobiles", f"Les applications MikoSokPhoto ne nécessitent pas de compte et ne collectent pas de données personnelles, sauf indication contraire dans la description de l’application concernée. Les données saisies dans les applications sont stockées localement sur l’appareil de l’utilisateur et ne sont pas transmises au responsable. Les autorisations demandées ne servent qu’au fonctionnement de l’application. Si une application traite des données supplémentaires, cela est indiqué dans cette politique et dans la section « Sécurité des données » de sa fiche Google Play. L’application Pediatria LEKI dispose de sa propre <a {APPPRIV}>politique de confidentialité</a> détaillée."),
        ("6. Destinataires", "Les données ne sont ni vendues ni communiquées à des tiers à des fins de marketing. Elles ne peuvent être transmises qu’à des prestataires techniques (p. ex. hébergement, messagerie) dans la mesure nécessaire, ou aux autorités habilitées par la loi."),
        ("7. Vos droits", f"Vous disposez d’un droit d’accès, de rectification et d’effacement de vos données, d’un droit à la limitation du traitement, à la portabilité et d’un droit d’opposition. Vous pouvez également introduire une réclamation auprès de l’autorité de contrôle polonaise, le Président de l’Office de protection des données personnelles (UODO, ul. Stawki 2, 00-193 Varsovie). Pour exercer vos droits, écrivez à {M}."),
        ("8. Modifications", "Cette politique peut être mise à jour, par exemple lors de la publication de nouvelles applications. La version en vigueur est toujours disponible sur cette page."),
    ],
    app_title="Pediatria LEKI – MikoSokPhoto",
    app_desc="Pediatria LEKI – application de formation pour calculer rapidement les doses de médicaments lors de cours de simulation médicale pédiatrique.",
    app_lead="Application de formation pour calculer rapidement les doses de médicaments dans des scénarios de simulation médicale pédiatrique.",
    app_notice="<strong>Uniquement pour l’apprentissage et la simulation.</strong> L’application sert à s’entraîner sur des cas pédagogiques lors de formations en pédiatrie. Elle n’est pas destinée à la prise de décisions concernant de vrais patients et n’a pas été validée pour un usage clinique.",
    app_sections=[
        ("À quoi elle sert", [
            "Pediatria LEKI a été conçue pour les formations et séances de simulation en urgences pédiatriques. Elle permet aux participants et aux formateurs de calculer en quelques secondes les doses de médicaments, les débits de perfusion et les tailles de matériel pour l’enfant ou le nouveau-né du scénario, afin de se concentrer sur la prise en charge pendant l’exercice, puis sur le débriefing.",
            "Il suffit de saisir les données du cas : l’application affiche les doses calculées, les tailles de matériel et les valeurs de référence à comparer avec les décisions prises pendant la simulation."]),
        ("Comment elle fonctionne", [
            ("Données du cas", "poids saisi manuellement, estimé à partir de l’âge ou lu d’après la taille sur le ruban de Broselow. Mode nouveau-né distinct avec poids en grammes, âge gestationnel et âge en jours."),
            ("Doses rapides", "vignettes avec les doses calculées regroupées par onglets (RCP, douleur, respiration, autres), un panneau d’induction en séquence rapide (ISR) et la fiche de chaque médicament avec schémas posologiques et sources. L’application avertit lorsqu’un médicament n’est pas prévu pour l’âge indiqué ou qu’il manque des données pour le calcul."),
            ("Paramètres vitaux", "normes selon l’âge et, chez le nouveau-né, percentiles de FC, FR, PAS et PAM."),
            ("Voies aériennes et réanimation", "taille et profondeur d’insertion de la sonde, énergie de défibrillation, ratios de RCP et réglages initiaux du respirateur après RACS."),
            ("Calculateurs", "pousse-seringue (concentration et débit en ml/h) et « Recalculer la dose » pour n’importe quel médicament."),
            ("Catalogue personnel de médicaments", "le formateur peut ajouter ses propres médicaments et catégories, les épingler aux doses rapides et transférer le catalogue sur un autre appareil grâce à un fichier de sauvegarde."),
            ("Méthodologie, formules et sources", "description des calculs et des sources de données (notamment RCP des médicaments, ERC, UK-WHO), utile lors du débriefing.")]),
        ("Confidentialité et fonctionnement hors ligne", [
            f"L’application fonctionne entièrement sur l’appareil : sans compte, sans internet, sans publicité ni outils d’analyse. Les données du cas ne sont ni enregistrées ni transmises. Utilisez uniquement des données fictives lors des exercices. Détails : <a {APPPRIV}>politique de confidentialité de Pediatria LEKI</a>."]),
        ("Pour qui", [
            "Pour les participants et formateurs des formations en pédiatrie, les étudiants et le personnel médical qui s’entraînent sur des scénarios de simulation. L’application n’est pas destinée aux enfants."]),
        ("Disponibilité", [
            "Application Android (bientôt sur Google Play) et version utilisable dans le navigateur. Langues : polonais, anglais, allemand, espagnol, français et ukrainien."]),
    ],
    ap_title="Politique de confidentialité – Pediatria LEKI",
    ap_desc="Politique de confidentialité de l’application Pediatria LEKI (pl.pediatrialeki.mobile).",
    ap_h1="Politique de confidentialité — Pediatria LEKI",
    ap_version="Version du 9 novembre 2026 · application Android",
    ap=[
        ("L’application ne collecte ni ne transmet de données", "Pediatria LEKI fonctionne entièrement sur l’appareil : elle ne nécessite pas de compte, n’utilise pas internet (elle n’a pas l’autorisation d’accès au réseau) et ne contient ni publicité, ni outils d’analyse ou de suivi. L’éditeur ne reçoit aucune donnée personnelle ni donnée de santé."),
        ("Données du cas", "Le poids, l’âge, la date de naissance, l’âge gestationnel et la taille servent uniquement aux calculs affichés à l’écran. Ils ne sont pas enregistrés : ils disparaissent après « Nouveau cas » ou à la fermeture de l’application. Utilisez des données fictives lors des exercices. Ne saisissez pas de données personnelles de vrais patients, y compris dans les champs de texte du catalogue."),
        ("Ce qui reste sur l’appareil", "L’application enregistre uniquement : la langue choisie, la taille du texte, votre catalogue personnel de médicaments (si vous en créez un) et l’ordre de tri du catalogue. Ces données ne quittent pas l’appareil et ne sont pas incluses dans la sauvegarde Android. Désinstaller l’application ou effacer ses données les supprime définitivement."),
        ("Sauvegarde du catalogue dans un fichier", "Le fichier de sauvegarde n’est créé que lorsque vous choisissez « Enregistrer une copie dans un fichier » et il est enregistré à l’emplacement choisi dans la fenêtre système. Le chargement d’une copie ne lit que le fichier que vous sélectionnez. Ce que devient ensuite le fichier (partage, suppression) relève de votre décision."),
        ("Liens vers les sources", "Les liens vers les RCP, recommandations et publications s’ouvrent dans un navigateur externe. Dès lors, la politique de confidentialité du site visité s’applique."),
        ("Autorisations et destinataires", "L’application ne demande aucune autorisation système et ne transmet aucune donnée à des tiers. Elle est destinée à la formation du personnel médical, pas aux enfants."),
        ("Modifications et contact", "Toute nouvelle version de cette politique apparaîtra dans l’application et à cette adresse, avec sa date."),
    ],
    ap_publisher="Éditeur", ap_contact="contact",
)

# ---------------------------------------------------------------- УКРАЇНСЬКА
T["uk"] = dict(
    nav=["Головна", "Pediatria LEKI", "Контакти", "Конфіденційність"],
    lang_aria="Мова",
    home_title="MikoSokPhoto – Mikołaj Sokołowski",
    home_desc="MikoSokPhoto Mikołaj Sokołowski – Краків, Польща. Дані компанії та контакти.",
    home_sub="Mikołaj Sokołowski · Краків, Польща",
    logo_alt="Логотип MikoSokPhoto",
    contact_title="Контакти – MikoSokPhoto",
    contact_desc="Контактні дані MikoSokPhoto Mikołaj Sokołowski, Краків, Польща.",
    contact_h1="Контакти",
    labels=["Компанія", "Адреса", "Податковий номер (NIP)", "Ел. пошта", "Телефон"],
    country="Польща",
    priv_title="Політика конфіденційності – MikoSokPhoto",
    priv_desc="Політика конфіденційності сайту та застосунків MikoSokPhoto.",
    priv_h1="Політика конфіденційності",
    priv_date="Діє з 12 листопада 2026 р.",
    priv=[
        ("1. Адміністратор даних", f"Адміністратором персональних даних є Mikołaj Sokołowski, який веде підприємницьку діяльність під назвою {COMPANY}, {STREET}, {CITY}, Польща, податковий номер (NIP) {NIP}. Контакт з питань персональних даних: {M}."),
        ("2. Сфера дії", "Ця політика стосується сайту mikosokphoto.pl та мобільних застосунків, опублікованих MikoSokPhoto в Google Play."),
        ("3. Сайт", "Сайт не використовує файли cookie, інструменти аналітики чи форми. Він розміщений на GitHub Pages (GitHub, Inc.), що може автоматично реєструвати технічні дані з’єднання, наприклад IP-адресу, для забезпечення безпеки та роботи сервісу. Обробку цих даних компанією GitHub описано в її заяві про конфіденційність."),
        ("4. Зв’язок електронною поштою та телефоном", "Якщо ви зв’яжетеся з нами електронною поштою або телефоном, ми обробляємо надані вами дані (наприклад, ім’я, адресу ел. пошти, номер телефону, зміст повідомлення) виключно для відповіді та розгляду вашого звернення на підставі ст. 6 ч. 1 п. f GDPR (законний інтерес). Ми зберігаємо дані стільки, скільки потрібно для розгляду звернення, а потім протягом строку позовної давності можливих претензій."),
        ("5. Мобільні застосунки", f"Застосунки MikoSokPhoto не вимагають облікового запису та не збирають персональних даних, якщо в описі конкретного застосунку не зазначено інше. Дані, введені в застосунки, зберігаються локально на пристрої користувача й не передаються адміністратору. Дозволи, які запитує застосунок, використовуються лише для його функцій. Якщо застосунок обробляє додаткові дані, це зазначено в цій політиці та в розділі «Безпека даних» на його сторінці в Google Play. Застосунок Pediatria LEKI має власну детальну <a {APPPRIV}>політику конфіденційності</a>."),
        ("6. Одержувачі даних", "Дані не продаються й не передаються третім особам з маркетинговою метою. Вони можуть передаватися лише постачальникам технічних послуг (наприклад, хостинг, ел. пошта) в необхідному обсязі або органам, уповноваженим законом."),
        ("7. Ваші права", f"Ви маєте право на доступ до своїх даних, їх виправлення, видалення, обмеження обробки, перенесення та заперечення проти обробки. Ви також можете подати скаргу до польського наглядового органу — Голови Управління із захисту персональних даних (UODO, ul. Stawki 2, 00-193 Варшава). Щоб скористатися своїми правами, напишіть на {M}."),
        ("8. Зміни", "Політика може оновлюватися, наприклад у зв’язку з публікацією нових застосунків. Актуальна версія завжди доступна на цій сторінці."),
    ],
    app_title="Pediatria LEKI – MikoSokPhoto",
    app_desc="Pediatria LEKI – навчальний застосунок для швидкого розрахунку доз ліків під час курсів педіатричної медичної симуляції.",
    app_lead="Навчальний застосунок для швидкого розрахунку доз ліків у сценаріях педіатричної медичної симуляції.",
    app_notice="<strong>Лише для навчання та симуляції.</strong> Застосунок призначений для відпрацювання навчальних випадків на педіатричних курсах. Він не призначений для прийняття рішень щодо реальних пацієнтів і не пройшов валідацію для клінічного застосування.",
    app_sections=[
        ("Для чого він", [
            "Pediatria LEKI створено для курсів і симуляційних занять з педіатричної екстреної допомоги. Він дає змогу учасникам та інструкторам за кілька секунд розрахувати дози ліків, швидкість інфузій і розміри обладнання для дитини чи новонародженого зі сценарію, щоб під час вправи зосередитися на діях, а після неї — на розборі результатів.",
            "Достатньо ввести дані випадку, і застосунок покаже розраховані дози, розміри обладнання та референтні значення для порівняння з рішеннями, ухваленими під час симуляції."]),
        ("Як він працює", [
            ("Дані випадку", "маса, введена вручну, оцінена за віком або визначена за довжиною тіла на стрічці Broselow. Окремий режим новонародженого: маса в грамах, гестаційний вік і вік у днях."),
            ("Швидкі дози ліків", "плитки з розрахованими дозами, згруповані у вкладки (СЛР, біль, дихання, інше), панель RSI з препаратами для інтубації та картка кожного препарату зі схемами дозування й джерелами. Застосунок попереджає, коли препарат не призначений для цього віку або бракує даних для розрахунку."),
            ("Життєві показники", "вікові норми, а для новонароджених — центилі ЧСС, ЧД, САТ і СерАТ."),
            ("Дихальні шляхи та реанімація", "розмір і глибина введення трубки, енергія дефібриляції, співвідношення СЛР і початкові налаштування апарата ШВЛ після ROSC."),
            ("Калькулятори", "інфузійна помпа (концентрація та швидкість у мл/год) і «Перерахувати дозу» для будь-якого препарату."),
            ("Власний каталог ліків", "інструктор може додати власні препарати й категорії, закріпити їх у швидких дозах і перенести каталог на інший пристрій за допомогою файлу резервної копії."),
            ("Методика, формули та джерела", "опис способу розрахунку та джерел даних (зокрема інструкції до препаратів, ERC, UK-WHO), корисний під час розбору сценарію.")]),
        ("Конфіденційність і робота офлайн", [
            f"Застосунок повністю працює на пристрої: без облікового запису, без інтернету, без реклами й аналітики. Дані випадку не зберігаються й не передаються. Під час вправ використовуйте лише вигадані дані. Докладніше: <a {APPPRIV}>політика конфіденційності Pediatria LEKI</a>."]),
        ("Для кого", [
            "Для учасників та інструкторів педіатричних курсів, студентів і медичного персоналу, який відпрацьовує симуляційні сценарії. Застосунок не призначений для дітей."]),
        ("Доступність", [
            "Застосунок для Android (незабаром у Google Play) і версія, що запускається в браузері. Мови: польська, англійська, німецька, іспанська, французька та українська."]),
    ],
    ap_title="Політика конфіденційності – Pediatria LEKI",
    ap_desc="Політика конфіденційності застосунку Pediatria LEKI (pl.pediatrialeki.mobile).",
    ap_h1="Політика конфіденційності — Pediatria LEKI",
    ap_version="Версія від 9 листопада 2026 р. · застосунок для Android",
    ap=[
        ("Застосунок не збирає й не передає даних", "Pediatria LEKI повністю працює на пристрої: не вимагає облікового запису, не використовує інтернет (не має дозволу на доступ до мережі) і не містить реклами, аналітики чи інструментів відстеження. Видавець не отримує жодних персональних даних чи даних про здоров’я."),
        ("Дані випадку", "Маса, вік, дата народження, гестаційний вік і довжина тіла використовуються лише для розрахунків, показаних на екрані. Вони не зберігаються — зникають після вибору «Новий випадок» або закриття застосунку. Під час вправ використовуйте вигадані дані. Не вводьте персональні дані реальних пацієнтів, зокрема в текстові поля каталогу."),
        ("Що залишається на пристрої", "Застосунок зберігає лише: вибрану мову, розмір тексту, власний каталог ліків (якщо ви його створите) та порядок сортування каталогу. Ці дані не залишають пристрій і не потрапляють до резервної копії Android. Видалення застосунку або очищення його даних знищує їх назавжди."),
        ("Копія каталогу у файлі", "Файл копії створюється лише після вибору «Зберегти копію у файл» і зберігається в місці, вказаному в системному вікні збереження. Під час завантаження копії зчитується лише вибраний вами файл. Подальшу долю файлу (надсилання, видалення) визначаєте ви."),
        ("Посилання на джерела", "Посилання на інструкції до препаратів, настанови та публікації відкриваються в зовнішньому браузері. Відтоді діє політика конфіденційності відвідуваного сайту."),
        ("Дозволи та одержувачі", "Застосунок не запитує жодних системних дозволів і не передає даних третім особам. Він призначений для навчання медичного персоналу, а не для дітей."),
        ("Зміни та контакт", "Нова версія політики з’явиться в застосунку та за цією адресою разом із датою."),
    ],
    ap_publisher="Видавець", ap_contact="контакт",
)
