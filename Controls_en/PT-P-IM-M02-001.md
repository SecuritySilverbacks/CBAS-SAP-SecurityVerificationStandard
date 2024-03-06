---
Security Function: Protect (PT)
Category: Improvements (RR.IM)
Technology: SAP HANA
Maturity Level: 3
SAP Operational Area: Platform (P)

Prerequisite:
---

## Description

As a general security measure, HANA tenants that are no longer used should be deleted, as the mere presence of any unsecured tenants can pose a risk to the overall system. Possible keywords would be undetected attack attempts on this tenant or exploitation of local vulnerabilities after successful login.


## Implementation

As of today, there are no standard tenants that would fall under this category. Therefore, every tenant that is not necessary from a functional or technical point of view should be removed using standard means.

## Verification of control

Check whether there are tenants that are not necessary from a professional or technical point of view.


## References
* SAP Security Baseline Template V2.4: 3.1.1.13.2
