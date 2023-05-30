---
Sicherheitsfunktion: PT
Kategorie: Benutzerverwaltung, Authentifizierung und Zugriffskontrolle
Technologie: SAP ABAP
Reifegrad: 1
IPAC: Zugriff (A)
Verteidiger: Technologie
Vorbedingung:
---

## Beschreibung

Es wird empfohlen, Single Sign-On (SSO) zu konfigurieren, wenn mehrere SAP-Systeme in der Umgebung des Unternehmens laufen. SSO kann den Prozess der Verwaltung und Konfiguration von Benutzerberechtigungen für mehrere Systeme und Anwendungen vereinfachen. Einem einzelnen Benutzer den Zugriff auf mehrere Anwendungen zu gestatten, birgt eigene Sicherheitsrisiken und Bedrohungen; eine sichere Konfiguration der ausgestellten Anmeldetickets muss vorhanden sein, um potenzielle Bedrohungen zu vermeiden.  

## Implementierung

Um ausgestellte Anmeldetickets während des Transports in ABAP-basierten Systemen zu schützen, müssen die folgenden Profilparameter vorhanden sein.  

- Verwenden Sie HTTPS, indem Sie login/ticket_only_by_https = 1 setzen.
- Um sicherzustellen, dass das Anmeldeticket an den erstellenden Host zurückgeschickt wird, setzen Sie login/ticket_only_to_host = 1
- Deklarieren Sie ein Cookie als HTTPonly, indem Sie icf/set_HTTPonly_flag_on_cookies = 1 oder 3 setzen. Dadurch wird anderen Anwendungen wie Applets, Plug-ins usw. der Zugriff auf das ausgestellte Cookie vom Webbrowser des Clients verweigert.


Hinweis: Diese Kontrolle setzt voraus, dass SSO in der Organisation bereits konfiguriert ist und verwendet wird.

## Überprüfung der Maßnahme

- Überprüfen Sie, ob der HTTPS-Profilparameter gesetzt ist, indem Sie login/ticket_only_by_https überprüfen.
- Überprüfen Sie, ob nur der erstellende Host das Anmeldeticket erhält, indem Sie login/ticket_only_to_host überprüfen.
- Prüfen Sie, ob der Profilparameter icf/set_HTTPonly_flag_on_cookies = 1 oder 3 ist.


## Referenzen:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A31 Konfiguration von SAP Single-Sign-On (S) / Konfiguration von SAP Single-Sign-On (S)
- SAP Security Baseline Template V2.1: 2.3.2.4.1
