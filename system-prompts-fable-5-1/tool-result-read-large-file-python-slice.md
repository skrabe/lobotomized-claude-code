<!--
name: Large-output read guidance (python slice)
description: >-
  Tool-result guidance fragment to slice the file in char spans via python until
  fully read.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_READ_LARGE_FILE_PYTHON_SLICE_VAR_0
  - TOOL_RESULT_READ_LARGE_FILE_PYTHON_SLICE_VAR_1
  - TOOL_RESULT_READ_LARGE_FILE_PYTHON_SLICE_VAR_2
-->
Slice ${TOOL_RESULT_READ_LARGE_FILE_PYTHON_SLICE_VAR_0} in ~${TOOL_RESULT_READ_LARGE_FILE_PYTHON_SLICE_VAR_1}-char spans via python (read()[A:B]) until you have read all ${TOOL_RESULT_READ_LARGE_FILE_PYTHON_SLICE_VAR_2.toLocaleString()} characters, then summarize and quote any key findings verbatim.
