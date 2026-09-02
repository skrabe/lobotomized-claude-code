<!--
name: 'Tool Description: Agent Available Types'
description: >-
  Agent tool description block listing that agent types appear in
  system-reminders and how to pass subagent_type including fork.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_0
  - TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_1
  - TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_2
  - TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_3
  - TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_4
  - TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_5
-->
${TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_0}.

Available agent types are listed in <system-reminder> messages in the conversation.${TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_1}

${TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_2?`When using the ${TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_3} tool, specify a subagent_type to select an agent: \`"fork"\` forks yourself (the fork inherits your full conversation context and always runs on your model — a \`model\` override is ignored); ${TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_4?"any other type — or omitting it — starts a fresh agent (general-purpose by default).":`any other type starts a fresh agent. ${TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_5}`}`:`When using the ${TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_3} tool, specify a subagent_type parameter to select which agent type to use. ${TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_4?"If omitted, the general-purpose agent is used.":TOOL_DESCRIPTION_AGENT_AVAILABLE_TYPES_VAR_5}`}
