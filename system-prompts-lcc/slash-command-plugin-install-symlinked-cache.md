<!--
name: 'Slash Command: /plugin Install Refused Through Symlinked Cache'
description: >-
  Tells the model /plugin install cannot write the plugin cache through a
  symbolic link, so the install was refused.
ccVersion: 2.1.237
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_SYMLINKED_CACHE_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_SYMLINKED_CACHE_VAR_1
-->
Cannot install into ${SLASH_COMMAND_PLUGIN_INSTALL_SYMLINKED_CACHE_VAR_0}: ${SLASH_COMMAND_PLUGIN_INSTALL_SYMLINKED_CACHE_VAR_1} is a symbolic link, and the plugin cache is not written through symbolic links
