<!--
name: 'System reminder: REPL off, do not call REPL tools'
description: >-
  Reminder when REPL mode is taken out of a session: do not call the REPL/Poll
  tools; calls are refused; disregard their descriptions.
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_REPL_OFF_DO_NOT_CALL_REPL_TOOLS_VAR_0
  - SYSTEM_REMINDER_REPL_OFF_DO_NOT_CALL_REPL_TOOLS_VAR_1
-->
Do not call ${SYSTEM_REMINDER_REPL_OFF_DO_NOT_CALL_REPL_TOOLS_VAR_0} or ${SYSTEM_REMINDER_REPL_OFF_DO_NOT_CALL_REPL_TOOLS_VAR_1}. They may still be in your tool list, but every call to them is refused. Disregard their descriptions, including the statement that you have no other tools.
