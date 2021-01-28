---
Security Function: PT
Category: Identity Management, Authentication and Access Control
Technology: SAP ABAP
Maturity Level: 1
IPAC: Access (A)
Defender: Technology
Prerequisite:
---

## Description

Single Sign-On (SSO) is recommended to be configured when multiple SAP systems are running in the organization's environment. SSO can simplify the process of managing and configuring user authorization to multiple systems and applications. Allowing a single user to access multiple applications comes with its own security risks and threats; a secure configuration of the issued logon tickets must be in place to avoid potential threats.  

## Implementation

In order to protect issued logon tickets during transport, in ABAP based systems, the below profile parameters are required to be in place.  

- [ ] Use HTTPS by setting login/ticket_only_by_https = 1
- [ ] To make sure that the login ticket is sent back to the creating host set login/ticket_only_to_host = 1
- [ ] Declare a cookie as HTTPonly by setting icf/set_HTTPonly_flag_on_cookies = 1 or 3, this denies access to the issued cookie from the clients web browser by other applications such as applets, plug-ins and so on.


Note: This control assumes that SSO is already configured and used in the organization.

## Verification of Control

- [ ] Verify if HTTPS profile parameter is set by checking login/ticket_only_by_https
- [ ] Verify that only the creating host receives the logon ticket by checking login/ticket_only_to_host
- [ ] Verify if the profile parameter icf/set_HTTPonly_flag_on_cookies = 1 or 3


## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A31 Configuration of SAP Single Sign-On (S) / Konfiguration von SAP Single-Sign-On (S)
- SAP Security Baseline Template V2.1: 2.3.2.4.1
