<!--
name: 'Tool Description: Choose a listed agent type'
description: >-
  Task/Agent tool description clause telling the model to pick "fork" or one of
  the listed agent types because no general-purpose agent is available
ccVersion: 2.1.235
variables:
  - TOOL_DESCRIPTION_TASK_CHOOSE_LISTED_AGENT_TYPE_VAR_0
  - TOOL_DESCRIPTION_TASK_CHOOSE_LISTED_AGENT_TYPE_VAR_1
-->
${TOOL_DESCRIPTION_TASK_CHOOSE_LISTED_AGENT_TYPE_VAR_0}, so choose ${TOOL_DESCRIPTION_TASK_CHOOSE_LISTED_AGENT_TYPE_VAR_1?'`"fork"` or ':""}one of the listed agent types.
