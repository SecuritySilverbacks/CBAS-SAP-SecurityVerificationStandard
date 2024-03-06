---
Security Function: Protect (PT)
Category: Information Protection Processes and Procedures (PT.IP)
Technology: SAP BTP
Maturity Level: 1
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

Custom applications can interact with a REST API to manage user credentials. The API offers four main functions for this purpose: Listing, creating, reading, updating and deleting credentials. The user data is encrypted by default according to the JSON Web Encryption Compact Serialization Format (JWE-CSF).

## Implementation

Never deactivate user data encryption in your production environment. Only in rare cases should you deactivate encryption for test purposes in test environments.


## Verification of control

> TODO


## References

* SAP BTP Security Recommendations: BTP-CRS-0002
