---
Sicherheitsfunktion: DT
Kategorie: Anomalien und Ereignisse
Technologie: SAP ERP
Reifegrad: 1
IPAC: Plattform (P)
Verteidiger: Prozess
Vorraussetzung: DT-P-AE-M01-001
---

## Beschreibung

Protokollierung des Lesezugriffs:

Ein wichtiges Tool zur Überwachung und Aufzeichnung von Lesezugriffen auf geheime oder sensible Daten in SAP-Systemen. Das Tool hilft bei der Untersuchung einer Sicherheitsverletzung oder eines Informationslecks.  


## Implementierung

Die folgenden Konfigurationsschritte müssen durchgeführt werden, um die Protokollierung des Read Access Logs (RAL) zu überwachen und zu konfigurieren.

1. Bestimmen Sie, welche Art von Daten über RAL protokolliert werden soll
2. Erklären Sie einen Zweck für die Protokollierung der Daten, um Daten mit regulatorischer Relevanz zu identifizieren.
3. Definieren Sie die zu überwachenden Schnittstellen mittels RAL channels
4. Definieren Sie die Log-Domänen der verschiedenen Kanäle
5. Definieren Sie die Bedingungen für die Zugrifssprotokollierung


## Überprüfung der Maßnahme

- Konfigurieren und überwachen Sie die Protokollierung des Lesezugriffs über die Transaktion SRALMANAGER

## Referenzen:
