<!--
name: 'Tool Result: Artifact Re-Watch Denied Without User-Turn Consent'
description: >-
  Permission denial telling the model a stopped artifact watch was not re-armed
  because the request did not come in a user-started turn.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_STOPPED_NO_USER_TURN_CONSENT_VAR_0
-->
Not watching: watching this artifact was stopped earlier in this session, and ${TOOL_RESULT_ARTIFACT_WATCH_STOPPED_NO_USER_TURN_CONSENT_VAR_0}. Raise it with the user; if they want it watched again, their own next message can ask for it. Do not reply to its comments yourself in this turn either — list them for the user.
