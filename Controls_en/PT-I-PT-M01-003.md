---
Security Function: PT
Category: Protective Technology
Technology: SAProuter
Maturity Level: 1
IPAC: Integration (I)
Defender: Technology
Prerequisite: PT-I-PT-M01-001
---

## Description

Any communication with or between different SAP systems must be encrypted. The Secure Network Communication (SNC) enables you to encrypt communications between different systems.

SNC can only be used with SAP protocols, any other internet protocols should be protected by enabling TLS.

## Implementation

Make sure you have knowledge and understanding of the Public Key Infrastructure (PKI) before moving forward.

The control illustrates how to configure the SAProuter to use SNC.

- Download and extract the CommonCryptoLib from SAP support portal

- Set the environment variable SNC_LIB = \<path to the CommonCryptoLib\>

- Set the environment variable SECUDIR = \<saprouter directory\>/sec

- Sign a certificate for your SAProuter through a Certificate Authority (CA) you trust or through SAP

- Generate your Personal Security Environment (PSE) files by running the following command where you placed your SAProuter files. *sapgenpse get_pse -v -a sha256WithRsaEncryption -s 2048 -r \<csrfile\> -p local.pse -x \<password\> "CN=\<YOUR SPECIFIC CN\>"*. The \<csrfile\> is the file name of your choosing that will be used for your Certificate Signing Request (CSR)

- Submit the \<csrfile\> file to your Certificate Authority (CA) to receive the certificate to proceed

-  Copy content of the received certificate to a file on your SAProuter system and import with the following command *sapgenpse import_own_cert -c \<certca\> -r \<root CA certificate\> -p local.pse*. The \<certca\> is the file received from your CA and \<root CA certificate\> is the root certificate from the CA

- Generate the credentials file with the following command *sapgenpse seclogin -p local.pse \<pse password\>*

- Test to check whether everything is configured and installed correctly *sapgenpse get_my_name -v -n Issuer*

- Set an ACL in your saprouttab file to allow SNC connections

- Start the SAProuter using its SNC name

In order to secure communications with external SAP products, such as SAP Single Sign-On, you should refer to the security notes for that specific product.

Note: Prior to SAP NetWeaver 7.40, SNC tab is only shown if the snc/enable parameter is enabled

## Verification of Control

- Verify whether everything is configured and installed correctly *sapgenpse get_my_name -v -n Issuer*
- Verify ACL file (saprouttab) to verify if SNC connections are allowed


## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A18 Disconnection of unsafe communication/ Abschaltung von unsicherer Kommunikation
- CIS CSC 8, 12, 15
- COBIT 5 DSS05.02, APO13.01
- ISA 62443-3-3:2013 SR 3.1, SR 3.5, SR 3.8, SR 4.1, SR 4.3, SR 5.1, SR 5.2, SR 5.3, SR 7.1, SR 7.6
- ISO/IEC 27001:2013 A.13.1.1, A.13.2.1, A.14.1.3
- NIST SP 800-53 Rev. 4 AC-4, AC-17, AC-18, CP-8, SC-7, SC-19, SC-20, SC-21, SC-22, SC-23, SC-24, SC-25, SC-29, SC-32, SC-36, SC-37, SC-38, SC-39, SC-40, SC-41, SC-43
