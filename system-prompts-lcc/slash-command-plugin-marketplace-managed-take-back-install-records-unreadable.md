<!--
name: 'Plugin marketplace: managed take-back held, install records unreadable'
description: >-
  Error when installed_plugins.json cannot be read so a managed marketplace
  cannot be taken back from another source.
ccVersion: 2.1.322
variables:
  - >-
    SLASH_COMMAND_PLUGIN_MARKETPLACE_MANAGED_TAKE_BACK_INSTALL_RECORDS_UNREADABLE_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_MARKETPLACE_MANAGED_TAKE_BACK_INSTALL_RECORDS_UNREADABLE_VAR_1
-->
The list of installed plugins (installed_plugins.json) could not be read, so marketplace ${SLASH_COMMAND_PLUGIN_MARKETPLACE_MANAGED_TAKE_BACK_INSTALL_RECORDS_UNREADABLE_VAR_0(SLASH_COMMAND_PLUGIN_MARKETPLACE_MANAGED_TAKE_BACK_INSTALL_RECORDS_UNREADABLE_VAR_1.name)}, which managed settings declare, cannot be taken back from another source. Repair or restore that file and try again.
