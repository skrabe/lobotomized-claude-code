<!--
name: 'Tool Result: REPL shell partial output rewritten by hook'
description: >-
  Warns that a $ reader saw a PostToolUse hook's replacement text and where the
  original output was saved
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_SHELL_PARTIAL_HOOK_REWRITTEN_VAR_0
  - TOOL_RESULT_REPL_SHELL_PARTIAL_HOOK_REWRITTEN_VAR_1
  - TOOL_RESULT_REPL_SHELL_PARTIAL_HOOK_REWRITTEN_VAR_2
  - TOOL_RESULT_REPL_SHELL_PARTIAL_HOOK_REWRITTEN_VAR_3
-->
${TOOL_RESULT_REPL_SHELL_PARTIAL_HOOK_REWRITTEN_VAR_0} the text that a PostToolUse hook put in place of the start of the command's output (${TOOL_RESULT_REPL_SHELL_PARTIAL_HOOK_REWRITTEN_VAR_1.stdoutChars} characters). ${TOOL_RESULT_REPL_SHELL_PARTIAL_HOOK_REWRITTEN_VAR_1.overCap?`The command printed ${TOOL_RESULT_REPL_SHELL_PARTIAL_HOOK_REWRITTEN_VAR_2} or more, and only its first ${TOOL_RESULT_REPL_SHELL_PARTIAL_HOOK_REWRITTEN_VAR_2}, as the command printed them, were saved, to ${TOOL_RESULT_REPL_SHELL_PARTIAL_HOOK_REWRITTEN_VAR_3}.`:`The output as the command printed it was saved to ${TOOL_RESULT_REPL_SHELL_PARTIAL_HOOK_REWRITTEN_VAR_3}.`}
