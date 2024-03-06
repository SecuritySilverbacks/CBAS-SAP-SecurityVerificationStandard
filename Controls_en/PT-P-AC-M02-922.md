---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP BTP
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

Managing identities in SAP cloud services for organizations that already have an existing identity management process in place can be challenging. These processes are often used as the leading identity management system, but may not provide best practices for effectively managing these systems. The SAP BTP solution serves as a centralized user store for both platform users and business users in applications. The default identity provider enables single sign-on to other SAP services.


## Implementation

1. Use Identity Provisioning with the Identity Authentication user store (Identity Directory) to synchronize users with your leading identity management solution. The Identity Directory acts as a central location for managing identities for SAP Cloud Services.

2. In the event that self-registration is active: Maintain all unwanted domains in e-mail addresses or user names. For example, do not allow the creation of the user Adminstrator@*.* to prevent a malicious user from infiltrating a specific role. Another example would be to block email providers that allow the creation of email addresses with scripts.

3.
* Configure the service to use SAP Cloud Identity Services - Identity Authentication as a custom identity provider to facilitate integration with other SAP solutions. Configure Identity Authentication as a proxy for your corporate identity provider. By hosting these users in your own identity provider, you gain a number of advantages over hosting them in the default identity provider.

* Integrate the management of these users into your broader identity management strategy hosted on your own identity providers. Control your own user lifecycle and single sign-on strategies across the landscape.

* Enforce your own password and authentication policies, e.g. stronger passwords or multi-factor authentication.

4. The number of active identity providers for the global account/sub-accounts should be strictly limited.


## Verification of control
> TODO


## References
* SAP BTP Security Recommendations: BTP-IAS-0015, BTP-IAS-0024, BTP-UAA-0008, BTP-UAA-0016
* SAP Security Baseline Template V2.4: 2.3.2.5.1
