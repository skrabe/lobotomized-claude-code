<!--
name: 'Slash Command: Plugin install — commit unverifiable in this build'
description: >-
  Plugin install, update or load refusal saying the plugin was not installed or
  updated because this build of Claude Code cannot verify it, or the commit it
  was installed at.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_COMMIT_UNVERIFIABLE_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_COMMIT_UNVERIFIABLE_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_COMMIT_UNVERIFIABLE_VAR_2
-->
"${SLASH_COMMAND_PLUGIN_INSTALL_COMMIT_UNVERIFIABLE_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_COMMIT_UNVERIFIABLE_VAR_1,120)}" was not ${SLASH_COMMAND_PLUGIN_INSTALL_COMMIT_UNVERIFIABLE_VAR_2}: this build of Claude Code cannot verify ${SLASH_COMMAND_PLUGIN_INSTALL_COMMIT_UNVERIFIABLE_VAR_2==="installed"?"it":"the commit it was installed at"}.
