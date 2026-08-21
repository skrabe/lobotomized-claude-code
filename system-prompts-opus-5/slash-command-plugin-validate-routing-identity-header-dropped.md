<!--
name: Plugin Validate Routing Identity Header Dropped
description: >-
  Marketplace validation warning that a request-routing/identity header on a
  catalog entry is dropped at download.
ccVersion: 2.1.238
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_ROUTING_IDENTITY_HEADER_DROPPED_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_ROUTING_IDENTITY_HEADER_DROPPED_VAR_1
-->
Header "${SLASH_COMMAND_PLUGIN_VALIDATE_ROUTING_IDENTITY_HEADER_DROPPED_VAR_0(SLASH_COMMAND_PLUGIN_VALIDATE_ROUTING_IDENTITY_HEADER_DROPPED_VAR_1)}" is a request-routing/identity header that catalog entries may not set; Claude Code drops it at download time.
