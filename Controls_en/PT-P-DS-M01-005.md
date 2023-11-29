---
Security Function: PT
Category: Data Security 
Technology: SAP ABAP
Maturity Level: 1
IPAC: Platform (P)
Defender: Technology
Prerequisite:
---

## Description

A directory/path traversal attacks can allow unauthorized access to files or directories by manipulating applications that are using physical or logical file names as input. This will allow attackers to read or write to sensitive/critical files that can lead to information disclosure and other attacks that may further exploit the system.

## Implementation

The following steps help mitigate vulnerabilities where an attacker can manipulate file names to read or write from different application servers.

- Update your kernel to the latest security patch level
- Verify any logical file names and file path definitions from the reports RSFILECR or RSFILENA to determine the required changes
- Profile parameter abap/path_normalizartion should be activated (value 1)
- Paths must be normalized (see SAP note 1497003 for normalizing file paths) if authorization object S_DATASET is used
- Paths must be normalized if table SPTH contains any entries
- If the user interface allows input of logical file names then define aliases for the logical file names being used

Note: Make sure to first implement the changes on the testing environment before applying to production systems. This will avoid any errors or service disruptions to the production systems.

## Verification of Control

- Identify logical file names from the RSFILENA report
- Identify logical file names and file path definitions from the RSFILECR
- Verify that profile parameter abap/path_normalization is not deactivated

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A1 Secure configuration of the SAP ABAP stack (B) / Sichere Konfiguration des SAP-ABAP-Stacks (B)
- SAP Security Baseline Template V2.1: 2.2.1.3.1
- SAP note 1497003
