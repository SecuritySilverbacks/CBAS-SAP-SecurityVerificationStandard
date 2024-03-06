---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP ABAP
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite:
---

## Description

The VSCAN interface is a way of checking files for malware when they are transferred to an SAP system. This interface makes it possible to automatically check for malware. The VSCAN interface can connect to various third-party virus protection solutions. If malicious files are detected, these files can be automatically blocked or quarantined. The use of the VSCAN interface offers the possibility to detect and prevent attacks for the distribution of malware via file interfaces of SAP ABAP systems according to the capabilities of the connected virus scanner.

## Implementation

**Prerequisite: You have installed the external antivirus product and the associated virus scan adapter in accordance with the manufacturer's instructions.**


1. Set up the virus scan adapter of the selected provider (see [2]) on each application server. This procedure eliminates the need to set up a virus scan server.
2. Configure the virus scanner interface of the SAP system (see also [6])
2.1 Define a scanner group using transaction VSCANGROUP and link the virus scanner to this group. Several virus scanners can be configured per group for load balancing.
2.2 Set the configuration parameters for the scanner group according to the specifications of the interface provider.
2.3 Create a virus scanner provider definition using transaction VSCAN. Select "Adapter (Virus Scan Adapter)" as the provider type. Reference the created scanner group in the virus scanner provider definition. Enter the path to the virus scanner adapter library as the adapter path. Please also note the specifications of the interface provider.
2.4 Start the Virus Scan Adapter and check that the connection is established correctly in the status output.
3. Configure the scan profile
3.1 Log in to a productive client.
3.2 Configure a scan profile using the transaction VSCANPROFILE. To do this, create a new profile in the customer namespace and set this as the default profile and as Active. Also observe the specifications of the interface provider.
3.3 Add the scanner group created in 2.1 as position 1 in the step configuration to this profile.
3.4 Create a profile configuration. Also observe the specifications of the interface provider.
3.5 In the profile overview, also activate all delivered SAP standard profiles.
3.6 Transport the scan profiles.
4. Check the setup of the virus scanner connection using transaction VSCANTEST and carry out a test with the EICAR character string provided. A message should be displayed stating that a virus has been found.

## Verification of control

1. Check the setup of the virus scanner connection using transaction VSCANTEST and carry out a test with a test file (EICAR see [1], or test file from the virus scanner provider).

## References

1. [The EICAR Anti-Virus Test File](https://www.eicar.org/)
2. [SAP Note - 786179 - Data security products: Use in the antivirus area](https://me.sap.com/notes/786179)
3. [SUSE - Protecting against malware with ClamSAP](https://documentation.suse.com/sles-sap/15-SP4/html/SLES-SAP-guide/cha-clamsap.html#)
4. [SAP Note - 817623 - Frequent questions about VSI in SAP applications](https://me.sap.com/notes/817623)
5. [SAP Help - Virus Scan Provider as an Application-Server-Starter](https://help.sap.com/docs/ABAP_PLATFORM/3cd5ac93e7ec4690bd804f0d23fed9da/4df58507472d41c4e10000000a42189c.html?locale=en-US)
6. [SAP Help - Setting Up a Virus Scan Provider (ABAP)](https://help.sap.com/docs/ABAP_PLATFORM/3cd5ac93e7ec4690bd804f0d23fed9da/4df582ed472d41c4e10000000a42189c.html?locale=en-US)