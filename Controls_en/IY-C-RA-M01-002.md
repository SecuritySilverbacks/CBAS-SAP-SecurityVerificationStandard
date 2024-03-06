---
Security Function: Identify (IY)
Category: Risk Assessment (IY.RA)
Technology: SAP ABAP
Maturity Level: 1
IPAC: Customization (C)
Defender: Process
Prerequisite: IY-C-RA-M01-001
---

## Description

Testability of ABAP software implementations.

A central security concept in the SAP standard system is the separation of development, test and productive systems.
The test system plays an important role here. In the test system, the decision is made as to whether an application satisfies the requirements of the company. In this process, both functional and non-functional quality aspects of the application are checked. For a quality check to provide reliable results, it is not sufficient for the tester to have comprehensive expertise in the quality assurance field. The application itself must also be testable. This means that a tester can run the application for test purposes and that, in cases of doubt, the tester can analyse the source code of the application.

If specific functionality in an application cannot be run (by a tester) in the test system, the tester cannot determine whether it satisfies the quality requirements. In this case, unchecked code would be transferred to a productive system exposing unverified risk to the system.

## Implementation

1. All custom developments that are to be used in systems processing productive data must be testable. This means that all functionality is documented and can be analysed and run in a test system.

2. Custom developments that should not be used in systems processing productive data shall not be deployed to according systems

3. As part of code change review process all custom code has to be checked to carry that:
  - security requirements are implemented with standardized and traceable procedures. Concealment is not a valid security strategy.
  - The change implements an architecture and uses interfaces in such a way that implemented security mechanisms for the protection of your business logic cannot be circumvented by side-effects or by reusing components of the change's implementation.
  - No part of the implementation uses code code obfuscation like the ABAP code hiding feature available up the ABAP release 7.4x
  - The implementation does not limit to run code based on system variables like sy-mandt and sy-sysid, providing the information to an ABAP program on the executing system in which it is currently being run if testing can't simulate the target system accordingly.

## Verification of control

- [ ] Review if test execution criteria, and path are specified and documented, and their execution is documented in the test protocol of the change.
- [ ] Audit if the source code review is carried out and documented on all custom code changes for the correct implementation of testability in the change.

## References

- CIS CSC 4
- COBIT 5 APO12.01, APO12.02, APO12.03, APO12.04
- ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12
- ISO/IEC 27001:2013 Clause 6.1.2
- NIST SP 800-53 Rev. 4 RA-3, SI-5, PM-12, PM-16
- BSI APP (February 2020) 4.6 A16, A21
