<!--
name: 'Plugin marketplace: withdraw held, install records unreadable'
description: >-
  Error when installed_plugins.json cannot be read so a marketplace's plugins
  cannot be withdrawn.
ccVersion: 2.1.322
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_WITHDRAW_INSTALL_RECORDS_UNREADABLE_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_WITHDRAW_INSTALL_RECORDS_UNREADABLE_VAR_1
-->
The list of installed plugins (installed_plugins.json) could not be read, so the plugins of marketplace ${SLASH_COMMAND_PLUGIN_MARKETPLACE_WITHDRAW_INSTALL_RECORDS_UNREADABLE_VAR_0(SLASH_COMMAND_PLUGIN_MARKETPLACE_WITHDRAW_INSTALL_RECORDS_UNREADABLE_VAR_1)} cannot be withdrawn. Repair or restore that file and try again.
