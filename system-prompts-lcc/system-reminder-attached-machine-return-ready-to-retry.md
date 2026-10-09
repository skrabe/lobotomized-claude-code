<!--
name: 'System Reminder: Attached machine return ready to retry'
description: >-
  Allows calls to a returned machine after the current step, with checks before
  repeating commands of unknown state.
ccVersion: 2.1.295
variables:
  - SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_READY_TO_RETRY_VAR_0
  - SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_READY_TO_RETRY_VAR_1
  - SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_READY_TO_RETRY_VAR_2
-->
- ${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_READY_TO_RETRY_VAR_0}${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_READY_TO_RETRY_VAR_1}${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_READY_TO_RETRY_VAR_2}. Nothing was replayed. You may call it again now: finish the step you are on, if any, then send again what still needs ${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_READY_TO_RETRY_VAR_0}; for a command whose state was unknown, check what it did before repeating it.
