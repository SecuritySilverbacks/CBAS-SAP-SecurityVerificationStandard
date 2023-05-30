---
Sicherheitsfunktion: PT
Kategorie: Benutzerverwaltung, Authentifizierung und Zugriffskontrolle
Technologie: SAP HANA
Reifegrad: 1
IPAC: Zugriff (A)
Verteidiger: Technologie
Vorraussetzung: PT-PA-IP-M01-001
---

## Beschreibung

SAP-Standardbenutzer müssen verwaltet und sicher konfiguriert werden, um jeglichen Missbrauch von SAP-Systemen zu verhindern. Dazu gehört das Ändern von Standardpasswörtern und die Einschränkung von Standardbenutzern.

## Implementierung

Die folgenden Standardbenutzer, die in HANA zu finden sind, müssen verwaltet und sicher konfiguriert werden: (Der Abschnitt Überprüfung der Maßnahme hilft Unternehmen, die grundlegenden Anforderungen für die Sicherheit der Benutzer zu erfüllen)
1. SYSTEM


## Überprüfung der Maßnahme

- SYSTEM
  - Administrator-Benutzer wurden erstellt
  - SYSTEM-Benutzer soll deaktiviert werden
  - Gültige Zeitspanne des Benutzers SYSTEM nicht einschränken

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A4 Konfiguration und Absicherung der SAP-Benutzerverwaltung / Konfiguration und Absicherung der SAP-Benutzerverwaltung
- SAP Security Baseline Template V2.1: 2.3.1.2.2
