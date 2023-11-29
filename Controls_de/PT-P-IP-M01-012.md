---
Sicherheitsfunktion: PT
Kategorie: Prozesse und Verfahren zum Schutz von Informationen
Technologie: Linux
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Technologie
Vorbedingung:
---

## Beschreibung

Die Stärkung und Härtung des Betriebssystems, auf dem das SAP-System des Unternehmens läuft, ist entscheidend für die Sicherheit Ihrer SAP-Implementierung und Ihres Netzwerks.

## Implementierung

Wenn Ihr Unternehmen andere Anwendungen unter Linux einsetzt, sollte es bereits eine definierte Baseline für den Einsatz von Linux-Maschinen geben. Im Folgenden finden Sie einige Bereiche, die Sie bei der Absicherung von SAP-Systemen unter Linux im Auge behalten sollten.

 - Verbieten Sie externe Root-Anmeldungen
 - Entfernen Sie nicht benötigte Dienste und Konten
 - Entfernen Sie alle nicht benötigten Linux-Anwendungen, Funktionen, Rollen und Komponenten
 - Deaktivieren Sie die Verwendung von X-Window-Systemen (SAP-Anwendungen benötigen sie nicht)
 - Verwenden Sie kein Telnet oder FTP für die Dateiübertragung
 - Regelmäßig Updates einspielen
 - Vermeiden Sie die Verwendung von SUID/SGID mit möglicherweise schwachstellenbehafteten Programmen
 - Dateien werden durch die Konfiguration der Standard-Dateimaske mit den entsprechenden Berechtigungen erstellt
 - Überprüfen Sie regelmäßig Signaturen und Schlüssel von heruntergeladenen Anwendungen oder Patches

Es wird empfohlen, die Vorgaben des Unternehmens für die Absicherung von Linux-Rechnern zu befolgen, sofern sie existieren.

Wenn Ihr Unternehmen SUSE Linux für das Hosting von SAP-Anwendungen verwendet, sollten Sie die folgenden Punkte beachten:

- Installieren und konfigurieren Sie den SUSE Security Checker (seccheck), um Benachrichtigungen über alle Sicherheitsänderungen zu aktivieren.

## Überprüfung der Maßnahme

- Überprüfen Sie, ob unerwünschte Anwendungen, Dienste, Funktionen, Rollen und Komponenten entfernt wurden
- Überprüfen Sie, ob die Dateiberechtigungen richtig konfiguriert sind.
- Überprüfen Sie, ob Telnet und FTP nicht verwendet werden
- Überprüfen Sie, ob regelmäßig Sicherheitsupdates durchgeführt werden

## Referenzen
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A16 Implementierung von Sicherheitsanforderungen für das Betriebssystem Windows (S) / Umsetzung von Sicherheitsanforderungen für das Betriebssystem Windows (S)
