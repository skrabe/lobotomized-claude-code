<!--
name: 'Tool Result: AppifactRepl Time Limit'
description: >-
  AppifactRepl stop-note interpolated into the tool_result when the REPL hits
  its wall-clock limit.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_APPIFACT_REPL_TIME_LIMIT_VAR_0
  - TOOL_RESULT_APPIFACT_REPL_TIME_LIMIT_VAR_1
-->
stopped after ${TOOL_RESULT_APPIFACT_REPL_TIME_LIMIT_VAR_0.round(TOOL_RESULT_APPIFACT_REPL_TIME_LIMIT_VAR_1/1000)}s, the REPL's time limit; the statements printed above ran
