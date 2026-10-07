<!--
name: 'Tool Result: Read refusing when opened path is unverifiable'
description: >-
  Read refusal when /proc/self/fd could not report where the file was opened, so
  it cannot be told apart from a path the session may not read
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_READ_REFUSING_FD_PATH_UNVERIFIABLE_VAR_0
  - TOOL_RESULT_READ_REFUSING_FD_PATH_UNVERIFIABLE_VAR_1
  - TOOL_RESULT_READ_REFUSING_FD_PATH_UNVERIFIABLE_VAR_2
-->
Refusing to read ${TOOL_RESULT_READ_REFUSING_FD_PATH_UNVERIFIABLE_VAR_0}: the system would not say where it was opened (reading /proc/self/fd failed with ${TOOL_RESULT_READ_REFUSING_FD_PATH_UNVERIFIABLE_VAR_1(TOOL_RESULT_READ_REFUSING_FD_PATH_UNVERIFIABLE_VAR_2)??"an error"}), so it cannot be told apart from a path this session may not read.
