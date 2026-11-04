<!--
name: 'Tool Result: REPL shell saved file failed checks'
description: >-
  Warns the rest of output was saved but not read back because the file failed
  the shell-tool file checks
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_SHELL_PARTIAL_FILE_REFUSED_VAR_0
  - TOOL_RESULT_REPL_SHELL_PARTIAL_FILE_REFUSED_VAR_1
  - TOOL_RESULT_REPL_SHELL_PARTIAL_FILE_REFUSED_VAR_2
-->
${TOOL_RESULT_REPL_SHELL_PARTIAL_FILE_REFUSED_VAR_0} only the first ${TOOL_RESULT_REPL_SHELL_PARTIAL_FILE_REFUSED_VAR_1.stdoutChars} characters of the command's output. The rest was saved to ${TOOL_RESULT_REPL_SHELL_PARTIAL_FILE_REFUSED_VAR_2}, and Claude Code did not read that file back, because the file did not pass the checks that it is the file the shell tool saved.
