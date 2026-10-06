<!--
name: '/plugin marketplace: URL connection failed'
description: >-
  Error when a URL marketplace cannot be downloaded because the host refused or
  was not found
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_CONNECT_FAILED_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_CONNECT_FAILED_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_CONNECT_FAILED_VAR_2
-->
Could not connect to ${SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_CONNECT_FAILED_VAR_0}. Please check your internet connection and verify the URL is correct.

Technical details: ${SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_CONNECT_FAILED_VAR_1(SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_CONNECT_FAILED_VAR_2.message)}
