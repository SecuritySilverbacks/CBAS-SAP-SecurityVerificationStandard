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

Protection of security sensitive data.

SAP systems contain large volumes of business-critical data. The SAP standard system provides various mechanisms to protect this critical data against unauthorized access.
However, errors in custom developments can enable unauthorized accesses and data leakage. If an employee obtains unauthorized access to data, he can subsequently transfer this data to an environment that is no longer controllable by the company.


## Implementation

1.	Business-critical data must also be protected by the program against unauthorized access.
2.	Company rules and, in particular, legal regulations must be complied with.
1.3.1	Handling of login data
These requirements for the protection of data must be complied with especially during the processing and administration of login data. This includes, in addition to login tokens, passwords and other possible authentication factors, also user names and identity information relating to users. Authentication features must satisfy the requirements of the strictest confidentiality when saved, transferred and during input. For example:
- Saving of passwords in the source text of programs is an infringement of this requirement!
- The plain text display of passwords on login screens is an infringement of this requirement!
- Saving of passwords in plain text in database tables or in the data system is an infringement of this requirement!
User names and identity information must be protected with particular care against unauthorized access. In particular, user names should only be viewable in logs and in restricted numbers.

## Verification of control

_Steps to verify if a control exists_

## References

_References_
