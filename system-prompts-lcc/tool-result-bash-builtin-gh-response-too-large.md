<!--
name: 'Tool Result: Built-in gh response larger than limit'
description: >-
  Error from the built-in gh when a response exceeds the maximum it reads,
  telling the model to ask for less (per_page, narrower endpoint).
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_RESPONSE_TOO_LARGE_VAR_0
-->
the response is larger than ${TOOL_RESULT_BASH_BUILTIN_GH_RESPONSE_TOO_LARGE_VAR_0/1048576} MB, the most this gh reads; ask for less (per_page, a narrower endpoint)
