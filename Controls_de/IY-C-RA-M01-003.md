---
Sicherheitsfunktion: IY
Kategorie: Risikobewertung
Technologie: ABAP
Reifegrad: 1
IPAC: Customizing (C)
Verteidiger: Prozess
Vorausgesetzt: IY-C-RA-M01-001, IY-C-RA-M01-004, IY-C-RA-M01-005
---

## Beschreibung

Schutz von sicherheitsrelevanten Daten.

SAP-Systeme enthalten große Mengen an geschäftskritischen Daten. Das SAP-Standardsystem bietet verschiedene Mechanismen, um diese kritischen Daten vor unberechtigtem Zugriff zu schützen.
Fehler in kundenspezifischen Entwicklungen können jedoch unbefugte Zugriffe und Datenverluste ermöglichen. Wenn sich ein Mitarbeiter unbefugt Zugang zu Daten verschafft, kann er diese Daten anschließend in eine Umgebung übertragen, die vom Unternehmen nicht mehr kontrolliert werden kann.


## Implementierung

1. Die Spezifikation der Änderung enthält eine knappe Beschreibung der erforderlichen Datenschutzanpassungen gemäß der Änderung.

2. Im Rahmen des Code Change Review-Prozesses muss der gesamte benutzerdefinierte Code auf folgende Eigenschaften überprüft werden:
  - Geschäftskritische Daten werden durch das Programm vor unbefugtem Zugriff geschützt werden.
  - Unternehmensregeln und insbesondere gesetzliche Vorschriften beachtet werden:
    - Umgang mit Anmeldedaten Diese Anforderungen an den Datenschutz müssen insbesondere bei der Verarbeitung und Verwaltung von Anmeldedaten beachtet werden. Dazu gehören neben Login-Tokens, Passwörtern und anderen möglichen Authentifizierungsfaktoren auch Benutzernamen und Identitätsinformationen von Benutzern. Authentifizierungsmerkmale müssen bei der Speicherung, der Übertragung und bei der Eingabe den Anforderungen strengster Vertraulichkeit genügen. Zum Beispiel:
      - Das Speichern von Kennwörtern im Quelltext von Programmen ist ein Verstoß gegen diese Anforderung.
      - Die Anzeige von Kennwörtern im Klartext auf Anmeldebildschirmen ist ein Verstoß gegen diese Anforderung.
      - Das Speichern von Passwörtern im Klartext in Datenbanktabellen oder im Datensystem ist ein Verstoß gegen diese Anforderung.
    Identitätsinformationen müssen auch in den von der Software erstellten Protokoll- und Ereignisdaten mit besonderer Sorgfalt gegen unbefugte und unangemessene Zugriffe geschützt werden.

## Überprüfung der Maßnahme

- Überprüfung, ob die Datenschutzanforderungen spezifiziert und dokumentiert sind und ihre Überprüfung im Testprotokoll der Änderung dokumentiert ist.
- Prüfen Sie, ob die Überprüfung des Quellcodes bei allen benutzerdefinierten Codeänderungen auf die korrekte Umsetzung der Datenschutzkriterien durchgeführt und dokumentiert wird.

## Referenzen

- CIS CSC 4
- COBIT 5 APO12.01, APO12.02, APO12.03, APO12.04
- ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12
- ISO/IEC 27001:2013 Klausel 6.1.2
- NIST SP 800-53 Rev. 4 RA-3, SI-5, PM-12, PM-16
- OWASP ASVS 2.0 V8.3.1, V8.3.4
