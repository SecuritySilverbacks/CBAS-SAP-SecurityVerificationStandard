---
Security Function: IY
Category: Risk Assessment
Technology: ABAP
Maturity Level: 1
IPAC: Customizing (C)
Defender: _People, Process, Technology_
Prerequisite: _A control that is required to be in place before the current one_
---

## Description

Prevention of injection & sanitisation vulnerabilities

Injection & sanitisation vulnerabilities refer to situations where a hacker introduces control characters and/or commands via the data channel (input) into an application. A successful attack can have a damaging impact on the scheduled program sequence as a result of unexpected commands.
Injection & sanitisation vulnerabilities represent an enormous security risk posed by custom developments. Depending on the type of injection, a hacker can gain complete control of the affected SAP system. Typically, the technical details of injection vulnerabilities are quite complex, extremely diverse, and generally very difficult to understand. Therefore, it is difficult both for developers and testers, without specific training, to identify vulnerabilities and to eliminate them.


## Implementation

1.	During processing of user entries, a plausibility check must normally be carried out. This is referred to as “input validation”. Input validation not only provides basic security protection (since control characters and special characters are ineffective in most data fields and can be removed) but it also improves the data quality in general. Input validation should be implemented in such a way that the inputs are compared with a list of permitted values, that is, using the “whitelist filter” approach.
2.	Special care should be taken if user input is mixed with control characters or language elements (semantics) and the result is then processed or executed as a whole. In this case, all the control characters in the data, which are relevant in the context, must be rendered harmless. This operation is referred to as “output encoding” or “escaping”.


## Verification of control

_Steps to verify if a control exists_

## References

_References_
