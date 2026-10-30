<!--
name: 'Tool Result: PreToolUse hook gave no verdict'
description: >-
  Reason a served-call PreToolUse hook refused the call: it ended in a
  non-blocking error without having run by contract, so it gave no verdict.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_2_VAR_0
  - TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_2_VAR_1
  - TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_2_VAR_2
  - TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_2_VAR_3
-->
${TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_2_VAR_0} gave no verdict${TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_2_VAR_1}${TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_2_VAR_2}${TOOL_RESULT_PRETOOLUSE_HOOK_COULD_NOT_RENDER_VERDICT_2_VAR_3}. This is a hard failure, not a transient one: the check cannot or does not judge this request, so retrying this action will get the same answer. Don't retry it. Continue with other tasks that don't require it; if it is essential, stop and tell the user that auto mode could not evaluate it. 
