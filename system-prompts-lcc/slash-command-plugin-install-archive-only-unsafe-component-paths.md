<!--
name: 'Plugin install: archive entry declares only unsafe paths'
description: >-
  Install failure for an archive plugin whose marketplace entry declares only
  unsafe or malformed component paths.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_ONLY_UNSAFE_COMPONENT_PATHS_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_ONLY_UNSAFE_COMPONENT_PATHS_VAR_1
-->
Plugin archive from ${SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_ONLY_UNSAFE_COMPONENT_PATHS_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_ONLY_UNSAFE_COMPONENT_PATHS_VAR_1.url)} was not installed: its marketplace entry declares only unsafe or malformed component paths. Fix the entry.
