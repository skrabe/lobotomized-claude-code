<!--
name: 'System Reminder: Async rewake hook script cannot be opened'
description: >-
  Wakes the model to report that an asyncRewake hook could not run because its
  script cannot be opened (optionally due to an unquoted path), not feedback on
  its work
ccVersion: 2.1.291
variables:
  - SYSTEM_REMINDER_ASYNC_REWAKE_HOOK_SCRIPT_CANNOT_BE_OPENED_VAR_0
  - SYSTEM_REMINDER_ASYNC_REWAKE_HOOK_SCRIPT_CANNOT_BE_OPENED_VAR_1
  - SYSTEM_REMINDER_ASYNC_REWAKE_HOOK_SCRIPT_CANNOT_BE_OPENED_VAR_2
-->
${SYSTEM_REMINDER_ASYNC_REWAKE_HOOK_SCRIPT_CANNOT_BE_OPENED_VAR_0} hook could not run: ${SYSTEM_REMINDER_ASYNC_REWAKE_HOOK_SCRIPT_CANNOT_BE_OPENED_VAR_1.scriptPath} cannot be opened${SYSTEM_REMINDER_ASYNC_REWAKE_HOOK_SCRIPT_CANNOT_BE_OPENED_VAR_2}, so its command exited with code 2 without doing any work. This is a broken hook installation, not feedback on your work; it is reported this once and identical repeats are dropped. Interpreter output:
