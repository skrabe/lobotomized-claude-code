<!--
name: Agent types removed
description: >-
  System-reminder injected into context listing agent types no longer available
  for the Agent tool.
ccVersion: 2.1.218
variables:
  - SYSTEM_REMINDER_AGENT_TYPES_REMOVED_VAR_0
  - SYSTEM_REMINDER_AGENT_TYPES_REMOVED_VAR_1
-->
The following agent types are no longer available:
${SYSTEM_REMINDER_AGENT_TYPES_REMOVED_VAR_0.map((SYSTEM_REMINDER_AGENT_TYPES_REMOVED_VAR_1)=>`- ${SYSTEM_REMINDER_AGENT_TYPES_REMOVED_VAR_1}`).join(`
`)}
