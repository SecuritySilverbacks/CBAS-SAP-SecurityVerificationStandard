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

Use of protective mechanisms

The SAP standard system provides companies with various mechanisms to protect their data. For this reason, the security strategies of many companies are based on the knowledge that the mechanisms in the SAP standard systems provide a solid foundation and are not (or should not be) compromised.
These mechanisms include:
- Client separation
- Identity management
- Roles and authorizations
- Separated development, test and productive systems
- Logging




## Implementation

1.	ABAP programs must not undermine the security mechanisms of the SAP standard system.
2.	If the SAP standard system has earmarked a security mechanism for specific tasks, then this security mechanism should also be used in ABAP programs.
3.	In the target system release, in which the application is to be run, the ABAP code should not use any obsolete language elements. The coding should be tested using the extended syntax check and any deficits should be eliminated.
4.	Customer-specific tables should generally be delivered with the maintenance setting “Display/maintenance not allowed” for table view maintenance. If table maintenance is required, then a maintenance view should be created for this table.


## Verification of control

_Steps to verify if a control exists_

## References

_References_
