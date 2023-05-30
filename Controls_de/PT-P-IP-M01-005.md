---
Sicherheitsfunktion: PT
Kategorie: Prozesse und Verfahren zum Schutz von Informationen
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Prozess / Technologie
Voraussetzung:
---

## Beschreibung

Die Festlegung einer strengen Kennwortrichtlinie ist unerlässlich, um sich vor unbefugtem Zugriff auf Ihre Systeme durch gestohlene Anmeldedaten oder Hashes zu schützen. Eine schwache Passwortpolitik kann zu verschiedenen Bedrohungen für das Unternehmen führen, die vom Zugang zu sensiblen Informationen bis zur Beschädigung eines ganzen Systems reichen.

## Implementierung

Nachfolgend finden Sie Informationen zur Festlegung von Passwortrichtlinien für ABAP-Systeme:

- Legen Sie die Mindestlänge des Passworts (1) mit dem Profilparameter login/min_password_lng >= 12 fest.
- Legen Sie mit dem Profilparameter login/password_max_idle_initial eine maximale Anzahl von Tagen fest, die ein Kennwort unbenutzt bleiben kann (zwischen 1 und 14)
- Legen Sie mit dem Profilparameter login/password_expiration_time <= 90 ein Ablaufdatum für zu ändernde Kennwörter fest.
- Legen Sie eine Größe für den Passwortverlauf mit dem Profilparameter login/password_history_size >= 5 fest
- Speichern Sie keine zu interpretierenden Passwörter für alte Kernel, indem Sie den Profilparameter login/password_downwards_compatibility=0 setzen
- Um Benutzer zur Einhaltung der Kennwortrichtlinie zu zwingen, setzen Sie den Profilparameter login/password_compliance_to_current_policy=1
- Entfernen Sie alte abwärtskompatible Passwort-Hashes in den Feldern BCODE und PASSCODE aus der Tabelle USR02
- Maximale Anmeldeversuche durch Profilparameter login/fails_to_user_lock <= 5 festlegen
- Deaktivieren der automatischen Entsperrung durch den Profilparameter login/failed_user_auto_unlock = 0
- Festlegen eines maximalen Zeitraums, in dem ein unbenutztes produktives Kennwort gültig bleibt durch den Profilparameter login/max_idle_productive <= 90
- Anmeldung mit ursprünglichen oder abgelaufenen Benutzerkonten verweigern durch Setzen des Profilparameters icf/reject_expired_passwd = 1
- Anmeldung mit anfänglichen oder abgelaufenen Benutzerkonten über RFC verweigern, indem Sie den Profilparameter rfc/reject_expired_passwd = 1 setzen.
- Deaktivieren Sie die Passwortanmeldung, wenn die Organisation andere Authentifizierungsmethoden verwendet, indem Sie den Profilparameter login/disable_password_logon > 0 setzen.
- Bei der Verwendung der Authentifizierungsmethode Single Sign-on (SSO) muss mit dem Profilparameter login/password_change_for_SSO geprüft werden, ob die Passwörter eines Benutzers geändert werden müssen.
- Legen Sie mit dem Profilparameter login/password_change_waittime > 0 eine Zeitspanne (gemessen in Tagen) fest, in der ein Benutzer sein Passwort erneut ändern kann.
- Legen Sie den Hash-Algorithmus und die Kodierung für das neue Passwort mit dem Profilparameter login/password_hash_algorithm = encoding=RFC2307, algorithm=iSSHA-512, iterations=15000, saltsize=256 fest (Der Profilparameter login/password_downwards_compatibility sollte nicht gleich 5 sein, sonst macht der Profilparameter für den Hash-Algorithmus keinen Sinn)

Passwortkomplexität einstellen:
- Setzen Sie den Profilparameter login/min_password_digits >= 1
- Setzen Sie den Profilparameter login/min_password_letters >= 1
- Setzen Sie den Profilparameter login/min_password_lowercase >= 1
- Setzen Sie den Profilparameter login/min_password_uppercase >= 1
- Setzen Sie den Profilparameter login/min_password_specials >= 1
- Profilparameter login/min_password_diff >= 3 setzen


(1) - Die SAP-Basisrichtlinie empfiehlt eine Mindestlänge von 8 Zeichen. Unsere Empfehlung und Untersuchungen zum Knacken von Passwörtern zeigen, dass eine Mindestlänge von 8 Zeichen mit den heutigen Geräten leicht zu knacken ist.

## Überprüfung der Maßnahme

- Überprüfen Sie, ob eine Kennwortrichtlinie mit den im Abschnitt Implementierung empfohlenen Werten vorhanden ist.
- Überprüfen Sie, ob die Tabelle USR02 alte abwärtskompatible Passwort-Hashes in den Feldern BCODE und PASSCODE enthält.


## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A13 SAP-Passwortsicherheit (S) / SAP-Passwortsicherheit (S)
- SAP Security Baseline Template V2.1: 2.3.2.2, 2.3.2.2.1
- SAP-Hinweis 1458262
