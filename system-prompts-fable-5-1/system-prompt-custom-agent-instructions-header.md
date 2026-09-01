<!--
name: Custom Agent Instructions Header
description: >-
  Model-facing system-prompt wrapper header prepended to an in-process
  teammate/sub-agent's custom system prompt ("# Custom Agent
  Instructions\n${V}"); conditional on the spawned agent supplying a system
  prompt.
ccVersion: 2.1.191
variables:
  - SYSTEM_PROMPT_CUSTOM_AGENT_INSTRUCTIONS_HEADER_VAR_0
-->

# Custom Agent Instructions
${SYSTEM_PROMPT_CUSTOM_AGENT_INSTRUCTIONS_HEADER_VAR_0}
