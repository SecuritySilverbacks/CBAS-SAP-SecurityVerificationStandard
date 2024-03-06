---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP HANA
Maturity Level: 3
SAP Operational Area: Access (A)

Prerequisite:
---

## Description

In a productive system, far-reaching system privileges should be reserved exclusively for the two users SYSTEM and _SYS_REPO.
This includes:
* The system privilege 'DATA ADMIN' with which any DDL commands can be executed in the SAP HANA database.
* The system privilege 'DEVELOPMENT' with which database-internal 'ALTER SYSTEM' commands can be executed.
* The analytic privilege '_SYS_BI_CP_ALL' allows you to view any data from active views that are protected by an XML-based analytic privilege.
* The debug privilege enables debugging across different user sessions and/or procedures, calculation views of individual schemas or in general.


## Implementation

Make sure that, apart from the users SYSTEM and _SYS_REPO 
* the 'DATA ADMIN' system privilege
* the 'DEVELOPMENT' system privilege
* the Analytic Privilege '_SYS_BI_CP_ALL'
* the Object privileges 'ATTACH DEBUGGER' or 'DEBUG'

is not assigned to anyone.


## Verification of control

The following SQL statements can be used to determine the users to whom the corresponding privilege is assigned.
* System privilege 'DATA ADMIN'
	* `SELECT * FROM EFFECTIVE_PRIVILEGE_GRANTEES WHERE OBJECT_TYPE = 'SYSTEMPRIVILEGE' AND PRIVILEGE = 'DATA ADMIN' AND GRANTEE NOT IN ('SYSTEM','_SYS_REPO');`
* System privilege 'DEVELOPMENT'
	* `SELECT * FROM EFFECTIVE_PRIVILEGE_GRANTEES WHERE OBJECT_TYPE = 'SYSTEMPRIVILEGE' AND PRIVILEGE = 'DEVELOPMENT' AND GRANTEE NOT IN ('SYSTEM','_SYS_REPO');`
* Analytic Privileg '_SYS_BI_CP_ALL'
	* `SELECT * FROM EFFECTIVE_PRIVILEGE_GRANTEES WHERE OBJECT_TYPE = 'ANALYTICALPRIVILEGE' AND OBJECT_NAME = '_SYS_BI_CP_ALL' AND PRIVILEGE = 'EXECUTE' AND GRANTEE NOT IN ('SYSTEM','MODELING', 'CONTENT_ADMIN');`
* Object Privileg 'ATTACH DEBUGGER' oder 'DEBUG'
	* `SELECT * FROM GRANTED_PRIVILEGES WHERE PRIVILEGE='DEBUG' OR PRIVILEGE='ATTACH DEBUGGER';`

## References
* SAP HANA Security Checklists and Recommendations 2.0 SPS 07: 2.1
