<!--
name: 'Tool Result: Remote Tool Timed Out Left Standing'
description: >-
  timed_out tool_result when the host did not answer and the request was left
  running there, telling the model to check effects before retrying.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_LEFT_STANDING_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_LEFT_STANDING_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_LEFT_STANDING_VAR_2
-->
${TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_LEFT_STANDING_VAR_0} did not answer within ${TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_LEFT_STANDING_VAR_1.round(TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_LEFT_STANDING_VAR_2/1000)}s, and what became of the call could not be learned from it afterwards; the request was left with ${TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_LEFT_STANDING_VAR_0}, so the command may have run or may still be running there. Check its effect on ${TOOL_RESULT_REMOTE_TOOL_TIMED_OUT_LEFT_STANDING_VAR_0} before repeating it.
