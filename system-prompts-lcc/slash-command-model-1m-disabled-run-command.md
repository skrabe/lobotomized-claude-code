<!--
name: 'Slash Command: /model 1M disabled (run command wording)'
description: >-
  /model result when a [1m] alias is picked but CLAUDE_CODE_DISABLE_1M_CONTEXT
  is set, telling the model to run /model with the standard alias instead.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_MODEL_1M_DISABLED_RUN_COMMAND_VAR_0
  - SLASH_COMMAND_MODEL_1M_DISABLED_RUN_COMMAND_VAR_1
  - SLASH_COMMAND_MODEL_1M_DISABLED_RUN_COMMAND_VAR_2
-->
1M context is turned off here (CLAUDE_CODE_DISABLE_1M_CONTEXT is set), so '${SLASH_COMMAND_MODEL_1M_DISABLED_RUN_COMMAND_VAR_0}' isn't available. Run ${SLASH_COMMAND_MODEL_1M_DISABLED_RUN_COMMAND_VAR_1} ${SLASH_COMMAND_MODEL_1M_DISABLED_RUN_COMMAND_VAR_2} instead.
