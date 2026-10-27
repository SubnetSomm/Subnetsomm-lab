# Packet capture and session interception

**Author:** Franco Pisano · **Context:** ITN 261 · Summer 2026 · **Type:** Guided lab

## Purpose

Examine how network position, certificates and application proxies affect traffic visibility in a controlled lab.

## Learning objectives

- Differentiate passive capture from active interception.
- Explain certificate trust in an interception exercise.
- Relate packet observations to application behavior.

## Workflow

1. Observe passive LAN traffic in Wireshark.
2. Complete the ARP-poisoning exercise with Ettercap.
3. Inspect the lab HTTPS/proxy workflow with Burp Suite.
4. Document the availability and certificate-trust challenges.

## Results and learning

The saved submission records ICMP capture, interception/proxy tasks and certificate-related results. This exercise does not establish that HTTPS is generally readable from a passive capture: the lab’s active position and configured trust are essential context.

## Coverage of the saved report

The submission includes these stages (original stage labels):

- Perform Passive Sniffing on a LAN
- Use Ettercap to Perform ARP Poisoning
- Hijack an HTTP Session with Burp Suite
- Use arpspoof for ARP Poisoning
- Enable Burp Suite to MITM Traffic on Port 443
- Hijack an HTTPS Session with Burp Suite
- Use Burp Suite to Perform a DOS Attack
- Install a CA Certificate on vWorkstation to Prevent SSL Warnings

## Source and evidence

Prepared from my saved submission, `Performing Packet Capture and Session Hijacking (4e) - Franco Pisano.pdf`, for ITN 261 · Summer 2026. The saved report records 100% progress and contains captured task results. This public entry summarizes the documented work; a progress indicator alone does not independently validate every conclusion. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
