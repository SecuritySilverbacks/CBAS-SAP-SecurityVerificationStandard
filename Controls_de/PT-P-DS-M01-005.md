---
Sicherheitsfunktion: PT
Kategorie: Datensicherheit
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Technologie
Voraussetzung:
---

## Beschreibung

Verzeichnis-/Pfadüberquerungsangriffe können unbefugten Zugriff auf Dateien oder Verzeichnisse ermöglichen, indem Anwendungen manipuliert werden, die physische oder logische Dateinamen als Eingabe verwenden. Dadurch können Angreifer sensible/kritische Dateien lesen oder beschreiben, was zur Offenlegung von Informationen und anderen Angriffen führen kann, die das System weiter ausbeuten.

## Implementierung

Die folgenden Schritte helfen, Schwachstellen zu entschärfen, bei denen ein Angreifer Dateinamen manipulieren kann, um von verschiedenen Anwendungsservern zu lesen oder zu schreiben.

- Aktualisieren Sie Ihren Kernel auf den neuesten Sicherheits-Patch-Level.
- Überprüfen Sie alle logischen Dateinamen und Dateipfaddefinitionen aus den Listenprogrammen RSFILECR oder RSFILENA, um die erforderlichen Anpassungen zu ermitteln
- Der Profilparameter abap/path_normalizartion sollte aktiviert sein (Wert 1).
- Pfade müssen normalisiert werden (siehe SAP-Hinweis 1497003 zur Normalisierung von Dateipfaden), wenn das Berechtigungsobjekt S_DATASET verwendet wird
- Pfade müssen normalisiert werden, wenn die Tabelle SPTH  Einträge enthält
- Wenn die Benutzeroberflächen die Eingabe von logischen Dateinamen erlaubt, definieren Sie Aliase für die verwendeten logischen Dateinamen

Hinweis: Stellen Sie sicher, dass Sie die Änderungen zunächst in der Testumgebung implementieren, bevor Sie sie auf die Produktionssysteme anwenden. So vermeiden Sie Fehler oder Serviceunterbrechungen auf den Produktionssystemen.

## Überprüfung der Maßnahme

- Identifizieren Sie logische Dateinamen aus dem Listenprogramm RSFILENA
- Identifizieren Sie logische Dateinamen und Dateipfaddefinitionen aus dem Listenprogramm RSFILECR
- Überprüfen Sie, ob der Profilparameter abap/path_normalization nicht deaktiviert ist

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A1 Sichere Konfiguration des SAP-ABAP-Stacks (B) / Secure Konfiguration des SAP-ABAP-Stacks (B)
- SAP Security Baseline Template V2.1: 2.2.1.3.1
- SAP-Hinweis 1497003
