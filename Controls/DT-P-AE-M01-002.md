---
Security Function: DT
Category: Anomalies and Events
Technology: SAP ERP
Maturity Level: 1
IPAC: Platform (P)
Defender: Technology
Prerequisite:
---

## Description

Identifying and collecting security related activities is important for evidence collection following a security incident or event. The security audit log might contain sensitive data that needs to be stored and encrypted properly.  

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
- The use of digital signatures performed by the system
- Viruses found by the Virus Scan Interface
- Errors that occur in the Virus Scan Interface
- Unsuccessful password checks for a specific user in a specific client

Personal identifiable information can be found in certain security audit logs, make sure to follow any data protection regulations your organizations falls under when storing personal information.

## Verification of Control

- [ ]


## References:
