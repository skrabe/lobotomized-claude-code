<!--
name: 'Tool Result: Remote Tool Timed Out Withdrawn'
description: >-
  timed_out tool_result when the unanswered call was withdrawn on the host and
  may have partially run.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_WITHDRAWN_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_WITHDRAWN_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_WITHDRAWN_VAR_2
-->
${TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_WITHDRAWN_VAR_0} did not answer within ${TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_WITHDRAWN_VAR_1.round(TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_WITHDRAWN_VAR_2/1000)}s, and what became of the call could not be learned from it afterwards, so it was withdrawn there; it may have partially run. Check its effect on ${TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_WITHDRAWN_VAR_0} before repeating it.
