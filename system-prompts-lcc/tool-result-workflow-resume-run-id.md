<!--
name: Workflow resume run ID result
description: >-
  Fragment of the Workflow tool result telling the model the run ID and how to
  resume after editing the script.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_WORKFLOW_RESUME_RUN_ID_VAR_0
-->

Run ID: ${TOOL_RESULT_WORKFLOW_RESUME_RUN_ID_VAR_0.runId}
To resume after editing the script: Workflow({scriptPath: "${TOOL_RESULT_WORKFLOW_RESUME_RUN_ID_VAR_0.scriptPath}", resumeFromRunId: "${TOOL_RESULT_WORKFLOW_RESUME_RUN_ID_VAR_0.runId}"}) — completed agents return cached results (cached results may themselves be empty — inspect journal.jsonl before assuming there is something to recover).
