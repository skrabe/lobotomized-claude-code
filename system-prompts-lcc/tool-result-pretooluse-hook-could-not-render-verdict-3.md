<!--
name: 'Tool Result: PreToolUse hook gave no verdict'
description: >-
  Reason a served-call PreToolUse hook refused the call: it ended in a
  non-blocking error without having run by contract, so it gave no verdict.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_0
  - TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_1
  - TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_2
  - TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_3
  - TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_4
  - TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_5
-->
${TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_0} gave no verdict${TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_1}${TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_2}${TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_3}. This is a transient failure of the check, not a judgment about the action: a later response may get a verdict. You may try the action again once, as-is. Repeated attempts are slowed by a growing delay, and after ${TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_4} responses in a row without a verdict the turn stops. ${TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_3_VAR_5} 
