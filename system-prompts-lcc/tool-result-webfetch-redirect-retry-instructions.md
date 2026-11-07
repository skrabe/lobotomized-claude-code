<!--
name: 'Tool Result: WebFetch redirect retry instructions'
description: >-
  Tells the model to call WebFetch again with the relayed redirect URL and the
  original prompt after a cross-host redirect was not followed
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_0
  - TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_1
  - TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_2
  - TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_3
  - TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_4
-->
${TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_0?`Please use ${TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_1} again with these parameters:
- url: "${TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_2}"
- prompt: "${TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_3}"${TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_4>0?`
- offset: ${TOOL_RESULT_WEBFETCH_REDIRECT_RETRY_INSTRUCTIONS_VAR_4}`:""}`:"The redirect target could not be relayed in full or is not a fetchable address, so it cannot be fetched from here; report the redirect instead."}
