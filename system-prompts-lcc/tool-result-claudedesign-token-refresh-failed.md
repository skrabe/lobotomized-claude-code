<!--
name: 'Tool Result: Claude Design — token refresh failed'
description: 'Error when the design token refresh failed, suggesting retry or /design login.'
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_CLAUDEDESIGN_TOKEN_REFRESH_FAILED_VAR_0
  - TOOL_RESULT_CLAUDEDESIGN_TOKEN_REFRESH_FAILED_VAR_1
  - TOOL_RESULT_CLAUDEDESIGN_TOKEN_REFRESH_FAILED_VAR_2
-->
Design token refresh failed${TOOL_RESULT_CLAUDEDESIGN_TOKEN_REFRESH_FAILED_VAR_0}. Retry shortly${TOOL_RESULT_CLAUDEDESIGN_TOKEN_REFRESH_FAILED_VAR_1?.TOOL_RESULT_CLAUDEDESIGN_TOKEN_REFRESH_FAILED_VAR_2?"":", or run /design login"}.
