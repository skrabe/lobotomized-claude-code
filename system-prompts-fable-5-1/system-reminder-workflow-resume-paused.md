<!--
name: Workflow resume instruction (paused)
description: >-
  Resume-workflow instruction injected into the model context (submitted as a
  prompt) when a paused workflow is resumed from the TUI.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_WORKFLOW_RESUME_PAUSED_VAR_0
  - SYSTEM_REMINDER_WORKFLOW_RESUME_PAUSED_VAR_1
-->
Resume the paused workflow by calling: Workflow({scriptPath: '${SYSTEM_REMINDER_WORKFLOW_RESUME_PAUSED_VAR_0.scriptPath}', resumeFromRunId: '${SYSTEM_REMINDER_WORKFLOW_RESUME_PAUSED_VAR_0.workflowRunId}'${SYSTEM_REMINDER_WORKFLOW_RESUME_PAUSED_VAR_1}}) — completed agents return cached results.
