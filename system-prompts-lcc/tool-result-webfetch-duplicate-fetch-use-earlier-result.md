<!--
name: 'Tool Result: WebFetch Duplicate Fetch Use Earlier Result'
description: >-
  WebFetch result when the same URL and prompt were already fetched in this
  conversation: points to the earlier tool call and cache window, and says to
  reuse that result or call again if it is gone.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_WEBFETCH_DUPLICATE_FETCH_USE_EARLIER_RESULT_VAR_0
  - TOOL_RESULT_WEBFETCH_DUPLICATE_FETCH_USE_EARLIER_RESULT_VAR_1
  - TOOL_RESULT_WEBFETCH_DUPLICATE_FETCH_USE_EARLIER_RESULT_VAR_2
  - TOOL_RESULT_WEBFETCH_DUPLICATE_FETCH_USE_EARLIER_RESULT_VAR_3
  - TOOL_RESULT_WEBFETCH_DUPLICATE_FETCH_USE_EARLIER_RESULT_VAR_4
-->
Already fetched ${TOOL_RESULT_WEBFETCH_DUPLICATE_FETCH_USE_EARLIER_RESULT_VAR_0} with the same prompt ${TOOL_RESULT_WEBFETCH_DUPLICATE_FETCH_USE_EARLIER_RESULT_VAR_1}s ago in this conversation (tool call ${TOOL_RESULT_WEBFETCH_DUPLICATE_FETCH_USE_EARLIER_RESULT_VAR_2.toolUseId}). ${TOOL_RESULT_WEBFETCH_DUPLICATE_FETCH_USE_EARLIER_RESULT_VAR_3} caches pages for ${TOOL_RESULT_WEBFETCH_DUPLICATE_FETCH_USE_EARLIER_RESULT_VAR_4()}, so fetching again now would return the same content; use that earlier result. If you can no longer see it, call ${TOOL_RESULT_WEBFETCH_DUPLICATE_FETCH_USE_EARLIER_RESULT_VAR_3} again with the same url and prompt and it will run normally.
