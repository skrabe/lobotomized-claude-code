<!--
name: 'Slash Command: /plugin marketplace list — load failed'
description: >-
  Tells the model the marketplace registry could not be read, so an empty result
  must not be read as 'no marketplaces'.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_LIST_LOAD_ERROR_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_LIST_LOAD_ERROR_VAR_1
-->
Error loading marketplaces: ${SLASH_COMMAND_PLUGIN_MARKETPLACE_LIST_LOAD_ERROR_VAR_0(SLASH_COMMAND_PLUGIN_MARKETPLACE_LIST_LOAD_ERROR_VAR_1)}
