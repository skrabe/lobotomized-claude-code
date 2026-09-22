<!--
name: 'Plugin Validate: HeadersHelper Requires Strict False'
description: >-
  Validation error that a headersHelper entry must inline its manifest with
  strict false; included in /plugin validate onComplete output.
ccVersion: 2.1.238
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HEADERS_HELPER_NOT_STRICT_FALSE_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HEADERS_HELPER_NOT_STRICT_FALSE_VAR_1
-->
Plugin "${SLASH_COMMAND_PLUGIN_VALIDATE_HEADERS_HELPER_NOT_STRICT_FALSE_VAR_0(SLASH_COMMAND_PLUGIN_VALIDATE_HEADERS_HELPER_NOT_STRICT_FALSE_VAR_1.name)}" sets headersHelper but is not "strict": false. An entry with headersHelper must inline its full manifest (strict: false, with commands/agents/hooks/mcpServers declared in the entry) so users can review what it ships before the command runs; Claude Code refuses to run the helper otherwise.
