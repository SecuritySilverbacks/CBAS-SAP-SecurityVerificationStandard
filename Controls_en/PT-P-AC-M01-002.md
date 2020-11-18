---
Security Function: Protect
Category: Identity Management, Authentication and Access Control
Technology: Windows OS
Maturity Level: 1
IPAC: Platform (P)
Defender: Technology
Prerequisite: PT-P-IP-M01-010
---

## Description

Authorization, permission, and access for SAP standard users must properly be secured and configured within the Windows OS.

## Implementation

Like local users and domain users on a Windows machine, SAP standard users must have the appropriate permissions and authorizations within the OS.

- [ ] Restrict access to root, SAPsid, dbsid
- [ ] Lock dbsid user from all application serves after initial installation
- [ ] SAPsid should not have any rights for interactive logon

Note: SAP systems should not be installed on domain controllers

## Verification of control

- [ ] Verify SAP system is not install on the domain controller
- [ ] Verify that all restrictions for SAP users are in place


## References
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A16 Implementation of security requirements for the Windows (S) operating system / Umsetzung von Sicherheitsanforderungen für das Betriebssystem Windows (S)
- CIS CSC 3, 5, 12, 14, 15, 16, 18
- COBIT 5 DSS05.04
- ISA 62443-2-1:2009 4.3.3.7.3
- ISA 62443-3-3:2013 SR 2.1
- ISO/IEC 27001:2013 A.6.1.2, A.9.1.2, A.9.2.3, A.9.4.1, A.9.4.4, A.9.4.5
- NIST SP 800-53 Rev. 4 AC-1, AC-2, AC-3, AC-5, AC-6, AC-14, AC-16, AC-24
