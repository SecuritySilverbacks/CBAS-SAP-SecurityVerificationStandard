---
Security Function: Protect (PT)
Category: Information Protection Processes and Procedures (PT.IP)
Technology: SAP Java
Maturity Level: 1
IPAC: Platform (P) & Access (A)
Defender: Process & Technology
Prerequisite: PT-A-AC-M01-009
---

## Description

 Standard user allowed to access SAP systems should be properly managed and configured. This will allow organizations to follow the least privilege principle.

## Implementation

Default passwords for the standard users should be changed and the companies password policy(1) should be applied. This applies in particular to the users defined during installation (list according to SAP name proposal):
- J2EE_ADM_\<SID\>
- J2EE_GST_\<SID\> 
- SAPJSF_\<SID\>
- Administrator
- Guest
- pcd_service
- ume_service
- SAP\*

Standard users that are not required should be deleted or disabled.

Standard user IDs such as EARLYWATCH should not exist in any client.

Self registration should not be allowed and turned off for better access control.

(1) Password policies changes across different organizations depending on several criteria's such criticality of the industry, local or federal laws, security standards that are mandatory to the industry and so on  

## Verification of Control

- Default password for standard user IDs are changed
- Password policy is applied properly across SAP systems
- Standard user IDs are deleted and disabled when not in use
- User self registration is turned off

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A4 Protection of the delivered SAP standard user IDs / Absicherung der ausgelieferten SAP-Standardbenutzer-Kennungen
- SAP Security Baseline Template V2.0: 2.3.1
