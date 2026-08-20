<!--
name: 'Tool Result: Artifact watches list item'
description: >-
  Per-watch line in the watches tool result showing url, connection state,
  whether requested or publish-armed, and the since timestamp.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1
-->
- ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_0(TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1.url)} — ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1.connected?TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1.connecting===!0?"connecting (handshake not finished; nothing reaches it yet)":"connected":"reconnecting"}, ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_2(TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_3(TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1.explicit,TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_4(TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1.armed_via))).row}${TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1.auto_reply===void 0||TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1.auto_reply==="none"?"":TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1.auto_reply==="armed"?", auto-replies armed":TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1.auto_reply==="stopped"?", auto-replies stopped (the user can ask to resume them)":TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1.auto_reply==="disarmed"?", auto-replies disarmed for this session":""}, since ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_5(TOOL_RESULT_ARTIFACT_WATCHES_LIST_ITEM_VAR_1.since)}
