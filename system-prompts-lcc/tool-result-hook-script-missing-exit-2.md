<!--
name: 'Tool Result: Hook script appears missing'
description: >-
  Hook error stderr when a hook exited 2 in a way that looks like a missing
  script, with plugin reinstall advice
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_HOOK_SCRIPT_MISSING_EXIT_2_VAR_0
  - TOOL_RESULT_HOOK_SCRIPT_MISSING_EXIT_2_VAR_1
  - TOOL_RESULT_HOOK_SCRIPT_MISSING_EXIT_2_VAR_2
-->
Hook script appears to be missing — ${TOOL_RESULT_HOOK_SCRIPT_MISSING_EXIT_2_VAR_0===void 0?`"${TOOL_RESULT_HOOK_SCRIPT_MISSING_EXIT_2_VAR_1}" exited 2 with: ${TOOL_RESULT_HOOK_SCRIPT_MISSING_EXIT_2_VAR_2.trim()}`:"the hook exited 2"}. 
