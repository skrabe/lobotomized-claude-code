<!--
name: 'Slash Command: /plugin Switch Note — Another Plugin Line Entry'
description: >-
  Entry in the switch note naming an enabledPlugins line that may belong to
  another installed plugin, with its settings source.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_SWITCH_OTHER_PLUGIN_LINE_ENTRY_VAR_0
  - SLASH_COMMAND_PLUGIN_SWITCH_OTHER_PLUGIN_LINE_ENTRY_VAR_1
  - SLASH_COMMAND_PLUGIN_SWITCH_OTHER_PLUGIN_LINE_ENTRY_VAR_2
  - SLASH_COMMAND_PLUGIN_SWITCH_OTHER_PLUGIN_LINE_ENTRY_VAR_3
-->
${SLASH_COMMAND_PLUGIN_SWITCH_OTHER_PLUGIN_LINE_ENTRY_VAR_0(SLASH_COMMAND_PLUGIN_SWITCH_OTHER_PLUGIN_LINE_ENTRY_VAR_1)} (${SLASH_COMMAND_PLUGIN_SWITCH_OTHER_PLUGIN_LINE_ENTRY_VAR_2}; it may be another installed plugin's own line${SLASH_COMMAND_PLUGIN_SWITCH_OTHER_PLUGIN_LINE_ENTRY_VAR_3==="userSettings"?"":": the list of installed plugins could not be read"})
