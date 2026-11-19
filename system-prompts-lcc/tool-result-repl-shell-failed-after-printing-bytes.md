<!--
name: 'Tool Result: REPL shell failed after printing bytes'
description: >-
  Fragment explaining a failed command printed N bytes and only the first part
  was kept, optionally with a middle cut
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_REPL_SHELL_FAILED_AFTER_PRINTING_BYTES_VAR_0
  - TOOL_RESULT_REPL_SHELL_FAILED_AFTER_PRINTING_BYTES_VAR_1
  - TOOL_RESULT_REPL_SHELL_FAILED_AFTER_PRINTING_BYTES_VAR_2
-->
the command failed after printing ${TOOL_RESULT_REPL_SHELL_FAILED_AFTER_PRINTING_BYTES_VAR_0} bytes. Claude Code kept only the first ${TOOL_RESULT_REPL_SHELL_FAILED_AFTER_PRINTING_BYTES_VAR_1()} bytes, so the end of the output is missing${TOOL_RESULT_REPL_SHELL_FAILED_AFTER_PRINTING_BYTES_VAR_2?', and stdout has a "characters truncated" line where the middle was cut out of those bytes':""}.
