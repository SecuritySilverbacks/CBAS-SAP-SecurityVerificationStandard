---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP BTP
Maturity Level: 3
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

The default authentication method for end users is to authenticate to a service using their username and password. There are currently no security measures that restrict access based on IP address ranges or group membership within the entire tenant.


## Implementation

1. Use passwordless authentication methods. To do this, deactivate password authentication for end users. Possible options for this:
* Kerberos authentication
* Activate users for generation and authentication using certificates
* Enable or disable FIDO2 biometric authentication for an application

2. Define group-based authentication policies according to the risk posed by the different user groups. This configuration is not applicable to all environments. Administrators should be aware of this option and decide according to internal requirements.
Examples of rule criteria are: IP range, authentication method, user type, group type or company attribute


## Verification of control
> TODO


## References
* SAP BTP Security Recommendations: BTP-IAS-0006, BTP-IAS-0026

