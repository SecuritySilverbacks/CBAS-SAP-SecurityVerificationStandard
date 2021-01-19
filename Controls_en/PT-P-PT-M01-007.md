---
Security Function: PT
Category: Protective Technology
Technology: SAP Java  
Maturity Level: 1
IPAC: Platform (P)
Defender: Technology
Prerequisite:
---

## Description

Security Audit Logs (SAL) are important to be activated and properly configured throughout the entire SAP environment. This help security teams identify and detect potential threats that might affect their environment.

## Implementation

It is important to activate and properly configure the UME properties pertaining to security audit logs. The following parameters help to do so:

- [ ] ume.secaudit.get_object_name = TRUE
- [ ] ume.secaudit.log_actor = TRUE
- [ ] ume.logon.security_policy.log_client_hostaddress = TRUE
- [ ] ume.logon.security_policy.log_client_hostname = FALSE (requires DNS lookup, which impacts system performance)
- [ ] enable.xml.hardener = TRUE

It is recommended to change the default severity of information being logged and set to a severity that your organization requires. The default severity is set to Info.

## Verification of Control

- [ ] Verify that security audit logs UME properties are configured
- [ ] Verify what is being logged by logging into the Netweaver Administrator and then navigate to -> Troubleshooting -> Logs and Traces -> Log Configuration, from Show filed choose 'Logging Categories'
- [ ] Verify the severity of information being logged

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A21 Configuration of the Security Audit Log (S) / Konfiguration des Security Audit Logs (S)
- SAP Security Baseline Template V2.1: 2.4.3.1.2
- CIS CSC 1, 3, 5, 6, 14, 15, 16
- COBIT 5 APO11.04, BAI03.05, DSS05.04, DSS05.07, MEA02.01
- ISA 62443-2-1:2009 4.3.3.3.9, 4.3.3.5.8, 4.3.4.4.7, 4.4.2.1, 4.4.2.2, 4.4.2.4
- ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR 2.11, SR 2.12
- ISO/IEC 27001:2013 A.12.4.1, A.12.4.2, A.12.4.3, A.12.4.4, A.12.7.1
- NIST SP 800-53 Rev. 4 AU Family
