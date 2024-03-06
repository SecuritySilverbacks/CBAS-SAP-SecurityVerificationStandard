---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP ABAP  
Maturity Level: 1
IPAC: Platform (P)
Defender: Technology
Prerequisite:
---

## Description

Security Audit Logs (SAL) are important to be activated and properly configured throughout the entire SAP environment. This help security teams identify and detect potential threats that might affect their environment.

## Implementation

It is important to activate and properly configure profile parameters pertaining to security audit logs. The following parameters help to do so:

- Use transaction RSAU_CONFIG or SM19 to set the required parameters
- rsau/enable = 1
- Specify the location of the security audit log by setting the rsau/local/file
- rsau/integrity = 1
- rsau/log_peer_address = 1 (note: the parameter can cause warnings, but these can be ignored without any problems)
- rsau/selection_slots ≥ 10 5
- rsau/user_selection = 1
- Specify the maximum length of the log by setting the rsau/max_diskspace_local

The following minimal settings of the security audit log must be implemented:

- Auditing should be active
- Active filter with generic user selection for all critical events
- Log protection format active

It is recommended to send the logs to a centralized log server to better analyze and filter logs. This will also help in maintaining the size on the actual system.

With transaction RSAU_CONFIG, further parameters can be configured depending on your organizations requirements.

Note: Reference DT-P-AE-M01-002 controls for identifying available logs that can be collected for your requirements

## Verification of Control

- Verify that security audit logs are enabled by checking the rsau/enable parameter
- Verify that security audit logs minimal settings are configured
- Verify if all events are for critical users, such as SAP*, DDIC, SAPCPIC, emergency and support users, are collected and audited for all clients
- Verify if all critical events for all clients are collected and audited

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A21 Configuration of the Security Audit Log (S) / Konfiguration des Security Audit Logs (S)
- SAP Security Baseline Template V2.1: 2.4.3.1.1
- CIS CSC 1, 3, 5, 6, 14, 15, 16
- COBIT 5 APO11.04, BAI03.05, DSS05.04, DSS05.07, MEA02.01
- ISA 62443-2-1:2009 4.3.3.3.9, 4.3.3.5.8, 4.3.4.4.7, 4.4.2.1, 4.4.2.2, 4.4.2.4
- ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR 2.11, SR 2.12
- ISO/IEC 27001:2013 A.12.4.1, A.12.4.2, A.12.4.3, A.12.4.4, A.12.7.1
- NIST SP 800-53 Rev. 4 AU Family
