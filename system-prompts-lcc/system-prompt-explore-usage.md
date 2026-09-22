<!--
name: Explore-agent usage note
description: >-
  Guidance on spawning the Explore agent for broad exploration, injected into
  the system prompt.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_EXPLORE_USAGE_VAR_0
  - SYSTEM_PROMPT_EXPLORE_USAGE_VAR_1
  - SYSTEM_PROMPT_EXPLORE_USAGE_VAR_2
  - SYSTEM_PROMPT_EXPLORE_USAGE_VAR_3
-->

When the central delegation rule calls for delegating broad codebase exploration or research, spawn ${SYSTEM_PROMPT_EXPLORE_USAGE_VAR_1} with subagent_type=${SYSTEM_PROMPT_EXPLORE_USAGE_VAR_2.agentType}. Otherwise use ${SYSTEM_PROMPT_EXPLORE_USAGE_VAR_3} directly.
