---
Security Function: PT
Category: Information Protection Processes and Procedures
Technology: RFC Connections
Maturity Level: 1
IPAC: Integration
Defender: Technology
Prerequisite: PT-I-P-M01-001
---

## Description

RFC gateways are commonly found on ABAP, Java and stand-alone systems. Securing access for the different RFC services mitigates unauthenticated and un-authorized access from taking place.

## Implementation

Profile parameters should be set for the different systems to restrict access from different RFC connections.

Profile parameters:

1. gw/sec_info to be set to absolute filename of secinfo (ACL file)
2. gw/reg_info to be set to absolute filename of reginfo (ACL file)
3. gw/reg_no_conn_info set to 1 or higher odd numbers
4. gw/acl_mode set to 1 (initial security environment), if gateway access lists do not exist or not linked to the profile parameters, setting this profile parameter can break connections.
5. gw/monitor set to 1 (monitoring to be set to local access only)
6. gw/sim_mode set to 0 (can temporarily be set to 1 to test ACL files, and find missing entries to be added to the ACL. Do not keep the value to 1)
7. gw/rem_start set to disable or SSH_SHELL (An acceptable method to allow the start of programs via the RFC gateway)

## Verification of Control

- Profile parameters are set as per the implementation section
- Missing entries are detected and added to the access control list (see no. 6 in implementation section)

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A8 Securing the SAP RFC interface/ Absicherung der SAP-RFC-Schnittstelle
- SAP Security Baseline Template V2.0: 2.3.2.3.1
- SAP Note 1480644
- SAP Note 1408081
- SAP Note 1444282
- SAP Note 1298433
- SAP Note 64016
- SAP Note 1689663
