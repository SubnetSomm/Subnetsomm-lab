# DNS HTTP and HTTPS observations

**Author:** Franco Pisano · **Context:** ITN 266 · Summer 2026 · **Type:** Documented coursework exercise

## Purpose

Capture web-related traffic and explain what is visible.

## Learning objectives

- Distinguish DNS resolution from an HTTP request.
- Explain the effect of HTTPS on payload visibility.
- Adapt traffic generation to the question being tested.

## Workflow

1. Install/configure Wireshark and select an interface.
2. Generate web traffic and locate the DNS query.
3. Recognize that the browser’s HTTPS traffic does not expose a normal HTTP GET in cleartext.
4. Use curl with an explicit HTTP URL to generate and inspect an observable GET.

## Results and learning

My submission records a specific adaptation: curl -v with an HTTP URL produced the GET/Host fields needed for the exercise when ordinary browsing used HTTPS. This preserves an important troubleshooting decision instead of making the packet list look like an unexplained result.

## Source and evidence

Prepared from my saved submission, `Assignment_6.1_Using_Wireshark.docx`, for ITN 266 · Summer 2026. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
