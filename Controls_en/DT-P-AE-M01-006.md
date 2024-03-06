---
Security Function: Detect (DT)
Category: Anomalies and Events (DT.AE)
Technology: SAP ERP
Maturity Level: 1
IPAC: Platform (P)
Defender: Process
Prerequisite: DT-P-AE-M01-001
---

## Description

Read access logging:

An important tool used to monitor and record any read access to classified or sensitive data found in SAP systems. The tool helps when investigating a security breach or information leak.  


## Implementation

The below configuration steps are required to be in place to monitor and configure read access logging (RAL).

1. Identify what type of data to log through the read access logging
2. Declare a purpose for logging the data to help identify data of regulatory relevance
3. Define the interfaces to monitor by RAL channels
4. Define the log domains of the different channels
5. Define a condition for the application to log the data


## Verification of Control

- Configure and monitor the read access logging through the SRALMANAGER transaction

## References:
