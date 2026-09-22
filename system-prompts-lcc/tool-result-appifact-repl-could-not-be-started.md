<!--
name: 'Tool Result: AppifactRepl Could Not Be Started'
description: >-
  Fallback parenthetical in the AppifactRepl tool_result when the process never
  started (null exitCode and signal, no note).
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_APPIFACT_REPL_COULD_NOT_BE_STARTED_VAR_0
-->
(${TOOL_RESULT_APPIFACT_REPL_COULD_NOT_BE_STARTED_VAR_0.note??"the REPL could not be started"})
