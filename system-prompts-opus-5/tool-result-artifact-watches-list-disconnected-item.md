<!--
name: Watches List Disconnected Item
description: >-
  Per-watch line in the watches tool_result for a disconnected watch, including
  the auto-reply stop cause and resume guidance.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_2
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_3
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_4
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_5
-->
- ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_0(TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.url)} — not connected${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.explicit===void 0?"":`, ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_2(TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_3(TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.explicit===!0,TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_4(typeof TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.armed_via==="string"?TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.armed_via:void 0))).row}`}, ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.auto_reply==="disarmed"?"auto-replies disarmed for this session; no comment notifications arrive":`${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.stop_kind==="interrupt"?"auto-replies paused by the user's interrupt (Ctrl+C or Stop) and the connection has since dropped — the next publish of this artifact the user asks for reconnects and resumes them, or the user can ask to resume them (comments sent to Claude meanwhile are answered then); publishing it without being asked, while handling a notification or a wake-up, leaves them paused":TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.stop_kind==="user"?"auto-replies stopped when the watch was killed or unwatched — they stay stopped: a publish does not re-arm them; the user can ask to resume them or to watch this artifact again":"auto-replies stopped"}; no comment notifications arrive until then (do not republish or resume just to re-enable them unless the user asks)`}${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.since===void 0?"":`, watching since ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_5(TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.since)}`}
