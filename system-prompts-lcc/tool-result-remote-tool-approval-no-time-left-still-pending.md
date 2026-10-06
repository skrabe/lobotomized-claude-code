<!--
name: Approval arrived with no time left to run call
description: >-
  tool_result message when an approval reaches the target with no time left to
  run the call because admission took longer than the caller allowed.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_REMOTE_TOOL_APPROVAL_NO_TIME_LEFT_STILL_PENDING_VAR_0
-->
The approval reached ${TOOL_RESULT_REMOTE_TOOL_APPROVAL_NO_TIME_LEFT_STILL_PENDING_VAR_0.targetName} with no time left to run the call (admission took longer than the caller allowed) — nothing ran, and the approval is used up. Run the tool again if it is still needed.
