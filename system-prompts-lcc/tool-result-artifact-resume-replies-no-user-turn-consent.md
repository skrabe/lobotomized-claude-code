<!--
name: 'Tool Result: Artifact Resume Replies No User-Turn Consent'
description: >-
  Permission denial telling the model auto-replies were not resumed because the
  request did not come in a user-started turn.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_NO_USER_TURN_CONSENT_VAR_0
-->
Auto-replies were NOT resumed: ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_NO_USER_TURN_CONSENT_VAR_0}, so there is no consent to reverse the stop. Raise it with the user; if they do want auto-replies back, their own next message can ask for it. Do not retry it in this turn, and do not reply to the comments yourself in this turn either — list them for the user.
