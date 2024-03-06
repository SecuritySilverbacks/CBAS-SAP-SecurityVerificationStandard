---
Security Function: Protect (PT)
Category: Identity Management, Authentication and Access Control (PT.AC)
Technology: SAP BTP
Maturity Level: 2
SAP Operational Area: Platform (P)

Prerequisite: 
---

## Description

Identity authentication is an important component of SAP cloud applications that provides access control and security for users. It has the ability to act as its own identity provider or delegate authentication to third-party providers in proxy mode. The service requires a reduction in the number of administrators with full access based on internal user store permissions. However, inactive users are not automatically removed. When handling personal data, take into account the legislation in the different countries/regions in which your organization operates, as additional regulations may make it necessary to keep the data longer than required by the purpose limitation regulations.


## Implementation

1. If the service is configured to delegate authentication to a third-party identity provider, the trust between the service and the other identity provider is critical. Manage any changes to the trust settings.

2. Assigning the following permissions is critical. Ideally, manage these as part of your identity lifecycle process.
* Manage corporate identity providers
* Managing the tenant configuration
* Manage users

3. Regularly search for users who have not logged in for a long time, have never logged in or have not been used for a long time. Define a procedure to decide whether the user can be deleted or at least have all access rights withdrawn. Reasons can be,
* for long periods of non-use, employees have left the company but the users are still in the system
* for users without a login, are manually created shadow users that have a typo in their email address so that they do not match the user ID provided by the identity provider. They have never been used and it may make sense to delete them.
* no longer used for some time, employees have left the company, but the users are still in the system

4. Implement a data deletion strategy to manage the deletion of personal data. The cockpit can be used to remove "shadow users" in order to comply with data protection.

5. If you have configured the service to delegate authentication, regularly check that the trust relationship with the third-party identity provider is still correct and has not been inadvertently changed to an untrusted or non-productive identity provider. Monitor the identity provider's certificate and renew the trust before the certificate expires.

6. Regularly check which users have access to the User and role administrator role.

7. The user base for platform users should be provided by the custom identity provider. This applies, among other things, to
* global account, directories and multi-environment subaccounts
* Cloud Foundry organizations and spaces
* Neo environment subaccounts
* Multi-Environment and Neo environment subaccounts 

8. No platform user from the default identity provider with an external email address domain should have viewer rights.

9. No Cloud Foundry Organization or Space member from a default identity provider with an external email address domain should be assigned any of the following viewer rights: Org Auditor, Space Auditor.

10. No platform user from the default identity provider should belong to the C, D or I user classes.

11. A custom platform identity provider should be configured for user authentication of the global account platform.

12. A custom platform identity provider should be configured for the user authentication of the subaccount platform.

13. A custom platform identity provider should be configured to authenticate Cloud Foundry organization members and Cloud Foundry space members.

14. A custom application identity provider should be configured for the authentication of business customers.

15. SAP recommends that you keep at least one administrator for the global account, each subaccount, and each Cloud Foundry organization from the default identity provider. You can then use this administrator to log in in the rare event that access to the custom identity provider fails.

16. The standard platform role collections Global Account Administrator and Directory Administrator should only be assigned to a minimum number of platform users. (global account and directories)

17. The standard platform role collection Subaccount Administrator, which contains all critical subaccount roles, should only be assigned to a minimum number of platform users. (global account and directories)

18. The Cloud Foundry roles Org Manager, Space Manager and Space Developer should only be assigned to a minimum number of members. (Cloud Foundry organizations and spaces)

19. The default platform role Administrator, which contains the critical area manageCustomPlatformRoles, should only be assigned to a minimum number of platform users. (Neo environment subaccounts)

20. Custom platform roles that contain the critical platform area manageCustomPlatformRoles should only be assigned to a minimum number of platform users. (Neo environment subaccounts)

21. A dedicated HTML5 application authorization for the application descriptor neo-app.json must exist and should not be assigned to a business user role. (Neo environment subaccounts)

22. Platform API OAuth clients with the critical areas of manage authorization, manage account members or manage audit logs must be limited to the minimum required. (Neo environment subaccounts)

23. There should be no individual user role assignments in the Java application. (Neo environment subaccounts)

24. HTML5 applications should not have individual user role assignments. (Neo environment subaccounts)

25. There should be no individual user role assignments for subscriptions for Java or HTML5 applications. (Neo environment subaccounts)

26. SAP recommends assigning a set of roles required for a specific task to a group, which allows easy management of the required authorizations for a specific group of users instead of individual users. (Neo environment subaccounts)

27. SAP recommends automating the assignment of users to groups via "assertion-based groups" or via the Identity Provisioning Service. (Neo environment subaccounts)

28. SAP recommends configuring the identity authentication service as a custom identity provider for platform users/members and as an identity provider for business users and connecting it to your own corporate identity provider.

29. Platform users are usually developers, administrators or operators who deploy, manage and troubleshoot applications and services on SAP BTP. SAP recommends configuring the Identity Authentication Service as a custom identity provider and connecting Identity Authentication to your own corporate identity provider.

30. Business users use the applications that are provided in SAP BTP. For example, the end users of SaaS applications or services, such as SAP Workflow Service or SAP Cloud Integration, or the end users of your custom applications are business users. SAP recommends configuring the Identity Authentication Service as an identity provider and linking identity authentication to your own corporate identity provider.

31. By configuring your own managed identity provider for BTP users, you can enforce custom security configurations such as two-factor authentication (2FA), password policies and administrative access (locking users, etc.) and have full control over the user base.


## Verification of control
> TODO


## References
* SAP BTP Security Recommendations: BTP-IAS-0014, BTP-IAS-0017, BTP-UAA-0010, BTP-UAA-0011, BTP-UAA-0015, BTP-UAA-0017
* SAP Security Baseline Template V2.4: 2.3.1.3.2, 2.3.2.5.1, 2.3.3.1.4, 2.3.3.2.1, 3.1.1.2.1, 3.1.1.8.1, 3.1.1.24.1