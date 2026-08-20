<!--
name: Watches List Disconnected Item
description: >-
  Per-watch line in the watches tool_result for a disconnected watch, including
  auto-reply stop cause.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_2
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_3
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_4
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_5
-->
- ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_0(TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.url)} — not connected${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.explicit===void 0?"":`, ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_2(TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_3(TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.explicit,TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_4(TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.armed_via))).row}`}, ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.auto_reply==="disarmed"?"auto-replies disarmed for this session; no comment notifications arrive":`${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.stop_kind==="interrupt"?"auto-replies stopped when the user interrupted the session (Ctrl+C or Stop) — the next publish of this artifact in a turn the user starts re-arms them, or the user can ask to resume them (comments sent to Claude meanwhile are picked up then); a publish from an unattended turn leaves them stopped":TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.stop_kind==="user"?"auto-replies stopped when the watch was killed or unwatched — they stay stopped: a publish does not re-arm them; the user can ask to resume them or to watch this artifact again":"auto-replies stopped"}; no comment notifications arrive until then (do not republish or resume just to re-enable them unless the user asks)`}${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.since===void 0?"":`, watching since ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_5(TOOL_RESULT_ARTIFACT_WATCHES_LIST_DISCONNECTED_ITEM_VAR_1.since)}`}
