<!--
name: 'Tool Result: Auto-memory Windows dot-dot denied'
description: >-
  Permission deny message for the memory agent on Windows with
  blockReadsOutsideWorkingDirectories when a shell command contains '..'.
ccVersion: 2.1.292
-->
On Windows with permissions.blockReadsOutsideWorkingDirectories on, the memory agent's shell commands may not contain '..' anywhere, even split by quotes or a backslash, because where it leads cannot be checked. Use absolute paths, and avoid '..' in patterns too.
