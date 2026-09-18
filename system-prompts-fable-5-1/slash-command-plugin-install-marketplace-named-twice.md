<!--
name: 'Slash Command: Plugin Install Marketplace Named Twice'
description: >-
  /plugin install usage error when the plugin name already embeds @marketplace
  and --marketplace is also given.
ccVersion: 2.1.276
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_MARKETPLACE_NAMED_TWICE_VAR_0
-->
Name the marketplace once: <plugin>@<marketplace>, or ${SLASH_COMMAND_PLUGIN_INSTALL_MARKETPLACE_NAMED_TWICE_VAR_0.slice(7)}
