<!--
name: 'Slash Command: Plugin Marketplace Remove Plugins Turned Off Catalog Unreadable'
description: >-
  Result note after removing a marketplace entry: names the plugins turned off
  because they could not be checked against the built-in marketplace's listed
  commit, and how to reinstate one once it is available.
ccVersion: 2.1.288
variables:
  - >-
    SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_CATALOG_UNREADABLE_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_CATALOG_UNREADABLE_VAR_1
  - >-
    SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_CATALOG_UNREADABLE_VAR_2
-->
Turned off ${SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_CATALOG_UNREADABLE_VAR_0}: they could not be checked against the commit the ${SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_CATALOG_UNREADABLE_VAR_1} lists. To use one again once the ${SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_CATALOG_UNREADABLE_VAR_1} is available: claude plugin update <id>, then claude plugin enable <id>.${SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_CATALOG_UNREADABLE_VAR_2}
