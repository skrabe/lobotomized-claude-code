<!--
name: Bash Sed Script Outside Reads Blocked
description: >-
  checkPermissions ask message for a non-allowlisted sed script that can touch
  any file under the read block.
ccVersion: 2.1.257
-->
This sed script is not on the allowlist and can read or write any file, which cannot be checked against the read block (permissions.blockReadsOutsideWorkingDirectories)
