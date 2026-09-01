<!--
name: Multiple background agents stopped notification
description: >-
  Task-notification injected into the model's context listing several background
  agents stopped by the user.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_BACKGROUND_AGENTS_STOPPED_VAR_0
  - SYSTEM_REMINDER_BACKGROUND_AGENTS_STOPPED_VAR_1
-->
${SYSTEM_REMINDER_BACKGROUND_AGENTS_STOPPED_VAR_0.length} background agents were stopped by the user: ${SYSTEM_REMINDER_BACKGROUND_AGENTS_STOPPED_VAR_0.map((SYSTEM_REMINDER_BACKGROUND_AGENTS_STOPPED_VAR_1)=>`"${SYSTEM_REMINDER_BACKGROUND_AGENTS_STOPPED_VAR_1}"`).join(", ")}.
