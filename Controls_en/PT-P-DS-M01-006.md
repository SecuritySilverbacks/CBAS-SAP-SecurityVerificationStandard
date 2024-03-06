---
Security Function: Protect (PT)
Category: Data Security (PT.DS)
Technology: SAP ABAP
Maturity Level: 1
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

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

1. Encryption of the key material: Make sure that the key material itself is also encrypted and protected. A specific SAP Security Store key must be generated using transaction SECSTORE. The default key supplied is publicly known and must not be used.
2. Activate the locally protected storage of PSE files by setting the PSE protection to "Protected" ()
3. Generate certificate requests with released algorithms and key lengths via the sapgenpse command line interface, as the STRUST transaction does not allow any parameters for the encryption properties. e.g.
> sapgenpse gen_pse -p SAPSSLS -a RSA:4096:SHA512 -k GN-dNSName:sapserver.example.com -k GN-dNSName:www.sapserver.example.com "CN=sapserver.example.com, OU=SAP-Basis, O=My Company, C=DE"
4. Only generate key material and certificates on trusted hardware and only manage them using the tools provided and released by SAP for this purpose. Certificates must always be signed by a trusted certification authority on the basis of signing requests and not locally or self-signed.

## Verification of control

1. Check the generation of the private master key using the SECSTORE transaction
2. Check individually that the certificates stored in the system comply with the current security guidelines and have not expired using transaction STRUST.
    1. Select a certificate and click on "Show details". Make sure that the key length for the certificate meets the minimum requirements of the BSI basic protection.
    2. You will also find the signing algorithm (e.g. SHA-256) in the certificate details. Make sure that the signing algorithms used comply with the current security standards.
3. Use transaction STRUST to check whether all PSE files are stored in "Protected" mode in the file system.

## References

1. [SAP Note - 1848999 - Central Note for CommonCryptoLib 8 (SAPCRYPTOLIB)](https://me.sap.com/notes/1848999)
2. [SAP Note - 2338952 - CommonCryptoLib 8.5: Configuration Profile Parameters](https://me.sap.com/notes/2338952)
3. [BSI TR-02102-1 - Cryptographic Mechanisms: Recommendations and Key Lengths](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.html)
4. VA_ISEC_09 CIO-Anweisung ISEC 09 - Verschlüsselung und Verwaltung kryptographischer Schlüssel
5. [SAP Note - 3158820 - Using Local Protection Storage in sapgenpse and STRUST](https://me.sap.com/notes/3158820/E)
6. [SAP Help - Digital Signatures and Encryption](https://help.sap.com/docs/ABAP_PLATFORM/cf1026f0534f408e849ee7feed288a66/53251a355d0c4d78e10000009b38f83b.html?locale=en-US)