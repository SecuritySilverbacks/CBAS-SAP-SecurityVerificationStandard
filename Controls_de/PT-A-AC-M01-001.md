---
Sicherheitsfunktion: PT
Kategorie: Benutzerverwaltung, Authentifizierung und Zugriffskontrolle
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Zugriff (A)
Verteidiger: Prozess
Vorbedingung:
---

## Beschreibung

Die SAP-Benutzerverwaltung sollte nur ausgewählten Administratoren gestattet sein und über die entsprechenden Rechte verfügen, um die Erstellung, das Löschen, die Zuweisung von Rollen und Profilen sowie die Passwortverwaltung von Benutzern durchzuführen.

## Implementierung

Rechte zur Verwaltung von Benutzern in SAP sollten nur an Benutzer vergeben werden, die dieselbe Jobrolle haben oder von der Organisation ausgewählt wurden(1).

Die Protokollierung und Überwachung von SAP-Administratoren erleichtert die Identifizierung von administrativem Missbrauch.

(1) - Die meisten Benutzeradministratoren kommen aus der IT-Abteilung eines Unternehmens. Einige Unternehmen überlassen die Benutzerverwaltung der Personalabteilung, was vorzuziehen ist.


## Überprüfung der Maßnahme

- Identifizieren Sie die SAP-Benutzeradministratoren und überprüfen Sie, ob diese Rollen nur erlaubten Benutzern zugewiesen werden.
- Protokolle sind verfügbar, um den Missbrauch von administrativen Aktionen zu überprüfen
- Überwachung ist verfügbar, um jeglichen Missbrauch bei der Benutzerverwaltung aufzudecken

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A5 Konfiguration und Absicherung der SAP-Benutzerverwaltung / Konfiguration und Absicherung der SAP-Benutzerverwaltung
- SAP Security Baseline Template V2.1: 2.3.1
- CIS CSC 1, 5, 15, 16
- COBIT 5 DSS05.04, DSS06.03
- ISA 62443-2-1:2009 4.3.3.5.1
- ISA 62443-3-3:2013 SR 1.1, SR 1.2, SR 1.3, SR 1.4, SR 1.5, SR 1.7, SR 1.8, SR 1.9
- ISO/IEC 27001:2013 A.9.2.1, A.9.2.2, A.9.2.3, A.9.2.4, A.9.2.6, A.9.3.1, A.9.4.2, A.9.4.3
- NIST SP 800-53 Rev. 4 AC-1, AC-2, IA-1, IA-2, IA-3, IA-4, IA-5, IA-6, IA-7, IA-8, IA-9, IA-10, IA-11
