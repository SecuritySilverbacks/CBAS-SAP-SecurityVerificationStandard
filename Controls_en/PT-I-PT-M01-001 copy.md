---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP HANA
Maturity Level: 2
SAP Operational Area: Integration (I)

Prerequisite: 
---

## Description

Especially in the cloud environment, such as Azure, it is advisable to only use encrypted communication channels. This also includes "internal" communication between the individual components of an SAP HANA network.

## Implementation

You have the following options in the 'communication' section of the 'global.ini' file:
1. 'ssl' = {on | systemPKI | off}
	* Should be set to 'on', e.g. if the TLS/SSL option is not available in HANA Studio, select 'systemPKI' here.
2. 'ssl_local' = {on | off}
	* If internal communication is also to be encrypted, this parameter must be set to 'on'. However, this parameter is only evaluated if the 'ssl' parameter is active, 'on' or 'systemPKI'.
3. 'sslinternalvalidatecertificate' = {true | false}
	* If the communication partner certificate is also to be validated for internal connections, this parameter must be set to 'true'.


## Verification of control

Check the 3 parameters in the 'communication' section in the 'global.ini' file according to your internal specifications.
* 'ssl' - general use of TLS/SSL
* 'ssl_local' - Use of TLS/SSL also for internal connections
* 'sslinternalvalidatecertificate' - Additional validation of the communication partner certificate
`SELECT * FROM "PUBLIC" . "M_INIFILE_CONTENTS" WHERE FILE_NAME = 'global.ini' AND SECTION = 'communication' AND KEY in ('ssl', 'ssl_local', 'sslinternalvalidatecertificate');`

## References
* SAP HANA Security Guide for SAP HANA Platform 2.0 SPS 07: 5.3.4.2
* SAP HANA Administration Guide for SAP HANA Platform 2.0 SPS 07: 
