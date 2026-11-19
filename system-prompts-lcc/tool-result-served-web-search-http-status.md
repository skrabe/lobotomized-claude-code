<!--
name: 'Tool result: served web search HTTP error'
description: >-
  Served SearchWeb call error giving the HTTP status the search request was
  answered with.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_SERVED_WEB_SEARCH_HTTP_STATUS_VAR_0
  - TOOL_RESULT_SERVED_WEB_SEARCH_HTTP_STATUS_VAR_1
-->
The search request was answered with HTTP ${TOOL_RESULT_SERVED_WEB_SEARCH_HTTP_STATUS_VAR_0.status}${TOOL_RESULT_SERVED_WEB_SEARCH_HTTP_STATUS_VAR_1===""?"":`: ${TOOL_RESULT_SERVED_WEB_SEARCH_HTTP_STATUS_VAR_1}`}
