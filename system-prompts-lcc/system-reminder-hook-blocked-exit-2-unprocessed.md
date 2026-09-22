<!--
name: Hook Blocked Exit 2 Unprocessed
description: >-
  Blocking-error body when an exit-2 hook block could not parse the hook's
  output.
ccVersion: 2.1.257
variables:
  - SYSTEM_REMINDER_HOOK_BLOCKED_EXIT_2_UNPROCESSED_VAR_0
  - SYSTEM_REMINDER_HOOK_BLOCKED_EXIT_2_UNPROCESSED_VAR_1
  - SYSTEM_REMINDER_HOOK_BLOCKED_EXIT_2_UNPROCESSED_VAR_2
-->
[${SYSTEM_REMINDER_HOOK_BLOCKED_EXIT_2_UNPROCESSED_VAR_0?`${SYSTEM_REMINDER_HOOK_BLOCKED_EXIT_2_UNPROCESSED_VAR_1.type} hook`:SYSTEM_REMINDER_HOOK_BLOCKED_EXIT_2_UNPROCESSED_VAR_2}]: blocked (exit 2); its output could not be processed
