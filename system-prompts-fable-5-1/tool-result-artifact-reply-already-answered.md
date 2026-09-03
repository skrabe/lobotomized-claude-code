<!--
name: Artifact Reply Already Answered
description: >-
  Artifact reply tool result telling the model that another session already
  answered the summon, its draft was discarded, and it should read rather than
  retry.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_REPLY_ALREADY_ANSWERED_VAR_0
-->
Reply not posted: this thread's request to Claude already has a standing answer from a Claude session${TOOL_RESULT_ARTIFACT_REPLY_ALREADY_ANSWERED_VAR_0!==void 0?` (comment ${TOOL_RESULT_ARTIFACT_REPLY_ALREADY_ANSWERED_VAR_0})`:""}. The draft was discarded. Do not retry — read the thread (action "comments") to see the answer that landed.
