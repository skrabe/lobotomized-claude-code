<!--
name: 'Guide agent: user-configuration wrapper'
description: >-
  Wrapper appended to the Claude guide-agent system prompt that injects the
  user's current configuration and asks the model to suggest relevant features.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_GUIDE_AGENT_USER_CONFIG_VAR_0
  - SYSTEM_PROMPT_GUIDE_AGENT_USER_CONFIG_VAR_1
-->
${SYSTEM_PROMPT_GUIDE_AGENT_USER_CONFIG_VAR_0}

---

# User's Current Configuration

The user has the following custom setup in their environment:

${SYSTEM_PROMPT_GUIDE_AGENT_USER_CONFIG_VAR_1.join(`

`)}
