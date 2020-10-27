---
Security Function: PT
Category: Information Protection Processes and Procedures
Technology: SAP ABAP
Maturity Level: 1
IPAC: Platform (P)
Defender: Process (P) / Technology (T)
Prerequisite:
---

## Description

To reduce any potential threats found in vulnerable SAP systems and maintain the organization's required security level, security professionals must regularly update security and software updates.


## Implementation

SAP Security Notes are usually released every second Tuesday of every month. These notes help in mitigating discovered vulnerabilities throughout SAP systems.

Places to get the latest SAP security notes and support packages:
- SAP Software Update Manager (license is required)
- SAP Patch Management tool (start with SPAM transaction; it will require a maintenance certificate)
- Identify SAP security notes for the system by using SNOTE transaction
- SAP Security Notes found in the SAP Support Launchpad

It is necessary to follow a patch management process [1] in order to maintain the availability and integrity of production systems.

[1] - It is recommended create a patch management process, if there is no process already existing in your organization; the process should also be applied to non-SAP solutions.

## Verification of Control

- [ ] Schedule a regular patching process to SAP systems
- [ ] Create/Follow a patch management process to maintain integrity and availability of SAP systems

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A1 Secure configuration of the SAP ABAP stack (B) / Sichere Konfiguration des SAP-ABAP-Stacks (B)
- SAP Security Baseline Template V2.0: 2.2.2.1
