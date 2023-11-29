---
Sicherheitsfunktion: PT
Kategorie: Prozesse und Verfahren zum Schutz von Informationen
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Plattform (P)/ Zugriff (A)
Verteidiger: Prozess & Technologie
Voraussetzung: PT-A-AC-M01-009
---

## Beschreibung

 Standard-Benutzer, die auf SAP-Systeme zugreifen dürfen, sollten ordnungsgemäß verwaltet und konfiguriert werden. Auf diese Weise können Unternehmen das Prinzip der geringsten Privilegien befolgen.

## Implementierung

Die Standardpasswörter für die Standard-Benutzer sollten geändert werden und die Passwortrichtlinie des Unternehmens(1) sollte angewendet werden.

Standard-Benutzer, die nicht benötigt werden, sollten gelöscht oder deaktiviert werden.

Obsolete standard-Benutzer wie EARLYWATCH sollten in keinem Client existieren.

(1) - Passwortrichtlinien ändern sich von Unternehmen zu Unternehmen, abhängig von verschiedenen Kriterien wie der Kritikalität der Branche, lokalen oder bundesstaatlichen Gesetzen, Sicherheitsstandards, die für die Branche verbindlich sind, usw.

## Überprüfung der Maßnahme

- Standard-Passwort für Standard-Benutzer-IDs wird geändert
- Die Kennwortrichtlinie wird in allen SAP-Systemen ordnungsgemäß angewendet.
- Standard-Benutzer werden gelöscht und deaktiviert, wenn sie nicht verwendet werden

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A4 Absicherung der ausgelieferten SAP-Standardbenutzer-IDs / Absicherung der ausgelieferten SAP-Standardbenutzer-Kennungen
- SAP Security Baseline Template V2.4.1: 2.3.1 [via SAP Security Optimization Services Portfolio](https://support.sap.com/sos)
