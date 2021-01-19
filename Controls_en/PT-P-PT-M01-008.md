---
Security Function: PT
Category: Protective Technology
Technology: SAP HANA
Maturity Level: 1
IPAC: Platform (P)
Defender: Technology
Prerequisite:
---

## Description

Security Audit Logs (SAL) are important to be activated and properly configured throughout the entire SAP environment. This help security teams identify and detect potential threats that might affect their environment.

## Implementation

It is important to activate and properly configure the audit trail for HANA in the SAP HANA Administration Console. The following parameters help to do so:

- [ ] global_auditing_state = true in global.ini file, section auditing configuration
- [ ] Audit policies should be configured as per the companies security requirements
- [ ] Set the default_audit_trail_type = SYSLOGPROTOCOL or CSTABLE in global.ini file, section auditing configuration. More information on Audit Trail Layout can be found [here](https://help.sap.com/viewer/b3ee5778bc2e4a089d3299b82ec762a7/2.0.03/en-US/0a57444d217649bf94a19c0b68b470cc.html)

Note: Critical users must be monitored

## Verification of Control

- [ ] Verify that security audit logs are enabled by checking the parameter global_auditing_state = true in global.ini file, section auditing configuration
- [ ] Verify if all events are for critical users are collected and audited
- [ ] Verify that the CSVFILE is not used to log security-critical information

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A21 Configuration of the Security Audit Log (S) / Konfiguration des Security Audit Logs (S)
- SAP Security Baseline Template V2.1: 2.4.3.1.3
- CIS CSC 1, 3, 5, 6, 14, 15, 16
- COBIT 5 APO11.04, BAI03.05, DSS05.04, DSS05.07, MEA02.01
- ISA 62443-2-1:2009 4.3.3.3.9, 4.3.3.5.8, 4.3.4.4.7, 4.4.2.1, 4.4.2.2, 4.4.2.4
- ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR 2.11, SR 2.12
- ISO/IEC 27001:2013 A.12.4.1, A.12.4.2, A.12.4.3, A.12.4.4, A.12.7.1
- NIST SP 800-53 Rev. 4 AU Family
