---
Sicherheitsfunktion: PT
Kategorie: Identitätsmanagement, Authentifizierung und Zugriffskontrolle
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Zugriff (A)
Verteidiger: Technologie
Vorbedingung:
---

## Beschreibung

Der Zugriff auf SAP-Datenbanken muss vor unberechtigtem Zugriff und Missbrauch geschützt werden.  

## Implementierung

SAP Benutzer dürfen grundsätzliche keinen Zugriff auf die SAP-Systemdatenbank erhalten. Sonstige Benutzern müssen spezifische Datenbankberechtigungen gemäß des Minimalitätsprinzips und der Aufgabentrennung erhalten.

Überprüfen Sie die Transaktionsprotokolldatei auf nicht benötigte Datenbankbenutzer. Die Transaktionsdatei können Sie durch Ausführen von R3trans -d einsehen.

Benutzer, die auf die Datenbank zugreifen dürfen, sind nur auf die für Ihre Aufgabe notwendigen Tabellen zu beschränken

## Überprüfung der Maßnahme

- SAPR3, SAPSID oder SAPABAP1 für den Zugriff auf die Datenbank deaktiviert.
- Benutzer, die nicht für den Zugriff auf die Datenbank benötigt werden, werden entfernt.
- Datenmanipulation sind nur dem SAP-Support gestattet
- Benutzer, die auf die Datenbank zugreifen müssen, erhalten keine Berechtigungen für die Tabelle USR\*, die Tabelle T000, SAPUSER, RFCDES, PA\*, HCL\* und alle anderen Tabellen, die für ihre Arbeit nicht erforderlich sind

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A7 Absicherung der SAP-Datenbank/ Absicherung der SAP-Datenbanken
