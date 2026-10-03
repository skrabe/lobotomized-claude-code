<!--
name: 'Slash Command: /plugin install — Switch, enabledPlugins Lines Still Present'
description: >-
  Switch-install note listing 'enabledPlugins' entries that are still present in
  settings and must be removed, because an old copy could load again beside the
  new one or show as enabled but not installed.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_LINES_REMAINING_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_LINES_REMAINING_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_LINES_REMAINING_VAR_2
-->
. Still listed under "enabledPlugins": ${SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_LINES_REMAINING_VAR_0.format(SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_LINES_REMAINING_VAR_1)}. Until ${SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_LINES_REMAINING_VAR_1.length===1?"that line is":"those lines are"} removed, an old copy can load again beside ${SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_LINES_REMAINING_VAR_2} or show as enabled but not installed
