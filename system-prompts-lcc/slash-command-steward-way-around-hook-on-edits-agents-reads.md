<!--
name: 'Slash Command: Steward way around hooks on edits and agents'
description: >-
  Names hooks on edits, agents, reads or check-in tools that can change a call
  after the limits pass it or add allow rules
ccVersion: 2.1.330
-->
a PreToolUse or PermissionRequest hook runs on file edits, agents, file reads, or another tool that a check-in uses, and it can change such a call after these limits have let it through, or at PermissionRequest add permission rules that allow other calls too
