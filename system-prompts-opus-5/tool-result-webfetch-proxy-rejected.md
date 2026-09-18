<!--
name: 'Tool Result: WebFetch proxy rejected'
description: >-
  errorMessage for a PROXY_REJECTED ccr response; JSON-serialized into a thrown
  TelemetrySafeError from the WebFetch path, which the tool harness returns to
  the model as <tool_use_error>. Sibling of
  tool-result-webfetch-proxy-transport-error.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_WEBFETCH_PROXY_REJECTED_VAR_0
  - TOOL_RESULT_WEBFETCH_PROXY_REJECTED_VAR_1
  - TOOL_RESULT_WEBFETCH_PROXY_REJECTED_VAR_2
  - TOOL_RESULT_WEBFETCH_PROXY_REJECTED_VAR_3
  - TOOL_RESULT_WEBFETCH_PROXY_REJECTED_VAR_4
-->
The ${TOOL_RESULT_WEBFETCH_PROXY_REJECTED_VAR_0} proxy rejected the request (HTTP ${TOOL_RESULT_WEBFETCH_PROXY_REJECTED_VAR_1.status}${TOOL_RESULT_WEBFETCH_PROXY_REJECTED_VAR_2}${TOOL_RESULT_WEBFETCH_PROXY_REJECTED_VAR_3})${TOOL_RESULT_WEBFETCH_PROXY_REJECTED_VAR_4?`: ${TOOL_RESULT_WEBFETCH_PROXY_REJECTED_VAR_4}`:"."}
