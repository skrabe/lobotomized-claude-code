<!--
name: 'System Prompt: Agent namer — names already taken'
description: >-
  The constraint listing names already in use, which the generated agent name
  must avoid.
ccVersion: 2.1.233
variables:
  - SYSTEM_PROMPT_AGENT_NAMER_AVOID_TAKEN_NAMES_VAR_0
-->


Avoid these (already taken): ${[...SYSTEM_PROMPT_AGENT_NAMER_AVOID_TAKEN_NAMES_VAR_0].join(", ")}
