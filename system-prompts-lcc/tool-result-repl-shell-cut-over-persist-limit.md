<!--
name: 'Tool Result: REPL shell output cut over persist limit'
description: >-
  Marker that output was cut and exceeded the persist limit so only its first
  part was saved
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_SHELL_CUT_OVER_PERSIST_LIMIT_VAR_0
  - TOOL_RESULT_REPL_SHELL_CUT_OVER_PERSIST_LIMIT_VAR_1
  - TOOL_RESULT_REPL_SHELL_CUT_OVER_PERSIST_LIMIT_VAR_2
-->
... [output cut at ${TOOL_RESULT_REPL_SHELL_CUT_OVER_PERSIST_LIMIT_VAR_0.length} chars; it exceeded the ${TOOL_RESULT_REPL_SHELL_CUT_OVER_PERSIST_LIMIT_VAR_1} persist limit, so only its first ${TOOL_RESULT_REPL_SHELL_CUT_OVER_PERSIST_LIMIT_VAR_1} were saved to ${TOOL_RESULT_REPL_SHELL_CUT_OVER_PERSIST_LIMIT_VAR_2??"the spill file"}]
