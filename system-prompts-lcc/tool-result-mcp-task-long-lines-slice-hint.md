<!--
name: 'Tool Result: MCP Task Long-Line Slice Hint'
description: >-
  Retrieval hint embedded in the MCP task result telling the model to slice the
  saved file by character range via Bash because its lines defeat Read's
  offset/limit.
ccVersion: 2.1.214
variables:
  - TOOL_RESULT_MCP_TASK_LONG_LINES_SLICE_HINT_VAR_0
  - TOOL_RESULT_MCP_TASK_LONG_LINES_SLICE_HINT_VAR_1
  - TOOL_RESULT_MCP_TASK_LONG_LINES_SLICE_HINT_VAR_2
-->
its lines are too long for Read's offset/limit — slice by character range via Bash instead, e.g. ${TOOL_RESULT_MCP_TASK_LONG_LINES_SLICE_HINT_VAR_0} -c 'print(open("${TOOL_RESULT_MCP_TASK_LONG_LINES_SLICE_HINT_VAR_1}").read()[A:B])' in ~${TOOL_RESULT_MCP_TASK_LONG_LINES_SLICE_HINT_VAR_2.toLocaleString()}-char spans
