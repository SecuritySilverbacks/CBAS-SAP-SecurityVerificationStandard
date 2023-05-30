---
Security Function: IY
Category: Risk Assessment
Technology: ABAP
Maturity Level: 1
IPAC: Customizing (C)
Defender: Process
Prerequisite: _A control that is required to be in place before the current one_
---

## Description

Prevention of injection vulnerabilities

Injection vulnerabilities refer to situations where a adversary introduces control characters and/or commands via the data channel (input) into an application. A successful attack can have a damaging impact on the scheduled program sequence as a result of unexpected commands.
Depending on the type of injection, an attacker can gain complete control of the affected SAP system. For the ABAP programming language this includes in particular implementations with:
- Access to the file system from file servers, or from the SAP operating systems for exchanges, or for processing of data takes place. With the number of interfaces (applications), the risk increases for each individual interface of receiving compromised data for processing, or of generating such data itself through faulty input.

- Using operating system commands via ABAP programs. The system access is carried out in the context of the SAP-system service user. This user necessarily has extensive privileges in the operating system. Considering the resulting overall risk, ABAP code that executes operating system commands should receive special protection.

- Using dynamic ABAP language features and database access. The options for using dynamic ABAP programming and access to databases have many uses. However, they are also associated with particular risks. If dynamic programming is necessary, these risks must be accounted for by the developer through the use of special protective measures.

## Implementation

1. As part of change review process the implementation's design has to be verified to against the the following properties:
    - During processing of input, a sufficient plausibility check must normally be carried out. This is referred to as “input validation”. Input validation not only provides basic security protection (since control characters and special characters are ineffective in most data fields and can be removed) but it also improves the data quality in general. Input validation should be implemented in such a way that the inputs are compared with a list of permitted values, that is, using the “allowlist filter” approach.
    - Special care should be taken if user input is mixed with control characters or language elements (semantics) and the result is then processed or executed as a whole. In this case, all the control characters in the data, which are relevant in the context, must be rendered harmless. This operation is referred to as “output encoding” or “sanitisation” depending on the output context.
      The implementation of the following measures in particular should be validated:
      - Indirection: The execution of critical code should be decoupled as much as possible from input
      - Plausibility: Range checks, allowlists and/or denylists should be used to restrict the input's value range to plausible values.
      - Context validation: Before execution, control logic must run which sufficiently check the execution authorization of the program, user and input.
      - Traceability: Consideration should be given to logging the execution of sensitive business logic for the user's context, execution time, and input sufficiently.
      - Equivalence: For dynamically executed code, the same level of control  must run as for an equivalent static implementation complying with the in the case of correct static implementation of the code execution.

2. As part of the change testing process all implementations has to be verified for protection against input based attacks as when suitable ABAP techniques being used in the implementation.
    - Directory & file traversal.
    - Operating system command injection.
    - SQL injection.
    - Forceful browsing
    - ABAP code injection.

## Verification of control

- [ ] Audit if the source code review is carried out and documented on all custom code changes to identify injection & sanitisation vulnerabilities.
- [ ] Audit if the change has been sufficiently tested and documented for the above vulnerabilities.

## References

- CIS CSC 4
- COBIT 5 APO12.01, APO12.02, APO12.03, APO12.04
- ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12
- ISO/IEC 27001:2013 Clause 6.1.2
- NIST SP 800-53 Rev. 4 RA-3, SI-5, PM-12, PM-16
- OWASP ASVS 2.0 V5.1, V5.3
- BSI APP (February 2020) 4.6 A7, A8, A11, A13, A18
