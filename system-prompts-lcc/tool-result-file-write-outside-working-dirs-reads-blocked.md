<!--
name: 'Tool result: file write path outside working dirs, reads blocked'
description: >-
  Validation message when a write/edit path is outside the working directories
  (or reached via link) while file-tool reads outside them are blocked.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_FILE_WRITE_OUTSIDE_WORKING_DIRS_READS_BLOCKED_VAR_0
  - TOOL_RESULT_FILE_WRITE_OUTSIDE_WORKING_DIRS_READS_BLOCKED_VAR_1
  - TOOL_RESULT_FILE_WRITE_OUTSIDE_WORKING_DIRS_READS_BLOCKED_VAR_2
-->
This path is outside the working directories, or a link in it leads there. Reads there are blocked (${TOOL_RESULT_FILE_WRITE_OUTSIDE_WORKING_DIRS_READS_BLOCKED_VAR_0(TOOL_RESULT_FILE_WRITE_OUTSIDE_WORKING_DIRS_READS_BLOCKED_VAR_1)}), so ${TOOL_RESULT_FILE_WRITE_OUTSIDE_WORKING_DIRS_READS_BLOCKED_VAR_2} cannot create or change it.
