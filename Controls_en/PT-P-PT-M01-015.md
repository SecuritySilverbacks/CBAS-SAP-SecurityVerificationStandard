---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP Java
Maturity Level: 1
SAP Operational Area: Platform (P)

Prerequisite:
---

## Description

Enabling enqueue server replication in an SAP system plays a key role in preventing data inconsistencies in the event of application server failures. The enqueue server is responsible for managing transaction consistency and lock management in an SAP system. Replication of the enqueue server ensures that the lock information is synchronized between the various instances of the enqueue server.

In the event of an application server failure, the activated enqueue server replication enables continuous availability of the locking functionality. Data inconsistencies are avoided as the information about set locks is transferred to the replicated enqueue servers. This means that open transactions can be rolled back completely.

In the case of SAP Java, replication requires the installation of a standalone enqueue server.

## Implementation

1. Determine the SCS instance of the SAP Java system. The enqueue server is installed there by default.

2. Use the Software Provisioning Manager (SWPM) to install the Enqueue Replication Server (ERS) on a host in a separate availability zone (path Installing SAP NetWeaver 7.5 → SAP HANA Database → Installation → Application Server ABAP → High-Availability System → Enqueue Replication Server Instance) and configure it.
3. Configure the ES to communicate with the ERS using the following parameters:
- enque/server/replication = true
4. Set up replication between the ES and the ERS. To do this, restart the ES while the ERS is running.
5. Make sure that replication works correctly and that the ERS can replace the primary enqueue server in the event of an error. Use ensmon for this:
> ensmon [--help|-help|-h] [pf=<profile>] [-H <hostname> [-I <serverinstance>|-S <serverservicename/serverport>]] 2 ;  echo $?
If replication is active, this should be output as status 0. 
6. Simulate the failure of the SCS instance to ensure that the high availability mechanisms function properly.

## Verification of control

1. Check whether the ES has switched on replication using the parameter enque/server/replication = true
2. Make sure that replication works correctly and that the ERS can replace the primary enqueue server in the event of an error. Use ensmon for this:
> ensmon [--help|-help|-h] [pf=<profile>] [-H <hostname> [-I <serverinstance>|-S <serverservicename/serverport>]] 2 ;  echo $?

## References
1. [2623468 - [WEBINAR] Understanding and Troubleshooting Standalone Enqueue Server](https://me.sap.com/notes/2623468)
2. [Installing the Standalone Enqueue Server](https://help.sap.com/docs/SAP_NETWEAVER_731_BW_ABAP/3442894b64c6492890fa3d07bc767e20/47e0203086983c85e10000000a42189c.html?locale=en-US)
3. [Configuring the Replication Server](https://help.sap.com/doc/7b178076728810148a4b1a83b0e91070/1511%20000/en-US/frameset.htm?47e0208d86983c85e10000000a42189c.html)
4. [Replication Server: Check Installation](https://help.sap.com/doc/7b178076728810148a4b1a83b0e91070/1511%20000/en-US/frameset.htm?47e020bb86983c85e10000000a42189c.html)
5. [SAP NetWeaver Enqueue Replication 1 High Availability Cluster](https://documentation.suse.com/sbp/all/html/SAP-nw740-sle15-setupguide/index.html#id-sap-installation)
6. [Monitoring the Standalone Enqueue Server](https://help.sap.com/docs/SAP_NETWEAVER_750/3442894b64c6492890fa3d07bc767e20/47ea3c8a00e83b8be10000000a421937.html?locale=en-US)
