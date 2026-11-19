<!--
name: 'Slash Command: /plugin discover — already installed (changed)'
description: >-
  Result when a discovered plugin is already installed and was re-resolved, with
  a suffix and optional couldn't-load note.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_PLUGIN_DISCOVER_ALREADY_INSTALLED_UPDATED_VAR_0
  - SLASH_COMMAND_PLUGIN_DISCOVER_ALREADY_INSTALLED_UPDATED_VAR_1
  - SLASH_COMMAND_PLUGIN_DISCOVER_ALREADY_INSTALLED_UPDATED_VAR_2
-->
Plugin "${SLASH_COMMAND_PLUGIN_DISCOVER_ALREADY_INSTALLED_UPDATED_VAR_0.pluginId}" is already installed${SLASH_COMMAND_PLUGIN_DISCOVER_ALREADY_INSTALLED_UPDATED_VAR_1.suffix}${SLASH_COMMAND_PLUGIN_DISCOVER_ALREADY_INSTALLED_UPDATED_VAR_2==="load-failed"?". The plugin couldn't load. See /plugin for details.":""}
