<!--
name: WebFetch HTTP error result
description: >-
  WebFetch tool_result returned to the model reporting a non-2xx HTTP status and
  suggesting an authenticated tool instead.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_WEBFETCH_HTTP_ERROR_VAR_0
  - TOOL_RESULT_WEBFETCH_HTTP_ERROR_VAR_1
  - TOOL_RESULT_WEBFETCH_HTTP_ERROR_VAR_2
-->
The server returned HTTP ${TOOL_RESULT_WEBFETCH_HTTP_ERROR_VAR_0.statusCode} ${TOOL_RESULT_WEBFETCH_HTTP_ERROR_VAR_1}.${TOOL_RESULT_WEBFETCH_HTTP_ERROR_VAR_2}

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. \`gh\` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
