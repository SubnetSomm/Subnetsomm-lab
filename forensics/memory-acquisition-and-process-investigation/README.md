# Memory acquisition and process investigation

**Author:** Franco Pisano · **Context:** ITN 276 · Spring 2026 · **Type:** Guided lab

## Purpose

Investigate volatile evidence using multiple acquisition and memory-analysis tools.

## Learning objectives

- Describe volatile evidence acquisition.
- Correlate processes with handles, network activity and privileges.
- Separate observations from hypotheses about malicious behavior.

## Workflow

1. Capture memory with DumpIt and inspect processes in E3.
2. Review process start times, opened registry keys and files.
3. Acquire memory with FTK Imager and analyze it with Volatility.
4. Correlate process listings and network artifacts, then examine YARA and privilege-comparison outputs.

## Results and learning

My report records process observations involving conhost.exe, hooker.exe and rvlkl.exe, plus a challenge involving connections to a common reverse-shell listener port. The public interpretation is deliberately narrower than some original notes: a filename or port alone does not prove malware, missing network artifacts do not prove concealment, and dynamic ports are not inherently safe. Corroboration requires process context, paths, hashes and other evidence.

## Coverage of the saved report

The submission includes these stages (original stage labels):

- Capture Memory using DumpIt
- Analyze Memory using E3
- Capture Memory using FTK Imager
- Analyze Memory using Volatility
- Identify Malicious Connections
- Identify Malicious Processes
- Identify Privilege Escalation

## Source and evidence

Prepared from my saved submission, `Conducting Forensic Investigations on System Memory (4e) - Franco Pisano.pdf`, for ITN 276 · Spring 2026. The saved report records 100% progress and contains captured task results. This public entry summarizes the documented work; a progress indicator alone does not independently validate every conclusion. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
