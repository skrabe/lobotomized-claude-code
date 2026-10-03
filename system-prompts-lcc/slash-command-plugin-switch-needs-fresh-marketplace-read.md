<!--
name: 'Slash Command: Plugin switch needs fresh marketplace read'
description: >-
  Refusal from the plugin switch flow when it needs a fresh read of the
  marketplace listing rather than the saved copy and that read failed, saying
  nothing was changed.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_SWITCH_NEEDS_FRESH_MARKETPLACE_READ_VAR_0
  - SLASH_COMMAND_PLUGIN_SWITCH_NEEDS_FRESH_MARKETPLACE_READ_VAR_1
  - SLASH_COMMAND_PLUGIN_SWITCH_NEEDS_FRESH_MARKETPLACE_READ_VAR_2
-->
A switch needs a fresh read of the ${SLASH_COMMAND_PLUGIN_SWITCH_NEEDS_FRESH_MARKETPLACE_READ_VAR_0}, not the copy saved on this machine, and it could not be read: ${SLASH_COMMAND_PLUGIN_SWITCH_NEEDS_FRESH_MARKETPLACE_READ_VAR_1(SLASH_COMMAND_PLUGIN_SWITCH_NEEDS_FRESH_MARKETPLACE_READ_VAR_2,200)}. Nothing was changed; try again once it can be read
