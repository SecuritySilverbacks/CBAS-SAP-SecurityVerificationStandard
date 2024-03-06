---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP ABAP
Maturity Level: 1
SAP Operational Area: Platform (P)

Prerequisite:
---

## Description

Enabling enqueue server replication (ERS) in an SAP system plays a key role in preventing data inconsistencies in the event of application server failures. The enqueue server (ES) is responsible for managing transaction consistency and lock management in an SAP system. The replication of the enqueue server ensures that the lock information is synchronized between the various instances of the enqueue server.

In the event of an application server failure, the activated enqueue server replication enables continuous availability of the locking functionality. Data inconsistencies are avoided as the information about set locks is transferred to the replicated enqueue servers. This means that open transactions can be rolled back completely.

## Implementation

**The description refers to the use of the Enqueue 2 server, which is installed by default with SAP_NETWEAVER_AS_ABAP_752**

1. Determining the replication system: Determine the replication system. The replication system should be operated in a different availability zone than the primary RS. (see also reference 1)
2. Installing the ERS: Make sure that the enqueue replication server is installed on the secondary system. This is normally done as part of the ASCS/ERS installation. Customize the start profile of the enqueue server by configuring the instance number of the ERS accordingly.
3. Configure the enqueue server for operation in replication mode by (see also [2]): 
in the default profile:
- enq/enable=TRUE
- enq/serverhost=\<Host of the ASCS instance\>
- enq/serverinst=\<Number of ASCS instance\>
- enq/replicatorhost=\<Host of ERS instance\>
- enq/replicatorinst=\<Number of ERS instance\>
- enque/process_location=REMOTESA
- enq/client/max_async_requests = 0
in the ASCS instance profile:
- enq/server/replication/enable = TRUE
- _ENQ = enq.sap$(SAPSYSTEMNAME)_$(INSTANCE_NAME)
- Execute_01 = local rm -f \$(_ENQ)
- Execute_02 = local ln -s -f \$(DIR_EXECUTABLE)/enq_server$(FT_EXE) $(_ENQ)
- Start_Program_01 = local \$(_ENQ) pf=$(_PF)

4. Configure the replication link between the enqueue server of the primary system and the ERS of the secondary system. Ensure that communication takes place via secure connections (e.g. SNC) to guarantee data integrity.
4. Configure cluster software: Use cluster software to monitor the ERS and automatically switch over if the primary enqueue server fails. Use standalone gateway: Ensure that the standalone gateway is configured to forward client requests in the event of a failover.
5. Monitor the ERS with transaction SMENQREP to monitor replication in real time.
6. Simulate a failure of the primary enqueue server and check whether the ERS takes over as expected.


## Verification of control

- Check the ERS with transaction SMENQREP. Determine whether replication is in "Active" status and whether the replication system is located in a different availability zone than the primary ERS.


## References
1. [SAP workload configurations with Azure Availability Zones - Active/Active](https://learn.microsoft.com/en-us/azure/sap/workloads/high-availability-zones#activeactive-deployment)
2. [SAP Help - Installation of the Standalone Enqueue Server 2 and Enqueue Replicator 2](https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_752/e458064e3077486994caaf9a85c4aa23/7aa4fc5e9e6047edb0505c59d968ca54.html?locale=de-de)
3. [SAP Help - High Availability with Standalone Enqueue Server 2](https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_752/e458064e3077486994caaf9a85c4aa23/6d655c383abf4c129b0e5c8683e7ecd8.html?locale=de-de)
4. [SAP Help - Checking the Status of the Replication](https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_752/e458064e3077486994caaf9a85c4aa23/c74dc9bdc2ba487f91e7acf80b2f729b.html?locale=de-de)
5. [SAP Note 2832507 - SMENQ shows replication status as "Active (update pending)"](https://me.sap.com/notes/2832507/E)
6. [SAP S/4 HANA - Enqueue Replication 2 High Availability Cluster With Simple Mount](https://documentation.suse.com/sbp/sap/html/SAP-S4HA10-setupguide-simplemount-sle15/index.html#id-implementing-the-cluster)
