<!--
name: '/plugin install: plugin tree not symlink-free'
description: >-
  Install refusal when the plugin tree could not be made symlink-free before
  caching.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_TREE_NOT_SYMLINK_FREE_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_TREE_NOT_SYMLINK_FREE_VAR_1
-->
Plugin tree at ${SLASH_COMMAND_PLUGIN_INSTALL_TREE_NOT_SYMLINK_FREE_VAR_0} could not be made symlink-free (${SLASH_COMMAND_PLUGIN_INSTALL_TREE_NOT_SYMLINK_FREE_VAR_1.readOnly?"not writable":`${SLASH_COMMAND_PLUGIN_INSTALL_TREE_NOT_SYMLINK_FREE_VAR_1.failed} failed`}); refusing to cache it
