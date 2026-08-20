<!--
name: 'Tool Result: Artifact Watching Armed Status'
description: >-
  Watch tool_result explaining the live watch is armed, including auto-reply
  state branches.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_2
  - TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_3
  - TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_4
  - TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_5
  - TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_6
-->
${TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_0}Watching ${TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_1(TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_2.url)} — the watch is armed (\`status\` shows whether it has connected yet); this session is notified if another session republishes it (watch is session-local; ${TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_3}).${!TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_4()?"":TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_2.auto_reply==="armed"?' A comment on it sent to Claude also reaches this session (its status row says auto-replies armed); plain comments never notify — read them with action "comments" when asked.':TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_2.auto_reply===void 0?" It is still connecting, so whether a comment sent to Claude reaches this session through it is not settled — its `status` row will say (auto-replies armed, or not); plain comments never notify.":` Comments on it do NOT reach this session through this watch (auto-replies are ${TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_2.auto_reply==="none"?"not armed — a publish can arm them when comment auto-replies are on for this session, or resume_replies when the user asks":TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_5(TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_2.auto_reply)}); read them with action "comments" when the user asks.`}${TOOL_RESULT_ARTIFACT_WATCHING_ARMED_STATUS_VAR_6}
