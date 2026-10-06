<!--
name: 'Slash command: /plugin marketplace add git URL backslash'
description: Refusal when an http(s) git URL has a backslash before the first slash.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_BACKSLASH_AUTHORITY_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_BACKSLASH_AUTHORITY_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_BACKSLASH_AUTHORITY_VAR_2
-->
Invalid git URL: ${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_BACKSLASH_AUTHORITY_VAR_0(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_BACKSLASH_AUTHORITY_VAR_1(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_BACKSLASH_AUTHORITY_VAR_2))} — a backslash before the first "/" can make git connect to a different server than this address names. Remove it, or write it as %5C if it is part of a user name.
