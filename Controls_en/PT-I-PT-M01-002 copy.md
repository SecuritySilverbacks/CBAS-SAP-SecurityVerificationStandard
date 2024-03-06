---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP HANA
Maturity Level: 2
SAP Operational Area: Integration (I)

Prerequisite: 
---

## Description

The network communication channels used by SAP HANA can be divided into
* connections for end user and admin clients and application servers via HTTPS and SQL
* internal database communication within the HANA database, between the hosts of a multi-host system or systems in system replication scenarios.

The external communication channels are:
* Connections from HTTP/S clients
* Connections of database clients that access the SQL/MDX interface of the SAP HANA database
* Connections for administrative purposes
* Connections for data provision
* General outgoing connections

The external communication channels are:
* Communication within the database
* Communication between multiple hosts in distributed scenarios
* Communication between multiple locations in system replication scenarios (high availability)
* Communication between the SAP HANA database and server components, such as extended storage (SAP HANA Dynamic Tiering)

Especially in the cloud environment, such as Azure, it is advisable to only use encrypted communication channels.


## Implementation

1. Allow only the required ports on the host firewalls and/or surrounding firewalls.

| Ports       | Beschreibung                                 |
| ----------- | -------------------------------------------- |
| 389         | LDAP (with STARTTLS)                         |
| 636         | LDAP over TLS/SSL                            |
| 1128        | HTTP                                         |
| 1129        | HTTPS                                        |
| 3xx00-3xx99 | Inter Tenant communication                   |
| 3xx08       | HTTP via XS classic server (tenant database) |
| 3xx09       | hdbrss/SAP Router                            |
| 3xx13       | SQL SystemDB                                 |
| 3xx14       | HTTP via XS classic server                   |
| 3xx15       | SQL Tenant                                   |
| 3xx17       | SQL SystemDB                                 |
| 3xx26       | Streaming Agent                              |
| 3xx33       | Platform Router to XSA (HTTP/S)              |
| 3xx41-3xx99 | SQL Tenant(1+n)                              |
| 4xx01-4xx99 | 2nd to 1st site communication                |
| 5xx13       | HTTP                                         |
| 5xx14       | HTTPS                                        |

2. Use TLS to secure communication between the SAP HANA database and clients that access the database via the SQL interface.
The "sslEnforce" parameter in the communication section of the 'global.ini' file must be set to either true or TRUE.


## Verification of control

1.
* Either evaluate the firewall rules or perform port scans from different network segments in both directions to "the" HANA database.
* With SQL statement for tenant database: `SELECT SERVICE_NAME, PORT, SQL_PORT, (PORT + 2) HTTP_PORT FROM SYS.M_SERVICES WHERE ((SERVICE_NAME='indexserver' and COORDINATOR_TYPE= 'MASTER') or (SERVICE_NAME='xsengine'))`
* With SQL statement for system database: `SELECT DATABASE_NAME, SERVICE_NAME, PORT, SQL_PORT, (PORT + 2) HTTP_PORT FROM SYS_DATABASES.M_SERVICES WHERE DATABASE_NAME='<DBNAME>' and ((SERVICE_NAME='indexserver' and COORDINATOR_TYPE= 'MASTER') or (SERVICE_NAME='xsengine'))`

2. Check that the "sslEnforce" parameter in the "global.ini" file in the "communication" section is assigned the value true or TRUE.

## References
* SAP HANA Security Guide for SAP HANA Platform 2.0 SPS 07: 12.3.1
* SAP HANA Administration Guide for SAP HANA Platform 2.0 SPS 07: 
