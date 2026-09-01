<!--
name: Workflow resumeFromRunId
description: >-
  Description of the 'resumeFromRunId' input parameter in the Workflow tool's
  inputSchema; model-facing as part of the tool definition serialized to the
  model.
ccVersion: 2.1.191
variables:
  - TOOL_PARAMETER_WORKFLOW_RESUME_FROM_RUN_ID_VAR_0
-->
Run ID of a prior Workflow invocation to resume from. Completed agent() calls with unchanged (prompt, opts) return their cached results instantly; only edited or new calls re-run. Same-session only. Stop the prior run first (${TOOL_PARAMETER_WORKFLOW_RESUME_FROM_RUN_ID_VAR_0}) before resuming.
