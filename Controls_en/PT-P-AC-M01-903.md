---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP BTP
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

Different types of authentication can be set up for HTTP and RFC (Remote Function Call) destinations in SAP systems. The default setting is Standard, but custom policies can be created if required. For all Internet-based proxy destinations, certificates from a third-party PKI or SAP-generated certificates can be used. OAuth SAML Bearer Assertion Authentication and Mutual TLS with X.509 client certificates are available options for HTTP and RFC destinations respectively, but only if the tokenService.KeyStoreLocation property is set in the destination configuration. Basic authentication, mTLS, oauth:mtls or oauth:key can also be used to access REST APIs. By default, there is a single administrator user in a file-based user store. The service uses an X.509 certificate to sign SAML 2.0 protocol messages between itself, a SAML service provider and a SAML identity provider.


## Implementation

1. If password-based authentication is mandatory for you, we recommend "Enterprise" over "Standard" as this is the only way to fix leaked accounts. It is better to disable passwords for employees if possible. See also BTP-IAS-0006

2. If you have decided to use SAP-generated certificates, you should also agree to the automatic renewal of these certificates. To do this, activate the "Automatic renewal for certificates in the keystore" checkbox.

3. 
- Use Principal Propagation SSO authentication for interactive HTTP sessions in the on-premise environment
- For Internet connections, use OAuth SAML Bearer Assertion Authentication or SAML Assertion Authentication
- If you need to use password-based authentication, use strong passwords. This recommendation applies to the BasicAuthentication and OAuth2Password types.
- Do **not** use SAP Assertion SSO. This type is obsolete.

4. If the SystemUser was maintained for test purposes and transported to the production system, make sure that the attribute ??? attribute is not maintained. This setting is obsolete and will be removed. Use the ClientCertificateAuthentication attribute instead.

5. Mutual TLS is recommended for all productive environments. To perform mutual TLS, use an X.509 client certificate instead of a client secret when connecting to the authorization server. Create a certificate configuration with a valid X.509 client certificate or a keystore and link it to the target configuration.

6. Use the following authentication types:
- Use BasicAuthentication for local connections.
- For Internet connections, use ClientCertificateAuthentication.
This option is part of the RFC configuration. Do not confuse this scenario with interactive scenarios where user forwarding is the recommendation. See also BTP-DES-0014.

7. Enable single sign-on (SSO) by forwarding the identity of cloud users to on-premise SAP systems. The user is redirected from a cloud application to an on-premise system by using a target configuration with the PrincipalPropagation authentication type. To enable Single Sign-On with Principal Propagation, set the value to PrincipalPropagation. In this case, you should not configure jco.client.user and jco.client.passwd. See also BTP-DES-0008.

8. Use the authentication types mTLS, oauth:mtls or oauth:key in productive environments.

9. Switch from a standard super administrator to several users from your own LDAP. You can achieve segregation of duties by splitting access for these users across multiple support roles. Moving away from the standard user is important for auditing so that it can be recorded who has made configuration changes.

10. Regularly check whether the signing keys for SAML tokens have expired. Replace them if necessary.

11. Only OAuth2 flows or client certificate authentication should be used for transport destinations.


## Verification of control
> TODO


## References
* SAP BTP Security Recommendations: BTP-IAS-0002, BTP-DES-0002, BTP-DES-0003, BTP-DES-0004, BTP-DES-0007, BTP-DES-0008, BTP-DES-0014, BTP-CRS-0007, BTP-CLC-0022, BTP-UAA-0020, BTP-TMS-0001
