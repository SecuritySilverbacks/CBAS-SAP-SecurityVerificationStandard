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

Jede Kommunikation mit oder zwischen verschiedenen SAP-Systemen muss verschlüsselt werden. Mit Secure Network Communication (SNC) können Sie die Kommunikation zwischen verschiedenen Systemen verschlüsseln.

SNC kann nur mit SAP-Protokollen verwendet werden. Alle anderen Internetprotokolle sollten durch Aktivierung von TLS geschützt werden.

## Implementierung

Stellen Sie sicher, dass Sie die Public Key Infrastructure (PKI) kennen und verstehen, bevor Sie fortfahren.

Die Steuerung veranschaulicht, wie Sie den SAProuter für die Verwendung von SNC konfigurieren.

- Laden Sie die CommonCryptoLib vom SAP-Supportportal herunter und extrahieren Sie sie.

- Setzen Sie die Umgebungsvariable SNC_LIB = \<Pfad zur CommonCryptoLib\>.

- Setzen Sie die Umgebungsvariable SECUDIR = \<Saprouter-Verzeichnis\>/sec

- Signieren Sie ein Zertifikat für Ihren SAProuter über eine Zertifizierungsstelle (CA) Ihres Vertrauens oder über SAP

- Erzeugen Sie Ihre persönlichen Sicherheitsumgebungsdateien (PSE), indem Sie den folgenden Befehl dort ausführen, wo Sie Ihre SAProuter-Dateien abgelegt haben. *sapgenpse get_pse -v -a sha256WithRsaEncryption -s 2048 -r \<csrfile\> -p local.pse -x \<password\> "CN=\<Ihr spezifisches CN\>"*. \<csrfile\> ist der von Ihnen gewählte Dateiname, der für Ihre Certificate Signing Request (CSR) verwendet werden soll.

- Senden Sie die Datei \<csrfile\> an Ihre Zertifizierungsstelle (CA), um das Zertifikat zu erhalten und fortzufahren

- Kopieren Sie den Inhalt des empfangenen Zertifikats in eine Datei auf Ihrem SAProuter-System und importieren Sie es mit dem folgenden Befehl *sapgenpse import_own_cert -c \<certca\> -r \<root CA certificate\> -p local.pse*. \<certca\> ist die von Ihrer CA erhaltene Datei und \<Stammzertifikat der CA\> ist das Stammzertifikat der CA

- Erzeugen Sie die Datei mit den Anmeldeinformationen mit dem folgenden Befehl *sapgenpse seclogin -p local.pse \<pse password\>*.

- Test, um zu prüfen, ob alles korrekt konfiguriert und installiert ist *sapgenpse get_my_name -v -n Issuer*.

- Setzen Sie eine ACL in Ihrer saprouttab-Datei, um SNC-Verbindungen zuzulassen.

- Starten Sie den SAProuter mit seinem SNC-Namen

Um die Kommunikation mit externen SAP-Produkten, wie z.B. SAP Single Sign-On, zu sichern, sollten Sie die Sicherheitshinweise für dieses spezielle Produkt beachten.

Hinweis: Vor SAP NetWeaver 7.40 wird die Registerkarte SNC nur angezeigt, wenn der Parameter snc/enable aktiviert ist.

## Überprüfung der Maßnahme

- Überprüfen Sie, ob alles korrekt konfiguriert und installiert ist *sapgenpse get_my_name -v -n Issuer*.
- Überprüfen Sie die ACL-Datei (saprouttab), um zu überprüfen, ob SNC-Verbindungen erlaubt sind.


## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A18 Abschaltung von unsicherer Kommunikation/ Disconnection of unsafe communication
- CIS CSC 8, 12, 15
- COBIT 5 DSS05.02, APO13.01
- ISA 62443-3-3:2013 SR 3.1, SR 3.5, SR 3.8, SR 4.1, SR 4.3, SR 5.1, SR 5.2, SR 5.3, SR 7.1, SR 7.6
- ISO/IEC 27001:2013 A.13.1.1, A.13.2.1, A.14.1.3
- NIST SP 800-53 Rev. 4 AC-4, AC-17, AC-18, CP-8, SC-7, SC-19, SC-20, SC-21, SC-22, SC-23, SC-24, SC-25, SC-29, SC-32, SC-36, SC-37, SC-38, SC-39, SC-40, SC-41, SC-43
