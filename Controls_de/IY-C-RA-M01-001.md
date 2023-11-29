---
Sicherheitsfunktion: IY
Kategorie: Risikobewertung
Technologie: ABAP
Reifegrad: 1
IPAC: Customizing (C)
Verteidiger: Prozess
Voraussetzung:
---

## Beschreibung

Zugang & Autorisierung

ABAP verwendet ein meist explizites Berechtigungsmodell. Das bedeutet, dass eine Berechtigungsprüfung nur dann stattfindet, wenn ein Programm die Prüfung explizit selbst durchführt. Mit anderen Worten: Wenn es keine explizite Berechtigungsprüfung im Code gibt, wird auch nicht geprüft, ob ein Benutzer tatsächlich berechtigt ist.
In individuell entwickeltem Code werden Berechtigungsprüfungen häufig übersehen. Das bedeutet, dass das Berechtigungskonzept keine Wirkung hat. Dies führt zu Compliance-Verstößen, die im Falle eines Audits schwerwiegende Folgen haben können. Aus diesem Grund ist es von entscheidender Bedeutung, dass bei Eigenentwicklungen Berechtigungsprüfungen von den Programmen selbst durchgeführt werden, wo immer dies erforderlich ist, und dass alle Berechtigungsprüfungen auch aus formaler Sicht korrekt programmiert sind.
Neben dem Fehlen von Berechtigungsprüfungen kann auch die Strukturierung von Programmkomponenten die Tragfähigkeit des Berechtigungskonzepts beeinflussen. So sollten Sie z.B. hinterfragen, wie ausführbare Module zusammengesetzt sind, unter der Annahme, dass Schnittstellenberechtigungen nicht granular für die exponierte Geschäftsfunktionalität vergeben werden oder vergeben werden können.
Berechtigungsprüfungen sind in der Regel der häufigste Sicherheitsfehler in ABAP-Anwendungsentwicklungen.

## Implementierung

1. Die Spezifikation der Änderung enthält eine präzise Beschreibung der Anpassungen der Berechtigungsanforderungen entsprechend der Änderung.
2. Als Teil des Code Change Review-Prozesses muss der gesamte benutzerdefinierte Code daraufhin überprüft werden:
  - Alle Berechtigungsprüfungen verwenden SAP-Standardmechanismen. Dies bedeutet in der Regel, dass entweder:
    - der Befehl AUTHORITY-CHECK OBJECT oder
    - ein Modul, das speziell für die Prüfung einer bestimmten Berechtigung entwickelt wurde (wie der SAP-Funktionsbaustein 'AUTHORITY_CHECK_DATASET'),
    - oder eine Zugriffsdeklaration durch die Data Access Control (DAC)-Sprache für Core Data Services (CDS) muss verwendet werden.
  - Alle direkt ausführbaren Module implementieren explizite Zugriffsbeschränkungen beim Ausführungsstart, indem sie die Benutzerberechtigungen zum Starten des Moduls überprüfen
  - Bevor der Befehl CALL TRANSACTION ausgeführt wird, sollte eine Berechtigungsprüfung stattfinden, um sicherzustellen, dass der aktuelle Benutzer tatsächlich berechtigt ist, die Transaktion zu starten. Wird eine Transaktion mit dem Ziel aufgerufen, nur einen eingeschränkten Zugriff auf die Funktionalität der Transaktion zu ermöglichen, z.B. mit vordefinierten Auswahlwerten und dem Zusatz SKIP FIRST SCREEN, kann es sinnvoll sein, keine Berechtigungsprüfung für die Benutzerrechte zum Starten der Transaktion durchzuführen, da dies dem Benutzer unnötig hohe Privilegien abverlangen kann.
  - Die Implementierung prüft die Berechtigung des Benutzers so nah wie möglich an der Ausführung der geschützten Geschäftsfunktion.
  - Die Implementierung verarbeitet das Ergebnis der Überprüfung der Benutzerberechtigungen, um den rechtmäßigen Zugriff und die Ausführung zu erlauben und andere durch die Überprüfung von Rückgabecodes wie sy-subrc und Ausnahmen entsprechend der Implementierung der Prüfungen zu verbieten.

## Überprüfung der Maßnahme

- Prüfen Sie, ob negative und positive Zugriffskontrolltests spezifiziert sind und die Durchführung im Testprotokoll der Änderung dokumentiert ist.
- Prüfen Sie, ob die Überprüfung des Quellcodes für alle benutzerdefinierten Codeänderungen durchgeführt und dokumentiert wird, um die korrekte Implementierung der Benutzerzugriffskontrolle in der Änderung zu gewährleisten.


## Referenzen

- CIS CSC 4
- COBIT 5 APO12.05, APO13.02
- ISO/IEC 27001:2013 Klausel 6.1.3
- NIST SP 800-53 Rev. 4 PM-4, PM-9
- BSI APP (Februar 2020) 4.6 A1, A2, A3, A6, A7
- OWASP ASVS 2.0 V4.1.3, V4.1.4, V4.1.5
