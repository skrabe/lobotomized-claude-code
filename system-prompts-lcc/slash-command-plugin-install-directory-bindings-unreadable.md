<!--
name: 'Plugin Install: Directory Bindings Unreadable'
description: >-
  Install refusal when plugin-directory-bindings.json could not be used
  (unreadable, symlink, over 1 MB, damaged or from a newer Claude Code), so the
  directory listing could not be checked against the repository the plugin was
  installed from.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_BINDINGS_UNREADABLE_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_BINDINGS_UNREADABLE_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_BINDINGS_UNREADABLE_VAR_2
-->
"${SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_BINDINGS_UNREADABLE_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_BINDINGS_UNREADABLE_VAR_1.name,120)}" was not installed: plugin-directory-bindings.json in the plugins folder could not be used (unreadable, a symbolic link or not a file, over 1 MB, damaged, or written by a newer Claude Code), so its ${SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_BINDINGS_UNREADABLE_VAR_2} listing could not be checked against the repository it was installed from. Nothing was changed. Try again; if this repeats, check the file for those causes.
