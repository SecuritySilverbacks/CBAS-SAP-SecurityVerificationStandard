---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP BTP
Maturity Level: 1
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

There are different authentication methods and security settings for different types of connections in a BTP technical environment. The default method for logging in to the administration console is username and password. HTTP destinations with proxy type Internet can use TLS 1.2 as the default version, but this change requires a restart of the application if it is used by a Java application. RFC destinations have three configuration options: direct connection (ABAP application server), load balancing group of ABAP servers or WebSocket to an ABAP application server over the Internet with HTTPS protocol and ProxyType=Internet. The Cloud Connector enables the release of internal systems on the Internet, there are no standard entries for this function. The Cloud Connector also enables the management of strict lists of permitted URLs for access control, whereby all other HTTP(S) requests are rejected. RFC SNC ensures a secure connection from the cloud application to the backend system through a TLS tunnel and can be used with the Cloud Connector. By default, the Cloud Connector trusts all root CAs.

## Implementation

1. Always protect the management console application with multi-level authentication.
2. Do not use older TLS versions and regularly check that all destinations are configured to use the TLS version recommended in the documentation.
3. Trusting all server certificates for web sockets is not recommended for productive landscapes. Make sure that the parameter "jco.client.tls_trust_all" is not set to "1". Instead, set the parameter to "0" and maintain the list of trusted certificates in the JDK trust store.
4. Ensure that HTTPS is enforced for all production environments. Check this setting regularly and manage any exceptions as part of your risk management process. Make sure that your target systems support HTTPS beforehand/afterwards.
5. Be very careful with the use of the "all sub-paths" option for productive landscapes. Make your URLs as specific as possible. Using sub-paths increases the risk of connecting to malicious or unintended resources. Regularly check whether root URLs have been made publicly accessible.
6. Use SNC for your productive environments. Manage all exceptions as part of your risk management process. Make sure that your target backend system supports SNC beforehand/afterwards.
7. Use LDAPS at least for your productive environments to encrypt LDAP data, including user credentials. Check regularly whether the configuration uses LDAPS.
8. Limit the number of root CAs that the Cloud Connector trusts.

## Verification of control

> TODO

## References

* SAP BTP Security Recommendations: BTP-IAS-0001, BTP-DES-0001, BTP-DES-0010, BTP-CLC-0008, BTP-CLC-0009, BTP-CLC-0015, BTP-CLC-0017, BTP-CLC-0018