---
Sicherheitsfunktion: PT
Kategorie: Prozesse und Verfahren zum Schutz von Informationen
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Integration (I)
Verteidiger: Prozess
Voraussetzung:
---

## Beschreibung

Um die Remote Function Call (RFC)-Schnittstelle, die als Kommunikationsschnittstelle zwischen SAP-Systemen verwendet wird, richtig abzusichern, müssen alle RFC-Verbindungen, RFC-Berechtigungen und RFC-Schnittstellen berücksichtigt werden.

## Implementierung

Für alle RFC-Verbindungen muss eine einheitliche Verwaltungsvorgabe vorhanden sein; Eigentum und Nutzung der RFC-Verbindung sollten eindeutig dokumentiert sein. Außerdem muss ein vollständiges Inventar für alle RFC-Verbindungen definiert und dokumentiert werden.

Alle RFC-Verbindungen, die nicht verwendet werden, müssen gelöscht werden. (Die Dokumentation sollte dies ebenfalls widerspiegeln)


## Überprüfung der Maßnahme

- Feststellen, ob eine RFC-Verbindung verwendet wird, indem Sie die RFC-Laufzeitmonitor-Transaktion SRTM oder die Workload-Monitor-Transaktion ST03N verwenden.
- Löschen Sie alle nicht verwendeten RFC-Verbindungen.
- Vorgaben in Bezug auf bestehende RFC-Verbindungen sind verfügbar und auf dem neuesten Stand.

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A8 Absicherung der SAP-RFC-Schnittstelle/ Absicherung der SAP-RFC-Schnittstelle
- SAP Security Baseline Template V2.4.1: 2.3.2.3 [via SAP Security Optimization Services Portfolio](https://support.sap.com/sos)
