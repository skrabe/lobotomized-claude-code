<!--
name: 'Tool result: built-in gh header not allowed'
description: >-
  Built-in gh stand-in refusal of a header that cannot be set through the
  session's GitHub proxy, listing allowed headers.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_HEADER_NOT_ALLOWED_VAR_0
  - TOOL_RESULT_BASH_BUILTIN_GH_HEADER_NOT_ALLOWED_VAR_1
-->
the ${/^[a-z0-9-]+$/.test(TOOL_RESULT_BASH_BUILTIN_GH_HEADER_NOT_ALLOWED_VAR_0)?`${TOOL_RESULT_BASH_BUILTIN_GH_HEADER_NOT_ALLOWED_VAR_0} `:""}header cannot be set through this session's GitHub proxy; headers that can: ${[...TOOL_RESULT_BASH_BUILTIN_GH_HEADER_NOT_ALLOWED_VAR_1].join(", ")}
