# Defense in depth and detection tuning

**Author:** Franco Pisano · **Context:** ITN 261 · Summer 2026 · **Type:** Guided lab

## Purpose

Reduce exposure and investigate defensive alerts across network layers.

## Learning objectives

- Connect segmentation with reduced attack paths.
- Explain detection tuning without disabling broad coverage.
- Require corroboration before classifying an alert as benign.

## Workflow

1. Review and update lab firewall and forwarding rules.
2. Apply the supplied network-defense configuration tasks.
3. Review resulting alerts and investigate false-positive candidates.
4. Document narrowly scoped suppression decisions.

## Results and learning

My saved analysis describes suppressing specific verified address/signature combinations rather than disabling whole rules. A refinement to the original reasoning is important: lab-generated traffic is not automatically benign. A defensible false-positive decision needs the triggering request, signature context and expected behavior.

## Coverage of the saved report

The submission includes these stages (original stage labels):

- Update the Firewall Rules
- Configure a Network-based IDS on pfSense
- Configure a Host-based IDS (HIDS) on Linux
- Validate Your IDS Security Controls
- Configure and Validate Protection Mode (IPS) on Network-based IDS
- Explore Protection Mode Options (HIPS) on Host-based IDS
- Snort: Identifying and Suppressing False Positive Alerts

## Source and evidence

Prepared from my saved submission, `Applying Defense-in-Depth Strategies to Secure Network Assets (4e) - Franco Pisano.pdf`, for ITN 261 · Summer 2026. The saved report records 100% progress and contains captured task results. This public entry summarizes the documented work; a progress indicator alone does not independently validate every conclusion. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
