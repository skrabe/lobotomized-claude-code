<!--
name: 'Plugin install: archive missing declared paths'
description: >-
  Install failure when a plugin archive lacks the component paths its
  marketplace entry declares.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_MISSING_DECLARED_PATHS_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_MISSING_DECLARED_PATHS_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_MISSING_DECLARED_PATHS_VAR_2
-->
Plugin archive from ${SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_MISSING_DECLARED_PATHS_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_MISSING_DECLARED_PATHS_VAR_1.url)} does not contain the component paths its marketplace entry declares${SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_MISSING_DECLARED_PATHS_VAR_2}. The archive was not installed. Repackage the zip so the declared paths sit at the plugin root (optionally inside a single wrapper directory), or fix the entry.
