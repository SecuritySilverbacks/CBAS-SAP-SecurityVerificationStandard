---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP HANA
Maturity Level: 2
SAP Operational Area: Access (A)

Prerequisite:
---

## Description

The standard password policy of an SAP HANA system limits the lifetime of user passwords to 182 days. However, this general default can be deactivated at user level.

## Implementation

Make sure that the "Password lifetime check" is not deactivated for database users of individuals.

## Verification of control

Using the SQL statement
`SELECT * FROM "SYS"."USERS" WHERE IS_PASSWORD_LIFETIME_CHECK_ENABLED='FALSE';`
you will receive all users for whom the password duration is not restricted.

## References
* SAP HANA Security Checklists and Recommendations 2.0 SPS 07: 2.1
