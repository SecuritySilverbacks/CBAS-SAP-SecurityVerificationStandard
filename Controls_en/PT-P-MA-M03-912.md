---
Security Function: Protect (PT)
Category: Maintenance (PT.MA)
Technology: SAP BTP
Maturity Level: 1
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

By default, bind and service key certificates expire after 60 days (with the exception of the older basic and oauth:key authentication, which are valid for 365 days by default). Custom domain server certificates are valid for one year, but there is no automatic certificate renewal. Once the certificate has expired, the custom domain and associated application routes will no longer work and TLS errors will occur on the client side. The service uses Subject Name Identifier as Common Name (CN) in requested client certificates by default or sls_common_name can also be used with mapped values configured via identity authentication and/or associated identity providers. Incorrect mappings can result in multiple users having the same values, which would result in access to the same data.


## Implementation

1. Change your access data before it expires and automate this.

2. The Custom Domain Manager displays warnings about the expiry of certificates long before the expiry date. Check the Custom Domain Manager regularly for such problems and renew your certificates in time.

3. To ensure that the subject of the client certificate is unique for each authenticated user, configure Subject Name Identifier or sls_common_name so that it contains a unique user store attribute (e.g. Global User ID).


## Verification of control

> TODO


## References

* SAP BTP Security Recommendations: BTP-CRS-0006, BTP-DOM-0002, BTP-SLS-0003
