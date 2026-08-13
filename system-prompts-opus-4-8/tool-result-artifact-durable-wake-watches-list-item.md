<!--
name: 'Tool Result: Artifact Durable Wake Watches List Item'
description: >-
  Per-watch line in the Artifact watches result for a durable-wake subscription,
  including wake events and since time.
ccVersion: 2.1.231
variables:
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_0
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_1
-->
- ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_0.url} — durable wake subscription (woken on ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_0.events?.TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_1("comment")?"publish and to-Claude comments":"publish"}; no live updates), since ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_0.since}
