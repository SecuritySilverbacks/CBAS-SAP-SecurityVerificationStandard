---
Security Function: Detect (DT)
Category: Anomalies and Events (DT.AE)
Technology: SAP HANA
Maturity Level: 1
SAP Operational Area: Access (A)

Prerequisite:
---

## Description

System privileges restrict administrative tasks for administrative users. In critical systems, the "DATA ADMIN" system privilege should not be assigned to any user. Users with this authorization can have read access to system tables and execute Data Definition Language (DDL) statements in the SAP HANA database.

## Implementation

Check that neither a user nor a role has been assigned the "DATA ADMIN" system privilege.

## Verification of control

Check that neither a user nor a role has been assigned the "DATA ADMIN" system privilege.

## References

* SAP Security Baseline Template V2.4: 2.3.2.2.3
* SAP HANA Security Guide for SAP HANA Platform 2.0 SPS 07: 7.3.1