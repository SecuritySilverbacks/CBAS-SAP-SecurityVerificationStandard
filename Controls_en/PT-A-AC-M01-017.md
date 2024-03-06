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
These should only be assigned according to the need-to-know principle.

## Implementation

1. In a productive database, only administrative or support users should be granted the following two system privileges:
* CATALOG READ
* TRACE ADMIN

2. In general, the following system privileges should only be assigned to administrative users if this is necessary for your task.
* ADAPTER ADMIN
* AGENT ADMIN
* AUDIT ADMIN
* AUDIT OPERATOR
* BACKUP ADMIN
* BACKUP OPERATOR
* CERTIFICATE ADMIN
* CREATE REMOTE SOURCE
* CREDENTIAL ADMIN
* ENCRYPTION ROOT KEY ADMIN
* EXTENDED STORAGE ADMIN
* INIFILE ADMIN
* LDAP ADMIN
* LICENSE ADMIN
* LOG ADMIN
* MONITOR ADMIN
* OPTIMIZER ADMIN
* RESOURCE ADMIN
* SAVEPOINT ADMIN
* SERVICE ADMIN
* SESSION ADMIN
* SSL ADMIN
* TABLE ADMIN
* TRUST ADMIN
* VERSION ADMIN
* WORKLOAD ADMIN
* WORKLOAD * ADMIN


## Verification of control

Using the SQL statement for example
`SELECT * FROM EFFECTIVE_PRIVILEGE_GRANTEES WHERE OBJECT_TYPE = 'SYSTEMPRIVILEGE' AND PRIVILEGE = 'SSL ADMIN' AND GRANTEE NOT IN ('SYSTEM','_SYS_REPO');`
you will receive all users who are assigned the system privilege 'SSL ADMIN'.

## References
* SAP HANA Security Checklists and Recommendations 2.0 SPS 07: 2.1
