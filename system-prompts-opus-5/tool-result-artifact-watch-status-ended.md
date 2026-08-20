<!--
name: 'Tool Result: Artifact Watch Status Ended'
description: >-
  Status-list row telling the model a watch ended and nothing will notify this
  session unless it watches again.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_STATUS_ENDED_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCH_STATUS_ENDED_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCH_STATUS_ENDED_VAR_2
  - TOOL_RESULT_ARTIFACT_WATCH_STATUS_ENDED_VAR_3
-->
- ${TOOL_RESULT_ARTIFACT_WATCH_STATUS_ENDED_VAR_0} — NOT watching: the watch ended at ${TOOL_RESULT_ARTIFACT_WATCH_STATUS_ENDED_VAR_1(TOOL_RESULT_ARTIFACT_WATCH_STATUS_ENDED_VAR_2.at)} (${TOOL_RESULT_ARTIFACT_WATCH_STATUS_ENDED_VAR_3(TOOL_RESULT_ARTIFACT_WATCH_STATUS_ENDED_VAR_2.reason)}). Nothing will notify this session about this artifact; pass action "watch" with its url if you need it again.
