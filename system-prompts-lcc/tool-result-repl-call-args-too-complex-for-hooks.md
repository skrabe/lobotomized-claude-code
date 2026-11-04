<!--
name: 'REPL: Call Arguments Too Complex For Hooks'
description: >-
  Refusal when a REPL inner call's arguments are too deep or large for the
  plugin hooks that check the tool.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_COMPLEX_FOR_HOOKS_VAR_0
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_COMPLEX_FOR_HOOKS_VAR_1
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_COMPLEX_FOR_HOOKS_VAR_2
-->
${TOOL_RESULT_REPL_CALL_ARGS_TOO_COMPLEX_FOR_HOOKS_VAR_0.name} was not called, because its arguments are too deep or too large for the plugin hooks that check this tool's calls: they are nested more than ${TOOL_RESULT_REPL_CALL_ARGS_TOO_COMPLEX_FOR_HOOKS_VAR_1} levels deep, have more than ${TOOL_RESULT_REPL_CALL_ARGS_TOO_COMPLEX_FOR_HOOKS_VAR_2} values, or contain themselves. Pass a smaller, flatter value, or split it over several calls.
