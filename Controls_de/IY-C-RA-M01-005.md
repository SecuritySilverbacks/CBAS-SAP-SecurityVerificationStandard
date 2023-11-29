---
Sicherheitsfunktion: IY
Kategorie: Risikobewertung
Technologie: ABAP
Reifegrad: 1
IPAC: Customizing (C)
Verteidiger: Prozess
Vorausgesetzt: IY-C-RA-M01-001, IY-C-RA-M01-004
---

## Beschreibung

Einsatz von Schutzmechanismen

Das SAP-Standardsystem bietet Unternehmen verschiedene Mechanismen zum Schutz ihrer Daten. Aus diesem Grund basieren die Sicherheitsstrategien vieler Unternehmen auf dem Wissen, dass die Mechanismen in den SAP-Standardsystemen eine solide Grundlage bieten und nicht gefährdet sind (oder sein sollten).
Zu diesen Mechanismen gehören:
- Trennung von Client und Mandant
- Benutzerverwaltung
- Rollen- und Berechtigungsverwaltung
- Trennung von Entwicklung, Test und Produktion
- Protokollierung von Sicherheitsereignissen

## Implementierung

1. Im Rahmen des Code Change Review-Prozesses muss der gesamte benutzerdefinierte Code daraufhin überprüft werden, dass:
    - er darf die Sicherheitsmechanismen des SAP-Standardsystems nicht untergraben.
    - Wenn das SAP-Standardsystem einen Sicherheitsmechanismus für bestimmte Aufgaben vorgesehen hat, dann sollte dieser Sicherheitsmechanismus auch im Custom Code der Änderung verwendet werden.
    - In der Zielsystemversion, in der die Anwendung ausgeführt werden soll, sollte der ABAP-Code keine veralteten Sprachelemente verwenden.
    - Die Codierung sollte mit der erweiterten Syntaxprüfung getestet und etwaige Defizite beseitigt werden.
    - Generell sollten kundeneigene Datenbanktabellen ausgeliefert werden, um eine manuelle Datenpflege durch SAP-Standardwerkzeuge auszuschließen. Wenn eine manuelle Tabellenpflege erforderlich ist, sollte eine Pflegeanwendung (Pflegeview) erstellt werden.

## Überprüfung der Maßnahme

- Prüfen Sie, ob die Überprüfung des Quellcodes bei allen benutzerdefinierten Codeänderungen durchgeführt und dokumentiert wird, um die korrekte Verwendung von Schutzmechanismen zu überprüfen.

## Referenzen

- CIS CSC 4
- COBIT 5 APO12.01, APO12.02, APO12.03, APO12.04
- ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12
- ISO/IEC 27001:2013 Klausel 6.1.2
- NIST SP 800-53 Rev. 4 RA-3, SI-5, PM-12, PM-16
