<!--
name: 'Tool Result: Remote Host Approval Asked Withdrawn Backed Up'
description: >-
  Tool-result error when the remote host had already asked for approval but this
  session could not forward the user's answer in time, so the pending request
  was withdrawn.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_ASKED_WITHDRAWN_BACKED_UP_VAR_0
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_ASKED_WITHDRAWN_BACKED_UP_VAR_1
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_ASKED_WITHDRAWN_BACKED_UP_VAR_2
-->
The call had reached ${TOOL_RESULT_REMOTE_HOST_APPROVAL_ASKED_WITHDRAWN_BACKED_UP_VAR_0} and asked for approval there, but the user's approval could not be sent within ${TOOL_RESULT_REMOTE_HOST_APPROVAL_ASKED_WITHDRAWN_BACKED_UP_VAR_1.round(TOOL_RESULT_REMOTE_HOST_APPROVAL_ASKED_WITHDRAWN_BACKED_UP_VAR_2/1000)}s — this session's connection to the service was backed up — and it was taken back before it left this session, so ${TOOL_RESULT_REMOTE_HOST_APPROVAL_ASKED_WITHDRAWN_BACKED_UP_VAR_0} never received it and nothing ran; the pending request on ${TOOL_RESULT_REMOTE_HOST_APPROVAL_ASKED_WITHDRAWN_BACKED_UP_VAR_0} is withdrawn. This is not a problem with ${TOOL_RESULT_REMOTE_HOST_APPROVAL_ASKED_WITHDRAWN_BACKED_UP_VAR_0}; send the call again and the user will be asked once more.
