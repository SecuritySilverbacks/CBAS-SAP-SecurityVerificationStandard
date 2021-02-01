---
Security Function: IY
Category: Risk Assessment
Technology: ABAP
Maturity Level: 1
IPAC: Customizing (C)
Defender: _People, Process, Technology_
Prerequisite: _A control that is required to be in place before the current one_
---

## Description

Testability of ABAP software implementations.

A central security concept in the SAP standard system is the separation of development, test and productive systems.
The test system plays an important role here. In the test system, the decision is made as to whether an application satisfies the requirements of the company. In this process, both functional and non-functional quality aspects of the application are checked. For a quality check to provide reliable results, it is not sufficient for the tester to have comprehensive expertise in the quality assurance field. The application itself must also be testable. This means that a tester can run the application for test purposes and that, in cases of doubt, he can analyse the source code of the application.

## Implementation

1. If specific functionality in an application cannot be run (by a tester) in the test system, the tester cannot determine whether it satisfies the quality requirements. In this case, unchecked code would be transferred to a productive system and this would mean a significant risk for a company.
It is therefore critical that custom developments can be adequately tested in the test system.

2. All custom developments that are used in the productive system must be testable. This means that all functionality is documented and can be analysed and run in a test system.


## Verification of control

_Steps to verify if a control exists_

## References

_References_
