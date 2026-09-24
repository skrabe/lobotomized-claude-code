<!--
name: 'Slash Command: /model 1M disabled (switch wording)'
description: >-
  /model result when a [1m] alias is picked but CLAUDE_CODE_DISABLE_1M_CONTEXT
  is set, telling the model to switch to the standard alias instead (wording
  used where no /model command name is shown).
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_MODEL_1M_DISABLED_SWITCH_TO_VAR_0
  - SLASH_COMMAND_MODEL_1M_DISABLED_SWITCH_TO_VAR_1
-->
1M context is turned off (CLAUDE_CODE_DISABLE_1M_CONTEXT is set), so '${SLASH_COMMAND_MODEL_1M_DISABLED_SWITCH_TO_VAR_0}' isn’t available. Switch to ${SLASH_COMMAND_MODEL_1M_DISABLED_SWITCH_TO_VAR_1} instead.
