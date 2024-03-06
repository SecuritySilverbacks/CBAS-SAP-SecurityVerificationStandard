---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP BTP
Maturity Level: 3
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

Updates to services associated with an application are synchronized and do not allow any other tasks or processes until they are completed. If there are more than 50 subscribers, timeouts may occur due to the increased load on the service instance.


## Implementation

To avoid a timeout, activate asynchronous processing in your application security descriptor (xs-security.json). To activate asynchronous processing, set the "xsenableasyncservice" attribute to "true".


## Verification of control

Check that the "xsenableasyncservice" attribute in the application security descriptor (xs-security.json) is set to "true".


## References

* SAP BTP Security Recommendations: BTP-UAA-0006
