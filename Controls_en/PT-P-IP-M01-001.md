---
Security Function: PT
Category: Identity Management, Authentication and Access Control
Technology: SAP Database
Maturity Level: 1
IPAC: Access (A)
Defender: Technology
Prerequisite:
---

## Description

Access to SAP databases must be protected from unauthorized access and misuse.  

## Implementation

Default SAP IDs are not to be allowed to access the SAP database. Removing other IDs and users from accessing the database allows the principle of least privilege, separation of duties, and need to know.

Check the transaction log file for unneeded accounts. The transaction file can be viewed by executing R3trans -d.

Users that are allowed to access the database are limited to only the tables that allows them to complete their job.

## Verification of Control

- [ ] SAPR3, SAPSID, or SAPABAP1 disabled to access the database
- [ ] Users not required to access the database are removed
- [ ] Data manipulation only given to SAP support
- [ ] Users that are required to access the database are not to be given permissions to Table USR\*, Table T000, SAPUSER, RFCDES, PA\*, HCL\*, and any other tables not required to get their job done

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A7 Securing the SAP database/ Absicherung der SAP-Datenbanken
