---
Security Function: PT
Category: Information Protection Processes and Procedures
Technology: SAP HANA
Maturity Level: 1
IPAC: Platform (P)
Defender: Process
Prerequisite: NA
---

## Description

SAP database contains critical information and data for different departments within an organization. The data must always be backed up, protected through encryption, maintained and reviewed on regular basis, and tested regularly.   

## Implementation

Database system backups and tenant backups are required to be done on a scheduled and consistent manner. A full database should be done on a weekly basis, and a differential or incremental backup throughout the week.

## Verification of Control

- [ ] A full database backup scheduled on a weekly bases
- [ ] Differential or incremental backups scheduled throughout the weekly

## References:
- CIS CSC 10
- COBIT 5 APO13.01, DSS01.01, DSS04.07
- ISA 62443-2-1:2009 4.3.4.3.9
- ISA 62443-3-3:2013 SR 7.3, SR 7.4
- ISO/IEC 27001:2013 A.12.3.1, A.17.1.2, A.17.1.3, A.18.1.3
- NIST SP 800-53 Rev. 4 CP-4, CP-6, CP-9
