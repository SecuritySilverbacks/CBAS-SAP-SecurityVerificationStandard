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

Protokolle der Sicherheitsüberprüfung:

Die Identifizierung und Erfassung sicherheitsrelevanter Aktivitäten ist wichtig für die Sammlung von Beweisen nach einem Sicherheitsvorfall oder Ereignis. Das Sicherheitsprotokoll kann sensible Daten enthalten, die ordnungsgemäß gespeichert und verschlüsselt werden müssen.  

## Implementierung

Die Aktivierung von Sicherheitsauditprotokollen hängt davon ab, welche Protokolle Ihr Unternehmen sammeln möchte. Die verfügbaren Protokolle sind unten aufgeführt:

- Erfolgreiche und erfolglose Dialog-Anmeldeversuche
- Erfolgreiche und erfolglose RFC-Anmeldeversuche
- RFCs zu Funktionsbausteinen
- Änderungen an Benutzerstammsätzen
- Erfolgreiche und erfolglose Transaktionsstarts
- Erfolgreiche und erfolglose Reportstarts
- Änderungen an der Audit-Konfiguration
- Aktivierung und Deaktivierung der HTTP-Sicherheitssitzungsverwaltung oder Instanzen, in denen HTTP-Sicherheitsabschnitte hart verlassen wurden
- Datei-Downloads
- Zugriffe auf das Dateisystem, die mit den im System angegebenen gültigen logischen Pfaden und Dateinamen übereinstimmen (besonders hilfreich in einer Analysephase, um festzustellen, wo der Zugriff auf Dateien stattfindet, bevor die eigentliche Überprüfung aktiviert wird)
- ICF-Recorder-Einträge oder Änderungen an den Verwaltungseinstellungen
- Die Valididerung von digitalen Signaturen, die vom System durchgeführt werden
- Viren, die von der Viren-Scan-Schnittstelle gefunden wurden
- Fehler, die in der Viren-Scan-Schnittstelle auftreten
- Erfolglose Passwortprüfungen für einen bestimmten Benutzer in einem bestimmten Client

Personenbezogene Daten können in bestimmten Sicherheitsprotokollen zu finden sein. Achten Sie darauf, dass Sie bei der Speicherung personenbezogener Daten alle Datenschutzbestimmungen einhalten, die für Ihr Unternehmen gelten.

Warnungen können konfiguriert werden, wenn ein bestimmtes Ereignis eintritt oder ein Schwellenwert erreicht wird. Dies trägt dazu bei, den Überprüfungsprozess von Sicherheitsauditprotokollen zu automatisieren und die Arbeitsbelastung der Administratoren zu verringern. Das Versenden von Protokollen an eine zentrale Stelle hilft bei der Einrichtung von Alarmen.

## Überprüfung der Maßnahme

- Konfigurieren Sie Alarme für wichtige Ereignisse, um reaktiv auf Sicherheitsereignisse zu reagieren


## Referenzen:
