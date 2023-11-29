---
Sicherheitsfunktion: PT
Kategorie: Schützende Technologie
Technologie: Alle
Reifegrad: 1
IPAC: Integration (I)
Verteidiger: Technologie
Vorbedingung:
---

## Beschreibung

SAP-Netzwerkimplementierungen sollten verwaltet, überwacht und kontrolliert werden, um Informationen in Anwendungen und Systemen zu schützen.

Die Kontrolle beinhaltet die Notwendigkeit, den SAP Router und den Web Dispatcher sicher zu konfigurieren, damit sie als Gateways auf Anwendungsebene in der DMZ-Zone fungieren.

## Implementierung

Externer Verkehr:

Der SAP-Router und der Web Dispatcher sollten in der demilitarisierten Zone (DMZ) betrieben werden, um den entsprechenden Datenverkehr zu filtern, bevor er durch eine weitere Firewall geleitet wird. 

Interner Verkehr:

SAP-Systeme sollten in einem separaten Subnetz innerhalb des internen Netzwerks untergebracht werden. Dies ermöglicht eine einfachere Verwaltung von Netzwerkzugriffsrichtlinien für SAP-Systeme.

Kontrolle:

Die Architektur von SAP-Systemen sollte ordnungsgemäß dokumentiert werden, einschließlich, aber nicht beschränkt auf Verbindungen, Kommunikation, Datenfluss, Benutzer und verwendete Protokolle.


## Überprüfung der Maßnahme

- SAP Router und Web Dispatcher werden in demilitarisierter Zone betrieben
- ACLs sind eingerichtet, um unerwünschten Datenverkehr zu filtern.
- Nur notwendige Ports dürfen auf das Netzwerk zugreifen.  
- SAP-Systeme befinden sich in einem separaten Subnetz innerhalb der Organisation
- Dokumentation, die einen anschaulichen Überblick über die SAP-Architektur gibt

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A3 Netzwerksicherheit/ Netzsicherheit
- CIS CSC 8, 12, 15
- COBIT 5 DSS05.02, APO13.01
- ISA 62443-3-3:2013 SR 3.1, SR 3.5, SR 3.8, SR 4.1, SR 4.3, SR 5.1, SR 5.2, SR 5.3, SR 7.1, SR 7.6
- ISO/IEC 27001:2013 A.13.1.1, A.13.2.1, A.14.1.3
- NIST SP 800-53 Rev. 4 AC-4, AC-17, AC-18, CP-8, SC-7, SC-19, SC-20, SC-21, SC-22, SC-23, SC-24, SC-25, SC-29, SC-32, SC-36, SC-37, SC- 38, SC-39, SC-40, SC-41, SC-43
