---
Security Function: Protect (PT)
Category: Information Protection Processes and Procedures (PT.IP)
Technology: SAP ABAP
Maturity Level: 1
IPAC: Platform (P) & Access (A)
Defender: Process & Technology
Prerequisite: PT-A-AC-M01-009
---

## Description

 Standard user allowed to access SAP systems should be properly managed and configured. This will allow organizations to follow the least privilege principle.

## Implementation

Default passwords for the standard users should be changed and the companies password policy(1) should be applied.

Standard users that are not required should be deleted or disabled.

Obsolete standard users such as EARLYWATCH should not exist in any client.

Self registration should not be allowed and turned off for better access control.

(1) Password policies changes across different organizations depending on several criteria's such criticality of the industry, local or federal laws, security standards that are mandatory to the industry and so on  

## Verification of Control

- Default password for standard user IDs are changed
- Password policy is applied properly across SAP systems
- Standard users are deleted and disabled when not in use

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A4 Protection of the delivered SAP standard user IDs / Absicherung der ausgelieferten SAP-Standardbenutzer-Kennungen
- SAP Security Baseline Template V2.0: 2.3.1
