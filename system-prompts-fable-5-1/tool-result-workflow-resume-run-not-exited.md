<!--
name: 'Tool Result: Workflow Resume Run Not Exited'
description: >-
  Workflow validateInput failure when resumeFromRunId ended but the run has not
  exited, so resuming would double-run agents on the same journal.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_0
  - TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_1
  - TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_2
-->
Workflow ${TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_0.resumeFromRunId} ended but its run has not exited yet (task ${TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_1}). Resuming now would run two copies of its agents against the same journal. Run ${TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_2}({taskId: "${TOOL_RESULT_WORKFLOW_RESUME_RUN_NOT_EXITED_VAR_1}"}) on it or wait for it to exit.
