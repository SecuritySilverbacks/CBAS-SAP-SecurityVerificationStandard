---
Security Function: Detect (DT)
Category: Detection Processes (DT.DP)
Technology: SAP BTP
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

The Cloud Foundry environment stores all audit logs written by other platform services on behalf of a sub-account. These can be retrieved via an API or viewed using the SAP Audit Log Viewer with a retention period of 90 days, which cannot currently be extended any further.


## Implementation

1. The Audit Log API allows you to retrieve the audit logs. Download audit logs regularly for each sub-account and ideally save them in an existing and centralized audit log system of your choice.

2. The audit log level of the Cloud Connector(s) should be set to 'Security'.


## Verification of control

1. Check that the download was carried out regularly, that the audit logs were stored internally, e.g. in a central audit log system, and randomly check their integrity.

2. Check that the audit log level of the Cloud Connector(s) is set to the value 'Security'.


## References
* SAP BTP Security Recommendations: BTP-AUD-0001
* SAP Security Baseline Template V2.4: 2.4.3.1.4
