<!--
name: 'Tool Result: Remote host never received'
description: >-
  Tells the model the machine reports it never received the call so it did not
  run and is safe to retry, telling the user if it is refused the same way again
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_0
  - TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_1
  - TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_2
  - TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_3
-->
${TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_0(TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_1,TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_2)}, and ${TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_1} reports it never received it: it did not run. ${TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_2==="unverified_refusal"&&TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_3==="desktop_app"?"It is safe to retry; if it is refused the same way again, tell the user.":"It is safe to retry."}
