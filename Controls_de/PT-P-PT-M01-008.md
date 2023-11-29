---
Sicherheitsfunktion: PT
Kategorie: Schutztechnologie
Technologie: SAP HANA
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Technologie
Vorbedingung:
---

## Beschreibung

Security Audit Logs (SAL) müssen in der gesamten SAP-Umgebung aktiviert und richtig konfiguriert sein. Dies hilft den Sicherheitsteams, potenzielle Bedrohungen, die ihre Umgebung beeinträchtigen könnten, zu identifizieren und zu erkennen.

## Implementierung

Es ist wichtig, dass Sie den Audit Trail für HANA in der SAP HANA Administration Console aktivieren und richtig konfigurieren. Die folgenden Parameter helfen Ihnen dabei:

- global_auditing_state = true in der Datei global.ini, Abschnitt Überwachungskonfiguration (auditing configuration)
- Die Audit-Richtlinien sollten entsprechend den Sicherheitsanforderungen des Unternehmens konfiguriert werden.
- Setzen Sie default_audit_trail_type = SYSLOGPROTOCOL oder CSTABLE in der Datei global.ini, Abschnitt auditing configuration. Weitere Informationen zum Audit Trail Layout finden Sie [hier](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/0a57444d217649bf94a19c0b68b470cc.html)

Hinweis: Kritische Benutzer müssen überwacht werden

## Überprüfung der Maßnahme

- Überprüfen Sie, ob die Sicherheitsauditprotokolle aktiviert sind, indem Sie den Parameter global_auditing_state = true in der Datei global.ini, Abschnitt auditing configuration, überprüfen.
- Überprüfen Sie, ob alle Ereignisse für kritische Benutzer gesammelt und geprüft werden.
- Überprüfen Sie, dass die CSV-Datei nicht für die Protokollierung sicherheitskritischer Informationen verwendet wird.

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A21 Configuration of the Security Audit Log (S) / Konfiguration des Security Audit Logs (S)
- SAP Security Baseline Template V2.4.1: 2.4.3.1.3 [via SAP Security Optimization Services Portfolio](https://support.sap.com/sos)
- [SAP HANA Audit Trails](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/db560e7bbb57101490d4a1364440077f.html)
- CIS CSC 1, 3, 5, 6, 14, 15, 16
- COBIT 5 APO11.04, BAI03.05, DSS05.04, DSS05.07, MEA02.01
- ISA 62443-2-1:2009 4.3.3.3.9, 4.3.3.5.8, 4.3.4.4.7, 4.4.2.1, 4.4.2.2, 4.4.2.4
- ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR 2.11, SR 2.12
- ISO/IEC 27001:2013 A.12.4.1, A.12.4.2, A.12.4.3, A.12.4.4, A.12.7.1
- NIST SP 800-53 Rev. 4 AU Familie
