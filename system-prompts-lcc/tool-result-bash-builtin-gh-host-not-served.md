<!--
name: 'Tool Result: Built-in gh host not served'
description: >-
  Refusal saying the named host is not served: the built-in gh reaches only the
  listed hosts through the session's GitHub proxy, fixed at session start.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_HOST_NOT_SERVED_VAR_0
  - TOOL_RESULT_BASH_BUILTIN_GH_HOST_NOT_SERVED_VAR_1
  - TOOL_RESULT_BASH_BUILTIN_GH_HOST_NOT_SERVED_VAR_2
  - TOOL_RESULT_BASH_BUILTIN_GH_HOST_NOT_SERVED_VAR_3
-->
${TOOL_RESULT_BASH_BUILTIN_GH_HOST_NOT_SERVED_VAR_0(TOOL_RESULT_BASH_BUILTIN_GH_HOST_NOT_SERVED_VAR_1)} is not served here: this gh reaches ${[TOOL_RESULT_BASH_BUILTIN_GH_HOST_NOT_SERVED_VAR_2,...TOOL_RESULT_BASH_BUILTIN_GH_HOST_NOT_SERVED_VAR_3].join(" and ")} only, through this session's GitHub proxy. Which GitHub Enterprise Server hosts it reaches is fixed when the session starts, and nothing run in the session adds one
