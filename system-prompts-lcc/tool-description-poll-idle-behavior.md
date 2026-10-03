<!--
name: 'Tool Description: Poll idle behavior'
description: >-
  Explains that calling Poll with nothing else to do signals idleness, returns
  pending events immediately, and otherwise waits.
ccVersion: 2.1.288
variables:
  - TOOL_DESCRIPTION_POLL_IDLE_BEHAVIOR_VAR_0
-->
Calling this tool with nothing else to do signals that you are idle. If events are pending, they are returned immediately as this call's result. Otherwise the call waits until something arrives: a delivered event returns as the result, and new user input usually returns the literal result "(no pending events)" so the turn can end and the input can be processed. ${TOOL_DESCRIPTION_POLL_IDLE_BEHAVIOR_VAR_0}
