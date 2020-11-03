---
Security Function: PT
Category: Information Protection Processes and Procedures
Technology: SAP HANA
Maturity Level: 1
IPAC: Platform (P)
Defender: Process
Prerequisite: PT-P-IP-M01-001
---

## Description

SAP database contains critical information and data for different departments within an organization. The data must always be backed up, protected through encryption, maintained and reviewed on regular basis, and tested regularly.   

## Implementation

Validating that a backup completed successfully is not enough to determine if restoration is possible. Scheduling a monthly restoration activity to ensure backups are verified and successfully restored is mandatory for the organization's disaster and contingency plans.

## Verification of Control

- [ ] Verify backup has completed successfully
- [ ] Schedule a monthly/weekly restore of data on a non-production environment to verify backups

## References:
- CIS CSC 10
- COBIT 5 APO13.01, DSS01.01, DSS04.07
- ISA 62443-2-1:2009 4.3.4.3.9
- ISA 62443-3-3:2013 SR 7.3, SR 7.4
- ISO/IEC 27001:2013 A.12.3.1, A.17.1.2, A.17.1.3, A.18.1.3
- NIST SP 800-53 Rev. 4 CP-4, CP-6, CP-9
