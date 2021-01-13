---
Security Function: PT
Category: Identity Management, Authentication and Access Control
Technology: SAP ABAP
Maturity Level: 1
IPAC: Access (A)
Defender: Process
Prerequisite:
---

## Description

Access control policies and specific guidelines pertaining to authorization restrictions and passwords should be regularly issued, verified, audited, and revoked where necessary.

## Implementation

It is important to create policies and guidelines which addresses the different authorizations and password policies in place.

- [ ] Create an access control policy to define users and their respective user groups
- [ ] Create a strong SAP password policy for all users
- [ ] Guidelines on setting a strong password should be created for users to follow 

Note: Controls PT-P-IP-M01-005 and PT-P-IP-M01-010 can assist with building a strong SAP password policy

## Verification of Control

- [ ] Verify that authorizations and access to SAP systems are documented
- [ ] Verify that users are assigned to their respective user groups as per their job roles
- [ ] Verify that a strong password policy is in place and implemented

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A19 Definition of the security guidelines for user / Definition der Sicherheitsrichtlinien für Benutzer
- CIS CSC 3, 5, 12, 14, 15, 16, 18
- COBIT 5 DSS05.04
- ISA 62443-2-1:2009 4.3.3.7.3
- ISA 62443-3-3:2013 SR 2.1
- ISO/IEC 27001:2013 A.6.1.2, A.9.1.2, A.9.2.3, A.9.4.1, A.9.4.4, A.9.4.5
- NIST SP 800-53 Rev. 4 AC-1, AC-2, AC-3, AC-5, AC-6, AC-14, AC-16, AC-24
