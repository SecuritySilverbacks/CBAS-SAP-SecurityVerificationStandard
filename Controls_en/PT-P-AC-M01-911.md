---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP BTP
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

In Cloud Foundry Spaces, there are different levels and permissions related to managing a secure login service. The API access plan provides administrator-level access to REST APIs for services that have this plan, while members with the Space Manager or Space Developer roles can access these API endpoints within the Space where instances exist. Org managers of parent organizations can grant these permissions to users who need them in a dedicated Custom Domain Administrator space. The Custom Domain Administrator role collection enables the weakening of TLS versions and cipher suites, while Custom Domain Manager administrators require the Cloud Foundry Space Developer role in this dedicated area. There are two levels of authorization: Viewing the Secure Login Service configurations of the sub-account (e.g. for technical rollout or support personnel) and managing these configurations (e.g. for administrators). The service is part of the authentication flow and each user assigned to one of these groups has access to configuration data related to this secure login service.


## Implementation

1. If applications use a service instance via a service key or a binding, define the namespace to restrict access. (Principle of Least Privilege)

2. Regularly check that only administrators have manager access to Cloud Foundry spaces in which service instances with this plan exist.

3.
* Assign only those administrators who need to manage your custom domains to the custom domain administrator role.
* Assign the Space Developer role in a special space for managing custom domains only to those administrators who need to manage your custom domains.

4.
* Assign the SecureLoginServiceViewer group only to those users who are required to implement and support this solution.
* Assign the SecureLoginServiceAdministrator group only to the administrators who are required to set up and configure this solution.


## Verification of control
> TODO


## References
* SAP BTP Security Recommendations: BTP-CRS-0003, BTP-UAA-0022, BTP-DOM-0001, BTP-SLS-0002
