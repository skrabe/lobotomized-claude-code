<!--
name: 'Tool Result: Resume MCP task refused'
description: >-
  Resume-MCP-task result: the polling service cannot take the task in this
  session, so nothing changed and a retry gives the same
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_RESUME_MCP_TASK_REFUSED_VAR_0
-->
The polling service cannot take task ${TOOL_RESULT_RESUME_MCP_TASK_REFUSED_VAR_0} in this session, so nothing changed: if this session polls the task, it polls on, and if tracking had stopped, nobody polls it. A second call now gives the same result.
