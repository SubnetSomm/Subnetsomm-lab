# FileVerifier integrity monitoring

**Author:** Franco Pisano · **Context:** ITN 266 · Summer 2026 · **Type:** Documented coursework exercise

## Purpose

Use a file-integrity baseline to detect changed content.

## Learning objectives

- Distinguish content identity from an explanation of changes.
- Protect the integrity baseline separately from monitored data.
- Explain why detecting change is not the same as classifying intent.

## Workflow

1. Install FileVerifier++ and select the hashing settings.
2. Select the target directory and verify the baseline.
3. Create or change the exercise text content.
4. Run verification again and interpret the difference.

## Results and learning

My written reflection notes that an attacker who can alter both files and the baseline may defeat a naive integrity check. A hash difference indicates changed bytes; it does not identify the changed words or determine whether the change was authorized.

## Source and evidence

Prepared from my saved submission, `Assignment 7.1 File Verifier.docx`, for ITN 266 · Summer 2026. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
