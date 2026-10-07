<!--
name: 'Tool Result: Project write local_path protected file'
description: >-
  project_write refusal when local_path names a credential file, a device, or
  Claude Code's own config/token files
ccVersion: 2.1.292
-->
project_write: local_path must not name a credential file, a device, or a file that Claude Code keeps for itself (its config and token folders).
