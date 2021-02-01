---
Security Function: IY
Category: Risk Assessment
Technology: ABAP
Maturity Level: 1
IPAC: Customizing (C)
Defender: Process
Prerequisite:
---

## Description

ABAP uses a mostly explicit authorization model. This means that an authorization check only takes place if a program carries out the check explicitly itself. In other words: If there is no explicit authorization check in the code, there is no check as to whether a user is actually authorized.
In custom-developed code, (important) authorization checks are frequently overlooked. This means that the authorization concept has no effect. This leads to compliance infringements, which can have serious consequences in the event of an audit. For this reason, it is critically important that authorization checks are carried out in custom developments by the programs themselves wherever necessary, and that all authorization checks are also correctly programmed from a formal perspective.
In addition to the lack of authorization checks, the structuring of program components can also influence the viability of the authorization concept. For example, you should query how function modules are comprised under the assumption that S_RFC authorizations are assigned at function group level.
Authorization checks are typically the most frequent security error in ABAP custom developments.

## Implementation

All authorization checks in ABAP must be carried out with SAP standard mechanisms. This typically means that, either the command AUTHORITY-CHECK OBJECT or a module, which has been specially developed for checking a specific authorization (such as the SAP function module 'AUTHORITY_CHECK_DATASET'), or an access declaration by the Data Access Control (DAC) language for Core Data Services (CDS) must be used.

## Verification of control

- [ ] Review if negative and positive access control testing is specified and the execution documented in the test protocol.
- [ ] Review source code review is carried out and documented on all code changes for the correct implementation of user access control in the change.


## References

- CIS CSC 4
- COBIT 5 APO12.05, APO13.02
- ISO/IEC 27001:2013 Clause 6.1.3
- NIST SP 800-53 Rev. 4 PM-4, PM-9
- BSI APP 4.6 ??
- OWASP
