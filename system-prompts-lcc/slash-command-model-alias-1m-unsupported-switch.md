<!--
name: 'Slash Command: /model 1M alias unsupported (switch wording)'
description: >-
  /model rejection when the requested [1m] alias's model has no 1M context
  window. This variant, used where there is no slash command (hie returns
  undefined), says 'switch to'.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_MODEL_ALIAS_1M_UNSUPPORTED_SWITCH_VAR_0
  - SLASH_COMMAND_MODEL_ALIAS_1M_UNSUPPORTED_SWITCH_VAR_1
  - SLASH_COMMAND_MODEL_ALIAS_1M_UNSUPPORTED_SWITCH_VAR_2
  - SLASH_COMMAND_MODEL_ALIAS_1M_UNSUPPORTED_SWITCH_VAR_3
-->
${SLASH_COMMAND_MODEL_ALIAS_1M_UNSUPPORTED_SWITCH_VAR_0(SLASH_COMMAND_MODEL_ALIAS_1M_UNSUPPORTED_SWITCH_VAR_1.carrier)} doesn’t have a 1M context window, so '${SLASH_COMMAND_MODEL_ALIAS_1M_UNSUPPORTED_SWITCH_VAR_2}' isn’t available. Switch to ${SLASH_COMMAND_MODEL_ALIAS_1M_UNSUPPORTED_SWITCH_VAR_3} to use its standard context window.
