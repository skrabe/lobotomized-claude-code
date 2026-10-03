<!--
name: >-
  Slash Command: /plugin uninstall leftover — uninstall again from the command
  line
description: >-
  Fallback remedy in the uninstall-leftover notes when no runnable command can
  be shown: uninstall the plugin again from the command line, with --scope
  project when it is still on in the project file.
ccVersion: 2.1.288
variables:
  - >-
    SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_UNINSTALL_AGAIN_FROM_COMMAND_LINE_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_UNINSTALL_AGAIN_FROM_COMMAND_LINE_VAR_1
-->
uninstall "${SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_UNINSTALL_AGAIN_FROM_COMMAND_LINE_VAR_0(SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_UNINSTALL_AGAIN_FROM_COMMAND_LINE_VAR_1.pluginId,200)}" again from the command line${SLASH_COMMAND_PLUGIN_UNINSTALL_LEFTOVER_UNINSTALL_AGAIN_FROM_COMMAND_LINE_VAR_1.stillOnProjectFile?" with --scope project":""}
