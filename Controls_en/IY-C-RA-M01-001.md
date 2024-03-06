---
Security Function: Identify (IY)
Category: Risk Assessment (IY.RA)
Technology: SAP ABAP
Maturity Level: 1
IPAC: Customization (C)
Defender: Process
Prerequisite:
---

## Description

Access & Authorization

ABAP uses a mostly explicit authorization model. This means that an authorization check only takes place if a program carries out the check explicitly itself. In other words: If there is no explicit authorization check in the code, there is no check as to whether a user is actually authorized.
In custom-developed code, authorization checks are frequently overlooked. This means that the authorization concept has no effect. This leads to compliance infringements, which can have serious consequences in the event of an audit. For this reason, it is critically important that authorization checks are carried out in custom developments by the programs themselves wherever necessary, and that all authorization checks are also correctly programmed from a formal perspective.
In addition to the lack of authorization checks, the structuring of program components can also influence the viability of the authorization concept. For example, you should query how executable modules are comprised under the assumption that interface authorizations are not, or can't be assigned granular for the exposed business functionality.
Authorization checks are typically the most frequent security error in ABAP custom developments.

## Implementation

1. The specification of the change includes a concise description of the authorization requirement adjustments according to the change.
2. As part of code change review process all custom code has to be checked to carry that:
  - All authorization checks using the SAP standard mechanisms. This typically means that, either:
    - the command AUTHORITY-CHECK OBJECT or
    - a module, which has been specially developed for checking a specific authorization (such as the SAP function module 'AUTHORITY_CHECK_DATASET'),
    - or an access declaration by the Data Access Control (DAC) language for Core Data Services (CDS) must be used.
  - All direct executable modules implement explicit access restrictions at the execution start checking on user permissions to start the module
  - Before the command CALL TRANSACTION is carried out, an authorization check should take place to ensure that the current user is actually authorized to start the transaction. In case a transaction is called with the attempt of only providing limited access to the transaction's functionality, for example with predefined selection values and the addition SKIP FIRST SCREEN it can be reasonable not to carry out an authorization check for user permissions of starting the transaction, as this may requires unnecessary high privileges for the user.
  - The implementation verifies the user's authorization as close as possible to the execution of the protected business function.
  - The implementation handles the result of the verification of user's authorizations to permit legitimate access and execution and prohibit other by the verification of return codes like sy-subrc and authorization exceptions according to the checks implementation.

## Verification of control

- [ ] Review if negative and positive access control testing is specified and the execution documented in the test protocol of the change.
- [ ] Audit if the source code review is carried out and documented on all custom code changes for the correct implementation of user access control in the change.


## References

- CIS CSC 4
- COBIT 5 APO12.05, APO13.02
- ISO/IEC 27001:2013 Clause 6.1.3
- NIST SP 800-53 Rev. 4 PM-4, PM-9
- BSI APP (February 2020) 4.6 A1, A2, A3, A6, A7
- OWASP ASVS 2.0 V4.1.3, V4.1.4, V4.1.5
