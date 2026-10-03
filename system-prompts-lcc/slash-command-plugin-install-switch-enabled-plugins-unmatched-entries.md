<!--
name: 'Slash Command: /plugin install — Switch, Unmatched enabledPlugins Entries'
description: >-
  Switch-install note listing 'enabledPlugins' entries that may refer to an old
  copy, saying to remove any that do not name an installed plugin, because the
  old copy could load again or show as enabled but not installed.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_UNMATCHED_ENTRIES_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_UNMATCHED_ENTRIES_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_UNMATCHED_ENTRIES_VAR_2
  - SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_UNMATCHED_ENTRIES_VAR_3
  - SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_UNMATCHED_ENTRIES_VAR_4
-->
. Still listed under "enabledPlugins": ${SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_UNMATCHED_ENTRIES_VAR_0.format([...SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_UNMATCHED_ENTRIES_VAR_1.keys()])}. ${SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_UNMATCHED_ENTRIES_VAR_1.size===1?`If ${SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_UNMATCHED_ENTRIES_VAR_2(SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_UNMATCHED_ENTRIES_VAR_3)} does not name a plugin you have installed, that line should be removed`:"Any of these that does not name a plugin you have installed should be removed"}: until then an old copy can load again beside ${SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_ENABLED_PLUGINS_UNMATCHED_ENTRIES_VAR_4} or show as enabled but not installed
