---
Sicherheitsfunktion: PT
Kategorie: Prozesse und Verfahren zum Schutz von Informationen
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Integration (I)
Verteidiger: Prozess
Voraussetzung ist: PT-I-IP-M01-001
---

## Beschreibung

Die Verwaltung von RFC-Verbindungen zwischen verschiedenen Systemen mit unterschiedlichen Klassifizierungsstufen ist erforderlich, um die Ausweitung von Rechten auf sensible oder Produktionssysteme zu verhindern.

## Implementierung

Als Faustregel gilt, dass Verbindungen von Systemen niedrigerer Klassifizierung, wie z.B. Entwicklungs- oder Testsystemen, zu Systemen hoher Klassifizierung, wie z.B. Produktionssystemen, keine Vertrauensstellungen (Trust Relations) zur Systemanmeldung verwenden oder Benutzeranmeldedaten des Zielsystems speichern sollten.
Die Daten der Verbindungskonfiguration sind das einzige, was in den verschiedenen Systemen gespeichert werden kann. Entsprechend muss die Anmeldung mittels des jeweiligen Benutzers im Zielsystem durch Authentifizierung erfolgen.


## Überprüfung der Maßnahme

- Authentifizierung ist bei jeder Verbindung von einem niedrigeren zu einem höheren Klassifizierungssystem erforderlich
- Um RFC-Verbindungen zu ermitteln, die Benutzer-Credentials speichern, verwenden Sie den Report RSRFCCHK in allen Systemen lokal
- Schränken Sie die Berechtigung zur Pflege von RFC-Destinationen in Transaktion SM59 ein, indem Sie das Berechtigungsobjekt S_RFC_ADM streng kontrollieren.

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A8 Absicherung der SAP-RFC-Schnittstelle/ Absicherung der SAP-RFC-Schnittstelle
- SAP Security Baseline Template V2.0: 2.3.2.3
