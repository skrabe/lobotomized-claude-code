<!--
name: 'Tool Result: Remote host parked approval at restart (not asked since)'
description: >-
  Tells the model a command waiting for approval at restart was likely not run
  and the host has not been asked since
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_HOST_PARKED_APPROVAL_AT_RESTART_NOT_ASKED_VAR_0
-->
This command was waiting for approval on ${TOOL_RESULT_REMOTE_HOST_PARKED_APPROVAL_AT_RESTART_NOT_ASKED_VAR_0.host} when the session restarted and was not run there — unless an approval reached ${TOOL_RESULT_REMOTE_HOST_PARKED_APPROVAL_AT_RESTART_NOT_ASKED_VAR_0.host} in the moment before the restart, which this session cannot rule out. ${TOOL_RESULT_REMOTE_HOST_PARKED_APPROVAL_AT_RESTART_NOT_ASKED_VAR_0.host} has not been asked about it since.
