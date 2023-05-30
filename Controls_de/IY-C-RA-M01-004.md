---
Sicherheitsfunktion: IY
Kategorie: Risikobewertung
Technologie: ABAP
Reifegrad: 1
IPAC: Customizing (C)
Verteidiger: Prozess
Bedingung: _Eine Kontrolle, die vor der aktuellen vorhanden sein muss_
---

## Beschreibung

Prävention von Injektionsschwachstellen

Injektionsschwachstellen beziehen sich auf Situationen, in denen ein Angreifer Steuerzeichen und/oder Befehle über den Datenkanal (Eingabe) in eine Anwendung einschleust. Ein erfolgreicher Angriff kann sich durch unerwartete Befehle schädlich auf den geplanten Programmablauf auswirken.
Je nach Art der Injektion kann ein Angreifer die vollständige Kontrolle über das betroffene SAP-System erlangen. Für die Programmiersprache ABAP umfasst dies insbesondere Implementierungen mit:
- Zugriff auf das Dateisystem von Dateiservern oder von den SAP-Betriebssystemen zum Austausch oder zur Verarbeitung von Daten erfolgt. Mit der Anzahl der Schnittstellen (Anwendungen) steigt für jede einzelne Schnittstelle das Risiko, kompromittierte Daten zur Verarbeitung zu erhalten oder solche Daten durch fehlerhafte Eingaben selbst zu erzeugen.

- Verwendung von Betriebssystembefehlen über ABAP-Programme. Der Systemzugriff erfolgt im Kontext des SAP-Systemdienstbenutzers. Dieser Benutzer verfügt notwendigerweise über weitreichende Privilegien im Betriebssystem. In Anbetracht des daraus resultierenden Gesamtrisikos sollte ABAP-Code, der Betriebssystembefehle ausführt, besonders geschützt werden.

- Verwendung der dynamischen ABAP-Sprachfunktionen und des Datenbankzugriffs. Die Möglichkeiten zur Verwendung der dynamischen ABAP-Programmierung und des Zugriffs auf Datenbanken sind vielseitig einsetzbar. Sie sind jedoch auch mit besonderen Risiken verbunden. Wenn eine dynamische Programmierung notwendig ist, muss der Entwickler diesen Risiken durch besondere Schutzmaßnahmen Rechnung tragen.

## Implementierung

1. Im Rahmen der Änderungsprüfung muss das Design der Implementierung auf die folgenden Eigenschaften hin überprüft werden:
    - Bei der Verarbeitung von Eingaben muss normalerweise eine ausreichende Plausibilitätsprüfung durchgeführt werden. Dies wird als "Eingabevalidierung" bezeichnet. Die Eingabevalidierung bietet nicht nur einen grundlegenden Sicherheitsschutz (da Steuerzeichen und Sonderzeichen in den meisten Datenfeldern unwirksam sind und entfernt werden können), sondern verbessert auch die Datenqualität im Allgemeinen. Die Eingabevalidierung sollte so implementiert werden, dass die Eingaben mit einer Liste zulässiger Werte verglichen werden, d.h. mit dem Ansatz des "Allowlist-Filters".
    - Besondere Vorsicht ist geboten, wenn Benutzereingaben mit Steuerzeichen oder Sprachelementen (Semantik) vermischt werden und das Ergebnis dann als Ganzes verarbeitet oder ausgeführt wird. In diesem Fall müssen alle Steuerzeichen in den Daten, die im Kontext relevant sind, unschädlich gemacht werden. Dieser Vorgang wird je nach Ausgabekontext als "Ausgabekodierung" oder "Sanitisierung" bezeichnet.
      Insbesondere die Umsetzung der folgenden Maßnahmen sollte validiert werden:
      - Indirektion: Die Ausführung von kritischem Code sollte so weit wie möglich von der Eingabe entkoppelt werden
      - Plausibilität: Bereichsprüfungen, Allowlists und/oder Denylists sollten verwendet werden, um den Wertebereich der Eingabe auf plausible Werte zu beschränken.
      - Kontext-Validierung: Vor der Ausführung muss eine Kontrolllogik ablaufen, die die Ausführungsberechtigung des Programms, des Benutzers und der Eingabe ausreichend prüft.
      - Nachvollziehbarkeit: Es sollte in Betracht gezogen werden, die Ausführung sensibler Geschäftslogik für den Kontext des Benutzers, die Ausführungszeit und die Eingabe ausreichend zu protokollieren.
      - Äquivalenz: Bei dynamisch ausgeführtem Code muss das gleiche Maß an Kontrolle ablaufen wie bei einer gleichwertigen statischen Implementierung, die den im Falle einer korrekten statischen Implementierung der Codeausführung entspricht.

2. Im Rahmen des Änderungstests müssen alle Implementierungen auf den Schutz vor eingabebasierten Angriffen überprüft werden, wenn geeignete ABAP-Techniken in der Implementierung verwendet werden.
    - Traversierung von Verzeichnissen und Dateien.
    - Injektion von Betriebssystembefehlen.
    - SQL-Injektion.
    - Ausprobier-Attacken.
    - ABAP-Code-Injektion.

## Überprüfung der Maßnahme

- Prüfen Sie, ob für alle Änderungen am benutzerdefinierten Code eine Überprüfung des Quellcodes durchgeführt und dokumentiert wurde, um Schwachstellen bei Injektion und Bereinigung zu identifizieren.
- Prüfen Sie, ob die Änderung ausreichend auf die oben genannten Sicherheitslücken getestet und dokumentiert wurde.

## Referenzen

- CIS CSC 4
- COBIT 5 APO12.01, APO12.02, APO12.03, APO12.04
- ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12
- ISO/IEC 27001:2013 Klausel 6.1.2
- NIST SP 800-53 Rev. 4 RA-3, SI-5, PM-12, PM-16
- OWASP ASVS 2.0 V5.1, V5.3
- BSI APP (Februar 2020) 4.6 A7, A8, A11, A13, A18
