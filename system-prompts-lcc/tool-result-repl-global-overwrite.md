<!--
name: 'Tool Result: REPL global overwrite'
description: >-
  Explains the script did not run because it would overwrite a global and how to
  keep names local
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_GLOBAL_OVERWRITE_VAR_0
-->
The script did not run: it would overwrite ${TOOL_RESULT_REPL_GLOBAL_OVERWRITE_VAR_0} (a helper, a tool or a JavaScript built-in). A top-level declaration, or an assignment to a name the script does not declare itself, writes the global and so changes it for every later script. Use another name, or declare it inside a function, where it stays local.
