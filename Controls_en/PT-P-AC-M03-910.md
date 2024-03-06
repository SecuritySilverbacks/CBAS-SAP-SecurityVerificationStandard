---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP BTP
Maturity Level: 1
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

Server certificates are only validated for servers that use the HTTPS protocol, regardless of whether they are accessed via a public Internet connection or a private connection (PrivateLink).

## Implementation

Validation of the server certificate is important to ensure that the connection (TLS session) is established to the correct (trusted) server. It is not recommended to trust all server certificates. This setting is only available for testing and development purposes.

## Verification of control
> TODO


## References
* SAP BTP Security Recommendations: BTP-DES-0015
