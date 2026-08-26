<!--
name: 'Tool Result: Device Hook Stale Deadline'
description: >-
  PreToolUse deny reason when the hook request reached the attached machine
  already past its deadline.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_DEVICE_HOOK_STALE_DEADLINE_VAR_0
-->
not run — the request reached ${TOOL_RESULT_DEVICE_HOOK_STALE_DEADLINE_VAR_0.displayName} already past its deadline (check that machine's clock); retry
