<!--
name: 'Tool Result: Artifact watches list item'
description: >-
  Per-watch line in the watches tool result showing url, connection state,
  whether requested or publish-armed, and the since timestamp.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1
-->
- ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0.url} — ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0.connected?"connected":"reconnecting"}, ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0.explicit?"requested by you":"armed by a publish"}${TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0.auto_reply===void 0||TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0.auto_reply==="none"?"":TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0.auto_reply==="armed"?", auto-replies armed":TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0.auto_reply==="stopped"?", auto-replies stopped (the user can ask to resume them)":TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0.auto_reply==="disarmed"?", auto-replies disarmed for this session":`, auto-replies state: ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0.auto_reply}`}, since ${new TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1(TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0.since).toISOString()}
