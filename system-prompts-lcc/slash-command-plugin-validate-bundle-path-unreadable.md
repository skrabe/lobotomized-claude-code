<!--
name: 'Plugin validate: path unreadable'
description: >-
  Plugin validate message that a path could not be read so it was not checked
  for links.
ccVersion: 2.1.325
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_PATH_UNREADABLE_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_PATH_UNREADABLE_VAR_1
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_PATH_UNREADABLE_VAR_0} could not be read, so it was not checked for a link at ${SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_PATH_UNREADABLE_VAR_1} or inside it. Claude Code may unpack the plugin's MCP bundles through a link there and write outside the plugin. Make it readable, or delete ${SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_PATH_UNREADABLE_VAR_1}.
