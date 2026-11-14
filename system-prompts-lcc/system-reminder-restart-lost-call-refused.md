<!--
name: 'System Reminder: Restart lost call refused'
description: >-
  Tells Claude a tool call lost by a restart was refused and not to make it
  again
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_RESTART_LOST_CALL_REFUSED_VAR_0
  - SYSTEM_REMINDER_RESTART_LOST_CALL_REFUSED_VAR_1
  - SYSTEM_REMINDER_RESTART_LOST_CALL_REFUSED_VAR_2
-->
A call of ${SYSTEM_REMINDER_RESTART_LOST_CALL_REFUSED_VAR_0?.SYSTEM_REMINDER_RESTART_LOST_CALL_REFUSED_VAR_1??"a tool"} that a restart lost was refused. Do not make it again.${SYSTEM_REMINDER_RESTART_LOST_CALL_REFUSED_VAR_2.message?` Reason: ${SYSTEM_REMINDER_RESTART_LOST_CALL_REFUSED_VAR_2.message}`:""}
