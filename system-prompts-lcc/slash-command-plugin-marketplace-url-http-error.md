<!--
name: '/plugin marketplace: URL HTTP error'
description: Error when downloading a URL marketplace returns an HTTP error status
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_HTTP_ERROR_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_HTTP_ERROR_VAR_1
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_HTTP_ERROR_VAR_2
-->
HTTP ${SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_HTTP_ERROR_VAR_0.response.status} error while downloading marketplace from ${SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_HTTP_ERROR_VAR_1}. The marketplace file may not exist at this URL.

Technical details: ${SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_HTTP_ERROR_VAR_2(SLASH_COMMAND_PLUGIN_MARKETPLACE_URL_HTTP_ERROR_VAR_0.message)}
