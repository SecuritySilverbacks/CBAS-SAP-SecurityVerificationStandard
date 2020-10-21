---
Security Function: PT
Category: Information Protection Processes and Procedures
Technology: RFC Connections
Maturity Level: 1
IPAC: Integration
Defender: Process
Prerequisite: NA
---

## Description

In order to properly secure the Remote Function Call (RFC) interface that is used as a communication interface between SAP systems, all RFC connections, RFC authorizations and RFC interfaces must be considered.

## Implementation

For all RFC connections a uniform administrative guideline must be available; ownership and usage of the RFC connection should be clearly documented. A complete inventory must also be defined and documented for all RFC connections.

Any RFC connections that are not in use must be deleted. (Documentation should reflect the same)


## Verification of Control

- [ ] Determine if an RFC connection is in use through using the RFC runtime monitor transaction SRTM6 or the workload monitor transaction ST03N
- [ ] Delete any RFC connections not in use
- [ ] Guidelines in regards to existing RFC connections are available and up to date

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A8 Securing the SAP RFC interface/ Absicherung der SAP-RFC-Schnittstelle
- SAP Security Baseline Template V2.0: 2.3.2.3
