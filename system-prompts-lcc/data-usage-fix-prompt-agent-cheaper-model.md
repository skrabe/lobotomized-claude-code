<!--
name: 'Data: Usage fix prompt agent cheaper model'
description: >-
  Usage-fix prompt saying a named agent's subagents were a given share of usage
  and asking Claude to check their model and set a cheaper one where it fits, or
  explain what can change if built in.
ccVersion: 2.1.325
variables:
  - DATA_USAGE_FIX_PROMPT_AGENT_CHEAPER_MODEL_VAR_0
-->
Subagents under \`${DATA_USAGE_FIX_PROMPT_AGENT_CHEAPER_MODEL_VAR_0.name}\` were ${DATA_USAGE_FIX_PROMPT_AGENT_CHEAPER_MODEL_VAR_0.pct}% of my usage. Check which model they run on, and if a cheaper one fits their work, set it in the agent file or skill that defines them. If they are built in, tell me what I can change.
