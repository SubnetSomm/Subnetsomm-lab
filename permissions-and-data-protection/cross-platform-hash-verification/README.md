# Cross-platform hash verification

**Author:** Franco Pisano · **Context:** ITN 276 · Spring 2026 · **Type:** Documented coursework exercise

## Purpose

Compare file hashes across Windows and Linux and after a content change.

## Learning objectives

- Explain deterministic content hashing.
- Compare like algorithms and bytes across platforms.
- Use a baseline to detect a content change.

## Workflow

1. Prepare a test file.
2. Calculate hashes with certutil/Get-FileHash and Linux sha256sum/OpenSSL.
3. Compare outputs for the same content and algorithm.
4. Modify the file and calculate its hash again.

## Results and learning

The written answers record matching values before modification and a changed value afterward. Portfolio clarification: this supports an integrity comparison; matching hashes alone do not document every custody event or decide admissibility.

## Source and evidence

Prepared from my saved submission, `Module 1 Hash Activity.docx`, for ITN 276 · Spring 2026. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
