# pfSense Snort and Splunk breach monitoring

**Author:** Franco Pisano · **Context:** ITN 263 · Summer 2026 · **Type:** Guided lab

## Purpose

Follow firewall and intrusion-detection events into centralized analysis.

## Learning objectives

- Trace events from source to collector to search.
- Connect segmentation weaknesses with lateral-movement risk.
- Explain how structured fields improve investigation.

## Workflow

1. Configure pfSense logs, Snort and forwarding to Kiwi Syslog.
2. Extend monitoring to the DMZ and index events in Splunk.
3. Generate the scoped Nmap/perimeter simulation.
4. Investigate the Infection Monkey challenge and search its traces.

## Results and learning

My challenge response records six discovered machines, one compromised host through the VSFTPD backdoor scenario, and 14 exposed services. I identified weak segmentation as a concern. The written recommendations propose extracting source/destination addresses, signature, severity, protocol and port, then adding dashboards and correlation. Those enhancements are recommendations, not claimed deployments.

## Coverage of the saved report

The submission includes these stages (original stage labels):

- Configure the pfSense Firewall Log
- Configure a Snort Intrusion Detection System
- Implement Firewall Log Forwarding with Kiwi Syslog Server
- Configure Snort Monitoring on the DMZ
- Implement Security Information and Event Management with Splunk
- Simulate and Detect a Perimeter Network Attack
- Simulate a DMZ Breach with Infection Monkey
- Detect a Simulated DMZ Breach with Snort and Splunk

## Source and evidence

Prepared from my saved submission, `Monitoring and Logging Network Traffic (3e) - Franco Pisano.pdf`, for ITN 263 · Summer 2026. The saved report records 100% progress and contains captured task results. This public entry summarizes the documented work; a progress indicator alone does not independently validate every conclusion. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
