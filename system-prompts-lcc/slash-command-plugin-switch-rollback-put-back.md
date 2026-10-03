<!--
name: 'Slash Command: /plugin Switch Rollback — Uninstalled Copies Put Back'
description: >-
  Sentence in the switch failure message saying what had been uninstalled was
  put back, optionally except the saved settings of other plugins.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_PUT_BACK_VAR_0
  - SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_PUT_BACK_VAR_1
  - SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_PUT_BACK_VAR_2
-->
 What had been uninstalled was put back${SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_PUT_BACK_VAR_0.length>0?`, except the settings and stored secrets saved for ${SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_PUT_BACK_VAR_1}: ${SLASH_COMMAND_PLUGIN_SWITCH_ROLLBACK_PUT_BACK_VAR_2}`:""}.
