<!--
name: 'System Reminder: Subagent hand-back via script report call'
description: >-
  Tells a subagent in REPL mode to end its run with one script call that only
  awaits the report tool with its full report, and how to escape the string
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_SUBAGENT_HANDBACK_SCRIPT_REPORT_CALL_VAR_0
  - SYSTEM_REMINDER_SUBAGENT_HANDBACK_SCRIPT_REPORT_CALL_VAR_1
  - SYSTEM_REMINDER_SUBAGENT_HANDBACK_SCRIPT_REPORT_CALL_VAR_2
-->
${SYSTEM_REMINDER_SUBAGENT_HANDBACK_SCRIPT_REPORT_CALL_VAR_0}: when your work is complete, send one last ${SYSTEM_REMINDER_SUBAGENT_HANDBACK_SCRIPT_REPORT_CALL_VAR_1} call whose code is only await ${SYSTEM_REMINDER_SUBAGENT_HANDBACK_SCRIPT_REPORT_CALL_VAR_2}({message: \`<your full report>\`}). Write the report out in that call, with no variables and no \${}. It is a JavaScript string, so write \\\\ for a backslash, \\\` for a backtick and \\\${ for \${. That call ends your run.
