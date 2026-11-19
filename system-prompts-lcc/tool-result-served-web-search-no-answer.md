<!--
name: 'Tool result: served web search got no answer'
description: >-
  Served SearchWeb call error when the search request got no response, with the
  network error code.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_SERVED_WEB_SEARCH_NO_ANSWER_VAR_0
-->
The search request got no answer (${/^\w{1,32}$/.test(TOOL_RESULT_SERVED_WEB_SEARCH_NO_ANSWER_VAR_0.code??"")?TOOL_RESULT_SERVED_WEB_SEARCH_NO_ANSWER_VAR_0.code:"network error"})
