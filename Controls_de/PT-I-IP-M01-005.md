---
Sicherheitsfunktion: PT
Kategorie: Prozesse und Verfahren zum Schutz von Informationen
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Integration (I)
Verteidiger: Technologie
Voraussetzung ist: PT-I-P-M01-001
---

## Beschreibung

RFC-Gateways sind häufig auf ABAP-, Java- und Standalone-Systemen zu finden. Die Sicherung des Zugriffs auf die RFC-Dienste verhindert den unauthentifizierten und nicht-berechtigten Zugriff.

## Implementierung

Für die verschiedenen Systeme sollten Profilparameter festgelegt werden, um den Zugriff von verschiedenen RFC-Verbindungen aus zu beschränken.

Profil-Parameter:

1. gw/sec_info muss auf Dateiname secinfo (ACL-Datei) gesetzt werden
2. gw/reg_info muss auf den Dateinamen reginfo (ACL-Datei) gesetzt werden
3. gw/reg_no_conn_info auf 1 oder höhere ungerade Zahlen gesetzt
4. gw/acl_mode auf 1 gesetzt (anfängliche Sicherheitsumgebung), wenn Gateway-Zugriffslisten nicht existieren oder nicht mit den Profilparametern verknüpft sind, kann das Setzen dieses Profilparameters Verbindungen unterbrechen.
5. gw/monitor auf 1 gesetzt (Überwachung nur auf lokalen Zugriff eingestellt)
6. gw/sim_mode auf 0 gesetzt (kann vorübergehend auf 1 gesetzt werden, um ACL-Dateien zu testen und fehlende Einträge zu finden, die der ACL hinzugefügt werden müssen. Belassen Sie den Wert nicht auf 1)
7. gw/rem_start auf disable oder SSH_SHELL gesetzt (eine akzeptable Methode, um den Start von Programmen über das RFC-Gateway zu ermöglichen)

## Überprüfung der Maßnahme

- Profilparameter werden gemäß dem Abschnitt zur Implementierung eingestellt
- Fehlende Einträge werden überprüft und wenn nötig der Zugriffskontrollliste hinzugefügt (siehe Nr. 6 im Abschnitt zur Implementierung)

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A8 Absicherung der SAP-RFC-Schnittstelle/ Absicherung der SAP-RFC-Schnittstelle
- SAP Security Baseline Template V2.0: 2.3.2.3.1
- SAP-Hinweis 1480644
- SAP-Hinweis 1408081
- SAP-Hinweis 1444282
- SAP-Hinweis 1298433
- SAP-Hinweis 64016
- SAP-Hinweis 1689663
