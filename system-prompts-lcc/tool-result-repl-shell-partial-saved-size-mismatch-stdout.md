<!--
name: 'Tool Result: REPL shell stdout-only with size mismatch'
description: >-
  Warns .stdout holds only the first characters and the saved file size does not
  match
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_STDOUT_VAR_0
  - TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_STDOUT_VAR_1
  - TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_STDOUT_VAR_2
-->
${TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_STDOUT_VAR_0} only the first ${TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_STDOUT_VAR_1.stdoutChars} characters of the command's output, which is all that .stdout has. The saved file ${TOOL_RESULT_REPL_SHELL_PARTIAL_SAVED_SIZE_MISMATCH_STDOUT_VAR_2} does not have the size that the shell tool counted for the output.
