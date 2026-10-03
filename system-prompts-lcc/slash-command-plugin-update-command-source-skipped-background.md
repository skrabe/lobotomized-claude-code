<!--
name: 'Plugin update: command-source skipped by background update'
description: >-
  Explains that a command-installed plugin is not updated by the background
  marketplace update, and points to /plugin update or automatic per-session
  re-resolve instead.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_SKIPPED_BACKGROUND_VAR_0
  - SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_SKIPPED_BACKGROUND_VAR_1
  - SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_SKIPPED_BACKGROUND_VAR_2
  - SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_SKIPPED_BACKGROUND_VAR_3
-->
${SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_SKIPPED_BACKGROUND_VAR_0(SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_SKIPPED_BACKGROUND_VAR_1,200)} is installed by running a command, which the background marketplace update never runs; it is left to the per-session re-resolve (when that is enabled) or an explicit update — ${SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_SKIPPED_BACKGROUND_VAR_2("plugin update",SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_SKIPPED_BACKGROUND_VAR_3,{extra:ve,fallback:"a per-plugin update reviews it"})}.
