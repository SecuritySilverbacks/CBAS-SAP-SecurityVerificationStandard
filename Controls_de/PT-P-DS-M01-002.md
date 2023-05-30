---
Sicherheitsfunktion: PT
Kategorie: Datensicherheit
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Technologie
Voraussetzung:
---

## Beschreibung

Um die Menge an Informationen, die bei der Auskundschaftung durch Angreifer offengelegt werden, zu reduzieren, wird empfohlen, alle Informationen zur Systemversion oder detaillierte Fehlerprotokolle zu entfernen, die gesammelt werden können, um mögliche Schwachstellen auszunutzen, die sich aus diesen Informationen ergeben könnten.

## Implementierung

Um alle detaillierten Fehler aus dem SAP ABAP-System Ihres Unternehmens zu entfernen, setzen Sie den Profilparameter login/show_detailed_errors auf 0.

Verwenden Sie die nachstehenden Parameter, um die Parameter anzuzeigen und zu ändern:

- RZ11-Transaktion: zum Anzeigen von Informationen über Parameter
- RZ10-Transaktion: zum Anzeigen und Ändern von Profilparametern
- RSPARAM-Bericht zum Anzeigen von Parametern (verwenden Sie Transaktion SA38)


## Überprüfung der Maßnahme

- Profilparameter login/show_detailed_errors=0

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A1 Sichere Konfiguration des SAP-ABAP-Stacks (B) / Secure Konfiguration des SAP-ABAP-Stacks (B)
- SAP Security Baseline Template V2.1: 2.2.1.2.1
