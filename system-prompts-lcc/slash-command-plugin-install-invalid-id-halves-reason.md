<!--
name: 'Slash Command: Plugin install invalid id halves reason'
description: >-
  Explains why a plugin id cannot be installed: each half of plugin@marketplace
  must start with a letter or digit and use only letters, digits, '-', '.' and
  '_', naming which half fails and who can rename it
ccVersion: 2.1.282
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_HALVES_REASON_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_HALVES_REASON_VAR_1
-->
each half of a plugin id (plugin@marketplace) must begin with a letter or digit and hold only letters, digits, "-", "." and "_". Here ${SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_HALVES_REASON_VAR_0&&!SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_HALVES_REASON_VAR_1?"the marketplace's name does not":!SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_HALVES_REASON_VAR_0&&SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_HALVES_REASON_VAR_1?"the plugin's name does not":"they do not"}; the marketplace's maintainer can rename ${SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_HALVES_REASON_VAR_0||SLASH_COMMAND_PLUGIN_INSTALL_INVALID_ID_HALVES_REASON_VAR_1?"it":"both"}.
