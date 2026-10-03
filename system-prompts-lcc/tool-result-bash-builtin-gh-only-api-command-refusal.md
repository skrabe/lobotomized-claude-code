<!--
name: 'Tool Result: Built-in gh only api command'
description: >-
  Refusal when the model runs a gh subcommand other than api: states this gh is
  Claude Code's built-in client where gh api <REST endpoint> works and nothing
  else.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_ONLY_API_COMMAND_REFUSAL_VAR_0
  - TOOL_RESULT_BASH_BUILTIN_GH_ONLY_API_COMMAND_REFUSAL_VAR_1
  - TOOL_RESULT_BASH_BUILTIN_GH_ONLY_API_COMMAND_REFUSAL_VAR_2
-->
this gh is ${TOOL_RESULT_BASH_BUILTIN_GH_ONLY_API_COMMAND_REFUSAL_VAR_0} (Claude Code ${TOOL_RESULT_BASH_BUILTIN_GH_ONLY_API_COMMAND_REFUSAL_VAR_1}): \`gh api <REST endpoint>\` works here, already authenticated through this session's GitHub proxy, and there is no other gh command (${TOOL_RESULT_BASH_BUILTIN_GH_ONLY_API_COMMAND_REFUSAL_VAR_2}).
