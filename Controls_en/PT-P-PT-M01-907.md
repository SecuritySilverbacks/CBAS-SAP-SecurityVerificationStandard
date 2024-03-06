---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP BTP
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

The system does not automatically update its client libraries provided by SAP, but it does provide regular updates to fix problems or improve the code. It is recommended that users who use optional client libraries check for updates regularly and ensure that they have the latest version of these libraries. New client libraries are available on Github as open source software.


## Implementation

1. Check the client libraries offered by SAP and used in your own source code regularly for updates.

2. Check the Github project regularly for new versions and update it as soon as new versions are available.

3. You should not use the beta functions of SAP BTP in sub-accounts that belong to productive company accounts.
Experimental functions are not part of the officially delivered scope that SAP guarantees for future releases. This means that experimental functions can be changed by SAP at any time and without giving reasons. Experimental functions are not intended for productive use. You may not demonstrate, test, examine, evaluate or otherwise use the experimental functions in a productive sub-account or with insufficiently secured data.

4. If the version of the Cloud Connector is outdated, the latest important bug fixes and security patches have not been applied, which can lead to operational and security problems. New versions of the Cloud Connector are announced in the SAP BTP release notes. SAP recommends that Cloud Connector administrators regularly check the release notes for updates to the Cloud Connector. The upgrade to the latest version should be carried out promptly.


## Verification of control
> TODO


## References
* SAP BTP Security Recommendations: BTP-UAA-0021, BTP-ALS-0001
* SAP Security Baseline Template V2.4: 2.2.2.2.1, 3.1.1.7.1, 3.1.1.18.1
* SAP BTP Security Services Integration Libraries: https://github.com/SAP/cloud-security-xsuaa-integration
