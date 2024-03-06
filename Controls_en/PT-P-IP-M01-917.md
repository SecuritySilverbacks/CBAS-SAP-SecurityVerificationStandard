---
Security Function: Protect (PT)
Category: Information Protection Processes and Procedures (PT.IP)
Technology: SAP BTP
Maturity Level: 2
SAP Operational Area: Platform (P) & Integration (I)

Prerequisite: 
Responsible: 
---

## Description

RFC access control can be configured for specific hosts and ports, and it is possible to specify which function modules (resources) are permitted on these hosts. By default, both the CPIC trace traces and the payload traces are disabled, but they can be enabled if required. In addition, the login page of the service cannot be embedded into other applications by default, but this can be changed to allow integration into other applications with iFrames. Components within the Cloud Foundry environment use digital signatures for access tokens, and these should remain secure even if a signing key is ever leaked.


## Implementation


<!---
SAP Operational Area: Customzing (C)
--->

1. At least for your productive environments, check whether the access controls are carried out correctly. Make the prefixes of your function names as specific as possible. We recommend using exact function names. If you make them too open, e.g. by using a poorly defined prefix, you run the risk of granting access to malicious or unintended modules.

<!---
SAP Operational Area: Platform (P)
--->

2. Only activate traces if you really need them. Check regularly whether the traces are deactivated. The traces can record sensitive data in unencrypted files. Activate the dual control principle for the activation of traffic traces.

3. Regularly check whether the configuration of your login service still meets your requirements. Make sure that no attacker can add malicious web pages or Javascript to any of the hosts that are authorized to embed the login page. This recommendation also applies to hosts that act as reverse proxies, where an attacker can drop their content on another host behind the reverse proxy. Make sure that everything issued by these framing hosts is secure. Instead of configuring lists of trusted domains, make sure that your application is running under the same domain as the framing application. For more information on SAP Custom Domain Service, see the SAP Custom Domain Service documentation. If your custom identity provider runs under a different domain than the framing application, you must configure the identity provider so that it also trusts the domain of the framing application.

4. Set the redirect-uris parameter so that access is restricted as far as possible. Check regularly whether this configuration still meets your requirements. If you use wildcards, we recommend that you make the URIs as specific as possible. By using wildcards, you open the redirect for multiple websites. Wildcards increase the risk of being redirected to malicious websites.

5. Change the signing key regularly, but at least every 18 months.

6. Use the standard TLS configurations offered by the Custom Domain Manager, but at least TLS 1.2. Actively manage use cases that require a different configuration, e.g. using an external service as a backward-compatible reverse proxy as part of a risk acceptance check.


## Verification of control

> TODO


## References

* SAP BTP Security Recommendations: BTP-CLC-0016, BTP-CLC-0020, BTP-UAA-0001, BTP-UAA-0002, BTP-UAA-0019, BTP-DOM-0005
* [SAP Help - Manage TLS Configurations](https://help.sap.com/docs/custom-domain/custom-domain-manager/manage-tls-configurations?locale=en-US)
* [SAP Note - 3308931 - TLS 1.3 Support for Cloud Foundry Platform Domains](https://me.sap.com/notes/3308931)