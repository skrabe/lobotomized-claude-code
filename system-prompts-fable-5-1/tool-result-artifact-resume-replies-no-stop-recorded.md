<!--
name: Auto-Replies Not Resumed — No Stop Recorded
description: >-
  resume_replies tool_result when reason is not_stopped: no auto-reply stop is
  recorded for this artifact, so there is nothing to resume.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_NO_STOP_RECORDED_VAR_0
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_NO_STOP_RECORDED_VAR_1
-->
Auto-replies were NOT resumed: no auto-reply stop is recorded for ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_NO_STOP_RECORDED_VAR_0(TOOL_RESULT_ARTIFACT_RESUME_REPLIES_NO_STOP_RECORDED_VAR_1.url)} in this session — there is nothing to resume (an interrupt's pause already lifts when the user sends a message). Whether auto-replies can arm here at all, and what is armed now, is what action "status" reports (a publish result reports the watch); do not tell the user they are on until status or a result line says so.
