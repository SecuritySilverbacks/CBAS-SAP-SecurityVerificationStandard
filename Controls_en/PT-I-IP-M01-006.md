---
Security Function: PT
Category: Information Protection Processes and Procedures
Technology: RFC Connections
Maturity Level: 1
IPAC: Integration
Defender: Process
Prerequisite: PT-I-IP-M01-001
---

## Description

Managing RFC connections between different systems of different classification levels is required in order to mitigate privilege escalation to sensitive or production systems.

## Implementation

As a rule of thumb, connections from lower classification systems, such as development or test systems, to high classification systems, such as production systems, should not use a trusted system logon or store user credentials of the target system.
Connectivity configuration data is the only thing that can be stored in the different systems. Accordingly, the logon must be performed by means of the respective user in the target system by authentication.


## Verification of Control

- Authentication is required on every connection from lower to higher classification system
- To determine RFC connections that store user credentials use the RSRFCCHK report in all systems locally
- Restrict authorization to maintain RFC destinations in transaction SM59 by strictly controlling  authorization  object S_RFC_ADM

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A8 Securing the SAP RFC interface/ Absicherung der SAP-RFC-Schnittstelle
- SAP Security Baseline Template V2.0: 2.3.2.3
