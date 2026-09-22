<!--
name: 'Slash Command: /plugin validate — duplicate hooks modules'
description: >-
  Validation error when both the plugin and a nested hooks.json each name a
  hooks module, so the loader refuses both.
ccVersion: 2.1.246
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULES_DUPLICATE_VAR_0
-->
The plugin names one hooks module per plugin, but ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULES_DUPLICATE_VAR_0.join(" and ")} each name one; the loader refuses both
