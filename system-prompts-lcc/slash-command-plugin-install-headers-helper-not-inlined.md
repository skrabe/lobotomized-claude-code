<!--
name: 'Slash Command: /plugin install headersHelper entry not inlined'
description: >-
  Install refusal when a plugin entry declares a headersHelper but is not
  strict:false, so its manifest cannot be reviewed before the command runs.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_HEADERS_HELPER_NOT_INLINED_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_HEADERS_HELPER_NOT_INLINED_VAR_1
-->
Plugin "${SLASH_COMMAND_PLUGIN_INSTALL_HEADERS_HELPER_NOT_INLINED_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_HEADERS_HELPER_NOT_INLINED_VAR_1.pluginName)}" declares a headersHelper but is not strict:false — an entry with headersHelper must inline its manifest so its capabilities can be reviewed before the command runs.
