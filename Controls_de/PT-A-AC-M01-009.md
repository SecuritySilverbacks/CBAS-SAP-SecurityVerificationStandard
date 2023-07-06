---
Sicherheitsfunktion: PT
Kategorie: Benutzerverwaltung, Authentifizierung und Zugriffskontrolle
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Zugriff (A)
Verteidiger: Technologie
Vorraussetzung: PT-PA-IP-M01-001
---

## Beschreibung

SAP-Standardbenutzer müssen verwaltet und sicher konfiguriert werden, um jeglichen Missbrauch von SAP-Systemen zu verhindern. Dazu gehört das Ändern von Standardpasswörtern und die Einschränkung von Standardbenutzern.

## Implementierung

Die folgenden Standardbenutzer, die in ABAP-Systemen zu finden sind, müssen verwaltet und sicher konfiguriert werden: (Der Abschnitt Überprüfung der Maßnahme hilft Unternehmen dabei, die grundlegenden Anforderungen zur Sicherung dieser Benutzer zu erfüllen)
1. SAP*
2. DDIC
3. SAPCPIC
4. TMSADM
5. EARLYWATCH
6. Vom SAP Solution Manager angelegte Benutzer


## Überprüfung der Maßnahme

- SAP*
  - Muss in allen Mandanten vorhanden sein
  - Muss in allen Mandanten gesperrt sein
  - Standard-Passwort muss geändert werden
  - Muss in allen Mandanten der Gruppe SUPER angehören
  - Es darf kein Profil zugewiesen werden (insbesondere SAP_ALL)
  - der Profilparameter login/no_automatic_user_sapstar muss auf 1 gesetzt sein


- DDIC
  - Standard-Passwort muss geändert werden
  - Muss in allen Clients zur Gruppe SUPER gehören

- SAPCPIC
  - Löschen, wenn der Benutzer nicht benötigt wird
  - Falls erforderlich, muss das Standardkennwort geändert werden
  - Muss in allen Mandanten der Gruppe SUPER angehören

- TMSADM
  - Standard-Passwort muss geändert werden
  - Sollte nur in Mandant 000 existieren
  - Muss der Gruppe SUPER in Mandant 000 angehören
  - Berechtigungsprofil S_A.TMSADM darf nur vergeben werden

- EARLYWATCH
  - Der Benutzer sollte in keinem Client existieren

- Andere vom SAP Solution Manager angelegte Benutzer (SOLMAN_BTC, CONTENTSERV, SMD_BI_RFC, SMD_RFC, SMDAGENT_SAPSolutionManagerSID, SMD_ADMIN, SMD_AGT, SAPSUPPORT, SOLMAN_ADMIN)
  - Standard-Passwort muss geändert werden

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A4 Konfiguration und Absicherung der SAP-Benutzerverwaltung / Konfiguration und Absicherung der SAP-Benutzerverwaltung
- SAP Security Baseline Template V2.4.1: 2.3.1, 2.3.1.2.1 [via SAP Security Optimization Services Portfolio](https://support.sap.com/sos)
