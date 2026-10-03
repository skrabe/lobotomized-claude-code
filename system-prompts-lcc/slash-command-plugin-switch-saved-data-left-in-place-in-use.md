<!--
name: >-
  Slash Command: /plugin Switch Note — Saved Data Left In Place (In Use Or List
  Unreadable)
description: >-
  Sentence in the switch success note saying an old plugin's saved data was left
  in place because the installed list could not be read or another plugin uses
  it.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_SWITCH_SAVED_DATA_LEFT_IN_PLACE_IN_USE_VAR_0
  - SLASH_COMMAND_PLUGIN_SWITCH_SAVED_DATA_LEFT_IN_PLACE_IN_USE_VAR_1
  - SLASH_COMMAND_PLUGIN_SWITCH_SAVED_DATA_LEFT_IN_PLACE_IN_USE_VAR_2
-->
. The saved data of ${SLASH_COMMAND_PLUGIN_SWITCH_SAVED_DATA_LEFT_IN_PLACE_IN_USE_VAR_0(SLASH_COMMAND_PLUGIN_SWITCH_SAVED_DATA_LEFT_IN_PLACE_IN_USE_VAR_1.pluginId)} was left in place because ${SLASH_COMMAND_PLUGIN_SWITCH_SAVED_DATA_LEFT_IN_PLACE_IN_USE_VAR_2===void 0?"the list of installed plugins could not be read":`${SLASH_COMMAND_PLUGIN_SWITCH_SAVED_DATA_LEFT_IN_PLACE_IN_USE_VAR_0(SLASH_COMMAND_PLUGIN_SWITCH_SAVED_DATA_LEFT_IN_PLACE_IN_USE_VAR_2)} is installed and uses it`}
