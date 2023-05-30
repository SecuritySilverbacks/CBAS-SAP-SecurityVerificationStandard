---
Sicherheitsfunktion: PT
Kategorie: Schutztechnologie
Technologie: SAP Java
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Technologie
Vorbedingung:
---

## Beschreibung

Der Schutz vor böswilligem oder unerkanntem Zugriff auf die Anwendungsserver über den Message Server ist entscheidend für die Aufrechterhaltung der Integrität, Verfügbarkeit und Vertraulichkeit der verschiedenen Anfragen zwischen den Anwendungsservern eines SAP-System, dass in Form eines Clusters betrieben wird.

## Implementierung

Ein Netzwerkgerät, das als abtrünniger Anwendungsserver fungiert, kann ein hohes Risiko für das Unternehmen darstellen, wenn die Kommunikation mit legitimen Anwendungsservern zugelassen wird..

Für den Message Server müssen Zugriffskontrolllisten (ACLs) konfiguriert werden, um Angriffe auf die Vertrauensstellung zwischen legitimen Anwendungsservern einzudämmen und abzuwehren.

- Profilparameter ms/acl_info ist im Default Profil angelegt und verweist auf eine gültige ACL-Datei.
- ACL-Datei sollte keinen Eintrag enthalten, der alle Hosts zulässt (d.h. HOST=* ist kritisch)
- Trennen Sie die Ports auf dem Message-Server für interne (1) und externe Kommunikation (2)
- Profilparameter rdisp/msserv_internal definiert die zu verwendenden internen Ports
- Unterbinden der Kommunikation von anderen Netzwerkgeräten zu dem im Profilparameter rdisp/msserv_internal definierten Port
- Externe Überwachung des Message Servers durch Setzen des Profilparameters ms/monitor=0 unterbinden
- Externe Verwaltung des Message-Servers durch Setzen des Profilparameters ms/admin_port=0 verbieten

(1) - Interne Kommunikation dient der Kommunikation zwischen verschiedenen Anwendungsdiensten im Unternehmen

(2) - Externe Kommunikation dient der Kommunikation mit den Benutzern/Kunden

## Überprüfung der Maßnahme

- Überprüfen Sie die ACLs für den Message Server anhand des Profilparameters ms/acl_info
- Überprüfen Sie, dass HOST=* nicht in der ACL definiert ist.
- Überprüfen Sie, ob die Ports für internen und externen Datenverkehr aufgeteilt sind und ob die Firewall die Kommunikation zum internen Port blockiert.
- Überprüfen Sie, dass der Profilparameter ms/monitor=0 ist.
- Überprüfen Sie, ob der Profilparameter ms/admin_port=0 ist.

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A9 Absicherung und Überwachung des Message-Servers (B) / Protection and monitoring of the Message-Servers (B)
- SAP Security Baseline Template V2.1: 2.2.1.4, 2.2.1.4.1, 2.2.1.4.2
