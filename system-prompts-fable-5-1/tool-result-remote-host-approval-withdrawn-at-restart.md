<!--
name: 'Tool Result: Remote Host Approval Withdrawn At Restart'
description: >-
  Remote-host tool_result when a pending approval could not be carried over a
  restart and the command was not run.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_AT_RESTART_VAR_0
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_AT_RESTART_VAR_1
-->
${TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_AT_RESTART_VAR_0(TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_AT_RESTART_VAR_1.host)} — it was waiting there for this session's approval, and that question could not be carried over the restart, so it has been withdrawn: the command was NOT run on ${TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_AT_RESTART_VAR_1.host}. If it is still wanted, issue it again — ${TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_AT_RESTART_VAR_1.host} will ask for approval again where its settings require it.
