# Apache service troubleshooting

**Author:** Franco Pisano · **Context:** ITN 170 · Fall 2025 · **Type:** Documented coursework exercise

## Purpose

Install Apache on Ubuntu and investigate why the service could not start.

## Learning objectives

- Use service status to narrow a failure.
- Diagnose a listener/port conflict.
- Verify a fix rather than stopping at installation.

## Workflow

1. Check whether Apache is already installed.
2. Update the package index and install apache2.
3. Inspect the failed service and confirm document-root permissions.
4. Use ss to identify nginx listening on port 80, stop/disable it, then restart Apache.
5. Verify service status and document the Hello World webpage.

## Results and learning

My submission records Apache becoming active after nginx was stopped and disabled in the shared lab environment. This resolved the observed conflict. In another environment, the intended architecture might instead require changing ports or retaining nginx as a proxy; stopping a service should follow the actual service requirements.

## Source and evidence

Prepared from my saved submission, `Pisano - Apache Server Assignment.docx`, for ITN 170 · Fall 2025. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
