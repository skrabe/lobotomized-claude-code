<!--
name: 'Tool Result: Workflow Resume Run Not Exited'
description: >-
  Workflow resume refusal when the run is not running but has not exited, so
  resuming would double-run agents on the same journal.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_0
  - TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_1
  - TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_2
-->
Workflow ${TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_0} is not running but its run has not exited yet (task ${TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_1}). Resuming now would run two copies of its agents against the same journal. Run ${TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_2}({taskId: "${TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_1}"}) on it or wait for it to exit.
