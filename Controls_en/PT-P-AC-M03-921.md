---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP BTP
Maturity Level: 1
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

In public scenarios, self-registration may be required, but is disabled by default by an internal value that can be configured per application. However, due to the lifecycle processes of the corporate identity, self-registration is undesirable in most B2E (Business to Employee) and B2B (Business to Business) scenarios. Similarly, social sign-on is disabled by default, but may be required for public scenarios. Due to corporate identity lifecycle processes, social sign-on is also undesirable in most B2E and B2B scenarios.


## Implementation

1. Deactivate self-registration (value = internal). Actively manage use cases that require this function.

2. Deactivate Social Sign-On (value = internal). Actively manage use cases that require this function.

3. No platform user from the default identity provider with an external email address domain should have administrative rights.

4. No Cloud Foundry organization or space member from a default identity provider with an external email address domain should be assigned any of the following administrative permissions:
* Org-Manager
* Space-Developer
* Space-Manager

5. No platform user from the default identity provider should be a public user (P user).

6. No business user of the standard identity provider may belong to the user classes C, D, I or P user or have an external e-mail address domain.

7. The HTML5 application authorization NonActiveApplicationPermission may not be assigned to roles other than developer roles such as AccountDeveloper. (Neo environment subaccounts)


## Verification of control
> TODO


## References
* SAP BTP Security Recommendations: BTP-IAS-0003, BTP-IAS-0005
* SAP Security Baseline Template V2.4: 2.3.1.3.2, 2.3.3.1.4
