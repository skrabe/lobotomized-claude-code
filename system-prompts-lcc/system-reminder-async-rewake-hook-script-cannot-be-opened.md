<!--
name: 'System Reminder: Async-rewake hook script cannot be opened'
description: >-
  Queued notice telling Claude an async-rewake hook could not run because its
  script cannot be opened and exited with code 2 without doing work, a broken
  hook installation rather than feedback on its work, followed by the
  interpreter output
ccVersion: 2.1.288
variables:
  - SYSTEM_REMINDER_ASYNC_REWAKE_HOOK_SCRIPT_CANNOT_BE_OPENED_VAR_0
  - SYSTEM_REMINDER_ASYNC_REWAKE_HOOK_SCRIPT_CANNOT_BE_OPENED_VAR_1
-->
${SYSTEM_REMINDER_ASYNC_REWAKE_HOOK_SCRIPT_CANNOT_BE_OPENED_VAR_0} hook could not run: ${SYSTEM_REMINDER_ASYNC_REWAKE_HOOK_SCRIPT_CANNOT_BE_OPENED_VAR_1.scriptPath} cannot be opened, so its command exited with code 2 without doing any work. This is a broken hook installation, not feedback on your work; it is reported this once and identical repeats are dropped. Interpreter output:
