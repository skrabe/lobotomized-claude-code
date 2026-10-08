<!--
name: Orphaned Shell Without Completion Record
description: >-
  Explains a restored background shell's uncertain completion and advises
  checking its output.
ccVersion: 2.1.294
variables:
  - SYSTEM_REMINDER_ORPHANED_SHELL_NO_COMPLETION_RECORD_VAR_0
-->
No completion record was found for it in the previous session. It may have been stopped (via the UI, Monitor timeout, or agent teardown — these leave no transcript marker), or it may have been running when the previous Claude Code process exited.${SYSTEM_REMINDER_ORPHANED_SHELL_NO_COMPLETION_RECORD_VAR_0()?"":" Check the output file for partial results before assuming it completed."}
