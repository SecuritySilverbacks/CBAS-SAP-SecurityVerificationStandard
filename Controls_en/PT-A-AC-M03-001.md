---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP HANA
Maturity Level: 1
SAP Operational Area: Access (A)

Prerequisite: PT-A-AC-M01-015
---

## Description

Passwords in SAP HANA must comply with certain guidelines in order to prevent any misuse of SAP systems. This includes the minimum password length for critical systems.

## Implementation

Change the following parameters in the "indexserver.ini" file in the "password policy" section on the HANA database

1. maximum_unused_initial_password_lifetime to an integer value between 1 and 14

* This parameter forces initial passwords to be valid for a maximum of the defined number of days and the user is automatically locked after the defined days have expired.

> * Default setting as of June 2023: 7 days

2. minimal_password_length to an integer value between 8 and 64

* This parameter forces passwords to meet a minimum length.

3. Check that the "effective" password policy of a user matches the "generic" password policy of the system.

## Verification of control

1. and 2. check that the parameter values for "maximum_unused_initial_password_lifetime" and "minimum_password_length" in the "indexserver.ini" file in the "password policy" section correspond to your specifications. `SELECT * FROM "PUBLIC" . "M_INIFILE_CONTENTS" WHERE FILE_NAME = 'indexserver.ini' AND SECTION = 'password policy' AND KEY IN ('maximum_unused_initial_password_lifetime', 'minimal_password_length')`
3. Manual comparison between the password policy of the system `SELECT * FROM "PUBLIC" . "M_INIFILE_CONTENTS" WHERE SECTION = 'password policy'` and the "effective" password policy of each user `SELECT * from "PUBLIC"."M_EFFECTIVE_PASSWORD_POLICY" where USER_NAME = '<USER_NAME>'`

## References

* SAP Security Baseline Template V2.4: 2.3.2.2.3, 3.1.1.14.2
* SAP HANA Security Guide for SAP HANA Platform 2.0 SPS 07: 7.3.1