<!--
name: 'Tool result: Send to project nothing created'
description: >-
  Error result that nothing was created or sent, with the reason, suggesting a
  rerun if the cause looks temporary.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_NOTHING_CREATED_VAR_0
-->
Nothing was created or sent: ${TOOL_RESULT_SEND_TO_PROJECT_NOTHING_CREATED_VAR_0.reason??"unknown error"}. Tell the user, and suggest running /send-to-project again if the cause looks temporary.
