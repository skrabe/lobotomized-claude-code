<!--
name: 'Slash command: /plugin marketplace add git URL %00'
description: Refusal when a marketplace git URL contains %00.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_PERCENT_00_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_PERCENT_00_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_PERCENT_00_VAR_2
-->
Invalid git URL: ${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_PERCENT_00_VAR_0(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_PERCENT_00_VAR_1(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_PERCENT_00_VAR_2))} — "%00" in a git address means different things to different versions of git, so it is not allowed. Remove it.
