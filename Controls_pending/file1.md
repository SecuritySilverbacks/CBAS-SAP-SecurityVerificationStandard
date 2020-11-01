---
Control: Access Control
Maturity Level: 1
NIST: IY/PT
IPAC: A
Defender: Process
---

## Objective
<applicability towards reducing the threat>


## Description
> Authorization to SAP application should be regularly monitored, verified, revoked, managed, issued and audited

## Implementation
> Operations: Consulted. Operations department defines the required access to individuals for the different SAP applications based on their job roles and based on need to know principle.

> Security: Responsible. Accountable. Security department is responsible to make sure that authorization is controlled and implemented as per permissions provided by operations department.

Baseline:

<SAP Security Baseline 2.3.3>

> Audit: Informed. Audit department to be informed about the necessary changes for their own records.

## Detect/Follow-up
> Operations:

> Security: Accountable. Security department should be able to control and identify the implementation of access controls by the below points:
> - Monitor: Logs are configured to be sent to a central log server or SIEM solution.
> - Revoke: User access to be removed or disabled from a directory service or SAP application.

> Audit: Responsibility. Audit department needs to make sure that access control is properly
> - Monitored: Identify if access control logs are being configured on a central log system aor SIEM.
> - Revoked: Identify users that have left the organization and determine whether their access has been disabled or revoked from the directory services and SAP applications.
> - Issue: Compare user rights based on roles and need to know permissions defined by the operation department.

## References
- NIST CSWP PR.AC-1
- CIS CSC 1, 5, 15, 16
- COBIT 5 DSS05.04, DSS06.03
- ISA 62443-2-1:2009 4.3.3.5.1
- ISA 62443-3-3:2013 SR 1.1, SR 1.2, SR 1.3, SR 1.4, SR 1.5, SR 1.7, SR 1.8, SR 1.9
- ISO/IEC 27001:2013 A.9.2.1, A.9.2.2, A.9.2.3, A.9.2.4, A.9.2.6, A.9.3.1, A.9.4.2, A.9.4.3
- NIST SP 800-53 Rev. 4 AC-1, AC-2, IA-1, IA-2, IA-3, IA-4, IA-5, IA-6, IA-7, IA-8, IA-9, IA-10, IA-11
