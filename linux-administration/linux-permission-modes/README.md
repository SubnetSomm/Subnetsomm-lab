# Linux permission modes

**Author:** Franco Pisano · **Context:** ITN 170 · Fall 2025 · **Type:** Documented coursework exercise

## Purpose

Apply and inspect owner/group/other access modes.

## Learning objectives

- Translate symbolic and numeric modes.
- Interpret owner/group/other permissions.
- Verify a configuration through observed output.

## Workflow

1. Create the exercise directory and two empty files.
2. Use symbolic chmod to grant the owner access while removing group/other access.
3. Use numeric chmod 550 for the second file.
4. Compare ls -l output with the intended permission bits.

## Results and learning

The saved output shows owner-only rwx for one file and r-x for owner/group with no other access for the second. Execute permission on a regular file controls executability; on a directory it controls traversal, so the object type matters.

## Source and evidence

Prepared from my saved submission, `Pisano - Use Case 1.docx`, for ITN 170 · Fall 2025. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
