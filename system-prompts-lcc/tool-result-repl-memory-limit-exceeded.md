<!--
name: 'Tool Result: REPL memory limit exceeded'
description: Error when REPL code used too much memory without awaiting and was stopped
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_REPL_MEMORY_LIMIT_EXCEEDED_VAR_0
  - TOOL_RESULT_REPL_MEMORY_LIMIT_EXCEEDED_VAR_1
-->
REPL: the code used more than ${TOOL_RESULT_REPL_MEMORY_LIMIT_EXCEEDED_VAR_0(TOOL_RESULT_REPL_MEMORY_LIMIT_EXCEEDED_VAR_1())} of memory without awaiting a tool call or a timer, and was stopped. Check for a loop that never ends. Set large variables to null to free them, and run work on large data in a shell command.
