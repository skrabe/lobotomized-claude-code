<!--
name: 'Tool Result: Remote Host Gone Mid Call'
description: >-
  host_gone tool_result when the machine withdrew or restarted while the call
  was with it; no result will arrive and the model must check effects before
  repeating.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_REMOTE_HOST_GONE_MID_CALL_VAR_0
  - TOOL_RESULT_REMOTE_HOST_GONE_MID_CALL_VAR_1
-->
The call was interrupted: ${TOOL_RESULT_REMOTE_HOST_GONE_MID_CALL_VAR_0} while the call was with it, so no result will arrive for it. It may have partially run — check its effects on ${TOOL_RESULT_REMOTE_HOST_GONE_MID_CALL_VAR_1} before repeating it.
