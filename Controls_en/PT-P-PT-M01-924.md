---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP BTP
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

If only one Cloud Connector instance is available and fails for any reason, cloud applications and services can no longer send requests from SAP BTP to on-premise backend systems. To ensure high availability of connectivity for cloud integration scenarios, operate productive instances of the Cloud Connector in high availability mode, i.e. with a second (redundant) Cloud Connector.

## Implementation

1. Install and operate at least one additional Cloud Connector installation on a separate host system. Set up one of the Cloud Connector instances as a so-called "shadow" and configure this instance according to the instructions at https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/shadow-instance-configuration in order to be able to query the configuration and status of the master instance.

2. The master should be configured according to the instructions https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/master-instance-configuration and thus set to high availability mode and allow the shadow to take over Cloud Connector operation.

3. When updating the Cloud Connector, test the high availability configuration by manually switching to the shadow instance.

## Verification of control
> TODO


## References
* SAP Security Baseline Template V2.4: 3.1.1.10.2