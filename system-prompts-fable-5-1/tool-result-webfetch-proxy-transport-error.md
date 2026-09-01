<!--
name: WebFetch proxy transport error
description: >-
  Error surfaced to the model (via the web-fetch-ccr-proxy error) when the
  request to the fetch proxy fails at transport level.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_WEBFETCH_PROXY_TRANSPORT_ERROR_VAR_0
  - TOOL_RESULT_WEBFETCH_PROXY_TRANSPORT_ERROR_VAR_1
-->
Request to the ${TOOL_RESULT_WEBFETCH_PROXY_TRANSPORT_ERROR_VAR_0} proxy failed (${TOOL_RESULT_WEBFETCH_PROXY_TRANSPORT_ERROR_VAR_1??"transport error"}).
