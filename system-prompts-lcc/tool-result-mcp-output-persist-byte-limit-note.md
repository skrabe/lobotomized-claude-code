<!--
name: 'Tool Result: MCP Output Persist Byte Limit Note'
description: >-
  Note appended to an MCP tool_result when the persisted file was cut at the
  persist byte cap, so line counts describe the full output rather than the
  truncated file.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_MCP_OUTPUT_PERSIST_BYTE_LIMIT_NOTE_VAR_0
  - TOOL_RESULT_MCP_OUTPUT_PERSIST_BYTE_LIMIT_NOTE_VAR_1
-->

Note: the output exceeded the persist byte limit; the saved file contains only the first ${TOOL_RESULT_MCP_OUTPUT_PERSIST_BYTE_LIMIT_NOTE_VAR_0(TOOL_RESULT_MCP_OUTPUT_PERSIST_BYTE_LIMIT_NOTE_VAR_1)} of it and may end mid-structure (a JSON parse of the whole file can fail). Any line/character counts or parsing recipes above describe the full output, not the truncated file.
