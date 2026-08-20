<!--
name: 'Tool Result: Artifact Resume Replies Stopped Again'
description: >-
  Reports that the user stopped auto-replies again while the resume was
  connecting.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_STOPPED_AGAIN_VAR_0
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_STOPPED_AGAIN_VAR_1
-->
Auto-replies were NOT resumed: the user stopped them again on ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_STOPPED_AGAIN_VAR_0(TOOL_RESULT_ARTIFACT_RESUME_REPLIES_STOPPED_AGAIN_VAR_1.url)} (or interrupted the session) while the resume was connecting. That newer stop stays in place — do not retry unless the user asks again. (The connection itself completes as a plain version watch — action "status" shows it.)
