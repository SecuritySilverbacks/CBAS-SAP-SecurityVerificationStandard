---
Security Function: Identify (IY)
Category: Risk Assessment (IY.RA)
Technology: SAP ABAP
Maturity Level: 1
IPAC: Customization (C)
Defender: Process
Prerequisite: IY-C-RA-M01-001, IY-C-RA-M01-004
---

## Description

Use of protective mechanisms

The SAP standard system provides companies with various mechanisms to protect their data. For this reason, the security strategies of many companies are based on the knowledge that the mechanisms in the SAP standard systems provide a solid foundation and are not (or should not be) compromised.
These mechanisms include:
- Client/tenant separation
- Identity management
- Roles and authorizations management
- Separation of development, test and production
- Logging of security events

## Implementation

1. As part of code change review process all custom code has to be checked to carry that:
    - it must not undermine the security mechanisms of the SAP standard system.
    - If the SAP standard system has earmarked a security mechanism for specific tasks, then this security mechanism should also be used in change's custom code.
    - In the target system release, in which the application is to be run, the ABAP code shouldn't use any obsolete language elements.
    - The coding should be tested using the extended syntax check and any deficits should be eliminated.
    - Customer-specific database tables should generally be delivered for disallowing manual data maintenance by SAP standard tools. If manual table maintenance is required, then a maintenance application (maintenance view) should be created.

## Verification of control

- [ ] Audit if the source code review is carried out and documented on all custom code changes to verify the correct use of protective mechanisms.

## References

- CIS CSC 4
- COBIT 5 APO12.01, APO12.02, APO12.03, APO12.04
- ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12
- ISO/IEC 27001:2013 Clause 6.1.2
- NIST SP 800-53 Rev. 4 RA-3, SI-5, PM-12, PM-16
