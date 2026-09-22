<!--
name: 'Slash Command: Cloud Plugins Save Failed'
description: >-
  local-jsx /cloud-plugins onDone stdout when the consent choice could not be
  written, wrapped as a user API message.
ccVersion: 2.1.246
variables:
  - SLASH_COMMAND_CLOUD_PLUGINS_SAVE_FAILED_VAR_0
  - SLASH_COMMAND_CLOUD_PLUGINS_SAVE_FAILED_VAR_1
  - SLASH_COMMAND_CLOUD_PLUGINS_SAVE_FAILED_VAR_2
-->
Couldn’t save that: ${SLASH_COMMAND_CLOUD_PLUGINS_SAVE_FAILED_VAR_0(SLASH_COMMAND_CLOUD_PLUGINS_SAVE_FAILED_VAR_1())} could not be written, so nothing changed — ${SLASH_COMMAND_CLOUD_PLUGINS_SAVE_FAILED_VAR_2}. Check that the folder is writable, then run /cloud-plugins again.
