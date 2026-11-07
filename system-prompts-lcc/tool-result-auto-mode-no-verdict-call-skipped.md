<!--
name: 'Tool Result: auto mode no verdict, call skipped'
description: >-
  Server classifier skipped a call it expected not to need review: the call did
  not run yet, re-issue it once in the next response, then stop and tell the
  user why it could not run.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_AUTO_MODE_NO_VERDICT_CALL_SKIPPED_VAR_0
  - TOOL_RESULT_AUTO_MODE_NO_VERDICT_CALL_SKIPPED_VAR_1
-->
${TOOL_RESULT_AUTO_MODE_NO_VERDICT_CALL_SKIPPED_VAR_0} did not run yet. ${TOOL_RESULT_AUTO_MODE_NO_VERDICT_CALL_SKIPPED_VAR_1} expected this call not to need a review, but it needs one. This is a routine re-check, not an error and not a refusal, and it says nothing about whether the action is safe. Issue the action again once, as-is, in your next response; if it is denied again, do not issue it again: continue with other tasks that don't require it and tell the user why it could not run.
