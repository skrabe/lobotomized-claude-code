<!--
name: 'Tool Result: REPL shell hook spill over persist limit'
description: >-
  Notes the output exceeded the persist limit so only its first part, without
  hook changes, was saved
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_SHELL_HOOK_SPILL_OVER_LIMIT_VAR_0
  - TOOL_RESULT_REPL_SHELL_HOOK_SPILL_OVER_LIMIT_VAR_1
-->
the output exceeded the ${TOOL_RESULT_REPL_SHELL_HOOK_SPILL_OVER_LIMIT_VAR_0} persist limit, so only its first ${TOOL_RESULT_REPL_SHELL_HOOK_SPILL_OVER_LIMIT_VAR_0}, without the hook's changes, were saved to ${TOOL_RESULT_REPL_SHELL_HOOK_SPILL_OVER_LIMIT_VAR_1??"a file that the hook's result does not name"}
