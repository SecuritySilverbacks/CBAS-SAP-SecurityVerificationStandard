---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP Java
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite:
---

## Description

The VSCAN interface is a way of checking files for malware when they are transferred to an SAP system. This interface makes it possible to automatically check for malware. The VSCAN interface can connect to various third-party virus protection solutions. If malicious files are detected, these files can be automatically blocked or quarantined. The use of the VSCAN interface offers the possibility to detect and prevent attacks for the distribution of malware via file interfaces of SAP ABAP systems according to the capabilities of the connected virus scanner.

## Implementation

**Prerequisite: You have installed the external antivirus product and the associated virus scan adapter in accordance with the manufacturer's instructions.**

1. Set up the virus scan adapter of the selected provider (see [2]) on each application server. This procedure eliminates the need to set up a virus scan server. Configure the virus scanner interface of the SAP system (see also [6]) using the NetWeaver Administrator web interface > Configuration > Virus Scan Provider
2. Create a scanner group in the Groups tab and link the virus scanner to this group. Several virus scanners can be configured per group for load balancing.
    1. Declare the new group as the standard scanner group.
    2. Set the configuration parameters for the scanner group according to the specifications of the interface provider.
    3. In the "Adapter" tab, create a new entry starting with the character string "VSA_". Reference the created scanner group in the virus scanner provider definition. Enter the path to the virus scanner adapter library as the adapter path. Please also note the specifications of the interface provider.
    4. Activate the Virus Scan Adapter.
3. Configure the scan profile in the "Profiles" tab
    1. Create a new profile in the customer namespace and set this as the default profile. Also observe the specifications of the interface provider.
    2. Add the scanner group created in 2.1 to this profile in the step configuration. 
    3. Create a profile configuration. Also observe the specifications of the interface provider.
4. In the profile overview, also activate all delivered SAP standard profiles.
5. Check the setup of the virus scanner connection using the HTTP service /vscantest/
    1. perform a scan of the virus scanner configuration objects and
    2. perform a test with the provided test servlet and the EICAR test file. A message should be displayed stating that a virus has been found and the process has been blocked.

## Verification of control

1. Check the setup of the virus scanner connection using the HTTP service /vscantest/
2. Perform a check of the virus scanner configuration objects
3. Perform a detection test with the provided test servlet and the EICAR test file. A message should be displayed stating that a virus has been found and the process has been blocked.

## References

1. [he EICAR Anti-Virus Test File](https://www.eicar.org/)
2. [SAP Note - 786179 - Data security products: Use in the antivirus area](https://me.sap.com/notes/786179)
3. [SUSE - Protecting against malware with ClamSAP](https://documentation.suse.com/sles-sap/15-SP4/html/SLES-SAP-guide/cha-clamsap.html#)
4. [SAP Note - 817623 - Frequent questions about VSI in SAP applications](https://me.sap.com/notes/817623)
6. [SAP Help - Setting Up Virus Scan Providers (Java)](https://help.sap.com/docs/JAVA_SERVER_FOR_S4HANA/007f2c7c77ae4e7884bba888e5aa5fe9/4e0ac1ca085c570ae10000000a42189e.html?locale=en-US)