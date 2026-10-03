<!--
name: '/plugin validate: third-party plugin name restrictions'
description: >-
  Validation rule text telling a plugin author that a third-party plugin name
  may not start with reserved prefixes, equal Anthropic product names, or pair
  official with claude/anthropic.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_PLUGIN_NAME_THIRD_PARTY_RESTRICTIONS_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_PLUGIN_NAME_THIRD_PARTY_RESTRICTIONS_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_PLUGIN_NAME_THIRD_PARTY_RESTRICTIONS_VAR_2
-->
A third party's plugin name cannot start with ${SLASH_COMMAND_PLUGIN_VALIDATE_PLUGIN_NAME_THIRD_PARTY_RESTRICTIONS_VAR_0}, be ${SLASH_COMMAND_PLUGIN_VALIDATE_PLUGIN_NAME_THIRD_PARTY_RESTRICTIONS_VAR_1(SLASH_COMMAND_PLUGIN_VALIDATE_PLUGIN_NAME_THIRD_PARTY_RESTRICTIONS_VAR_2)}, or put "official" beside "claude" or "anthropic".
