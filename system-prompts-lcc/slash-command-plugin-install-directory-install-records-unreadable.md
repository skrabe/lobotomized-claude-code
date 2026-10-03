<!--
name: 'Plugin Install: Directory Install Records Unreadable'
description: >-
  Install refusal thrown when installed_plugins.json cannot be read, so Claude
  Code cannot tell whether the plugin is already installed from another
  repository.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_INSTALL_RECORDS_UNREADABLE_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_INSTALL_RECORDS_UNREADABLE_VAR_1
-->
"${SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_INSTALL_RECORDS_UNREADABLE_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_INSTALL_RECORDS_UNREADABLE_VAR_1.name,120)}" was not installed: installed_plugins.json in the plugins folder could not be read, so Claude Code cannot tell whether it is already installed from another repository. Nothing was changed. Try again once the file can be read.
