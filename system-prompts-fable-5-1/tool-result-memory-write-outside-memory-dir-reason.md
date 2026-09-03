<!--
name: 'Tool Result: Memory Write Outside Memory Dir Reason'
description: >-
  checkPermissions safetyCheck reason for a personal memory save outside the
  unattended memory directory.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_MEMORY_WRITE_OUTSIDE_MEMORY_DIR_REASON_VAR_0
  - TOOL_RESULT_MEMORY_WRITE_OUTSIDE_MEMORY_DIR_REASON_VAR_1
  - TOOL_RESULT_MEMORY_WRITE_OUTSIDE_MEMORY_DIR_REASON_VAR_2
-->
${TOOL_RESULT_MEMORY_WRITE_OUTSIDE_MEMORY_DIR_REASON_VAR_0==="plan"?"You are in plan mode, and this":"This"} personal memory save falls outside the memory directory Claude Code saves to without asking — it would be stored at ${TOOL_RESULT_MEMORY_WRITE_OUTSIDE_MEMORY_DIR_REASON_VAR_1(TOOL_RESULT_MEMORY_WRITE_OUTSIDE_MEMORY_DIR_REASON_VAR_2)}
