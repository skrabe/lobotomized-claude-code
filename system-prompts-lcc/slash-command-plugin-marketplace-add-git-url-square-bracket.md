<!--
name: 'Slash command: /plugin marketplace add git URL square bracket'
description: >-
  Refusal when a marketplace git URL contains square brackets git could read as
  a host or path boundary.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_SQUARE_BRACKET_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_SQUARE_BRACKET_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_SQUARE_BRACKET_VAR_2
-->
Invalid git URL: ${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_SQUARE_BRACKET_VAR_0(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_SQUARE_BRACKET_VAR_1(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_GIT_URL_SQUARE_BRACKET_VAR_2))} — git can read a square bracket (also written %5B or %5D) as marking a server name or where a local path starts, so it could connect to a different server or open a different folder than this address names. In a server address, brackets may only surround an IPv6 address, as in git@[2001:db8::1]:repo.git. Remove them, or rename the folder whose name has them.
