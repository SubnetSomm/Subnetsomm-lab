# Birthday manager

**Author:** Franco Pisano · **Context:** ITP 150 · Spring 2026 · **Type:** Coursework program

## Purpose

Manage an in-memory birthday directory with a menu and CSV export.

## Learning objectives

- Use a dictionary for keyed records.
- Implement menu-driven control flow.
- Export structured data with the standard csv module.

## Workflow

1. Choose lookup, add, change, delete, print, save or quit.
2. Store names and birthdays as dictionary keys and values.
3. Append the dictionary entries to a CSV file when saving.

## Results and learning

The source implements dictionary CRUD and CSV export. It starts with an empty dictionary and does not reload the exported CSV. Repeated saves append duplicate rows. Non-numeric menu input is not handled. These are preserved coursework limitations; use invented names and dates when demonstrating the program.

## Run the original program

Requires Python 3 and the standard library.

```bash
python3 birthdays.py
```

The source preserves the coursework version. See the limitations above before extending it.

## Source and evidence

Prepared from my saved submission, `birthdays.py`, for ITP 150 · Spring 2026. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
