---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP BTP
Maturity Level: 3
SAP Operational Area: Platform (P)
: Human
Prerequisite: 
---

## Description

The Identity Authentication login page does not include organization-specific branding, which can make it more difficult for users to recognize it as part of their own organization. Branding is an important step in preventing phishing attacks, as some of these attacks fail when they send links without proper branding. When signing up, the service offers all identity providers supported by the business application. The service also uses its own mail server for emails sent to users for various application processes and includes branding as a small step to protect against phishing attacks.


## Implementation

1. Use your company's corporate domains for business-critical SAP services with the Customer Domain Service.

2. Maintain your company's mail server for all outgoing mails in Identity Authentication.

3. Add your organization's branding to the login screen.

4. Provide a clear link on the login page so that business users know where to log in. Hide the default identity provider used by users of the platform.


## Verification of control
> TODO


## References
* SAP BTP Security Recommendations: BTP-IAS-0019, BTP-IAS-0020, BTP-IAS-0021, BTP-UAA-0018

