---
Security Function: Detect (DT)
Category: Security Continuous Monitoring (DT.CM)
Technology: SAP BTP
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

Administrative settings for running a secure service, such as receiving alerts about critical changes and enabling audits to track user activity, are important. By default, administrators do not receive emails about critical changes, user-related security alerts are disabled by default, and Cloud Connector does not automatically send alert emails. However, some features are disabled by default, including the sending of security-related alerts and the automatic sending of emails from Cloud Connectors. To access these features, users must manually configure their email addresses or mail servers in the organization's settings.


## Implementation

1. Configure the administration console so that emails about expiring certificates, system notifications and new administrators are sent to specific email addresses or to the email addresses of all administrators.

2. Activate emails for security alerts for end users. Configure at least the following settings:
* E-mail change
* Change of the login name
* Change of login information
* Activating or deactivating the TFA device

3. Configure the Cloud Connector so that it sends e-mail messages at least for certificates.

4. Regularly check that audit logging has not been deactivated.


## Verification of control

> TODO


## References

* SAP BTP Security Recommendations: BTP-IAS-0022, BTP-IAS-0023, BTP-CLC-0007, BTP-CLC-0021

