<!--
name: >-
  Slash Command: /plugin Uninstall Note — Still Switched On, Nothing Saved
  Removed
description: >-
  Uninstall note saying the plugin is still switched on in the listed settings,
  so nothing it saved was removed, with how to finish removal.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_STILL_SWITCHED_ON_VAR_0
  - SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_STILL_SWITCHED_ON_VAR_1
  - SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_STILL_SWITCHED_ON_VAR_2
-->
It is still switched on${SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_STILL_SWITCHED_ON_VAR_0.stillOnUnsure?", or may be,":""} in ${SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_STILL_SWITCHED_ON_VAR_0.stillOnIn.join(" and ")}, so nothing it saved was removed${SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_STILL_SWITCHED_ON_VAR_1}. ${SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_STILL_SWITCHED_ON_VAR_0.stillOnProjectFile?"To remove it there too":SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_STILL_SWITCHED_ON_VAR_0.stillOnNotReadHere?"Once this workspace is trusted and Claude Code has been started again":"Once it is switched off there"}, ${SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_STILL_SWITCHED_ON_VAR_2}.
