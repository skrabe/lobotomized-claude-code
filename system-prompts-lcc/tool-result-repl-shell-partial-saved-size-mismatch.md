<!--
name: 'Tool Result: REPL shell saved file size mismatch'
description: >-
  Warns the saved output file size differs from the counted size so the rest was
  not read
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_VAR_0
  - TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_VAR_1
  - TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_VAR_2
-->
${TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_VAR_0} only the first ${TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_VAR_1.stdoutChars} characters of the command's output. The saved file ${TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_VAR_2} does not have the size that the shell tool counted for the output, so Claude Code did not read the rest of it.
