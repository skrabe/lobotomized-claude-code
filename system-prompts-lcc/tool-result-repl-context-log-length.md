<!--
name: 'REPL: Context log() Text Length'
description: >-
  Error thrown into the script when contexts.<name>.log text is empty or over
  the cap.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CONTEXT_LOG_LENGTH_VAR_0
  - TOOL_RESULT_REPL_CONTEXT_LOG_LENGTH_VAR_1
-->
contexts.${TOOL_RESULT_REPL_CONTEXT_LOG_LENGTH_VAR_0}.log: text must be 1-${TOOL_RESULT_REPL_CONTEXT_LOG_LENGTH_VAR_1} chars
