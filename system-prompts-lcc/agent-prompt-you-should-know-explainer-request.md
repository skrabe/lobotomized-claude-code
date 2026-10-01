<!--
name: 'Agent Prompt: You Should Know Explainer Request'
description: >-
  Prompt for the You should know side agent to write the plain-language
  explainer the person said yes to, optionally rewriting a previous version in a
  requested direction
ccVersion: 2.1.286
variables:
  - AGENT_PROMPT_YOU_SHOULD_KNOW_EXPLAINER_REQUEST_VAR_0
  - AGENT_PROMPT_YOU_SHOULD_KNOW_EXPLAINER_REQUEST_VAR_1
-->
${AGENT_PROMPT_YOU_SHOULD_KNOW_EXPLAINER_REQUEST_VAR_0}

Answer straight away: do not think it over first, do not call any tool.

The person watching you work said yes to: "${AGENT_PROMPT_YOU_SHOULD_KNOW_EXPLAINER_REQUEST_VAR_1}"

