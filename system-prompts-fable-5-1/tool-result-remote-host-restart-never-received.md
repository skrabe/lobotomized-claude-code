<!--
name: 'Tool Result: Remote Host Restart Never Received'
description: >-
  Remote-host tool_result when the session restarted before the command reached
  the host and the host reports it never ran.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_REMOTE_HOST_RESTART_NEVER_RECEIVED_VAR_0
-->
This session restarted before this command reached ${TOOL_RESULT_REMOTE_HOST_RESTART_NEVER_RECEIVED_VAR_0.host}; ${TOOL_RESULT_REMOTE_HOST_RESTART_NEVER_RECEIVED_VAR_0.host} reports it never received it: it did not run there. Issue it again if it is still wanted.
