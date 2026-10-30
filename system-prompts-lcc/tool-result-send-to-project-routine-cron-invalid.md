<!--
name: 'Send to Project: Routine cron field error'
description: >-
  Validation message prefixing a routine's cron_expression path to the cron
  problem.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_ROUTINE_CRON_INVALID_VAR_0
  - TOOL_RESULT_SEND_TO_PROJECT_ROUTINE_CRON_INVALID_VAR_1
-->
routines[${TOOL_RESULT_SEND_TO_PROJECT_ROUTINE_CRON_INVALID_VAR_0}].cron_expression ${TOOL_RESULT_SEND_TO_PROJECT_ROUTINE_CRON_INVALID_VAR_1}
