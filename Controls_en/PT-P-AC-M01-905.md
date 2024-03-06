---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP BTP
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

All bindings of a service instance share a single secret by default, with the exception of those with an API access plan, which use a separate secret per binding. The secrets do not expire and can be used to access the service instance if they become known. X.509 certificates have an automatic 7-day expiration period for service-managed certificates, but the expiration period for self-managed certificates depends on the provider used. When the secrets expire, clients can no longer authenticate to the service instance. In addition, there is a timeout mismatch between the application and the SAP Authorization and Trust Management Service, which triggers an error message indicating that the current business user is logging off.

## Implementation

1. In the Application Security Descriptor (xs-security.json), activate individual secrets for each binding of a service instance. We recommend this configuration so that you can change the secret of a binding without affecting the other bindings of the service instance. Use X.509 secrets if you can. See also BTP-UAA-0004. (2.)

2. Regular rotation of secrets to reduce the potential exposure of a secret. See also BTP-UAA-0003. (1.)

3. Automate your provisioning process to take into account the lifetime of the X.509 certificates. Check regularly whether the process matches the configured lifetime. See also BTP-UAA-0004. (2.)

4. Administrators should make business users aware of the potential security risk associated with the timeout mismatch. To address this security risk, advise business users to re-access the application URL, log in to the application and log out immediately, or log out directly from the identity provider.


## Verification of control
> TODO


## References
* SAP BTP Security Recommendations: BTP-UAA-0003, BTP-UAA-0004, BTP-UAA-0014, BTP-UAA-0023
