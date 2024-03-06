---
Security Function: Detect (DT)
Category: Anomalies and Events (DT.AE)
Technology: SAP HANA
Maturity Level: 2
SAP Operational Area: Access (A)

Prerequisite:
---

## Description

HANA audit trails should be written to either the system or tenant database. In the standard configuration, the audit trail parameters can only be changed in the system database.


## Implementation

The parameter "default_audit_trail_type" must be set to either the value SYSLOGPROTOCOL or CSTABLE.
The value "SYSLOGPROTOCOL" means that the log is written to the system database, while the value "CSTABLE" means that the log is written to the tenant database.
This is done in the "global.ini" file in the "auditing configuration" section of the HANA database.
* ALTER SYSTEM ALTER CONFIGURATION ( 'global.ini', 'SYSTEM' ) set ( 'auditing configuration' , 'default_audit_trail_type' ) = 'SYSLOGPROTOCOL';
* ALTER SYSTEM ALTER CONFIGURATION ( 'global.ini', 'SYSTEM' ) set ( 'auditing configuration' , 'default_audit_trail_type' ) = 'CSTABLE';


## Verification of control

Check that the "default_audit_trail_type" parameter in the "global.ini" file in the "auditing configuration" section is assigned either the value SYSLOGPROTOCOL or CSTABLE.


## References
* SAP Security Baseline Template V2.4: 2.4.3.1.3
* SAP HANA Security Guide for SAP HANA Platform 2.0 SPS 07: 12.3.1
