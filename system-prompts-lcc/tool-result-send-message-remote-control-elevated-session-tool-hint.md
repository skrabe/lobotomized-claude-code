<!--
name: 'Tool Result: SendMessage Remote Control elevated session tool hint'
description: >-
  Hint appended to a SendMessage Remote Control failure saying the target may be
  reachable with the session service's own send tool and giving that session's
  id.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_MESSAGE_REMOTE_CONTROL_ELEVATED_SESSION_TOOL_HINT_VAR_0
-->
This target may be reachable with ${TOOL_RESULT_SEND_MESSAGE_REMOTE_CONTROL_ELEVATED_SESSION_TOOL_HINT_VAR_0.sendTool}, the session service's own tool, if your user has allowed this cloud session to reach that computer; that session's id there is "${TOOL_RESULT_SEND_MESSAGE_REMOTE_CONTROL_ELEVATED_SESSION_TOOL_HINT_VAR_0.sessionId}". A tool of that name on any other server is not it.
