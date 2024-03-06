---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP HANA
Maturity Level: 3
SAP Operational Area: Access (A)

Prerequisite: PT-A-AC-M01-014
---

## Description

Passwords in SAP HANA landscapes with increased security requirements must comply with certain guidelines in order to prevent any misuse of SAP systems. This includes the use of upper and lower case letters, numbers and special characters.

## Implementation

Change the following parameters in the "indexserver.ini" file in the "password policy" section on the HANA database

1. password_layout e.g. to the value A1a_
* This parameter defines which character types predefined by SAP must be contained in a password.
	* A means that capital letters must be included in the password
	* 1 means that numbers must be included in the password
	* a means that lower case letters must be included in the password
	* _ means that special characters must be included in the password
* As of June 2023, the SAP standard configuration for HANA states that the password must contain at least one lowercase letter, one uppercase letter and one number; the use of special characters is optional.


2. last_used_passwords to an integer value greater than or equal to 5
* This parameter prevents passwords that have already been used from being reused too quickly.


3. Set maximum_unused_productive_password_lifetime to an integer value between 1 and 180
* Users who have not logged into the system for a longer period of time using different authentication mechanisms are automatically deactivated after the defined days have elapsed.


4. maximum_password_lifetime to an integer value of less than or equal to 183; corresponds to half a year
* This parameter forces a regular password change
> * Default setting as of June 2023: 182 days


## Verification of control

Check that the parameter values for "password_layout", "last_used_passwords", "maximum_password_lifetime" and "minimum_password_length" in the "indexserver.ini" file in the "password policy" section correspond to your specifications.


## References
* SAP Security Baseline Template V2.4: 2.3.2.2.3
* SAP HANA Security Guide for SAP HANA Platform 2.0 SPS 07: 7.3.1