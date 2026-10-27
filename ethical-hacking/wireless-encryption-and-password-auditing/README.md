# Wireless encryption and password auditing

**Author:** Franco Pisano · **Context:** ITN 261 · Summer 2026 · **Type:** Guided lab

## Purpose

Compare wireless protection mechanisms using supplied captures and controlled auditing tasks.

## Learning objectives

- Explain why encryption changes traffic visibility.
- Distinguish protocol weaknesses from guessable passwords.
- Document the assumptions of a capture-based password audit.

## Workflow

1. Inspect unencrypted traffic with Wireshark.
2. Work through the WEP exercise.
3. Generate candidate words and analyze the WPA2 capture with the lab’s auditing tools.
4. Complete a separate supplied-capture challenge.

## Results and learning

The report records wireless capture and recovered lab-passphrase tasks. Public notes omit the supplied credentials. The important lesson is that an audit result depends on both the protection scheme and the password candidates available; it is not evidence that every WPA2 network can be recovered in the same way.

## Coverage of the saved report

The submission includes these stages (original stage labels):

- Capture Unencrypted Traffic with Wireshark
- Encrypt Wireless Traffic with WEP
- Break WEP Encryption
- Encrypt Wireless Traffic with WPA2
- Break WPA2 Encryption
- Mangle a Wordlist with John the Ripper
- Perform a Dictionary Attack using a WPA2 Network Capture

## Source and evidence

Prepared from my saved submission, `Exploiting Wireless Vulnerabilities (4e) - Franco Pisano.pdf`, for ITN 261 · Summer 2026. The saved report records 100% progress and contains captured task results. This public entry summarizes the documented work; a progress indicator alone does not independently validate every conclusion. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
