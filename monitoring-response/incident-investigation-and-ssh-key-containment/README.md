# Incident investigation and SSH key containment

**Author:** Franco Pisano · **Context:** ITN 261 · Summer 2026 · **Type:** Guided lab

## Purpose

Follow an incident from monitoring and scope determination through containment, root-cause investigation and recovery.

## Learning objectives

- Use logs to establish incident scope.
- Connect a response action to the compromised access mechanism.
- Preserve authorized access while revoking a specific key.

## Workflow

1. Review SIEM inputs and inspect the reported suspicious content.
2. Trace relevant events to affected servers and investigate SSH activity.
3. Document containment, root cause and recovery tasks.
4. Remove the identified compromised authorized key and verify the remaining fingerprints.

## Results and learning

My written response records backing up authorized_keys on three supplied servers, removing the key identified by fingerprint, retaining other keys, applying 700 to .ssh and 600 to authorized_keys, and verifying the result with ssh-keygen. This is a concrete containment action. It removes that authorized key from those accounts; it does not by itself establish that every possible persistence mechanism was removed.

## Coverage of the saved report

The submission includes these stages (original stage labels):

- Review the SIEM configuration
- Identify the scope of a reported issue
- Contain and Investigate the event
- Recover from the incident
- Investigate the root cause using log files
- Add remediation tasks
- Add real time monitoring for nginx load balancer configuration
- Disable the compromised key

## Source and evidence

Prepared from my saved submission, `Investigating and Responding to Security Incidents (4e) - Franco Pisano.pdf`, for ITN 261 · Summer 2026. The saved report records 100% progress and contains captured task results. This public entry summarizes the documented work; a progress indicator alone does not independently validate every conclusion. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
