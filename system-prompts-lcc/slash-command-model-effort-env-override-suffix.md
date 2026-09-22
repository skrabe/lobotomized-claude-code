<!--
name: 'Slash Command: /model — CLAUDE_CODE_EFFORT_LEVEL overrides this session'
description: >-
  Suffix appended to the /model confirmation when CLAUDE_CODE_EFFORT_LEVEL is
  set to a value other than xhigh, telling the model the env var is what
  actually applies until it is cleared.
ccVersion: 2.1.246
variables:
  - SLASH_COMMAND_MODEL_EFFORT_ENV_OVERRIDE_SUFFIX_VAR_0
  - SLASH_COMMAND_MODEL_EFFORT_ENV_OVERRIDE_SUFFIX_VAR_1
-->
 — CLAUDE_CODE_EFFORT_LEVEL=${SLASH_COMMAND_MODEL_EFFORT_ENV_OVERRIDE_SUFFIX_VAR_0} overrides effort this session; clear it and ${SLASH_COMMAND_MODEL_EFFORT_ENV_OVERRIDE_SUFFIX_VAR_1} takes over
