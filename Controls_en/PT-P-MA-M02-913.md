---
Security Function: Protect (PT)
Category: Maintenance (PT.MA)
Technology: SAP BTP
Maturity Level: 3
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

Custom domain certificates (CA certificates) that are trusted for client authentication are only valid for a limited period of time (e.g. 5 years). No automatic certificate renewal is available. Once the trusted CA certificate expires, there may be issues with the custom domain and associated application routes no longer working, resulting in TLS errors on the client side as new certificates are now issued by a different CA.

In addition, Custom Domain Certificate Authority (CA) certificates are mandatory for identifying authorized client certificates that can successfully authenticate mutual TLS connections between clients and servers. However, further identity verification and mapping on the side of the called cloud application as part of a custom domain configuration is not possible.

## Implementation

1. The Custom Domain Manager displays warnings long before the expiry date of the certificates. Check the Custom Domain Manager regularly for such problems and renew your certificates in good time.

2. Only configure the certificates of the certification authorities (CA) as trustworthy for client authentication that are really needed. Do not add all known CAs just to avoid the maintenance effort for the configuration.


## Verification of control

> TODO


## References

* SAP BTP Security Recommendations: BTP-DOM-0003, BTP-DOM-006
