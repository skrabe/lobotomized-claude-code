<!--
name: 'Tool Result: Workflow Resume Paused Run Not Exited'
description: >-
  Workflow resume refusal when the run is paused but has not exited, so agents
  are still stopping against the same journal.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_WORKFLOW_RESUME_PAUSED_RUN_NOT_EXITED_VAR_0
  - TOOL_RESULT_WORKFLOW_RESUME_PAUSED_RUN_NOT_EXITED_VAR_1
-->
Workflow ${TOOL_RESULT_WORKFLOW_RESUME_PAUSED_RUN_NOT_EXITED_VAR_0} is paused but its run has not exited yet (task ${TOOL_RESULT_WORKFLOW_RESUME_PAUSED_RUN_NOT_EXITED_VAR_1}); its agents are being stopped. Resuming now would run two copies of its agents against the same journal — wait for it to exit.
