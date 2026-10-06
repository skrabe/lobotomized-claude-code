<!--
name: '/plugin marketplace: staging cleanup failed'
description: >-
  Error when a leftover marketplace staging directory cannot be removed before
  fetching
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_STAGING_CLEANUP_FAILED_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_STAGING_CLEANUP_FAILED_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_STAGING_CLEANUP_FAILED_VAR_2
-->
Failed to clean up a leftover marketplace staging directory. Please manually delete the directory at ${SLASH_COMMAND_PLUGIN_MARKETPLACE_STAGING_CLEANUP_FAILED_VAR_0} and try again.

Technical details: ${SLASH_COMMAND_PLUGIN_MARKETPLACE_STAGING_CLEANUP_FAILED_VAR_1(SLASH_COMMAND_PLUGIN_MARKETPLACE_STAGING_CLEANUP_FAILED_VAR_2)}
