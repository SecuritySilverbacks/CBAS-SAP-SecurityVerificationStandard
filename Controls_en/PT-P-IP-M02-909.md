---
Security Function: Protect (PT)
Category: Information Protection Processes and Procedures (PT.IP)
Technology: SAP BTP
Maturity Level: 3
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

Once a custom identity provider has been configured, it is possible to revoke administrator access from all users using the default identity provider. This means that no one who has an account through an SAP-managed identity provider will have access to your sub-accounts. The service will not modify any content you have uploaded and will only store it temporarily for provisioning or import tasks. Once these tasks are completed, the data is deleted from your system.

## Implementation

1. Keep some global account administrators of the default identity provider. Use these administrators in the rare event that access to the custom identity provider fails.

2. If necessary, save your content in a separate repository. Export transport-related action logs, MTA extension descriptors and the current landscape configuration. Request a final export of customer data as part of the decommissioning process.


## Verification of control

1. Regularly check whether you have global account administrators for the default identity provider.

> 2. TODO

## References

* SAP BTP Security Recommendations: BTP-UAA-0009, BTP-TMS-0004
