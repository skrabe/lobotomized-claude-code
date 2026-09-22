<!--
name: 'Tool Result: Remote Host Parked Approval At Restart'
description: >-
  Remote-host refused tool_result when a command was waiting for approval at
  restart and may still have been approved in the last moment.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_REMOTE_HOST_PARKED_APPROVAL_AT_RESTART_VAR_0
-->
This command was waiting for approval on ${TOOL_RESULT_REMOTE_HOST_PARKED_APPROVAL_AT_RESTART_VAR_0.host} when the session restarted and was not run there — unless an approval reached ${TOOL_RESULT_REMOTE_HOST_PARKED_APPROVAL_AT_RESTART_VAR_0.host} in the moment before the restart, which this session cannot rule out. If it is still wanted, issue it again — ${TOOL_RESULT_REMOTE_HOST_PARKED_APPROVAL_AT_RESTART_VAR_0.host} will ask for approval again where its settings require it.
