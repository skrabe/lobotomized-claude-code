<!--
name: Workflow still running
description: >-
  Workflow tool validateInput error returned to the model when the run being
  resumed is still active.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_WORKFLOW_STILL_RUNNING_VAR_0
  - TOOL_RESULT_WORKFLOW_STILL_RUNNING_VAR_1
  - TOOL_RESULT_WORKFLOW_STILL_RUNNING_VAR_2
-->
Workflow ${TOOL_RESULT_WORKFLOW_STILL_RUNNING_VAR_0.resumeFromRunId} is still running (task ${TOOL_RESULT_WORKFLOW_STILL_RUNNING_VAR_1}). Stop it first with ${TOOL_RESULT_WORKFLOW_STILL_RUNNING_VAR_2}({taskId: "${TOOL_RESULT_WORKFLOW_STILL_RUNNING_VAR_1}"}) before resuming.
