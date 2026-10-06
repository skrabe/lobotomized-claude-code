<!--
name: '/plugin marketplace: finalize cache failed'
description: >-
  Error when the marketplace cache directory holding the catalog name cannot be
  removed
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_FINALIZE_CACHE_FAILED_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_FINALIZE_CACHE_FAILED_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_FINALIZE_CACHE_FAILED_VAR_2
-->
Failed to finalize marketplace cache. Please manually delete the directory at ${SLASH_COMMAND_PLUGIN_MARKETPLACE_FINALIZE_CACHE_FAILED_VAR_0} if it exists and try again.

Technical details: ${SLASH_COMMAND_PLUGIN_MARKETPLACE_FINALIZE_CACHE_FAILED_VAR_1(SLASH_COMMAND_PLUGIN_MARKETPLACE_FINALIZE_CACHE_FAILED_VAR_2)}
