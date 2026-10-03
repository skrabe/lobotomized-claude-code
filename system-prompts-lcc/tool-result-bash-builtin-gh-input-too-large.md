<!--
name: 'Tool Result: Built-in gh input larger than limit'
description: >-
  Error from the built-in gh when a --input file or stdin exceeds the size cap
  it sends.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_INPUT_TOO_LARGE_VAR_0
  - TOOL_RESULT_BASH_BUILTIN_GH_INPUT_TOO_LARGE_VAR_1
  - TOOL_RESULT_BASH_BUILTIN_GH_INPUT_TOO_LARGE_VAR_2
-->
${TOOL_RESULT_BASH_BUILTIN_GH_INPUT_TOO_LARGE_VAR_0==="-"?"standard input":TOOL_RESULT_BASH_BUILTIN_GH_INPUT_TOO_LARGE_VAR_1(TOOL_RESULT_BASH_BUILTIN_GH_INPUT_TOO_LARGE_VAR_0)} is larger than ${TOOL_RESULT_BASH_BUILTIN_GH_INPUT_TOO_LARGE_VAR_2/1048576} MB, the most this gh sends
