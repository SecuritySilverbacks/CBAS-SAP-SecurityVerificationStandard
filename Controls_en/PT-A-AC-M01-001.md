---
Security Function: PT
Category: Identity Management, Authentication and Access Control
Technology: SAP ABAP
Maturity Level: 1
IPAC: Access (A)
Defender: Process
Prerequisite:
---

## Description

SAP user administration should be only allowed to administrators that are identified by the organization and have the appropriate rights to handle the creation, deletion, assigning roles and profiles, and password management of users.

## Implementation

Rights to administer users in SAP should only be given to users that have the same job role or identified by the organization(1).

Logging and monitoring SAP administrators allows easier identification of administrative misuse.

(1) - Most user administrators are from the IT department in organizations. Some organizations leave the user administration to HR, which is more preferable.


## Verification of Control

- Identify SAP user administrators and verify that these roles are given to only allowed users
- Logs are available to verify the misuse of administrative actions
- Monitoring is available to detect any misuse with user administration

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A5 Configuration and protection of the SAP user administration / Konfiguration und Absicherung der SAP-Benutzerverwaltung
- SAP Security Baseline Template V2.1: 2.3.1
- CIS CSC 1, 5, 15, 16
- COBIT 5 DSS05.04, DSS06.03
- ISA 62443-2-1:2009 4.3.3.5.1
- ISA 62443-3-3:2013 SR 1.1, SR 1.2, SR 1.3, SR 1.4, SR 1.5, SR 1.7, SR 1.8, SR 1.9
- ISO/IEC 27001:2013 A.9.2.1, A.9.2.2, A.9.2.3, A.9.2.4, A.9.2.6, A.9.3.1, A.9.4.2, A.9.4.3
- NIST SP 800-53 Rev. 4 AC-1, AC-2, IA-1, IA-2, IA-3, IA-4, IA-5, IA-6, IA-7, IA-8, IA-9, IA-10, IA-11
