<!--
name: 'Slash command: plugin install marketplace folder unconfirmed'
description: >-
  Plugin install refusal when Claude Code cannot confirm the plugin folder is
  inside its marketplace.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_MARKETPLACE_FOLDER_UNCONFIRMED_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_MARKETPLACE_FOLDER_UNCONFIRMED_VAR_1
-->
"${SLASH_COMMAND_PLUGIN_INSTALL_MARKETPLACE_FOLDER_UNCONFIRMED_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_MARKETPLACE_FOLDER_UNCONFIRMED_VAR_1.name,120)}" was not installed: Claude Code could not confirm that its folder is inside its marketplace. Nothing was changed. Update the marketplace, or ask its owner to fix the entry.
