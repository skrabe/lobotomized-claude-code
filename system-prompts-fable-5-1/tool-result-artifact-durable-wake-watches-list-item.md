<!--
name: 'Tool Result: Artifact Durable Wake Watches List Item'
description: >-
  Per-watch line in the Artifact watches result for a durable-wake subscription,
  including wake events and since time.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_0
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_1
-->
- ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_0(TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_1.url)} — durable wake subscription (woken on ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_2.isArray(TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_1.events)&&TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_1.events.includes("comment")?"publish and to-Claude comments":"publish"}; no live updates), since ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_3(TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_1.since)}${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_WATCHES_LIST_ITEM_VAR_1.restored===!0?"; restored after this session restarted and not re-verified since (no action needed unless the user asks)":""}
