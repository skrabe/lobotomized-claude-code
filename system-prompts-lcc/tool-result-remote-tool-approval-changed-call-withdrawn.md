<!--
name: 'Tool Result: Remote tool approval changed call withdrawn'
description: >-
  Tool result saying an approval edited the remote tool call, which runs only
  the call it asked about, so nothing ran and the user must be told
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_REMOTE_TOOL_APPROVAL_CHANGED_CALL_WITHDRAWN_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_APPROVAL_CHANGED_CALL_WITHDRAWN_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_APPROVAL_CHANGED_CALL_WITHDRAWN_VAR_2
  - TOOL_RESULT_REMOTE_TOOL_APPROVAL_CHANGED_CALL_WITHDRAWN_VAR_3
-->
${TOOL_RESULT_REMOTE_TOOL_APPROVAL_CHANGED_CALL_WITHDRAWN_VAR_0===void 0?"The approval":TOOL_RESULT_REMOTE_TOOL_APPROVAL_CHANGED_CALL_WITHDRAWN_VAR_1[TOOL_RESULT_REMOTE_TOOL_APPROVAL_CHANGED_CALL_WITHDRAWN_VAR_0]} changed this ${TOOL_RESULT_REMOTE_TOOL_APPROVAL_CHANGED_CALL_WITHDRAWN_VAR_2} call, but ${TOOL_RESULT_REMOTE_TOOL_APPROVAL_CHANGED_CALL_WITHDRAWN_VAR_3} runs only the call it asked permission for, so the request there was withdrawn and nothing ran. Do not guess at the change: tell the user that the approval changed the call and that nothing ran.
