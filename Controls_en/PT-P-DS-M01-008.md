---
Security Function: Protect (PT)
Category: Data Security (PT.DS)
Technology: SAP HANA
Maturity Level: 1
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

Compliance with cryptographic key generation requirements is critical to the security of an SAP system. Longer keys provide protection against brute force attacks, resist modern attack methods, ensure confidentiality and integrity of data, meet regulatory requirements and protect against future threats. They are a fundamental security measure to secure sensitive data and ensure the integrity of the system.

Different key material is used in an SAP HANA system depending on the purpose of the system. In addition to transport encryption keys, this also includes the digital signing of memories and documents, as well as the protection of secrets (e.g. login information for peripheral systems) against unauthorized access. 

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

1. Encryption of the key material: For an SAP HANA system, you should ensure that the key material itself is encrypted and protected. This is normally done automatically during the installation of a HANA system.
2. Generate certificate requests with approved algorithms and key lengths: To do this, use the sapgenpse command line tool to create certificate requests. Ensure that the algorithms and key lengths used meet the security requirements. e.g.
> sapgenpse gen_pse -p SAPSSLS -a RSA:4096:SHA512 -k GN-dNSName:sapserver.example.com -k GN-dNSName:www.sapserver.example.com "CN=sapserver.example.com, OU=SAP-Basis, O=My Company, C=DE"
3. Use of trusted hardware and SAP tools: Generate and manage key material and certificates in a secure environment and on trusted hardware. Use the tools and recommended procedures provided by SAP to manage certificates. Note that, depending on the purpose, the certificates must be managed in the database or in the file system (see also [5]). Sign certificates that are used in the SAP HANA system, preferably from a trusted certification authority (CA), to ensure the integrity and authenticity of the certificates.


## Verification of control

1. Check the settings for keys and key management by querying the system view M_ENCRYPTION_OVERVIEW.

## References

1. [SAP Note - 1848999 - Central Note for CommonCryptoLib 8 (SAPCRYPTOLIB)](https://me.sap.com/notes/1848999)
2. [SAP Note - 2338952 - CommonCryptoLib 8.5: Configuration Profile Parameters](https://me.sap.com/notes/2338952)
3. [BSI TR-02102-1 - Cryptographic Mechanisms: Recommendations and Key Lengths](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.html)
4. VA_ISEC_09 CIO-Anweisung ISEC 09 - Verschlüsselung und Verwaltung kryptographischer Schlüssel
5. [SAP Help - Certificate Management in SAP HANA](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/1e6042c4402545f7a0574f7bc91fab25.html?locale=en-US)
6. [Server-Side Data Encryption Services](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/b30fda1483b34628802a8d62bd5d39df.html?locale=en-US)