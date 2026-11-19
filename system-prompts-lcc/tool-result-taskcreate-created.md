<!--
name: 'Tool Result: TaskCreate created'
description: >-
  TaskCreate result confirming the task id and subject, with an optional
  app-keeps-statuses note
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_TASKCREATE_CREATED_VAR_0
  - TOOL_RESULT_TASKCREATE_CREATED_VAR_1
  - TOOL_RESULT_TASKCREATE_CREATED_VAR_2
-->
Task #${TOOL_RESULT_TASKCREATE_CREATED_VAR_0.id} created successfully: ${TOOL_RESULT_TASKCREATE_CREATED_VAR_0.subject}${TOOL_RESULT_TASKCREATE_CREATED_VAR_1===!0?`

${TOOL_RESULT_TASKCREATE_CREATED_VAR_2}`:""}
