<!--
name: 'Tool result: Edit file reports 0 bytes but too large'
description: >-
  Edit validateInput refusal when a file reports size 0 but holds more than the
  read cap
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_EDIT_FILE_TOO_LARGE_ZERO_SIZE_REPORT_VAR_0
  - TOOL_RESULT_EDIT_FILE_TOO_LARGE_ZERO_SIZE_REPORT_VAR_1
-->
File is too large to edit: it reports a size of 0 bytes and holds more than ${TOOL_RESULT_EDIT_FILE_TOO_LARGE_ZERO_SIZE_REPORT_VAR_0(TOOL_RESULT_EDIT_FILE_TOO_LARGE_ZERO_SIZE_REPORT_VAR_1)}.
