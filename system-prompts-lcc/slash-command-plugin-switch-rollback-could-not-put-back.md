<!--
name: 'Slash Command: /plugin Switch Rollback — Could Not Be Put Back'
description: >-
  Sentence in the switch failure message listing what could not be put back
  after a rollback, with an optional note about other uninstalled plugins' saved
  settings.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_COULD_NOT_PUT_BACK_VAR_0
  - SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_COULD_NOT_PUT_BACK_VAR_1
  - SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_COULD_NOT_PUT_BACK_VAR_2
  - SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_COULD_NOT_PUT_BACK_VAR_3
  - SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_COULD_NOT_PUT_BACK_VAR_4
-->
 Could not be put back: ${SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_COULD_NOT_PUT_BACK_VAR_0.format(SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_COULD_NOT_PUT_BACK_VAR_1)}.${SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_COULD_NOT_PUT_BACK_VAR_2.length>0?` The settings and stored secrets saved for ${SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_COULD_NOT_PUT_BACK_VAR_3} did not come back either: ${SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_COULD_NOT_PUT_BACK_VAR_4}.`:""}
