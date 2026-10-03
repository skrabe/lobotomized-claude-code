<!--
name: 'Tool Result: MCP Output Saved — JSON Is a Single Line'
description: >-
  Note in the saved-large-MCP-output result explaining that a JSON file's long
  value is a single line that Read's offset/limit cannot split, and to probe the
  structure with jq or python if a shell tool is available.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_MCP_OUTPUT_JSON_SINGLE_LINE_NOTE_VAR_0
  - TOOL_RESULT_MCP_OUTPUT_JSON_SINGLE_LINE_NOTE_VAR_1
-->
- Note: this file is JSON, so a long value (or the whole file) is a single line. ${TOOL_RESULT_MCP_OUTPUT_JSON_SINGLE_LINE_NOTE_VAR_0}'s offset/limit cannot split a line, so reading in chunks works only if every line is short. If a shell tool is available, ${TOOL_RESULT_MCP_OUTPUT_JSON_SINGLE_LINE_NOTE_VAR_1}.
