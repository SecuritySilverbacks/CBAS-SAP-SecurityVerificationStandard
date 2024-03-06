---
Security Function: Protect (PT)
Category: Data Security (PT.DS)
Technology: SAP ABAP
Maturity Level: 1
SAP Operational Area: Integration (I)

Prerequisite: 
---

## Description

Transport encryption using TLS (Transport Layer Security) and SNC (Secure Network Communications) with strong cipher configurations is crucial for ensuring secure application operation and compliance with regulatory requirements such as BSI basic protection. It ensures the confidentiality and integrity of data during transmission, protects against tampering and enables reliable authentication of communication partners. The use of strong encryption strengthens security against known attacks and is a prerequisite for compliance with data protection and security standards in cloud environments.

Transport encryption is supported in SAP systems by various protocols and integration interfaces. These include HTTPS, SMTPS using TLS, RFC and SAP GUI communication based on the NI protocol using SNC for secure communication between SAP systems and end users via SAP GUI.

## Implementation

1. In preparation, you should set the environment variable CCL_PROFILE (configuration for the CommonCryptoLib (CCL)) for \<sid\>adm so that it refers to the DEFAULT profile file.

**TLS configuration**

**Note: For existing interfaces, it should be checked whether the corresponding ciphers are supported on the client side. If this is not the case and compatibility cannot be ensured on the client application, an HTTP proxy can terminate the client's SSL/TLS connection and establish a new TLS connection to the SAP system to forward the HTTP requests. The following specifications for the TLS configuration require at least TLS 1.2 on the client and server side. Downward compatibility is not supported with this configuration**


1. In order to also cover the TLS configuration of the SAP Instance Agent, the integrated SAP Web Dispatcher, the profile parameters should be included in DEFAULT.PFL. This allows some command line tools to read the configuration of the CommonCryptoLibs from a profile. This applies to 'sapcontrol' or 'sapgenpse', for example. The following parameters should be adjusted:
    1. For server-side provision
    > ssl/ciphersuites = 544:TLS_FALLBACK_SCSV:eAES_GCM:+eAES128:!kRSA::EC_X25519:EC_P256:EC_P384:EC_P521:+EC_OPT
    2. For negotiation as a client
    > ssl/client_ciphersuites = 562:eAES_GCM:+eAES128:!kRSA::EC_X25519:EC_P256:EC_P384:EC_P521:+EC_OPT
2. To cover the SAP Host Agent, these profile parameters should be added to the host_profile. Since the sapadm user is usually a non-logged-in user without a shell, these environment variables must be set via the host_profile by adding the parameters to the profile according to the following pattern. This is necessary for other components such as SAP JCo or SAP NCo.
> SETENV_\<xx\>=\<environment variable\>=\<value\> 
The \<xx\> is to be replaced by a free numbering. e.g.: 
    1. For server-side provision
    > SETENV_00=SAPSSL_CIPHERSUITES=544:TLS_FALLBACK_SCSV:eAES_GCM:+eAES128:!kRSA::EC_X25519:EC_P256:EC_P384:EC_P521:+EC_OPT
    2. For negotiation as a client
    > SETENV_01=SAPSSL_CLIENT_CIPHERSUITES=544:eAES_GCM:+eAES128:!kRSA::EC_X25519:EC_P256:EC_P384:EC_P521:+EC_OPT
3. To make the configuration changes effective, you must restart the SAP system.

**SNC configuration**

**Note: For existing interfaces, it should be checked whether the corresponding Ciper is supported on the client side. If this is not the case and compatibility cannot be ensured on the client application, an SAP router can terminate the client's SNC connection and establish a new SNC connection to the SAP system to forward the RFC call. The following specifications for SNC configuration require at least protocol version 2010_1_1 on the client and server side. Downward compatibility is not supported with this configuration.**

The following parameters are not known to the SAP kernel. It is not possible to maintain these parameters with RZ11, but with the environment variable mentioned above they can be maintained in RZ10 in DEFAULT.PFL and as soon as the changes are activated, i.e. written to the file system, the CCL uses the new settings.

1. Defining the SNC protocol version
    1. For server-side provisioning, define
    > ccl/snc/server_protocol = 2010_1_1
    2. To negotiate as a client, define
    > ccl/snc/client_protocol = 2010_1_1
2. Definition of the cipher for key exchange and symmetric encryption
    1. For server-side provisioning, define
    > ccl/snc/server_cipher_suites = SNC_ECDHE_P256_AES256_SHA256:SNC_ECDHE_P384_AES256_SHA512:SNC_ECDHE_P521_AES256_SHA512
    2. To negotiate as a client, define
    > ccl/snc/client_cipher_suites = HIGH
3. Definition of the signing algorithm for X.509 certificates
    1. For server-side provisioning, define
    > ccl/snc/server_accepted_signature_algorithms = SHA256_DSA:PKCS_BT_01_SHA256_RSA:PKCS_BT_01_SHA512_RSA:SHA256_ECDSA:SHA512_ECDSA:SHA384_ECDSA
    2. To negotiate as a client, define
    > ccl/snc/client_accepted_signature_algorithms = SHA256_DSA:PKCS_BT_01_SHA256_RSA:PKCS_BT_01_SHA512_RSA:SHA256_ECDSA:SHA512_ECDSA:SHA384_ECDSA

## Verification of control

**TLS configuration**
Check the setting of the TLS configurations in the default profile of the SAP application and in the host_profile of the SAP Host Agent.

**SNC configuration**
Check the setting of the TLS configurations in the default profile of the SAP application and that the environment variable CCL_PROFILE references the default profile correctly.


## References

1. [BSI TR-02102-2 - Cryptographic Mechanisms: Recommendations and Key Lengths](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.html)
2. [SAP Note - 455033 – SAPCRYPTOLIB versions, bugs and fixes](https://launchpad.support.sap.com/#/notes/455033)
3. [SAP Note - 511150 – SAPCRYPTOLIB 555pl10: feature update](https://launchpad.support.sap.com/#/notes/0000511150)
4. [SAP Note - 510007 – Additional considerations for setting up SSL on Application Server ABAP](https://launchpad.support.sap.com/#/notes/510007)
5. [SAP Note - 1433874 – SapSSLReloadCred fix, SSLv3/TLSv1.0 configurability](https://launchpad.support.sap.com/#/notes/1433874)
6. [SAP Note - 2180024 – HANA & ABAP: New Option to Enable/Disable FIPS 140-2 Certified Crypto Kernel](https://launchpad.support.sap.com/#/notes/2180024)
7. [SAP Note - 2284059 – Update of SSL library within NW Java server](https://launchpad.support.sap.com/#/notes/2284059)
8. [SAP Note - 2384243 – NetWeaver Application Server: How to configure strict TLS 1.2](https://launchpad.support.sap.com/#/notes/2384243)
9. [SAP Blog - CommonCryptoLib: TLS protocol versions and cipher suites](https://blogs.sap.com/2021/05/03/commoncryptolib-tls-protocol-versions-and-cipher-suites/)
10. [SAP Blog - CommonCryptoLib: SNC protocol versions and cipher suites](https://blogs.sap.com/2021/11/05/commoncryptolib-snc-protocol-versions-and-cipher-suites/)
11. [SAP Note - 2384243 - NetWeaver Application Server: How to configure strict TLS 1.2](https://me.sap.com/notes/2384243)
