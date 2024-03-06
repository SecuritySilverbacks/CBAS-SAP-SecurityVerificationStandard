---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP HANA
Maturity Level: 2
SAP Operational Area: Access (A)

Prerequisite:
---

## Description

System privileges allow database users to execute administrative commands database-wide.
It can happen that individual system privileges are necessary for daily administrative work, but certain combinations of several system privileges can be considered particularly critical.

## Implementation

The following combinations of system privileges should not be assigned together to one user:

1. USER ADMIN and ROLE ADMIN

2. CREATE SCENARIO and SCENARIO ADMIN

3. AUDIT ADMIN and AUDIT OPERATOR

4. CREATE STRUCTURED PRIVILEGE and STRUCTUREDPRIVILEGE ADMIN


## Verification of control

Using the SQL statement
`SELECT * FROM "PUBLIC"."EFFECTIVE_PRIVILEGES" WHERE USER_NAME
= '<USER_NAME>';`
can be used to determine which system privileges are assigned to a user.

## References
* SAP HANA Security Checklists and Recommendations 2.0 SPS 07: 2.1
