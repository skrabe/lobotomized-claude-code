<!--
name: 'Tool Result: REPL shell whole output capped'
description: Warns the read text is the capped saved output and may end mid-line
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_SHELL_PARTIAL_WHOLE_CAPPED_VAR_0
  - TOOL_RESULT_REPL_SHELL_PARTIAL_WHOLE_CAPPED_VAR_1
  - TOOL_RESULT_REPL_SHELL_PARTIAL_WHOLE_CAPPED_VAR_2
  - TOOL_RESULT_REPL_SHELL_PARTIAL_WHOLE_CAPPED_VAR_3
-->
${TOOL_RESULT_REPL_SHELL_PARTIAL_WHOLE_CAPPED_VAR_0} the first ${TOOL_RESULT_REPL_SHELL_PARTIAL_WHOLE_CAPPED_VAR_1.wholeChars} characters of the command's output. The command printed ${TOOL_RESULT_REPL_SHELL_PARTIAL_WHOLE_CAPPED_VAR_2} or more, and only its first ${TOOL_RESULT_REPL_SHELL_PARTIAL_WHOLE_CAPPED_VAR_2} were saved, to ${TOOL_RESULT_REPL_SHELL_PARTIAL_WHOLE_CAPPED_VAR_3}. Anything after that was not kept, so the text can end in the middle of a line.
