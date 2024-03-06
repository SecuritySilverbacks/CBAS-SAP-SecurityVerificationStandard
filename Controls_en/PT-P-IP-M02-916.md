---
Security Function: Protect (PT)
Category: Information Protection Processes and Procedures (PT.IP)
Technology: SAP BTP
Maturity Level: 3
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

Password logon is vulnerable in business scenarios and SAP recommends self-registration to prevent automated attacks. Fake users can be created to influence the rating system of a community. Connections to a local system can be configured by specifying the host name and exposing the system in the cloud with a virtual host name as an alias for the local system. By default, the service supports all cipher suites used by Java virtual machines.


## Implementation

1. Only if self-registration is enabled: Enable CAPTCHA for the login or registration pages to distinguish humans from computers.

2. Use the virtual host name to prevent information about the name of the physical computer of a system from being passed on to the cloud.

3. Only trust the cipher suites that meet your security requirements and deactivate the rest.


## Verification of control

> TODO


## References

* SAP BTP Security Recommendations: BTP-IAS-0025, BTP-CLC-0014, BTP-CLC-0019
