---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP HANA
Maturity Level: 2
SAP Operational Area: Access (A) & Platform (P)

Prerequisite:
---

## Description

In most cases, SAP installations are either provided by a service provider or created as a copy of an existing SAP installation.
In both cases, the settings do not have to comply with the internal specifications or you may not want the passwords of sensitive system users to be known to too many people.
It therefore makes sense to carry out certain follow-up work after the handover of an SAP installation as part of a "secure handover".

## Implementation

1. Change the passwords of all operating system users, in particular the following
* \<sid>adm,\<sid>crypt, root, sapadm

2. Make sure that
* the file mask has been set appropriately (critical systems: high, other systems: medium [is the default value]); this corresponds to the file mask 600 or 640

3. ÜCheck the file /etc/sudoers for occurrences of
* Defaults targetpw
	* With this setting, the root password must be specified when sudo is generally executed.
* ALL ALL=(ALL) ALL
	This should only be used if Defaults targetpw is also set at the same time.


4. In all databases (SystemDB, Tenant DBs), check all database users that were created by the service provider and delete or deactivate those database users that are not required in your application scenario.

The predefined database users include:
* SYS, SYSTEM, XSSQLCC_AUTO_USER_<generated_ID>, _SYS_AFL, _SYS_DATA_ANONYMIZATION, _SYS_EPM, _SYS_PLAN_STABILITY, _SYS_REPO, _SYS_SQL_ANALYZER, _SYS_STATISTICS, _SYS_TABLE_REPLICAS, _SYS_TABLE_REPLICA_DATA, _SYS_TASK, _SYS_WORKLOAD_REPLAY, _SYS_XB

Database users in connection with the SAP HANA Deployment Infrastructure (HDI)
* _SYS_DI*

5. Change the passwords of all database users in all databases (SystemDB, Tenant DBs).
The user SYSTEM should be emphasized here, for which a deactivation must be carried out in addition to the password change.

6. Change the following two encryption master keys:
* Instance secure store in the file system (SSFS)
* System public key infrastructure (PKI) SSFS
SAP Note 2183624 describes the potential information leak when using the standard SSFS master key.

7. Recreate the system's PKI, which is used to protect internal communication, to generate new certificates and keys.

8. All tenant databases use the same trust store as the system database for SAML-based user authentication. To prevent users of one tenant database from logging on to another tenant database, including the system database, via SAML, create individual certificate collections in each tenant database with the purpose SAML and SSL.
As an additional safeguard, the parameter 'sslTrustStore' in the 'communication' section of the 'global.ini' file should be set to a non-existent trust store in each tenant database.

9. After installation or handover by your service provider, first change all root encryption keys and activate data and log volume encryption.

10. The SAP HANA database offers the option of preventing changes in the tenant databases using a block list for configuration changes in the 'multidb.ini' file. Check whether the parameters contained in the multidb.ini file meet your requirements and adjust them if necessary.

11. Certain database functions can be deactivated to protect and/or customize your system. This includes, for example 
* Direct access to the file system or network
* Restrictions of import/export or backup functionalities
Check the list of functions that can be deactivated and deactivate those that are not required in your implementation scenario.


## Verification of control

1. Under Linux, the last modification date for a user can be queried using the command 'chage -l <user>'.

2. You can check the directory authorizations with the following SQL statements and tools.
* With the SQL statement `SELECT * FROM "PUBLIC" . "M_INIFILE_CONTENTS" WHERE SECTION = 'import_export' AND KEY = 'file_security';` you can check the parameter.
* With the SQL statement `SELECT * FROM EFFECTIVE_PRIVILEGE_GRANTEES WHERE (OBJECT_TYPE = 'SYSTEMPRIVILEGE') AND (PRIVILEGE = 'EXPORT' OR  PRIVILEGE='IMPORT');` you can check which users have the 'EXPORT' or 'IMPORT' system privilege.
* You can use the SAP HANA database lifecycle manager (HDBLCM) and its installation parameter 'check_installation' to check the directory authorizations of the files and directories used by the SAP HANA database.

3. If you use the storage connector option to mount SAP HANA volumes, your sudo configuration is changed during the SAP HANA installation so that <sid>adm can execute a special set of commands as root.
This is intentional and does not represent a security risk. However, <sid>adm should not be able to execute arbitrary commands as root without proper authentication.

4. With the SQL statement `SELECT * FROM "SYS"."USERS";` all database users of a tenant are returned.
The SQL statement `SELECT * FROM "SYS"."USERS" WHERE USER_DEACTIVATED='TRUE';` returns the deactivated users.

5. The column 'LAST_PASSWORD_CHANGE_TIME' of the system view '"SYS". "USERS"' contains the time of the last password change of a user.

6. Check the date of the two files for System PKI SSFS
* `SELECT * FROM M_HOST_INFORMATION WHERE KEY IN ('SSFS_MASTERKEY_CHANGED',
'SSFS_MASTERKEY_SYSTEMPKI_CHANGED');`
* `SELECT * FROM M_HOST_INFORMATION WHERE KEY IN ('SSFS_MASTERKEY_CHANGED', 'SSFS_MASTERKEY_SYSTEMPKI_CHANGED')`

7. The following two SQL statements can be used to select the certificates of a system; the 'VALID_FROM' column usually indicates the creation date of a certificate.
* `SELECT * FROM "SYS"."ENCRYPTION_ROOT_KEYS"`
* `SELECT * FROM CERTIFICATES`
* `SELECT * FROM PSE_CERTIFICATES`

8. You can use the following SQL statements to check whether a separate certificate store for SAML and SSL is used for each tenant and whether the parameter 'sslTrustStore' points to "nothing".
* Execute individually in each tenant database: `SELECT * FROM PSES WHERE PURPOSE ='SAML' OR PURPOSE ='SSL';`
* Executed in the system database: `SELECT * FROM SYS_DATABASES.M_INIFILE_CONTENTS WHERE DATABASE_NAME='<TENANT_DB_NAME>' AND SECTION='communication' AND KEY = 'ssltruststore';`

9. With the SQL statement `SELECT * FROM M_ENCRYPTION_OVERVIEW WHERE SCOPE='LOG' OR SCOPE = 'PERSISTENCE'` you can check whether data and log volume encryption is active.

10. With the SQL statement `SELECT * FROM "PUBLIC". "M_INIFILE_CONTENTS" WHERE FILE_NAME = 'multidb.ini';` you can have the list of parameters to be configured exclusively in the system database returned to you.

11. With the SQL statement `SELECT * FROM "PUBLIC"."M_CUSTOMIZABLE_FUNCTIONALITIES";` you can view the status of the functions that can be deactivated.


## References
* SAP HANA Security Checklists and Recommendations 2.0 SPS 07: 1.2, 2.3, 2.4, 2.7
* [SAP Note 2252941](https://launchpad.support.sap.com/#/notes/2252941)
