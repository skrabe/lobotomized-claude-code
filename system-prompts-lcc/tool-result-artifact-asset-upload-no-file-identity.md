<!--
name: 'Tool Result: Artifact asset upload volume has no file identity'
description: >-
  Preflight error (J3a) for volumes that report no usable file identity, so the
  approved file cannot be distinguished from a replacement.
ccVersion: 2.1.234
-->
file_path is on a volume that reports no usable file identity (some network, FUSE, and virtual-disk mounts), so the approved file cannot be told apart from a replacement — copy it to an ordinary local directory and upload the copy
