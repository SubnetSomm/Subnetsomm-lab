# Windows ICMP and outbound HTTP rules

**Author:** Franco Pisano · **Context:** ITN 266 · Summer 2026 · **Type:** Documented coursework exercise

## Purpose

Observe the effect of a scoped host-firewall change.

## Learning objectives

- Use before/after tests.
- Distinguish protocol-specific and port-specific rules.
- Keep test scope aligned with the conclusion.

## Workflow

1. Run an initial ping test.
2. Apply the exercise ICMP rule and compare the failed test.
3. Create an outbound port 80 block and attempt an HTTP visit.
4. Confirm that the separate HTTPS path still works, then disable the exercise rules.

## Results and learning

The screenshot captions document a port 80 block with HTTPS still available. One original question discusses blocking port 443; this public account follows the documented port 80 test and does not treat that question as evidence that port 443 was blocked.

## Source and evidence

Prepared from my saved submission, `Assignment_6.2_Creating_Firewall_Rules.docx`, for ITN 266 · Summer 2026. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
