<!--
name: 'System Reminder: Attached machine return with unknown duration'
description: >-
  Warns that a returned machine's earlier command state is unknown and must be
  checked before replay.
ccVersion: 2.1.295
variables:
  - SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_UNKNOWN_DURATION_VAR_0
  - SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_UNKNOWN_DURATION_VAR_1
-->
- ${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_UNKNOWN_DURATION_VAR_0}${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_UNKNOWN_DURATION_VAR_1}. Nothing was replayed. This session cannot tell whether a command that was running on ${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_UNKNOWN_DURATION_VAR_0} when it went quiet has finished, is still running, or never ran: before sending any such command again, look at what it did on ${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_UNKNOWN_DURATION_VAR_0} with a read-only command. Anything else that needs ${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_UNKNOWN_DURATION_VAR_0} you may send now, once the step you are on is done.
