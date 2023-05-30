---
Security Function: PT
Category: Identity Management, Authentication and Access Control
Technology: SAP Java
Maturity Level: 1
IPAC: Access (A)
Defender: Technology
Prerequisite:
---

## Description

Single Sign-On (SSO) is recommended to be configured when multiple SAP systems are running in the organization's environment. SSO can simplify the process of managing and configuring user authorization to multiple systems and applications. Allowing a single user to access multiple applications comes with its own security risks and threats; a secure configuration of the issued logon tickets must be in place to avoid potential threats.  

## Implementation

In order to protect issued logon tickets during transport, in Java based systems, the below profile parameters are required to be in place.  

- Use HTTPS by setting ume.logon.security.enforce_secure_cookie = true
- Set an expiry for the issued ticket by setting login.ticket_lifetime ≤ 8 (hh:mm)
- Declare a cookie as HTTPonly by setting ume.logon.httponlycookie = true, this denies access to the issued cookie from the clients web browser by other applications such as Javascript access, plug-ins and so on.


Note: This control assumes that SSO is already configured and used in the organization.

## Verification of Control

- Verify if HTTPS profile parameter is set by checking ume.logon.security.enforce_secure_cookie = true
- Verify if an expiry exists for issued logon tickets by verifying login.ticket_lifetime ≤ 8
- Verify if the profile parameter ume.logon.httponlycookie = true

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A31 Configuration of SAP Single Sign-On (S) / Konfiguration von SAP Single-Sign-On (S)
- SAP Security Baseline Template V2.1: 2.3.2.4.2
