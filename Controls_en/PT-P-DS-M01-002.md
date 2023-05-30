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

To reduce the amount of information disclosed during reconnaissance by adversaries, it is recommended to remove any system version information or detailed error logs that can be gathered to exploit possible vulnerabilities that might arise from this information.

## Implementation

To remove any detailed errors from your organization's SAP ABAP system set the login/show_detailed_errors profile parameter to 0.

Use the below parameters to view and change parameters:

- RZ11 transaction: to view information about parameters
- RZ10 transaction: to view and change profile parameters
- RSPARAM report to view parameters (use transaction SA38)


## Verification of Control

- [ ] profile parameter login/show_detailed_errors=0

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A1 Secure configuration of the SAP ABAP stack (B) / Sichere Konfiguration des SAP-ABAP-Stacks (B)
- SAP Security Baseline Template V2.1: 2.2.1.2.1
