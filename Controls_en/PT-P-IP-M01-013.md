---
Security Function: PT
Category: Information Protection Processes and Procedures
Technology: Windows OS
Maturity Level: 1
IPAC: Platform (P)
Defender: Technology
Prerequisite:
---

## Description

Strengthening and hardening the OS running the organization's SAP system is critical to securing your SAP implementation and network. The windows operating system is quite famous for its abundance of vulnerabilities found daily.  

## Implementation

If your organization runs a Windows environment, there should already be a defined baseline when deploying Windows machines. With that in mind, the below are a few areas to keep in mind while hardening SAP systems running on Windows OS.

 - Disable or secure remote desktop
 - Remove unneeded services and accounts
 - Remove any unneeded Windows applications, features, roles, and components
 - Local administrator accounts to be disabled or secured  
 - Updates to be applied regularly

It is recommended to follow the organization's baseline, if it exists, for securing Windows machines.

## Verification of control

- Verify that unwanted applications, services, features, roles, and components are removed
- Verify that local administrators accounts are disable or properly secure
- Verify that security updates are done regularly  

## References
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A16 Implementation of security requirements for the Windows (S) operating system / Umsetzung von Sicherheitsanforderungen für das Betriebssystem Windows (S)
