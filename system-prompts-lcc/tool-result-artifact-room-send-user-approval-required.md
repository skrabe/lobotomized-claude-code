<!--
name: 'Tool Result: Artifact room_send User Approval Required'
description: >-
  safetyCheck decisionReason for the room_send ask: viewer page events can steer
  the broadcast, so the auto-permission classifier must not approve it.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_ARTIFACT_ROOM_SEND_USER_APPROVAL_REQUIRED_VAR_0
  - TOOL_RESULT_ARTIFACT_ROOM_SEND_USER_APPROVAL_REQUIRED_VAR_1
-->
Sending a live event to everyone currently viewing the artifact${TOOL_RESULT_ARTIFACT_ROOM_SEND_USER_APPROVAL_REQUIRED_VAR_0}${TOOL_RESULT_ARTIFACT_ROOM_SEND_USER_APPROVAL_REQUIRED_VAR_1} can be steered by those viewers' page events — approval must come from the user, not the auto-permission classifier
