# Windows Linux and file integrity monitoring

**Author:** Franco Pisano · **Context:** ITN 262 · Summer 2026 · **Type:** Guided lab

## Purpose

Combine authentication logs, network detection and integrity monitoring.

## Learning objectives

- Match event sources to the activity being investigated.
- Distinguish network alerts from host-integrity changes.
- Explain the difference between detection and blocking.

## Workflow

1. Identify Windows failed-login events.
2. Configure Snort monitoring and observe ICMP alerts.
3. Inspect Linux failed-login messages and logging configuration.
4. Review Tripwire changes and the additional event/IPS challenges.

## Results and learning

My written analysis discusses a Windows cryptographic-operation failure event; the saved report also records login events, Snort alerts, a Tripwire report and a blocking-mode challenge. An event identifier should be interpreted with its fields and context rather than used as a complete incident conclusion.

## Coverage of the saved report

The submission includes these stages (original stage labels):

- Identify Failed Logon Attempts on Windows Systems
- Monitor Network Activity with Snort
- Identify Failed Logon Attempts on Linux Systems
- Monitor File Integrity with Tripwire
- Identify Additional Event Types in the Event Viewer
- Configure Snort as an Intrusion Prevention System

## Source and evidence

Prepared from my saved submission, `Implementing Security Monitoring and Logging (4e) - Elem - Franco Pisano.pdf`, for ITN 262 · Summer 2026. The saved report records 100% progress and contains captured task results. This public entry summarizes the documented work; a progress indicator alone does not independently validate every conclusion. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
