---
Sicherheitsfunktion: PT
Kategorie: Benutzerverwaltung, Authentifizierung und Zugriffskontrolle
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Zugriff (A)
Verteidiger: Prozess
Voraussetzung:
---

## Beschreibung

Spezifische Vorgaben in Bezug auf Autorisierungsbeschränkungen und Passwörter sollten regelmäßig veröffentlicht, überprüft, kontrolliert und gegebenenfalls überarbeitet werden.

## Implementierung

Es ist wichtig, spezifische Vorgaben zu erstellen, die die verschiedenen Berechtigungs- und Passwortrichtlinien der Organisation berücksichtigen.

- Erstellen Sie eine Vorgaben zur Zugriffskontrolle, um Benutzer und ihre jeweiligen Benutzergruppen zu definieren.
- Erstellen Sie eine Vorgaben für sichere SAP-Passwörter für alle Benutzer.
- Erstellen Sie Vorgaben für die Festlegung eines sicheren Passworts, die die Benutzer befolgen können.

Hinweis: Die Kontrollen PT-P-IP-M01-005 und PT-P-IP-M01-010 können beim Aufbau einer starken SAP-Passwortvorgabe helfen.

## Überprüfung der Maßnahme

- Überprüfen Sie, ob die Berechtigungen und der Zugriff auf SAP-Systeme dokumentiert sind.
- Überprüfen Sie, ob die Benutzer ihren jeweiligen Benutzergruppen entsprechend ihrer Arbeitsrolle zugeordnet sind.
- Überprüfen Sie, ob eine strenge Kennwortvorgabe vorhanden ist und befolgt wird.

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A19 Definition der Sicherheitsrichtlinien für Benutzer / Definition der Sicherheitsrichtlinien für Benutzer
- CIS CSC 3, 5, 12, 14, 15, 16, 18
- COBIT 5 DSS05.04
- ISA 62443-2-1:2009 4.3.3.7.3
- ISA 62443-3-3:2013 SR 2.1
- ISO/IEC 27001:2013 A.6.1.2, A.9.1.2, A.9.2.3, A.9.4.1, A.9.4.4, A.9.4.5
- NIST SP 800-53 Rev. 4 AC-1, AC-2, AC-3, AC-5, AC-6, AC-14, AC-16, AC-24
