<!--
name: '/plugin marketplace add: reserved claude.ai prefix'
description: >-
  Refusal to add a marketplace whose name starts with the prefix reserved for
  claude.ai-hosted marketplaces
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_RESERVED_CLAUDEAI_PREFIX_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_RESERVED_CLAUDEAI_PREFIX_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_RESERVED_CLAUDEAI_PREFIX_VAR_2
-->
Cannot add marketplace ${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_RESERVED_CLAUDEAI_PREFIX_VAR_0(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_RESERVED_CLAUDEAI_PREFIX_VAR_1)}: names starting with "${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_RESERVED_CLAUDEAI_PREFIX_VAR_2}" are reserved for marketplaces hosted on claude.ai (claude plugin marketplace add --claudeai <name>).
