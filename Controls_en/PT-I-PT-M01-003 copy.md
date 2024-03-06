---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP HANA
Maturity Level: 2
SAP Operational Area: Integration (I)

Prerequisite: 
---

## Description

If LDAP is used for user authentication, the communication can be secured using TLS; protect any transmitted passwords.
SAP HANA supports both 'LDAP with STARTTLS' and 'LDAP over TLS/SSL'.

Especially in the cloud environment, such as Azure, it is advisable to only use encrypted communication channels.


## Implementation

Check and set the parameters for secure LDAP communication.
The parameters can be found in the 'ldap' section in the 'global.ini' file.
These are the parameters: 'sslMinProtocolVersion', 'sslMaxProtocolVersion', 'sslCipherSuites' and 'sslenforce'.


## Verification of control

Check the following parameters in the 'ldap' section in the 'global.ini' file 'sslMinProtocolVersion' (=TLS12), 'sslMaxProtocolVersion' (=MAX), 'sslCipherSuites' (=PFS:HIGH::EC_HIGH:+EC_OPT) and 'sslenforce' (=true).
`SELECT * FROM "PUBLIC" . "M_INIFILE_CONTENTS" WHERE FILE_NAME = 'global.ini' AND SECTION = 'ldap' AND KEY LIKE 'ssl%'`


## References
* SAP HANA Security Guide for SAP HANA Platform 2.0 SPS 07: 5.3.2
* SAP HANA Administration Guide for SAP HANA Platform 2.0 SPS 07: 
