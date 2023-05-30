---
Sicherheitsfunktion: PT
Kategorie: Benutzerverwaltung, Authentifizierung und Zugriffskontrolle
Technologie: Betriebssystem
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Technologie
Vorraussetzung: PT-P-IP-M01-012 PT-P-IP-M01-013
---

## Beschreibung

Die Autorisierung, die Berechtigung und der Zugriff für SAP-Standardbenutzer müssen innerhalb des verwendeten Betriebssystems ordnungsgemäß gesichert und konfiguriert werden.

## Implementierung

Wie lokale Benutzer und Domänenbenutzer auf einem Windows-Rechner müssen auch SAP-Standardbenutzer über die entsprechenden Rechte und Berechtigungen innerhalb des Betriebssystems verfügen.

- Beschränken Sie den Zugriff auf die Benutzer root, SAPsid und dbsid auf jedem System
- Sperren Sie den Benutzer dbsid nach der Erstinstallation für alle Anwendungsdienste
- SAPsid sollte keine Rechte für die interaktive Anmeldung haben

Hinweis: SAP-Systeme dürfen nicht auf Domänencontrollern installiert werden.

## Überprüfung der Maßnahme

- Überprüfen Sie, dass das SAP-System nicht auf dem Domänencontroller installiert ist.
- Überprüfen Sie, ob alle Einschränkungen für SAP-Benutzer in Kraft sind.


## Referenzen
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A16 Implementierung von Sicherheitsanforderungen für das Betriebssystem Windows (S) / Umsetzung von Sicherheitsanforderungen für das Betriebssystem Windows (S)
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A17 Implementierung von Sicherheitsanforderungen für das Betriebssystem Unix (S) / Umsetzung von Sicherheitsanforderungen für das Betriebssystem Unix (S)
- CIS CSC 3, 5, 12, 14, 15, 16, 18
- COBIT 5 DSS05.04
- ISA 62443-2-1:2009 4.3.3.7.3
- ISA 62443-3-3:2013 SR 2.1
- ISO/IEC 27001:2013 A.6.1.2, A.9.1.2, A.9.2.3, A.9.4.1, A.9.4.4, A.9.4.5
- NIST SP 800-53 Rev. 4 AC-1, AC-2, AC-3, AC-5, AC-6, AC-14, AC-16, AC-24
