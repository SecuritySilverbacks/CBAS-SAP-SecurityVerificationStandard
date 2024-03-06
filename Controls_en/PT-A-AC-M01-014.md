---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP HANA
Maturity Level: 2
SAP Operational Area: Access (A)

Prerequisite:
---

## Description

Passwords in SAP HANA must comply with certain guidelines in order to prevent any misuse of SAP systems. This includes changing the initial password when logging in for the first time.

## Implementation

The "force_first_password_change" parameter of the password policy must be set to either true or TRUE.
This is done in the "indexserver.ini" file in the "password policy" section of the HANA database.


## Verification of control

### Indirect verification

Create a new user and then log in with this user. If you are prompted to change this user's password, the check is successful.

### Direct verification

Check that the "force_first_password_change" parameter in the "indexserver.ini" file in the "password policy" section is assigned either the value true or TRUE.


## References
- SAP Security Baseline Template V2.4: 2.3.2.2.3, 3.1.1.14.2
- SAP HANA Security Guide for SAP HANA Platform 2.0 SPS 07: 7.3.1
