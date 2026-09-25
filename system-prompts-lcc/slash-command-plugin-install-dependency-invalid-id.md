<!--
name: 'Slash Command: Plugin Install — Dependency Has Invalid Id'
description: >-
  Install refusal when the requested plugin depends on a plugin whose id is
  invalid, followed by the reason the id is invalid.
ccVersion: 2.1.282
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_DEPENDENCY_INVALID_ID_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_DEPENDENCY_INVALID_ID_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_DEPENDENCY_INVALID_ID_VAR_2
  - SLASH_COMMAND_PLUGIN_INSTALL_DEPENDENCY_INVALID_ID_VAR_3
-->
Plugin "${SLASH_COMMAND_PLUGIN_INSTALL_DEPENDENCY_INVALID_ID_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_DEPENDENCY_INVALID_ID_VAR_1)}" cannot be installed, because it depends on "${SLASH_COMMAND_PLUGIN_INSTALL_DEPENDENCY_INVALID_ID_VAR_2}", whose id is invalid: ${SLASH_COMMAND_PLUGIN_INSTALL_DEPENDENCY_INVALID_ID_VAR_3}
