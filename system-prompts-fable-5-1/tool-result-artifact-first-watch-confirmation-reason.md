<!--
name: Artifact First Watch Confirmation Reason
description: >-
  Default first-watch decisionReason: a republish (and optional comment-wake)
  subscription is held for the rest of the session.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_FIRST_WATCH_CONFIRMATION_REASON_VAR_0
  - TOOL_RESULT_ARTIFACT_FIRST_WATCH_CONFIRMATION_REASON_VAR_1
-->
First artifact watch this session requires confirmation — a subscription to republish notifications${TOOL_RESULT_ARTIFACT_FIRST_WATCH_CONFIRMATION_REASON_VAR_0()?" (and, in cloud sessions, comment wakes)":""} is held for the rest of the session; later watches are not re-asked${TOOL_RESULT_ARTIFACT_FIRST_WATCH_CONFIRMATION_REASON_VAR_1?" unless they would turn on auto-replies for an artifact":""}; republish notifications carry no content
