<!--
name: 'Tool Result: Remote Host Approval Withdrawn Unconfirmed'
description: >-
  Remote-host tool_result when restart withdrawal of a pending approval could
  not be confirmed, so the command may still have run.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_UNCONFIRMED_VAR_0
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_UNCONFIRMED_VAR_1
-->
${TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_UNCONFIRMED_VAR_0(TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_UNCONFIRMED_VAR_1.host)} — it was waiting there for this session's approval; that question could not be carried over the restart and its withdrawal could not be confirmed. It has not run on ${TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_UNCONFIRMED_VAR_1.host} unless an approval reached it meanwhile. If it is still wanted, issue it again — ${TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_UNCONFIRMED_VAR_1.host} will ask for approval again where its settings require it.
