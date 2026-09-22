<!--
name: Workflow tool note in worker context
description: >-
  Workflow-tool bullet in the subagent tools context injected into a worker's
  system prompt.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_WORKFLOW_TOOL_NOTE_VAR_0
  - SYSTEM_PROMPT_WORKFLOW_TOOL_NOTE_VAR_1
-->

- **${SYSTEM_PROMPT_WORKFLOW_TOOL_NOTE_VAR_0}** (if available) - After its explicit opt-in condition is satisfied, run a matching multi-step subagent pipeline instead of hand-orchestrating ${SYSTEM_PROMPT_WORKFLOW_TOOL_NOTE_VAR_1} calls
