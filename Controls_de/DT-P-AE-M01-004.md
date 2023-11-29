---
Sicherheitsfunktion: DT
Kategorie: Anomalien und Ereignisse
Technologie: SAP ERP
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Prozess
Vorraussetzung: DT-P-AE-M01-001
---

## Beschreibung

Tabellenprotokollierung:

Die Identifizierung und Sammlung von Protokollen zur Ermittlung von Änderungen in kritischen Tabellen ist notwendig, um die Integrität der in verschiedenen Tabellen verfügbaren Daten zu erhalten.


## Implementierung

Aktivieren Sie die Tabellenprotokollierung über den Profilparameter rec/client. Es wird empfohlen, diesen Parameter so einzustellen, dass die Protokollierung von allen Mandanten innerhalb Ihrer SAP-Umgebung erfolgt.

Als Faustregel gilt: Wählen Sie Tabellen aus, die entweder mit der höchsten Schutzklasse klassifiziert sind, oder wählen Sie Tabellen je nach der Kritikalität der darin enthaltenen Daten.

Sie können Warnmeldungen konfigurieren, wenn ein bestimmtes Ereignis eintritt oder ein Schwellenwert erreicht wird. Dies trägt dazu bei, den Überprüfungsprozess der Tabellenprotokolle zu automatisieren und die Arbeitsbelastung der Administratoren zu verringern. Das Versenden von Protokollen an eine zentrale Stelle hilft bei der Einrichtung von Warnmeldungen.

## Überprüfung der Maßnahme

- Stellen Sie den Parameter rec/client so ein, dass die Protokollierung aktiviert wird.
- Setzen Sie den rec/client-Parameter, um von allen Clients zu sammeln
- Definieren Sie die zu protokollierenden Tabellen mit der Transaktion SE13
- Verwenden Sie Transaktion SCU3, um einen Überblick über alle Tabellen zu erhalten, für die die Tabellenprotokollierung aktiviert ist, sowie über die Änderungen an diesen Tabellen
- Konfigurieren Sie Alarme für wichtige Ereignisse, um auf Änderungen in den Tabellen zu reagieren

## Referenzen:
