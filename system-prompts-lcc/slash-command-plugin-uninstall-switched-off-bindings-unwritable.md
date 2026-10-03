<!--
name: 'Plugin Uninstall: Switched Off But Directory Bindings Unwritable'
description: >-
  Uninstall refusal when the plugin was only switched off at a scope, with
  nothing it saved removed, because plugin-directory-bindings.json could not be
  used or written; tells the user to uninstall again once the file can be
  written.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UNINSTALL_SWITCHED_OFF_BINDINGS_UNWRITABLE_VAR_0
  - SLASH_COMMAND_PLUGIN_UNINSTALL_SWITCHED_OFF_BINDINGS_UNWRITABLE_VAR_1
  - SLASH_COMMAND_PLUGIN_UNINSTALL_SWITCHED_OFF_BINDINGS_UNWRITABLE_VAR_2
-->
"${SLASH_COMMAND_PLUGIN_UNINSTALL_SWITCHED_OFF_BINDINGS_UNWRITABLE_VAR_0(SLASH_COMMAND_PLUGIN_UNINSTALL_SWITCHED_OFF_BINDINGS_UNWRITABLE_VAR_1)}" was switched off at ${SLASH_COMMAND_PLUGIN_UNINSTALL_SWITCHED_OFF_BINDINGS_UNWRITABLE_VAR_2} scope but not uninstalled, and nothing it saved was removed: plugin-directory-bindings.json in the plugins folder could not be used or written (unreadable, a symbolic link or not a file, over 1 MB, damaged, written by a newer Claude Code, or not writable), so nothing would keep the name for the repository it was installed from. Once the file can be written, uninstall it again.
