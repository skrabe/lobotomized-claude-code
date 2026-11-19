<!--
name: 'Slash Command: /plugin browse — already installed (changed)'
description: >-
  Result when browsing a marketplace for a plugin that is already installed and
  was re-resolved, with a suffix and optional couldn't-load note.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_PLUGIN_BROWSE_ALREADY_INSTALLED_UPDATED_VAR_0
  - SLASH_COMMAND_PLUGIN_BROWSE_ALREADY_INSTALLED_UPDATED_VAR_1
  - SLASH_COMMAND_PLUGIN_BROWSE_ALREADY_INSTALLED_UPDATED_VAR_2
-->
Plugin "${SLASH_COMMAND_PLUGIN_BROWSE_ALREADY_INSTALLED_UPDATED_VAR_0}" is already installed${SLASH_COMMAND_PLUGIN_BROWSE_ALREADY_INSTALLED_UPDATED_VAR_1.suffix}${SLASH_COMMAND_PLUGIN_BROWSE_ALREADY_INSTALLED_UPDATED_VAR_2==="load-failed"?". The plugin couldn't load. See /plugin for details.":""}
