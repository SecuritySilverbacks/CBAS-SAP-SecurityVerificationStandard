---
Security Function: PT
Category: Identity Management, Authentication and Access Control
Technology: SAP ABAP
Maturity Level: 1
IPAC: Access (A)
Defender: Technology
Prerequisite: PT-PA-IP-M01-001
---

## Description

SAP standard users are required to be managed and securely configured to avoid any misuse to SAP systems. This includes changing default passwords and restricting standard users.

## Implementation

The below standard users, found in ABAP systems, are required to be managed and securely configured: (The Verification of Control section will help organizations have the basic requirements to secure these users)
1. SAP*
2. DDIC
3. SAPCPIC
4. TMSADM
5. EARLYWATCH
6. Users creates by the SAP solution manager


## Verification of Control

- SAP*
  - Must exist in all clients
  - Must be locked in all clients
  - Default password must be changed
  - Must belong to the group SUPER in all clients
  - No profile should be assigned (especially SAP_ALL)
  - login/no_automatic_user_sapstar profile parameter must be set to 1

- DDIC
  - Default password must be changed
  - Must belong to the group SUPER in all clients

- SAPCPIC
  - Delete if user not required
  - If required, default password must be changed
  - Must belong to the group SUPER in all clients

- TMSADM
  - Default password must be changed
  - Should only exist in client 000
  - Must belong to the group SUPER in client 000
  - Authorization profile S_A.TMSADM should only be assigned

- EARLYWATCH
  - The user should not exist in any client

- Other users created by the SAP Solution Manager (SOLMAN_BTC, CONTENTSERV, SMD_BI_RFC, SMD_RFC, SMDAGENT_SAPSolutionManagerSID, SMD_ADMIN, SMD_AGT, SAPSUPPORT, SOLMAN_ADMIN)
  - Default password must be change

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A4 Configuration and protection of the SAP user administration / Konfiguration und Absicherung der SAP-Benutzerverwaltung
- SAP Security Baseline Template V2.1: 2.3.1
