# LVM storage provisioning

**Author:** Franco Pisano · **Context:** ITN 170 · Fall 2025 · **Type:** Documented coursework exercise

## Purpose

Build a logical volume from two supplied lab disks.

## Learning objectives

- Distinguish PV, VG and LV layers.
- Connect formatting, mounting and ordinary file access.
- Verify storage provisioning with a file operation.

## Workflow

1. Inspect block devices and partition the two exercise disks.
2. Initialize the partitions as physical volumes and create a volume group.
3. Create a 500 MB logical volume and format it as ext4.
4. Mount the volume, create a text file and verify its contents.

## Results and learning

The written submission documents two physical volumes, the volume group, a 500 MB logical volume, an ext4 filesystem and a mounted test file. Automatic mounting across reboot was not established in this saved account. Commands that partition or format disks belong only on identified disposable lab devices.

## Source and evidence

Prepared from my saved submission, `Pisano - Use Case 2.docx`, for ITN 170 · Fall 2025. The original course worksheet and unreviewed screenshots are retained in my private archive. Learning objectives here describe the skills practiced in the documented workflow.
