---
Sicherheitsfunktion: PT
Kategorie: Schutztechnik
Technologie: SAProuter
Reifegrad: 1
IPAC: Integration (I)
Verteidiger: Technologie
Vorraussetzung: PT-I-PT-M01-001
---

## Beschreibung

Wenn Sie SAPGUI- oder RFC-Verbindungen verwenden, um vom Internet oder von verschiedenen externen Netzwerken aus auf veröffentlichte SAP-Systeme zuzugreifen, die zu Ihrem Unternehmen gehören, muss SAProuter ordnungsgemäß konfiguriert werden, um den Datenverkehr zuzulassen und zu verweigern. Der SAProuter muss auch mit der Firewall Hand in Hand arbeiten, um verschiedene Zugriffsregeln zu übernehmen und eine Multi-Access-Control-Architektur zu ermöglichen.

## Implementierung

Die Implementierung sicherer Verbindungen von externen Netzwerken oder dem Internet aus erfordert eine kontinuierliche Abstimmung und Anpassung, um unbefugten Zugriff auf SAP-Systeme zu verhindern. Die unten stehende Implementierung ist eine Basis, die es Unternehmen ermöglicht, sichere Verbindungen zu ihren internen Systemen zu implementieren.

- Konfigurieren Sie Ihre Firewall so, dass sie nur einen Port zulässt, 32NN, wobei NN die Instanznummer des Unternehmens für den SAProuter ist.
- Konfigurieren Sie SNC(1), um dem SAP-Support eine sichere Anmeldung an Ihrem System zu ermöglichen. (Dies ist hauptsächlich für Supportzwecke gedacht)
- Konfigurieren Sie ein implizites Deny in der letzten Zeile der ACL-Datei (routtab-Datei), (Verweigern Sie jeglichen Datenverkehr mit der folgenden Regel D * * *)
- Konfigurieren Sie autorisierte Verbindungen über SAPGUI, um SAProuter für die Verbindung zu verwenden
- Für den Fall, dass eine Verbindung von nicht verwalteten Geräten erforderlich ist, konfigurieren Sie eine bestimmte autorisierte Verbindung mit Hilfe eines sicheren Passworts (Aktualisieren Sie die routtab-Datei, z.B. P * * 3201 secure_password, erlaubt Anfragen an Port 3201, wenn ein Kennwort verwendet wird)
- Kontinuierliche Überwachung des dev_route-Protokolls. Dies ermöglicht es den Sicherheitsteams, ihre ACLs auf ihre Bedürfnisse abzustimmen.


(1) - Referenzsteuerung PT-I-PT-M01-003 zur Konfiguration und Aktivierung von SNC

## Überprüfung der Maßnahme

- Überprüfen Sie die ACL-Datei (routtab), um unerwünschte oder falsch konfigurierte Regeln zuzuweisen.
- Überprüfen Sie, ob in der ACL-Datei eine implizite Verweigerung vorhanden ist (d.h. D * * *)
- Überprüfen Sie, ob ein sicheres Passwort für autorisierten Datenverkehr konfiguriert ist.
- Überprüfen Sie, ob Verbindungen, die von SAPGUI kommen, so konfiguriert sind, dass sie den SAProuter benutzen.
- Überprüfen Sie, ob die Firewall so konfiguriert ist, dass sie die eine Portnummer für SAProuter zulässt.

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A3 Netzwerksicherheit/ Netzsicherheit
- CIS CSC 8, 12, 15
- COBIT 5 DSS05.02, APO13.01
- ISA 62443-3-3:2013 SR 3.1, SR 3.5, SR 3.8, SR 4.1, SR 4.3, SR 5.1, SR 5.2, SR 5.3, SR 7.1, SR 7.6
- ISO/IEC 27001:2013 A.13.1.1, A.13.2.1, A.14.1.3
- NIST SP 800-53 Rev. 4 AC-4, AC-17, AC-18, CP-8, SC-7, SC-19, SC-20, SC-21, SC-22, SC-23, SC-24, SC-25, SC-29, SC-32, SC-36, SC-37, SC- 38, SC-39, SC-40, SC-41, SC-43
