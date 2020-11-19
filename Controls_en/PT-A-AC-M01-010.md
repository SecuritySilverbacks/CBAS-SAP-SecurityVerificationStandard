---
Security Function: PT
Category: Identity Management, Authentication and Access Control
Technology: SAP HANA
Maturity Level: 1
IPAC: Access (A)
Defender: Technology
Prerequisite: PT-PA-IP-M01-001
---

## Description

SAP standard users are required to be managed and securely configured to avoid any misuse to SAP systems. This includes changing default passwords and restricting standard users.

## Implementation

The below standard user, found in HANA, are required to be managed and securely configured: (The Verification of Control section will help organizations have the basic requirements to secure the user)
1. SYSTEM


## Verification of Control

- [ ] SYSTEM
  - [ ] Administrator users have been created
  - [ ] SYSTEM user to be deactivated
  - [ ] Do not restrict the valid time range of user SYSTEM

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A4 Configuration and protection of the SAP user administration / Konfiguration und Absicherung der SAP-Benutzerverwaltung
- SAP Security Baseline Template V2.1: 2.3.1.2.2
