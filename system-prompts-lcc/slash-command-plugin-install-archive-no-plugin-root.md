<!--
name: 'Plugin install: archive has no plugin root'
description: >-
  Install failure when a plugin archive has no recognizable plugin content at
  its root.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_NO_PLUGIN_ROOT_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_NO_PLUGIN_ROOT_VAR_1
-->
Plugin archive from ${SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_NO_PLUGIN_ROOT_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_NO_PLUGIN_ROOT_VAR_1.url)} has no plugin content at its root (expected .claude-plugin/ or a commands/, skills/, agents/, hooks/, themes/, output-styles/, monitors/, workflows/, SKILL.md, .mcp.json, or .lsp.json at the top level, optionally inside a single wrapper directory). The archive was not installed.
