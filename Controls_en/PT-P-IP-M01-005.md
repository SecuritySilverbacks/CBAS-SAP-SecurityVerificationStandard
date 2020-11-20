---
Security Function: PT
Category: Information Protection Processes and Procedures
Technology: SAP ABAP
Maturity Level: 1
IPAC: Platform (P)
Defender: Process / Technology
Prerequisite:
---

## Description

Setting a strong password policy is essential to protect from unauthorized access to your systems caused by stolen credentials or hashes. A weak password policy can result in several threats to the company, ranging from gaining access to sensitive information to corrupting an entire system.

## Implementation

Below helps organization's set a password policy for ABAP systems:

- [ ] Set Minimum password length (1) with the profile parameter login/min_password_lng >= 12
- [ ] Set a maximum number of days a password can be unused with profile parameter login/password_max_idle_initial (set between 1 to 14)
- [ ] Set expiry for passwords to be changed with profile parameter login/password_expiration_time <= 90
- [ ] Define a password history size with the profile parameter login/password_history_size >= 5
- [ ] Do not store passwords for old kernels to interpret by setting profile parameter login/password_downwards_compatibility=0
- [ ] To enforce users to comply with the password policy set profile parameter login/password_compliance_to_current_policy=1
- [ ] Remove old downward compatible password hashes in fields BCODE and PASSCODE from the USR02 table
- [ ] Set maximum login attempts by profile parameter login/fails_to_user_lock <= 5
- [ ] Disable auto unlock by profile parameter login/failed_user_auto_unlock = 0
- [ ] Setting a maximum period for an unused productive password to stay valid by profile parameter login/max_idle_productive <= 90
- [ ] Deny logging in with initial or expired user accounts by setting profile parameter icf/reject_expired_passwd = 1
- [ ] Deny logging in with initial or expired user accounts via RFC by setting profile parameter rfc/reject_expired_passwd = 1
- [ ] Disable password login when the organization is using other authentication methods with the profile parameter login/disable_password_logon > 0
- [ ] When using Single Sign-on (SSO) authentication method it is mandatory to check whether a users passwords needs changing with the profile parameter login/password_change_for_SSO
- [ ] Define a period of time (measured in days) that a user is able to change their password again with the profile parameter login/password_change_waittime > 0
- [ ] Set the hashing algorithm and encoding for new password with the profile parameter login/password_hash_algorithm = encoding=RFC2307, algorithm=iSSHA-512, iterations=15000, saltsize=256

Setting password complexity:
- [ ] Set profile parameter login/min_password_digits >= 1
- [ ] Set profile parameter login/min_password_letters >= 1
- [ ] Set profile parameter login/min_password_lowercase >= 1
- [ ] Set profile parameter login/min_password_uppercase >= 1
- [ ] Set profile parameter login/min_password_specials >= 1
- [ ] Set profile parameter login/min_password_diff >= 3


(1) - SAP baseline recommends a minimum length of 8 characters. Our recommendation and research on cracking passwords, a minimum length of 8 characters can be easily broken with today's machines.

## Verification of Control

- [ ] Verify a that a password policy is in place with the recommended values in the implementation section
- [ ] Verify if table USR02 contains old downward compatible password hashes in fields BCODE and PASSCODE


## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A13 SAP password security (S) / SAP-Passwortsicherheit (S)
- SAP Security Baseline Template V2.1: 2.3.2.2, 2.3.2.2.1
- SAP Note 1458262
