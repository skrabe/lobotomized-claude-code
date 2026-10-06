<!--
name: 'Tool Result: temp dir not a directory'
description: >-
  Error when Claude Code's per-uid temp directory is a symlink or not a
  directory (possible attacker plant), refusing to use it; reaches the model as
  a Bash tool error or /copy output.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_TEMP_DIR_NOT_A_DIRECTORY_VAR_0
  - TOOL_RESULT_TEMP_DIR_NOT_A_DIRECTORY_VAR_1
-->
Temp directory ${TOOL_RESULT_TEMP_DIR_NOT_A_DIRECTORY_VAR_0} is not a directory (may be an attacker-planted symlink). Refusing to use it. ${TOOL_RESULT_TEMP_DIR_NOT_A_DIRECTORY_VAR_1}
