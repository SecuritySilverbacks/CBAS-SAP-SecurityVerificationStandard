---
Sicherheitsfunktion: PT
Kategorie: Benutzerverwaltung, Authentifizierung und Zugriffskontrolle
Technologie: SAP Java
Reifegrad: 1
IPAC: Zugriff (A)
Verteidiger: Technologie
Vorbedingung:
---

## Beschreibung

Es wird empfohlen, Single Sign-On (SSO) zu konfigurieren, wenn mehrere SAP-Systeme in der Umgebung des Unternehmens laufen. SSO kann den Prozess der Verwaltung und Konfiguration von Benutzerberechtigungen für mehrere Systeme und Anwendungen vereinfachen. Einem einzelnen Benutzer den Zugriff auf mehrere Anwendungen zu gestatten, birgt eigene Sicherheitsrisiken und Bedrohungen; eine sichere Konfiguration der ausgestellten Anmeldetickets muss vorhanden sein, um potenzielle Bedrohungen zu vermeiden.  

## Implementierung

Um ausgestellte Anmeldetickets während des Transports in Java-basierten Systemen zu schützen, müssen die folgenden Profilparameter vorhanden sein.  

- Verwenden Sie HTTPS, indem Sie ume.logon.security.enforce_secure_cookie = true setzen.
- Legen Sie ein Ablaufdatum für das ausgestellte Ticket fest, indem Sie login.ticket_lifetime ≤ 8 (hh:mm) setzen.
- Deklarieren Sie ein Cookie als HTTPonly, indem Sie ume.logon.httponlycookie = true setzen. Dadurch wird der Zugriff auf das ausgestellte Cookie vom Webbrowser des Clients durch andere Anwendungen wie z.B. Javascript-Zugriff, Plug-ins usw. verhindert.


Hinweis: Diese Kontrolle setzt voraus, dass SSO in der Organisation bereits konfiguriert ist und verwendet wird.

## Überprüfung der Maßnahme

- Überprüfen Sie, ob der HTTPS-Profilparameter gesetzt ist, indem Sie ume.logon.security.enforce_secure_cookie = true überprüfen.
- Überprüfen Sie, ob ein Ablaufdatum für ausgestellte Anmeldetickets existiert, indem Sie login.ticket_lifetime ≤ 8 überprüfen.
- Prüfen Sie, ob der Profilparameter ume.logon.httponlycookie = true

## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A31 Konfiguration von SAP Single-Sign-On (S) / Konfiguration von SAP Single-Sign-On (S)
- SAP Security Baseline Template V2.1: 2.3.2.4.2
