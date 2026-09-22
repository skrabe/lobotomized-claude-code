<!--
name: 'Tool Result: Resume Replies Refused — Arm In Flight'
description: >-
  Tells the model resume_replies could not attach because a live-watch
  connection that started before the stop is still winding down, and to check
  action status then ask the user before retrying.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_ARM_IN_FLIGHT_VAR_0
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_ARM_IN_FLIGHT_VAR_1
-->
Auto-replies were NOT resumed: a live-watch connection for ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_ARM_IN_FLIGHT_VAR_0(TOOL_RESULT_ARTIFACT_RESUME_REPLIES_ARM_IN_FLIGHT_VAR_1.url)} that started before the watch was stopped is still winding down, and a resume cannot attach to it — that connection ends on its own and the stop stays in place. Check action "status"; then ask the user, and call resume_replies again only if they still want auto-replies resumed.
