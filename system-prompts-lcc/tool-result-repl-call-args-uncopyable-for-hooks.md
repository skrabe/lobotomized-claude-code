<!--
name: 'REPL: Call Arguments Uncopyable For Hooks'
description: >-
  Refusal when a REPL inner call's arguments contain values (e.g. symbols) that
  cannot be copied to plugin hooks.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CALL_ARGS_UNCOPYABLE_FOR_HOOKS_VAR_0
-->
${TOOL_RESULT_REPL_CALL_ARGS_UNCOPYABLE_FOR_HOOKS_VAR_0.name} was not called, because one of its arguments (a symbol, for example) can't be copied to the plugin hooks that check this tool's calls. Pass only strings, numbers, booleans, null, arrays and plain objects.
