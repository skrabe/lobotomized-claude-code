<!--
name: 'Slash Command: /plugin Switch Item — Enabled Line Not Put Back (Restored Copy)'
description: >-
  List item in the plugin-switch rollback message naming an enabledPlugins
  settings line for a restored old copy that could not be put back, with a note
  when the line that turned it off was left out.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_SWITCH_NOT_PUT_BACK_ENABLED_LINE_RESTORED_COPY_VAR_0
  - SLASH_COMMAND_PLUGIN_SWITCH_NOT_PUT_BACK_ENABLED_LINE_RESTORED_COPY_VAR_1
  - SLASH_COMMAND_PLUGIN_SWITCH_NOT_PUT_BACK_ENABLED_LINE_RESTORED_COPY_VAR_2
-->
the "enabledPlugins" line for ${SLASH_COMMAND_PLUGIN_SWITCH_NOT_PUT_BACK_ENABLED_LINE_RESTORED_COPY_VAR_0(SLASH_COMMAND_PLUGIN_SWITCH_NOT_PUT_BACK_ENABLED_LINE_RESTORED_COPY_VAR_1.copy.pluginId)} in ${SLASH_COMMAND_PLUGIN_SWITCH_NOT_PUT_BACK_ENABLED_LINE_RESTORED_COPY_VAR_1.scope} settings${SLASH_COMMAND_PLUGIN_SWITCH_NOT_PUT_BACK_ENABLED_LINE_RESTORED_COPY_VAR_2.has(SLASH_COMMAND_PLUGIN_SWITCH_NOT_PUT_BACK_ENABLED_LINE_RESTORED_COPY_VAR_1.copy.pluginId)?" (left out, because the line that turned it off could not be put back; if you want it on, enable it in /plugin)":""}
