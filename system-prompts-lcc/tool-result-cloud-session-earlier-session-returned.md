<!--
name: 'Tool Result: Cloud session earlier session returned'
description: >-
  Create-fail text when the service answered with a cloud session it had already
  created for this request: no new session started, the prompt may not have been
  sent, and the existing session should be inspected before rerunning the
  command
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_CLOUD_SESSION_EARLIER_SESSION_RETURNED_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_EARLIER_SESSION_RETURNED_VAR_1
-->
No new cloud session was started: the service answered with a session it had already created for this request.${TOOL_RESULT_CLOUD_SESSION_EARLIER_SESSION_RETURNED_VAR_0.promptHeld?" Your prompt was not sent.":""} That session was left as it is. Look at it before you run the command again: ${TOOL_RESULT_CLOUD_SESSION_EARLIER_SESSION_RETURNED_VAR_1(TOOL_RESULT_CLOUD_SESSION_EARLIER_SESSION_RETURNED_VAR_0.sessionUrl)}
