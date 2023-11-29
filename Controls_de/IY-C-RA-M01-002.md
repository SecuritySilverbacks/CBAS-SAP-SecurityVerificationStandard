---
Sicherheitsfunktion: IY
Kategorie: Risikobewertung
Technologie: ABAP
Reifegrad: 1
IPAC: Customizing (C)
Verteidiger: Prozess
Voraussetzung ist: IY-C-RA-M01-001
---

## Beschreibung

Testbarkeit von ABAP-Software-Implementierungen.

Ein zentrales Sicherheitskonzept des SAP-Standardsystems ist die Trennung von Entwicklungs-, Test- und Produktivsystemen.
Das Testsystem spielt dabei eine wichtige Rolle. Im Testsystem wird die Entscheidung getroffen, ob eine Anwendung den Anforderungen des Unternehmens gerecht wird. Dabei werden sowohl funktionale als auch nicht-funktionale Qualitätsaspekte der Anwendung geprüft. Damit eine Qualitätsprüfung zuverlässige Ergebnisse liefert, reicht es nicht aus, dass der Tester über umfassende Fachkenntnisse im Bereich der Qualitätssicherung verfügt. Die Anwendung selbst muss auch testbar sein. Das bedeutet, dass ein Tester die Anwendung zu Testzwecken ausführen kann und dass der Tester im Zweifelsfall den Quellcode der Anwendung analysieren kann.

Wenn eine bestimmte Funktionalität in einer Anwendung nicht (von einem Tester) im Testsystem ausgeführt werden kann, kann der Tester nicht feststellen, ob sie die Qualitätsanforderungen erfüllt. In diesem Fall würde ungeprüfter Code in ein produktives System übertragen werden und das System einem ungeprüften Risiko aussetzen.

## Implementierung

1. Alle Eigenentwicklungen, die in Systemen zur Verarbeitung produktiver Daten eingesetzt werden sollen, müssen testbar sein. Das bedeutet, dass alle Funktionen dokumentiert sind und in einem Testsystem analysiert und ausgeführt werden können.

2. Kundenspezifische Entwicklungen, die nicht in Systemen zur Verarbeitung produktiver Daten verwendet werden sollten, dürfen nicht in entsprechende Systemen ausgeliefert werden

3. Im Rahmen der Überprüfung von Codeänderungen muss der gesamte benutzerdefinierte Code daraufhin überprüft werden, dass:
  - die Sicherheitsanforderungen mit standardisierten und nachvollziehbaren Verfahren umgesetzt werden. Verschleierung keine valide Sicherheitsstrategie.
  - die Änderung eine Architektur implementiert und  Schnittstellen so verwendet, dass Sicherheitsmechanismen zum Schutz der Geschäftslogik nicht durch Seiteneffekte oder durch die Wiederverwendung von Komponenten der Implementierung umgangen werden können.
  - eine Techniken zur Codeverschleierung wie die ab ABAP Release 7.4x verfügbare Funktion zum Verbergen von Code verwendet wird.
  - die Implementierung sich nicht darauf beschränkt, Code auf der Grundlage von systemspezifischen Variablen wie sy-mandt und sy-sysid auszuführen. Dadurch erhält ein ABAP-Programm die Informationen über das ausführende System, in dem es gerade ausgeführt wird, den die Tests für Zielsystem nicht entsprechend simulieren können.

## Überprüfung der Maßnahme

- Prüfen Sie, ob Testausführungskriterien und -pfade festgelegt und dokumentiert sind und ihre Ausführung im Testprotokoll der Änderung dokumentiert ist.
- Prüfen Sie, ob die Überprüfung des Quellcodes für alle benutzerdefinierten Codeänderungen durchgeführt und dokumentiert wird, um die korrekte Implementierung der Testbarkeit in der Änderung zu gewährleisten.

## Referenzen

- CIS CSC 4
- COBIT 5 APO12.01, APO12.02, APO12.03, APO12.04
- ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12
- ISO/IEC 27001:2013 Klausel 6.1.2
- NIST SP 800-53 Rev. 4 RA-3, SI-5, PM-12, PM-16
- BSI APP (Februar 2020) 4.6 A16, A21
