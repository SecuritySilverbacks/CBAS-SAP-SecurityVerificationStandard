---
Security Function: Protect (PT)
Category: Data Security (PT.DS)
Technology: SAP Java
Maturity Level: 1
SAP Operational Area: Platform (P)

Prerequisite: 
---

Compliance with cryptographic key generation requirements is critical to the security of an SAP system. Longer keys provide protection against brute force attacks, resist modern attack methods, ensure confidentiality and integrity of data, meet regulatory requirements and protect against future threats. They are a fundamental security measure to secure sensitive data and ensure the integrity of the system.

Different key material is used in an SAP ABAP system depending on the purpose of the system. In addition to transport encryption keys, this also includes the digital signing of memories and documents, as well as the protection of secrets (e.g. logon information for peripheral systems) against unauthorized access.

## Implementation

**Specification of key lengths and algorithms**

According to the internal specifications for key management, at least the BSI specifications must be complied with. For the supported cryptographic algorithms of SAP CommonCryptoLib, this means the following:

- RSA (Rivest-Shamir-Adleman) key: The minimum key length for RSA keys should be 3072 bits, preferably 4096 bits.

- DSA (Digital Signature Algorithm) key: For DSA keys, a minimum key length of 3072 bits, preferably 4096 bits, is recommended to ensure a strong digital signature.

- ECDSA (Elliptic Curve Digital Signature Algorithm) key: When using ECDSA keys, curves with a minimum key length of 256 bits (NIST P-256 curve) or higher should be used.

- AES (Advanced Encryption Standard) key: The minimum key length for RSA keys should be 128 bits, preferably 256 bits.

- Hash functions: At least SHA-256, preferably SHA-384 and SHA-512, must be used as checksum functions for the signature algorithm.

- Notes on legacy algorithms: DES must no longer be used and Triple-DES should only be used in exceptional cases where backward compatibility is required. 

**Specification for certificate generation and protection of private keys**

1. Encryption of the key material: Make sure that the key material in your SAP NetWeaver Java system is also encrypted and protected. This is done during the installation of the system by using a password and a key derivation generated from it.
2. Generating certificate requests and certificates: Certificate requests and certificates are generated via the SAP NetWeaver Administrator interface (NWA). Here you can create certificate requests and have them signed by a trusted certification authority (CA).
3. Use trusted hardware and SAP tools: Make sure to create and manage key material and certificates in a secure environment. Use the tools and recommended procedures provided by SAP to manage certificates in your Java system.

## Verification of control

1. Use the NWA to check the individual keystore views and the certificates they contain for their cryptographic parameters and their compliance with the specifications and validity.

## References

1. [SAP Note - 1848999 - Central Note for CommonCryptoLib 8 (SAPCRYPTOLIB)](https://me.sap.com/notes/1848999)
2. [SAP Note - 2338952 - CommonCryptoLib 8.5: Configuration Profile Parameters](https://me.sap.com/notes/2338952)
3. [BSI TR-02102-1 - Cryptographic Mechanisms: Recommendations and Key Lengths](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.html)
4. VA_ISEC_09 CIO-Anweisung ISEC 09 - Verschlüsselung und Verwaltung kryptographischer Schlüssel
5. [SAP Help -  Using the AS Java Key Storage](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/007f2c7c77ae4e7884bba888e5aa5fe9/e9a1dd44d2c83c43afb5ec8a4292f3e0.html?locale=en-US)
6. [SAP Help - Java Key Storage and Maintenance](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/2f64847a81a84bda878e32d5a4dae0a2/d53c25f95e68499abf62ece2f6b6f896.html?locale=en-US)
7. [SAP Help - Secure Storage in the File System](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/007f2c7c77ae4e7884bba888e5aa5fe9/b6b92640632cec01e10000000a155106.html?locale=en-US)
8. [SAP Blog - How to troubleshoot, import/renew and monitor java Keystore certificates in SAP PI 7.5 – Part 3](https://blogs.sap.com/2020/12/28/how-to-troubleshoot-import-renew-and-monitor-java-keystore-certificates-in-sap-pi-7.5-part-3/)