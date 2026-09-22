<!--
name: 'Tool Result: SendUserFile Plan Mode Ask'
description: >-
  SendUserFile checkPermissions ask in plan mode that placing files in the
  shared folder requires plan approval first.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_SENDUSERFILE_PLAN_MODE_ASK_VAR_0
  - TOOL_RESULT_SENDUSERFILE_PLAN_MODE_ASK_VAR_1
  - TOOL_RESULT_SENDUSERFILE_PLAN_MODE_ASK_VAR_2
  - TOOL_RESULT_SENDUSERFILE_PLAN_MODE_ASK_VAR_3
  - TOOL_RESULT_SENDUSERFILE_PLAN_MODE_ASK_VAR_4
-->
${TOOL_RESULT_SENDUSERFILE_PLAN_MODE_ASK_VAR_0} would place ${TOOL_RESULT_SENDUSERFILE_PLAN_MODE_ASK_VAR_1(TOOL_RESULT_SENDUSERFILE_PLAN_MODE_ASK_VAR_2.files.length,"a file","files")} in the project's shared folder${TOOL_RESULT_SENDUSERFILE_PLAN_MODE_ASK_VAR_3?.TOOL_RESULT_SENDUSERFILE_PLAN_MODE_ASK_VAR_4==="ask"?` (${TOOL_RESULT_SENDUSERFILE_PLAN_MODE_ASK_VAR_3.message})`:""} — approve the plan first.
