---
Security Function: Protect (PT)
Category: Maintenance (PT.MA)
Technology: SAP BTP
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

The default setting for an access token in this system is set to 12 hours, and a refresh token lasts for 28 days, but changing these policies may result in the user having to re-authenticate less often.


## Implementation

Check regularly whether this configuration still meets your requirements. Increasing the token validity means that a malicious user who manages to steal a token will have access until the token expires. Keep the token validity as short as possible, but not less than 30 minutes.

## Verification of control

> TODO


## References

* SAP BTP Security Recommendations: BTP-UAA-0005
