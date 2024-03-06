---
Security Function: Detect (DT)
Category: Anomalies and Events (DT.AE)
Technology: SAP HANA
Maturity Level: 3
SAP Operational Area: Access (A)

Prerequisite: DT-A-AE-M01-001
---

## Description

Logging (audit trail) is deactivated by default. In critical systems, however, complete logging must be ensured.


## Implementation

Each tenant has to be activated individually
* For tenant databases, the "global_auditing_state" parameter in the "global.ini" file in the "auditing configuration" section must be set to either true or TRUE.
	* ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'system') set ('auditing configuration', 'global_auditing_state') = 'true';
* For the system database, the parameter "global_auditing_state" must be set differently in the "nameserver.ini" file in the "auditing configuration" section to either the value true or TRUE.
* ALTER SYSTEM ALTER CONFIGURATION ( 'nameserver.ini', 'system' ) set ( 'auditing configuration' , 'global_auditing_state' ) = 'true' ;


## Verification of control

Check that the parameter "global_auditing_state"
* is assigned either the value true or TRUE in the "global.ini" file in the "auditing configuration" section
* either the value true or TRUE is assigned in the "nameserver.ini" file in the "auditing configuration" section


## References
* SAP Security Baseline Template V2.4: 2.4.3.1.3
* SAP HANA Security Guide for SAP HANA Platform 2.0 SPS 07: 12.3.1
