<!--
name: 'Tool Result: REPL shell saved output not read back'
description: >-
  Warns stdout may be only the start of output because the saved file was not
  read back
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_SHELL_PARTIAL_NOT_READ_BACK_VAR_0
  - TOOL_RESULT_REPL_SHELL_PARTIAL_NOT_READ_BACK_VAR_1
  - TOOL_RESULT_REPL_SHELL_PARTIAL_NOT_READ_BACK_VAR_2
-->
${TOOL_RESULT_REPL_SHELL_PARTIAL_NOT_READ_BACK_VAR_0} ${TOOL_RESULT_REPL_SHELL_PARTIAL_NOT_READ_BACK_VAR_1.stdoutChars} characters, which is all that the result has in stdout. The result gives ${TOOL_RESULT_REPL_SHELL_PARTIAL_NOT_READ_BACK_VAR_2} as a file that the output was saved to, and Claude Code did not read that file, so these characters may be only the start of the output.
