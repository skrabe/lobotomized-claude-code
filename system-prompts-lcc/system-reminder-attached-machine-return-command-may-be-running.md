<!--
name: 'System Reminder: Attached machine return command may be running'
description: >-
  Warns that a previously abandoned command may still be running and should not
  be repeated.
ccVersion: 2.1.295
variables:
  - SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_COMMAND_MAY_BE_RUNNING_VAR_0
  - SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_COMMAND_MAY_BE_RUNNING_VAR_1
  - SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_COMMAND_MAY_BE_RUNNING_VAR_2
-->
- ${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_COMMAND_MAY_BE_RUNNING_VAR_0}${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_COMMAND_MAY_BE_RUNNING_VAR_1}${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_COMMAND_MAY_BE_RUNNING_VAR_2}. Nothing was replayed. A command this session stopped waiting for may be running on ${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_COMMAND_MAY_BE_RUNNING_VAR_0} right now: do not send it again, and do not take "not done yet" to mean it did not run. If its outcome comes in, a correction note will say what became of it. If none has come by the time you need to know, look at what it did on ${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_COMMAND_MAY_BE_RUNNING_VAR_0} with a read-only command before deciding anything about it. Anything else that needs ${SYSTEM_REMINDER_ATTACHED_MACHINE_RETURN_COMMAND_MAY_BE_RUNNING_VAR_0} you may send now, once the step you are on is done.
