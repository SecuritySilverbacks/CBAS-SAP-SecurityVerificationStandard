---
Security Function: PT
Category: Information Protection Processes and Procedures
Technology: SAP Java
Maturity Level: 1
IPAC: Platform (P)
Defender: Process / Technology
Prerequisite:
---

## Description

Setting a strong password policy is essential to protect from unauthorized access to your systems caused by stolen credentials or hashes. A weak password policy can result in several threats to the company, ranging from gaining access to sensitive information to corrupting an entire system.

## Implementation

Below helps organization's set a password policy for ABAP systems:

- [ ] Set minimum password length (1) with the UME property ume.logon.security_policy.password_min_length >= 12
- [ ] Increase maximum password lengthe with the UME property ume.logon.security_policy.password_max_length (default is only 14)
- [ ] Set an expiry for passwords to be changed with UME property ume.logon.security_policy.password_expire_days <= 90
- [ ] Define a password history size with the UME property ume.logon.security_policy.password_history >= 5
- [ ] To enforce users to comply with the password policy set UME property ume.logon.security_policy.enforce_policy_at_logon = TRUE
- [ ] Set maximum login attempts by UME property ume.logon.security_policy.lock_after_invalid_attempts <= 5
- [ ] Deny the use of old passwords in new passwords by setting the UME property ume.logon.security_policy.oldpass_in_newpass_allowed = FALSE
- [ ] Allow users to change their own password ume.logon.security_policy.password_change_allowed = TRUE
- [ ] Define a list of well-known passwords that are not allowed to be used by users through ume.logon.security_policy.password_impermissible
- [ ] Deny the use of user IDs as part of the password by setting the UME propertyume.logon.security_policy.userid_in_password_allowed = FALSE


Setting password complexity:
- [ ] Set UME propoerty ume.logon.security_policy.password_alpha_numeric_required >= 1
- [ ] Set UME ume.logon.security_policy.password_mix_case_required >= 1
- [ ] Set UME ume.logon.security_policy.password_special_char_required >= 1


(1) - SAP baseline recommends a minimum length of 8 characters. Our recommendation and research on cracking passwords, a minimum length of 8 characters can be easily broken with today's machines.

## Verification of Control

- [ ] Verify a that a password policy is in place with the recommended values in the implementation section

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A13 SAP password security (S) / SAP-Passwortsicherheit (S)
- SAP Security Baseline Template V2.1: 2.3.2.2, 2.3.2.2.2
