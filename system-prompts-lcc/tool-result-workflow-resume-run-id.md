<!--
name: 'Tool Result: Workflow resume run ID'
description: >-
  Workflow launch result giving the run ID and the call to resume after editing
  the script, with cache-replay semantics and a journal.jsonl caveat
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_WORKFLOW_RESUME_RUN_ID_VAR_0
-->

Run ID: ${TOOL_RESULT_WORKFLOW_RESUME_RUN_ID_VAR_0.runId}
To resume after editing the script, with the same args if this run had any: Workflow({scriptPath: "${TOOL_RESULT_WORKFLOW_RESUME_RUN_ID_VAR_0.scriptPath}", resumeFromRunId: "${TOOL_RESULT_WORKFLOW_RESUME_RUN_ID_VAR_0.runId}"}) — agent() calls return cached results up to the first one that failed, no longer matches (edited, added, removed, or in a different call order) or never started. Cached results may themselves be empty: inspect journal.jsonl before assuming there is something to recover.
