---
Security Function: DT
Category: Anomalies and Events
Technology: SAP ERP
Maturity Level: 1
IPAC: Platform (P)
Defender: Process
Prerequisite: DT-P-AE-M01-001
---

## Description

Security audit logs:

Identifying and collecting security-related activities is important for evidence collection following a security incident or event. The security audit log might contain sensitive data that needs to be stored and encrypted properly.  

## Implementation

Activating security audit logs depends on which logs your organization wants to collect. Available logs are shown below:

- Successful and unsuccessful dialog logon attempts
- Successful and unsuccessful RFC logon attempts
- RFCs to function modules
- Changes to user master records
- Successful and unsuccessful transaction starts
- Successful and unsuccessful report starts
- Changes to the audit configuration
- Activation and deactivation of the HTTP security session management or instances in which HTTP security sections were hard-exited
- File downloads
- Access to the file system that coincides with the valid logical paths and file names specified in the system  (particularly helpful in an analysis phase to determine where access to files takes place before activating the actual validation)
- ICF recorder entries or changes to the administration settings
- The use of digital signature validations performed by the system
- Viruses found by the Virus Scan Interface
- Errors that occur in the Virus Scan Interface
- Unsuccessful password checks for a specific user in a specific client

Personal identifiable information can be found in certain security audit logs, make sure to follow any data protection regulations your organizations falls under when storing personal information.

Alerts can be configured when a certain event occurs or a threshold is reached, this helps automate the review process of security audit logs and reduces workload from administrators. Sending logs to a central location helps to achieve setting up alerts.

## Verification of Control

- Configure alerts for important events to reactively respond to security events


## References:
