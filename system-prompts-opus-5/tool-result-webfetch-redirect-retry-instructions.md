<!--
name: 'Tool Result: WebFetch redirect retry instructions'
description: >-
  Tells the model to call WebFetch again with the relayed redirect URL and the
  original prompt after a cross-host redirect was not followed
ccVersion: 2.1.232
variables:
  - TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_0
  - TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_1
  - TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_2
-->
Please use ${TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_0} again with these parameters:
- url: "${TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_1}"
- prompt: "${TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_2}"
