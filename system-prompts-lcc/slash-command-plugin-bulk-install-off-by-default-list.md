<!--
name: 'Slash Command: /plugin bulk install — off-by-default list'
description: >-
  Bulk-install note listing installed plugins that are off by default and can be
  turned on in /plugin.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_PLUGIN_BULK_INSTALL_OFF_BY_DEFAULT_LIST_VAR_0
-->
 Off by default (turn on in /plugin): ${SLASH_COMMAND_PLUGIN_BULK_INSTALL_OFF_BY_DEFAULT_LIST_VAR_0.join(", ")}.
