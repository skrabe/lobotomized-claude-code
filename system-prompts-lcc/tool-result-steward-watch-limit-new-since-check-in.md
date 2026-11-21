<!--
name: 'Tool Result: Steward watch limit new since check-in'
description: >-
  Notes the watch-defeating setting is new since the last start or check-in,
  possibly from an unfinished merge
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_WATCH_LIMIT_NEW_SINCE_CHECK_IN_VAR_0
-->
This is new since the last start or check-in${TOOL_RESULT_STEWARD_WATCH_LIMIT_NEW_SINCE_CHECK_IN_VAR_0?". If a merge brought it, that merge may not be finished: git status will show that":""}
