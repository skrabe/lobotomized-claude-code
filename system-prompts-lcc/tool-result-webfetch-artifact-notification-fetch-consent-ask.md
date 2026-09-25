<!--
name: 'Tool Result: WebFetch Artifact — Notification-Prompted Fetch Consent Ask'
description: >-
  WebFetch consent ask for fetching an artifact prompted by the new-comments
  notification, noting its content enters this conversation; becomes the tool
  result on decline.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_WEBFETCH_ARTIFACT_NOTIFICATION_FETCH_CONSENT_ASK_VAR_0
  - TOOL_RESULT_WEBFETCH_ARTIFACT_NOTIFICATION_FETCH_CONSENT_ASK_VAR_1
  - TOOL_RESULT_WEBFETCH_ARTIFACT_NOTIFICATION_FETCH_CONSENT_ASK_VAR_2
-->
${TOOL_RESULT_WEBFETCH_ARTIFACT_NOTIFICATION_FETCH_CONSENT_ASK_VAR_0?.TOOL_RESULT_WEBFETCH_ARTIFACT_NOTIFICATION_FETCH_CONSENT_ASK_VAR_1??`Claude wants to fetch the artifact at ${TOOL_RESULT_WEBFETCH_ARTIFACT_NOTIFICATION_FETCH_CONSENT_ASK_VAR_2}`} — prompted by the new-comments notification; its content enters this conversation
