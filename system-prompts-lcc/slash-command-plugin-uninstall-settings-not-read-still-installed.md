<!--
name: 'Plugin Uninstall: Settings Source Not Read, Still Installed'
description: >-
  Uninstall refusal from Dt() when a settings source is not read here or sits on
  a network path, so it may still switch the plugin on; the plugin stays
  installed, and the closing advice depends on why the file was not read.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_0
  - SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_1
  - SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_2
  - SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_3
  - SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_4
-->
"${SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_0}" was not uninstalled: ${SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_1}, so it may still switch "${SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_0}" on${SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_2}. It is still installed. ${SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_3==="not-read-here"?"Once that file can be saved, uninstall it again.":SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_4==="vet-network"||SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_4==="suspect-link"||SLASH_COMMAND_PLUGIN_UNINSTALL_SETTINGS_NOT_READ_STILL_INSTALLED_VAR_4==="crossing"?`If that file, its ".claude" folder or a folder above them is a link to another machine, replace the link with a real file or folder, or start Claude Code from the folder's real location. Then uninstall it again.`:"Try uninstalling it again: if the path to that file changed during the check, that will work. If you see this again, the path cannot be checked, and trying again will not help."}
