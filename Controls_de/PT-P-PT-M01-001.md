---
Sicherheitsfunktion: PT
Kategorie: Schutztechnologie
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Technologie
Vorbedingung:
---

## Beschreibung

Security Audit Logs (SAL) müssen in der gesamten SAP-Umgebung aktiviert und richtig konfiguriert sein. Dies hilft den Sicherheitsteams, potenzielle Bedrohungen zu erkennen, die ihre Umgebung beeinträchtigen könnten.

## Implementierung

Es ist wichtig, dass Sie die Profilparameter für die Sicherheitsauditprotokolle aktivieren und richtig konfigurieren. Die folgenden Parameter helfen Ihnen dabei:

- Verwenden Sie die Transaktion RSAU_CONFIG oder SM19, um die erforderlichen Parameter einzustellen.
- rsau/enable = 1
- Geben Sie den Speicherort des Sicherheitsauditprotokolls an, indem Sie rsau/local/file setzen.
- rsau/integrity = 1
- rsau/log_peer_address = 1 (Hinweis: der Parameter kann zu Warnungen führen, die aber problemlos ignoriert werden können)
- rsau/selection_slots ≥ 10 5
- rsau/user_selection = 1
- Geben Sie die maximale Länge des Protokolls an, indem Sie den Parameter rsau/max_diskspace_local setzen.

Die folgenden Mindesteinstellungen des Security Audit Logs müssen vorgenommen sein:

- Auditing sollte aktiv sein
- Aktiver Filter für alle Benutzer für alle kritischen Ereignisse
- Protkollschutzformat aktiv

Es wird empfohlen, die Protokolle an einen zentralen Protokollserver zu senden, um die Protokolle besser analysieren und filtern zu können. Dies hilft auch dabei, die Größe auf dem eigentlichen System zu erhalten.

Mit der Transaktion RSAU_CONFIG können Sie je nach den Anforderungen Ihres Unternehmens weitere Parameter konfigurieren.

Hinweis: Referenz DT-P-AE-M01-002 Kontrollen zur Identifizierung von verfügbaren Protokollen, die für Ihre Anforderungen gesammelt werden können

## Überprüfung der Maßnahme

- Überprüfen Sie, ob die Sicherheitsauditprotokolle aktiviert sind, indem Sie den Parameter rsau/enable überprüfen.
- Überprüfen Sie, ob die Mindesteinstellungen für Security Audit Logs konfiguriert sind.
- Überprüfen Sie, ob alle Ereignisse für kritische Benutzer, wie SAP*, DDIC, SAPCPIC, Notfall- und Support-Benutzer, für alle Clients gesammelt und geprüft werden.
- Prüfen Sie, ob alle kritischen Ereignisse für alle Clients gesammelt und geprüft werden

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A21 Configuration of the Security Audit Log (S) / Konfiguration des Security Audit Logs (S)
- SAP Security Baseline Template V2.1: 2.4.3.1.1
- CIS CSC 1, 3, 5, 6, 14, 15, 16
- COBIT 5 APO11.04, BAI03.05, DSS05.04, DSS05.07, MEA02.01
- ISA 62443-2-1:2009 4.3.3.3.9, 4.3.3.5.8, 4.3.4.4.7, 4.4.2.1, 4.4.2.2, 4.4.2.4
- ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR 2.11, SR 2.12
- ISO/IEC 27001:2013 A.12.4.1, A.12.4.2, A.12.4.3, A.12.4.4, A.12.7.1
- NIST SP 800-53 Rev. 4 AU Familie
