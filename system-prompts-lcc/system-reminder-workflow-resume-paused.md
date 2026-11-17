<!--
name: Workflow resume instruction (paused)
description: >-
  Resume-workflow instruction injected into the model context (submitted as a
  prompt) when a paused workflow is resumed from the TUI.
ccVersion: 2.1.326
variables:
  - SYSTEM_REMINDER_WORKFLOW_RESUME_PAUSED_VAR_0
  - SYSTEM_REMINDER_WORKFLOW_RESUME_PAUSED_VAR_1
-->
Resume the paused workflow by calling: ${SYSTEM_REMINDER_WORKFLOW_RESUME_PAUSED_VAR_0(SYSTEM_REMINDER_WORKFLOW_RESUME_PAUSED_VAR_1)} — agent() calls return cached results up to the first one that failed, no longer matches or never started.
