<!--
name: 'Tool result: REPL output withheld by hook with reason'
description: >-
  REPL result text when a hook withheld the output, quoting the hook's first
  line
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_OUTPUT_WITHHELD_BY_HOOK_REASON_VAR_0
  - TOOL_RESULT_REPL_OUTPUT_WITHHELD_BY_HOOK_REASON_VAR_1
-->
Output withheld by a hook: ${TOOL_RESULT_REPL_OUTPUT_WITHHELD_BY_HOOK_REASON_VAR_0.length<TOOL_RESULT_REPL_OUTPUT_WITHHELD_BY_HOOK_REASON_VAR_1.length?`${TOOL_RESULT_REPL_OUTPUT_WITHHELD_BY_HOOK_REASON_VAR_0}…`:TOOL_RESULT_REPL_OUTPUT_WITHHELD_BY_HOOK_REASON_VAR_0}
