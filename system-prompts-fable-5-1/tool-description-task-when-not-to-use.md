<!--
name: 'Tool Description: Task When Not To Use'
description: >-
  Task/agent tool description fragment advising to use direct tools for known
  targets and reserve this tool for open-ended work.
ccVersion: 2.1.178
variables:
  - TOOL_DESCRIPTION_TASK_WHEN_NOT_TO_USE_VAR_0
  - TOOL_DESCRIPTION_TASK_WHEN_NOT_TO_USE_VAR_1
-->

## When not to use

If the target is already known, use the direct tool: ${TOOL_DESCRIPTION_TASK_WHEN_NOT_TO_USE_VAR_0} for a known path, ${TOOL_DESCRIPTION_TASK_WHEN_NOT_TO_USE_VAR_1} for a specific symbol or string. Reserve this tool for open-ended questions that span the codebase, or tasks that match an available agent type.
