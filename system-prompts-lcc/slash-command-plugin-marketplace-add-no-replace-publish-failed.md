<!--
name: '/plugin marketplace add: no-replace publish failed'
description: >-
  Error when a marketplace add that never replaces the cache fails to cache the
  marketplace
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_NO_REPLACE_PUBLISH_FAILED_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_NO_REPLACE_PUBLISH_FAILED_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_NO_REPLACE_PUBLISH_FAILED_VAR_2
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_NO_REPLACE_PUBLISH_FAILED_VAR_3
-->
Marketplace ${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_NO_REPLACE_PUBLISH_FAILED_VAR_0(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_NO_REPLACE_PUBLISH_FAILED_VAR_1.name)} was not added: this add never replaces what is cached at ${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_NO_REPLACE_PUBLISH_FAILED_VAR_2}, and caching it there failed. If a marketplace of that name is added, remove it first with /plugin marketplace remove ${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_NO_REPLACE_PUBLISH_FAILED_VAR_1.name}; if none is, delete that path and try again.

Technical details: ${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_NO_REPLACE_PUBLISH_FAILED_VAR_3}
