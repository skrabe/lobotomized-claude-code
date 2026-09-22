<!--
name: 'Slash Command: /plugin Marketplace Already Added From Different Source'
description: >-
  Error from /plugin marketplace add when that name is already registered from a
  different source, telling the model to remove it first.
ccVersion: 2.1.276
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_DIFFERENT_SOURCE_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_DIFFERENT_SOURCE_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_DIFFERENT_SOURCE_VAR_2
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_DIFFERENT_SOURCE_VAR_3
-->
Marketplace ${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_DIFFERENT_SOURCE_VAR_0(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_DIFFERENT_SOURCE_VAR_1)} is already added from a different source (${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_DIFFERENT_SOURCE_VAR_2(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_DIFFERENT_SOURCE_VAR_3.source)}). To use this source instead, remove that marketplace first with /plugin marketplace remove ${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_DIFFERENT_SOURCE_VAR_1}.
