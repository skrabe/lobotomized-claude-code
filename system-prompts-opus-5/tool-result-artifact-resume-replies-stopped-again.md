<!--
name: 'Tool result: Artifact resume replies stopped again'
description: >-
  Reports that the user stopped auto-replies again while the resume was
  connecting
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_STOPPED_AGAIN_VAR_0
-->
Auto-replies were NOT resumed: the user stopped them again on ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_STOPPED_AGAIN_VAR_0.url} (or interrupted the session) while the resume was connecting. That newer stop stays in place — do not retry unless the user asks again. (The connection itself completes as a plain version watch — action "status" shows it.)
