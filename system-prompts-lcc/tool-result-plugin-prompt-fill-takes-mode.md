<!--
name: 'Plugin hook error: takes { mode } of …'
description: >-
  Rejection of a plugin's $-API call; when the mod's hook does not catch it, the
  mod-under-development failure notice tells the model.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_PLUGIN_PROMPT_FILL_TAKES_MODE_VAR_0
-->
takes { mode } of ${TOOL_RESULT_PLUGIN_PROMPT_FILL_TAKES_MODE_VAR_0.join(", ")}
