<!--
name: 'MCP redial: retry backoff'
description: >-
  Redial note that the server did not connect when last tried and is not retried
  for a number of seconds.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_REDIAL_TOO_SOON_VAR_0
  - TOOL_RESULT_MCP_REDIAL_TOO_SOON_VAR_1
-->
${TOOL_RESULT_MCP_REDIAL_TOO_SOON_VAR_0} did not connect when it was last tried, and is not tried again for ${TOOL_RESULT_MCP_REDIAL_TOO_SOON_VAR_1} s.
