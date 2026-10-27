# Windows IKEv2 client and IPsec policy

**Author:** Franco Pisano · **Context:** ITN 263 · Summer 2026 · **Type:** Guided lab

## Purpose

Configure a remote-access client and examine the resulting negotiation.

## Learning objectives

- Use PowerShell to express client settings.
- Distinguish tunnel setup from cryptographic-policy negotiation.
- Relate packet evidence to the configured VPN.

## Workflow

1. Configure the Windows VPN client and transfer exercise.
2. Create an additional connection with PowerShell.
3. Apply a custom IPsec-policy challenge.
4. Inspect CREATE_CHILD_SA and the selected Diffie-Hellman transform in Wireshark.

## Results and learning

The written challenge records an Add-VpnConnection invocation using IKEv2, EAP and required encryption, with split tunneling enabled for that lab connection. That historical lab setting is not the full-tunnel recommendation in the separate architecture design. Captures document negotiation tasks; they should not be replaced by an assumption that the desired policy was selected.

## Coverage of the saved report

The submission includes these stages (original stage labels):

- Configure a Windows VPN Client
- Compare Secure and Non-Secure File Transfers in Wireshark
- Create a New VPN Connection using PowerShell
- Implement a Custom IPsec Policy
- Verify Your VPN Implementation using Wireshark

## Source and evidence

Prepared from my saved submission, `Configuring a VPN Client for Secure File Transfers (3e) - Franco Pisano.pdf`, for ITN 263 · Summer 2026. The saved report records 100% progress and contains captured task results. This public entry summarizes the documented work; a progress indicator alone does not independently validate every conclusion. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
