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

Table logging:

Identifying and collecting logs to identify changes in critical tables is necessary to maintain the integrity of data available in different tables.


## Implementation

Activate the table logging in the profile parameter rec/client. It is recommended to set this parameter to log from all clients within your SAP environment.

As a rule of thumb, choose tables that are either classified with the highest protection level or choose tables depending on the criticality of data found in them.

Alerts can be configured when a certain event occurs or a threshold is reached, this helps automate the review process of table logging and reduces workload from administrators. Sending logs to a central location helps to achieve setting up alerts.

## Verification of Control

- Set the rec/client parameter to enable logging
- Set the rec/client parameter to collect from all clients
- Define tables to be logged using transaction SE13
- Use transaction SCU3 to get an overview of all tables that have table logging enabled and the changes to these tables
- Configure alerts for important events to reactively respond to any changes in tables

## References:
