<!--
name: 'Slash command: plugin claude.ai marketplace refresh failed'
description: >-
  Note that a claude.ai-hosted marketplace was not refreshed, with the status
  reason.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_CLAUDEAI_REFRESH_FAILED_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_CLAUDEAI_REFRESH_FAILED_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_CLAUDEAI_REFRESH_FAILED_VAR_2
-->
Marketplace "${SLASH_COMMAND_PLUGIN_MARKETPLACE_CLAUDEAI_REFRESH_FAILED_VAR_0}" was not refreshed: ${SLASH_COMMAND_PLUGIN_MARKETPLACE_CLAUDEAI_REFRESH_FAILED_VAR_1(SLASH_COMMAND_PLUGIN_MARKETPLACE_CLAUDEAI_REFRESH_FAILED_VAR_2.status)??"claude.ai did not serve its plugins"}
