---
Security Function: PT
Category: Protective Technology
Technology: SAProuter
Maturity Level: 1
IPAC: Integration (I)
Defender: Technology
Prerequisite: PT-I-PT-M01-001
---

## Description

When using SAPGUI or RFC connections to access published SAP systems that pertain to your organizations, from the internet, or different external networks, SAProuter must be properly configured to allow and deny traffic. The SAProuter must also work hand-in-hand with the firewall to adopt different access rules and allow a multi-access control architecture.

## Implementation

Implementing secure connections from external networks or the internet requires continuous tuning and adjustments to deny unauthorized access to SAP systems. The below implementation is a baseline to allow organizations to implement secure connections to their internal systems.

- [ ] Configure your firewall to allow only one port, 32NN, where NN is the organization's instance number for the SAProuter
- [ ] Configure SNC(1) to allow and authorize SAP support to login to your system securely. (This is mainly for support purposes)
- [ ] Configure an implicit deny on the last line of the ACL file (routtab file), (Deny all traffic with the following rule D * * *)
- [ ] Configure authorized connections using SAPGUI to use SAProuter for connection
- [ ] Configure authorized connections to use a secure password (Update routtab file for example P * * 3201 secure_password, allows requests to port 3201 if a password is used)
- [ ] Continuous monitoring of the dev_route log. This will enable security teams to tune their ACLs according to their needs


(1) - Reference control PT-I-PT-M01-003 to configure and enable SNC

## Verification of Control

- [ ] Verify ACL file (routtab) to allocate any unwanted or misconfigured rules
- [ ] Verify that an implicit deny is avaiable in the ACL file (i.e. D * * *)
- [ ] Verify that a secure password is configured for authorized traffic
- [ ] Verify that connections coming from SAPGUI are configured to us the SAProuter
- [ ] Verify that the firewall is configured to allow the one port number for SAProuter

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A3 Network Security/ Netzsicherheit
- CIS CSC 8, 12, 15
- COBIT 5 DSS05.02, APO13.01
- ISA 62443-3-3:2013 SR 3.1, SR 3.5, SR 3.8, SR 4.1, SR 4.3, SR 5.1, SR 5.2, SR 5.3, SR 7.1, SR 7.6
- ISO/IEC 27001:2013 A.13.1.1, A.13.2.1, A.14.1.3
- NIST SP 800-53 Rev. 4 AC-4, AC-17, AC-18, CP-8, SC-7, SC-19, SC-20, SC-21, SC-22, SC-23, SC-24, SC-25, SC-29, SC-32, SC-36, SC-37, SC- 38, SC-39, SC-40, SC-41, SC-43
