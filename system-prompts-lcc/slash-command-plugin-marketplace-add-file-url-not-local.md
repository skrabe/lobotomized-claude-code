<!--
name: 'Slash command: /plugin marketplace add file URL not local'
description: >-
  Refusal when a file: git URL names a host or network path instead of a local
  path.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_FILE_URL_NOT_LOCAL_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_FILE_URL_NOT_LOCAL_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_FILE_URL_NOT_LOCAL_VAR_2
-->
Refusing git URL ${SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_FILE_URL_NOT_LOCAL_VAR_0(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_FILE_URL_NOT_LOCAL_VAR_1(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_FILE_URL_NOT_LOCAL_VAR_2))}: a file: URL must name a local path (no host, no network-shaped path).${/^file:\/\/[a-z]:/i.test(SLASH_COMMAND_PLUGIN_MARKETPLACE_ADD_FILE_URL_NOT_LOCAL_VAR_2)?" A drive letter such as C: counts as a local path only on Windows.":""}
