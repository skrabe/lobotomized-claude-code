<!--
name: Artifact Reply Posted
description: >-
  tool_result content confirming a reply landed on a comment thread and noting
  viewers see it attributed as "Claude · via the user".
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_ARTIFACT_REPLY_POSTED_VAR_0
  - TOOL_RESULT_ARTIFACT_REPLY_POSTED_VAR_1
-->

Replied to comment thread ${TOOL_RESULT_ARTIFACT_REPLY_POSTED_VAR_0??"(id unreadable)"}${TOOL_RESULT_ARTIFACT_REPLY_POSTED_VAR_1!==void 0?` (comment ${TOOL_RESULT_ARTIFACT_REPLY_POSTED_VAR_1})`:""}.
