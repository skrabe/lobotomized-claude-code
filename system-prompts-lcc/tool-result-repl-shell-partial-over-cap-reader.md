<!--
name: 'Tool Result: REPL shell over-cap output with reader hint'
description: >-
  Warns .stdout is partial, output was capped when saved, and an immediate
  reader reads the saved part
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_0
  - TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_1
  - TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_2
  - TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_3
  - TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_4
-->
${TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_0} only the first ${TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_1.stdoutChars} characters of the command's output, which is all that .stdout has. The command printed ${TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_2} or more, and only its first ${TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_2} were saved, to ${TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_3}. ${TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_4} those ${TOOL_RESULT_REPL_SHELL_PARTIAL_OVER_CAP_READER_VAR_2}.
