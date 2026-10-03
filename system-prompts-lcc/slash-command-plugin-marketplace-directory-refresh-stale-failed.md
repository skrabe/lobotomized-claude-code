<!--
name: 'Slash Command: Plugin Directory Marketplace Refresh Served Stale'
description: >-
  Error that the Anthropic Directory marketplace could not be refreshed, with
  the staleness reason. It appears as a marketplace-not-refreshed note or a
  could-not-check failure in plugin update and install results.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_DIRECTORY_REFRESH_STALE_FAILED_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_DIRECTORY_REFRESH_STALE_FAILED_VAR_1
-->
${SLASH_COMMAND_PLUGIN_MARKETPLACE_DIRECTORY_REFRESH_STALE_FAILED_VAR_0} could not be refreshed: ${SLASH_COMMAND_PLUGIN_MARKETPLACE_DIRECTORY_REFRESH_STALE_FAILED_VAR_1.staleReason}
