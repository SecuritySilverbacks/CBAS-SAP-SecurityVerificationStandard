---
Sicherheitsfunktion: PT
Kategorie: Datensicherheit
Technologie: SAP Java
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Technologie
Vorbedingung:
---

## Beschreibung

Um die Menge an Informationen zu reduzieren, die bei der Auskundschaftung durch Angreifer offengelegt werden, wird empfohlen, alle Informationen zur Systemversion oder detaillierte Fehlerprotokolle zu entfernen, die gesammelt werden können, um mögliche Schwachstellen auszunutzen, die sich aus diesen Informationen ergeben könnten.

## Implementierung

1. Um eine beliebige Version aus dem SAP Java-System Ihres Unternehmens zu entfernen, setzen Sie die Einstellung UseServerHeader sowohl im HTTP-Providerdienst (globale Konfiguration des Dispatchers) als auch in den Serverknoten auf false.

2. Webmethoden müssen geschützt werden, indem der Profilparameter service/protectedwebmethods auf SDEFAULT (oder ALL) gesetzt wird, mit einer begrenzten Liste von Ausnahmen.

## Überprüfung der Maßnahme

- Setzen Sie UserServerHeader im HTTP-Provider-Dienst in der globalen Konfiguration des Dispatchers auf false.
- Setzen Sie UserServerHeader in den Server-Knoten auf false.
- Setzen Sie service/protectedwebmethods auf SDEFAULT

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A1 Sichere Konfiguration des SAP-ABAP-Stacks (B) / Secure Konfiguration des SAP-ABAP-Stacks (B)
- SAP Security Baseline Template V2.4.1: 2.2.1.2.2 [via SAP Security Optimization Services Portfolio](https://support.sap.com/sos)
