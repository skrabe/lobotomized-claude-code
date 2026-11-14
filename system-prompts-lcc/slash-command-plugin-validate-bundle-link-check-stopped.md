<!--
name: 'Plugin validate: link check stopped'
description: >-
  Plugin validate message when the link check of the MCP bundles folder stopped
  at its entry or problem cap.
ccVersion: 2.1.325
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_LINK_CHECK_STOPPED_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_LINK_CHECK_STOPPED_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_LINK_CHECK_STOPPED_VAR_2
  - SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_LINK_CHECK_STOPPED_VAR_3
-->
The check of ${SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_LINK_CHECK_STOPPED_VAR_0} stopped at ${SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_LINK_CHECK_STOPPED_VAR_1}: it looks at ${SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_LINK_CHECK_STOPPED_VAR_2} entries and lists ${SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_LINK_CHECK_STOPPED_VAR_3} problems at most, so the rest was not checked. Claude Code may unpack the plugin's MCP bundles through a link there and write outside the plugin. Delete ${SLASH_COMMAND_PLUGIN_VALIDATE_BUNDLE_LINK_CHECK_STOPPED_VAR_0}; Claude Code unpacks what it needs again.
