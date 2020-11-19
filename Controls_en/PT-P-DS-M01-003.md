---
Security Function: PT
Category: Data Security
Technology: SAP Java
Maturity Level: 1
IPAC: Platform (P)
Defender: Technology
Prerequisite: PT-P-IP-M01-002
---

## Description

To reduce the amount of information disclosed during reconnaissance, it is recommended to remove any system version information or detailed error logs that can be gathered to exploit possible vulnerabilities that might arise from this information.

## Implementation

To remove any version from your organization's SAP Java system set the UseServerHeader setting to false in both the HTTP provider service (global configuration of dispatcher) and server nodes.


## Verification of Control

- [ ] Set UserServerHeader to false in the HTTP provider service in the global configuration of dispatcher
- [ ] Set UserServerHeader to false in the server nodes

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A1 Secure configuration of the SAP ABAP stack (B) / Sichere Konfiguration des SAP-ABAP-Stacks (B)
- SAP Security Baseline Template V2.1: 2.2.1.2.2
