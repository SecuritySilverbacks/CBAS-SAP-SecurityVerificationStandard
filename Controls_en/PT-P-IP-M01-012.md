---
Security Function: PT
Category: Information Protection Processes and Procedures
Technology: Linux
Maturity Level: 1
IPAC: Platform (P)
Defender: Technology
Prerequisite:
---

## Description

Strengthening and hardening the OS running the organization's SAP system is critical to securing your SAP implementation and network.

## Implementation

If your organization deploys other application on Linux, there should already be a defined baseline when deploying Linux machines. With that in mind, the below are a few areas to keep in mind while hardening SAP systems running on Linux.

 - Prohibit root logons remotely 
 - Remove unneeded services and accounts
 - Remove any unneeded Linux applications, features, roles, and components
 - Disable the use of X window systems (SAP applications do not require it)
 - Do not use telnet or FTP for file transfer  
 - Updates to be applied regularly
 - Avoid using SUID/SGID with potentially vulnerable programs
 - Files are created with the appropriate permission through configuring the default file mask
 - Regularly check signatures and keys on downloaded applications or patches

It is recommended to follow the organization's baseline, if it exists, for securing Linux machines.

If your organization is using SUSE Linux for hosting SAP applications, below are additional points to consider:

- Install and configure the SUSE security checker (seccheck) to enable notifications of any security changes

## Verification of control

- Verify that unwanted applications, services, features, roles, and components are removed
- Verify if file permissions are properly configured
- Verify that telnet and FTP are not in use
- Verify that security updates are done regularly  

## References
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A16 Implementation of security requirements for the Windows (S) operating system / Umsetzung von Sicherheitsanforderungen für das Betriebssystem Windows (S)
