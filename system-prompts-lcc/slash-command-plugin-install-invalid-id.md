<!--
name: 'Slash Command: Plugin Install — Invalid Plugin Id'
description: >-
  Install refusal when the plugin's own id is invalid, followed by the reason
  the id is invalid.
ccVersion: 2.1.282
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_VAR_1
-->
Plugin "${SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_VAR_0}" cannot be installed, because its id is invalid: ${SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_VAR_1}
