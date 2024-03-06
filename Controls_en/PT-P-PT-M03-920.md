---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP BTP
Maturity Level: 1
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

The Cloud Connector is a tool that customers can use to connect their systems with SAP solutions in the cloud. However, it cannot be updated automatically by SAP and requires regular updates to its local Java SDK in order to operate.


## Implementation

1. SAP publishes new versions of the Cloud Connector in the SAP BTP release notes. Check the release notes regularly for updates to the Cloud Connector. New versions of the Cloud Connector can be applied using the Cloud Connector upgrade functions.

2. Sometimes you need to update the Java VM used by the Cloud Connector, e.g. due to expired SSL certificates contained in the JVM, bug fixes, outdated JVM versions and so on. Include this point in your continuous update processes.


## Verification of control

> TODO


## References

* SAP BTP Security Recommendations: BTP-CLC-0001, BTP-CLC-0011
* SAP Security Baseline Template V2.4: 2.2.2.1.5
* SapMachine: https://sap.github.io/SapMachine/
