---
Sicherheitsfunktion: PT
Kategorie: Schutztechnologie
Technologie: SAP Java
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Technologie
Voraussetzung:
---

## Beschreibung

Security Audit Logs (SAL) müssen in der gesamten SAP-Umgebung aktiviert und richtig konfiguriert sein. Dies hilft den Sicherheitsteams, potenzielle Bedrohungen zu erkennen, die ihre Umgebung beeinträchtigen könnten.

## Implementierung

Es ist wichtig, dass Sie die UME-Eigenschaften in Bezug auf Sicherheitsauditprotokolle aktivieren und richtig konfigurieren. Die folgenden Parameter helfen Ihnen dabei:

- ume.secaudit.get_object_name = TRUE
- ume.secaudit.log_actor = TRUE
- ume.logon.security_policy.log_client_hostaddress = TRUE
- ume.logon.security_policy.log_client_hostname = FALSE (erfordert DNS-Lookup, was die Systemleistung beeinträchtigt)
- enable.xml.hardener = TRUE

Es wird empfohlen, das Loglevel der protokollierten Informationen entsprechendem dem Schutzbedarf der Anwendung anzupassen. Der minimale Schweregrad sollte auf *"Info"* gesetzt werden..

## Überprüfung der Maßnahme

- Überprüfen Sie, ob die UME-Eigenschaften der Sicherheitsauditprotokolle konfiguriert sind.
- Überprüfen Sie, was protokolliert wird, indem Sie sich beim Netweaver Administrator anmelden und dann zu -> Fehlerbehebung -> Protokolle und Traces -> Protokollkonfiguration navigieren und im Feld Anzeigen die Option 'Protokollierungskategorien' wählen.
- Überprüfen Sie die Logleveleinstellungen auf den zu protokollierenden Schweregrad.

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A21 Configuration of the Security Audit Log (S) / Konfiguration des Security Audit Logs (S)
- SAP Security Baseline Template V2.4.1: 2.4.3.1.2 [via SAP Security Optimization Services Portfolio](https://support.sap.com/sos)
- [SAP-Hinweis 2372626](https://launchpad.support.sap.com/#/notes/2372626)
- CIS CSC 1, 3, 5, 6, 14, 15, 16
- COBIT 5 APO11.04, BAI03.05, DSS05.04, DSS05.07, MEA02.01
- ISA 62443-2-1:2009 4.3.3.3.9, 4.3.3.5.8, 4.3.4.4.7, 4.4.2.1, 4.4.2.2, 4.4.2.4
- ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR 2.11, SR 2.12
- ISO/IEC 27001:2013 A.12.4.1, A.12.4.2, A.12.4.3, A.12.4.4, A.12.7.1
- NIST SP 800-53 Rev. 4 AU Familie
