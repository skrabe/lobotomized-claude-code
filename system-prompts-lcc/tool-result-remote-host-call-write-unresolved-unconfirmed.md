<!--
name: Remote Host Call Write Unresolved Unconfirmed
description: >-
  Full tool result telling the model a backed-up upload left it unknown whether
  the remote command ran, so it must check before retrying.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_REMOTE_HOST_CALL_WRITE_UNRESOLVED_UNCONFIRMED_VAR_0
-->
This call may or may not have reached ${TOOL_RESULT_REMOTE_HOST_CALL_WRITE_UNRESOLVED_UNCONFIRMED_VAR_0}: this session's connection to the service was backed up and the upload carrying it could not be confirmed in time, and what became of it could not be learned from ${TOOL_RESULT_REMOTE_HOST_CALL_WRITE_UNRESOLVED_UNCONFIRMED_VAR_0} afterwards. This is not a problem with ${TOOL_RESULT_REMOTE_HOST_CALL_WRITE_UNRESOLVED_UNCONFIRMED_VAR_0}. Check whether the command took effect before re-running it.
