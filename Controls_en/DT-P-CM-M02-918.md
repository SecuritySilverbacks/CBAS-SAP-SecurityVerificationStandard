---
Security Function: Detect (DT)
Category: Security Continuous Monitoring (DT.CM)
Technology: SAP BTP
Maturity Level: 3
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

The SAP Audit Log service on the Cloud Foundry environment is used for audit logging with a retention time of 90 days. The service uses various security mechanisms to protect the platform, and suggests checking the audit log regularly as it is useful for monitoring and identifying potential security issues.


## Implementation

1. To keep the audit log entries for longer, you should regularly download and archive the log entries.
* Access Audit Logs (AWS, Azure Infrastructure)
* Auditing and Logging Information
* Auditing and Logging Information for SAP Authorization and Trust Management Service

2. Integrate the audit log into your existing enterprise event management system to check logs for anomalies, such as unexpected logins or multiple failed login attempts.


## Verification of control

> TODO


## References

* SAP BTP Security Recommendations: BTP-IAS-0011, BTP-CRS-0010, BTP-UAA-0012, BTP-UAA-0013, BTP-TMS-0002, BTP-DOM-0004, BTP-SLS-0001
