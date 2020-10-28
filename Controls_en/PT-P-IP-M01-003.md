---
Security Function: PT
Category: Information Protection Processes and Procedures
Technology: SAP Kernel
Maturity Level: 1
IPAC: Platform (P)
Defender: Technology 
Prerequisite:
---

## Description

To reduce any potential threats found in the SAP kernel and maintain the organization's required security level, security professionals must regularly update the kernel.

Note: The SAP kernel has a separate update mechanism then other SAP systems


## Implementation

In order to check your organization's current kernel release:
1. Navigate to system > status
2. Press shift + F5 to get the kernel info

Places to get the latest SAP kernel updates:
- SAP Software Update Manager (license is required)
- SAP Security Notes found in the SAP Support Launchpad

It is necessary to follow a patch management process [1] in order to maintain the availability and integrity of production systems.

[1] - It is recommended create a patch management process, if there is no process already existing in your organization; the process should also be applied to non-SAP solutions.

## Verification of Control

- [ ] Schedule a regular patching process to the SAP kernel
- [ ] Create/Follow a patch management process to maintain integrity and availability of SAP systems


## References:
