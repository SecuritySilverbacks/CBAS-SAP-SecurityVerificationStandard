---
Sicherheitsfunktion: PT
Kategorie: Prozesse und Verfahren zum Schutz von Informationen
Technologie: SAP Java
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Prozess / Technologie
Voraussetzung:
---

## Beschreibung

Die Festlegung einer strengen Kennwortrichtlinie ist unerlässlich, um sich vor unbefugtem Zugriff auf Ihre Systeme durch gestohlene Anmeldedaten oder Hashes zu schützen. Eine schwache Passwortpolitik kann zu verschiedenen Bedrohungen für das Unternehmen führen, die vom Zugang zu sensiblen Informationen bis zur Beschädigung eines ganzen Systems reichen.

## Implementierung

Nachfolgend finden Sie Informationen zur Festlegung von Passwortrichtlinien für ABAP-Systeme:

- Setzen Sie die minimale Passwortlänge (1) mit der UME-Eigenschaft ume.logon.security_policy.password_min_length >= 12
- Erhöhen Sie die maximale Passwortlänge mit der UME-Eigenschaft ume.logon.security_policy.password_max_length (Standard ist nur 14)
- Legen Sie ein Verfallsdatum für zu ändernde Kennwörter mit der UME-Eigenschaft ume.logon.security_policy.password_expire_days <= 90 fest
- Definieren Sie eine Größe für den Passwortverlauf mit der UME-Eigenschaft ume.logon.security_policy.password_history >= 5
- Definieren Sie eine maximale Passwortgültigkeit mit der UME-Eigenschaft ume.logon.security_policy.password_max_idle_time zwischen 1 und 180
- Um die Benutzer zur Einhaltung der Kennwortrichtlinie zu zwingen, setzen Sie die UME-Eigenschaft ume.logon.security_policy.enforce_policy_at_logon = TRUE
- Setzen Sie die maximalen Anmeldeversuche durch die UME-Eigenschaft ume.logon.security_policy.lock_after_invalid_attempts <= 5
- Verweigern Sie die Verwendung alter Passwörter in neuen Passwörtern, indem Sie die UME-Eigenschaft ume.logon.security_policy.oldpass_in_newpass_allowed = FALSE setzen
- Erlauben Sie Benutzern, ihr eigenes Passwort zu ändern ume.logon.security_policy.password_change_allowed = TRUE
- Definieren Sie eine Liste bekannter Passwörter, die von Benutzern nicht verwendet werden dürfen, durch ume.logon.security_policy.password_impermissible
- Verhindern Sie die Verwendung von Benutzer-IDs als Teil des Passworts, indem Sie die UME-Eigenschaftume.logon.security_policy.userid_in_password_allowed = FALSE setzen.


Passwortkomplexität einstellen:
- Setzen Sie UME propoerty ume.logon.security_policy.password_alpha_numeric_required >= 1
- Setzen Sie UME ume.logon.security_policy.password_mix_case_required >= 1
- Setzen Sie UME ume.logon.security_policy.password_special_char_required >= 1


(1) - Die SAP-Basisrichtlinie empfiehlt eine Mindestlänge von 8 Zeichen. Unsere Empfehlung und Untersuchungen zum Knacken von Passwörtern zeigen, dass eine Mindestlänge von 8 Zeichen mit den heutigen Computern leicht geknackt werden kann.

## Überprüfung der Maßnahme

- Überprüfen Sie, ob eine Kennwortrichtlinie mit den im Abschnitt Implementierung empfohlenen Werten vorhanden ist.

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A13 SAP-Passwortsicherheit (S) / SAP-Passwortsicherheit (S)
- SAP Security Baseline Template V2.4.1: 2.3.2.2, 2.3.2.2.2 [via SAP Security Optimization Services Portfolio](https://support.sap.com/sos)
