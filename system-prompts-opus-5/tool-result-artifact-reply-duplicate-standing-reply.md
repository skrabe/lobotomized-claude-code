<!--
name: 'Tool Result: Artifact reply refused as duplicate of standing reply'
description: >-
  Artifact tool result explaining that the reply was not posted because a Claude
  reply already stands after every "sent to Claude" request on the thread, and
  that acknowledge_duplicate: true is needed for a genuinely new follow-up
ccVersion: 2.1.233
variables:
  - TOOL_RESULT_ARTIFACT_REPLY_DUPLICATE_STANDING_REPLY_VAR_0
-->
Reply not posted: a Claude reply${TOOL_RESULT_ARTIFACT_REPLY_DUPLICATE_STANDING_REPLY_VAR_0!==void 0?` (comment ${TOOL_RESULT_ARTIFACT_REPLY_DUPLICATE_STANDING_REPLY_VAR_0})`:""} already stands after every "sent to Claude" request on this thread, so another reply would read as a duplicate to the commenter. The draft was discarded. Read the thread (action "comments") if you have not; only if a further reply adds something genuinely new, send it again with acknowledge_duplicate: true.
