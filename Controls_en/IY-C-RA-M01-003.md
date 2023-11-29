---
Security Function: IY
Category: Risk Assessment
Technology: ABAP
Maturity Level: 1
IPAC: Customizing (C)
Defender: Process
Prerequisite: IY-C-RA-M01-001, IY-C-RA-M01-004, IY-C-RA-M01-005
---

## Description

Protection of security sensitive data.

SAP systems contain large volumes of business-critical data. The SAP standard system provides various mechanisms to protect this critical data against unauthorized access.
However, errors in custom developments can enable unauthorized accesses and data leakage. If an employee obtains unauthorized access to data, he can subsequently transfer this data to an environment that is no longer controllable by the company.


## Implementation

1. The specification of the change includes a concise description of the required data protection adjustments according to the change.

2. As part of code change review process all custom code has to be checked to carry that:
  - Business-critical data must also be protected by the program against unauthorized access.
  - Company rules and, in particular, legal regulations must be complied with. Like:
    -	Handling of login data These requirements for the protection of data must be complied with especially during the processing and administration of login data. This includes, in addition to login tokens, passwords and other possible authentication factors, also user names and identity information relating to users. Authentication features must satisfy the requirements of the strictest confidentiality when saved, transferred and during input. For example:
      - Saving of passwords in the source text of programs is an infringement of this requirement.
      - The plain text display of passwords on login screens is an infringement of this requirement.
      - Saving of passwords in plain text in database tables or in the data system is an infringement of this requirement.
    identity information must be protected with particular care against unauthorized, and unreasonable  also in log and event data created by the software.

## Verification of control

- Review if data protection requirements are specified and documented, and their verification is documented in the test protocol of the change.
- Audit if the source code review is carried out and documented on all custom code changes for the correct implementation of data protection criteria.

## References

- CIS CSC 4
- COBIT 5 APO12.01, APO12.02, APO12.03, APO12.04
- ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12
- ISO/IEC 27001:2013 Clause 6.1.2
- NIST SP 800-53 Rev. 4 RA-3, SI-5, PM-12, PM-16
- OWASP ASVS 2.0 V8.3.1, V8.3.4
