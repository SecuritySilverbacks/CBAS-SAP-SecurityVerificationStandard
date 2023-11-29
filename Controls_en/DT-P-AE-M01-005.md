---
Security Function: DT
Category: Anomalies and Events
Technology: SAP ERP
Maturity Level: 1
IPAC: Platform (P)
Defender: Process
Prerequisite: DT-P-AE-M01-001
---

## Description

Workload monitor:

The workload monitor helps with analyzing system statistics in SAP systems. An important part of the workload monitor is its capability to collect activities performed by users against the system. This avoids repudiation and helps in analyzing changes or security events that caused an incident to take place.

## Implementation

Workload monitor is deactivated by default, and needs to be activated when investigating events or incidents caused by users.

Tracking user activity may not be permitted in different parts of the world. Make sure to follow any data protection regulations your organizations falls under when tracking use activity.

## Verification of Control

- Start the workload monitor using the STO3N transaction

## References:
