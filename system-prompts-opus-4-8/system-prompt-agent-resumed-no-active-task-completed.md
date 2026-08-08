<!--
name: Agent Resumed (No Active Task) Completed Result
description: >-
  sendMessage tool-result message returned to the model when a target agent that
  had no active task was resumed from transcript and ran to completion
  synchronously, carrying its final text.
ccVersion: 2.1.199
variables:
  - SYSTEM_PROMPT_AGENT_RESUMED_NO_ACTIVE_TASK_COMPLETED_VAR_0
  - SYSTEM_PROMPT_AGENT_RESUMED_NO_ACTIVE_TASK_COMPLETED_VAR_1
-->
Agent "${SYSTEM_PROMPT_AGENT_RESUMED_NO_ACTIVE_TASK_COMPLETED_VAR_0.agentName}" had no active task; resumed from transcript with your message and ran to completion. Result:

${SYSTEM_PROMPT_AGENT_RESUMED_NO_ACTIVE_TASK_COMPLETED_VAR_1.finalText||"(no text output)"}
