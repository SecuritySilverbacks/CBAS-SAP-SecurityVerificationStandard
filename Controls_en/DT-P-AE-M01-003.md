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

System logs:

Identifying and collecting system problems through system logs is important to enabling the system to run with good performance. Maintaining the healthiness of your system and keeping it running avoids any service disruptions that may be caused by errors.


## Implementation

Whether your organization is running a UNIX or Windows host, systems logs should be checked on a regular basis. It is recommended to send the logs to a central location to avoid any logs that might overwritten once the buffer is full; especially in Windows hosts.

Alerts can be configured when a certain event occurs or a threshold is reached, this helps automate the review process of system logs and reduces workload from administrators. Sending logs to a central location helps to achieve setting up alerts.


## Verification of Control

- [ ] Check system logs through the SM21 transaction
- [ ] Configure alerts for certain events such as rollbacks and system error messages to reactively respond and fix issues

## References:
