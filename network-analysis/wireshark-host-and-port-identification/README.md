# Wireshark host and port identification

**Author:** Franco Pisano · **Context:** ITN 262 · Summer 2026 · **Type:** Documented coursework exercise

## Purpose

Use packet fields to identify both endpoints of a lab web connection.

## Learning objectives

- Read link, network and transport fields separately.
- Use a filter to answer a specific question.
- Connect an application request to its source/destination ports.

## Workflow

1. Inspect a DNS query to identify the Kali source address.
2. Filter the Kali-to-DVWA HTTP traffic.
3. Expand Ethernet II and IPv4 fields to record endpoint addresses.
4. Expand TCP to compare the ephemeral source port with destination port 80.

## Results and learning

The completed submission records the Kali/DVWA IP and MAC fields and an HTTP request using a client ephemeral port and server port 80. Addresses are omitted here because the learning objective is field interpretation rather than retaining environment identifiers.

## Source and evidence

Prepared from my saved submission, `Pisano_Wireshark Lab Assignment.pdf`, for ITN 262 · Summer 2026. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
