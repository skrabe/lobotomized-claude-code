<!--
name: 'Tool Result: Artifact file read permission check expired'
description: >-
  Artifact tool error when the save permission check expired before the reads
  ran.
ccVersion: 2.1.291
-->
the permission check for these saves expired before they ran (too many concurrent file operations) — nothing was fetched; retry so it is checked again
