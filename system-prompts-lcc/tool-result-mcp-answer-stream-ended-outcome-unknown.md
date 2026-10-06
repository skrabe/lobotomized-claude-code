<!--
name: 'Tool Result: MCP answer stream ended, outcome unknown'
description: >-
  Error returned when an MCP server's answer stream ends before it answers a
  tool call, telling Claude the outcome is unknown and to check before repeating
  it
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_MCP_ANSWER_STREAM_ENDED_OUTCOME_UNKNOWN_VAR_0
  - TOOL_RESULT_MCP_ANSWER_STREAM_ENDED_OUTCOME_UNKNOWN_VAR_1
-->
MCP server "${TOOL_RESULT_MCP_ANSWER_STREAM_ENDED_OUTCOME_UNKNOWN_VAR_0}" never answered tool "${TOOL_RESULT_MCP_ANSWER_STREAM_ENDED_OUTCOME_UNKNOWN_VAR_1}": the stream that was to bring its answer ended first. The outcome is unknown: the call may have finished, may still be running, or may never have started. Check what it did before you repeat it.
