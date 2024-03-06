---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP HANA
Maturity Level: 3
SAP Operational Area: Access (A)

Prerequisite:
---

## Description

SAP delivers a number of predefined roles that are to be regarded by SAP exclusively as role templates and contain all authorizations for a specific task.
* Predefined Catalog role 'CONTENT_ADMIN' which contains all authorizations required for working with information models in the SAP HANA database repository.
* Predefined catalog role 'MODELING' that contains the analytic privilege '_SYS_BI_CP_ALL', which can be used to view any data from active views that are protected by an XML-based analytic privilege.
* Predefined Catalog Role 'SAP_INTERNAL_HANA_SUPPORT' which contains all authorizations that allow access to certain internal low-level system views required by SAP HANA development support in support situations.


## Implementation

Make sure that 
* only the user 'SYSTEM' is assigned the predefined Catalog role 'CONTENT_ADMIN'
* only the user 'SYSTEM' is assigned the predefined Catalog role 'MODELING'
* no one is assigned the predefined Catalog role 'SAP_INTERNAL_HANA_SUPPORT' in normal operation


## Verification of control

The following SQL statements can be used to determine the users to whom the corresponding predefined Catalog role is assigned.
* Predefined Catalog Role 'CONTENT_ADMIN'
	* `SELECT * FROM GRANTED_ROLES WHERE ROLE_NAME = 'CONTENT_ADMIN' AND GRANTEE NOT IN ('SYSTEM');`
* Predefined Catalog Role 'MODELING'
	* `SELECT * FROM GRANTED_ROLES WHERE ROLE_NAME = 'MODELING' AND GRANTEE NOT IN ('SYSTEM');`
* Predefined Catalog Role 'SAP_INTERNAL_HANA_SUPPORT'
	* `SELECT * FROM EFFECTIVE_ROLE_GRANTEES WHERE ROLE_NAME = 'SAP_INTERNAL_HANA_SUPPORT';`

## References
* SAP HANA Security Checklists and Recommendations 2.0 SPS 07: 2.1
