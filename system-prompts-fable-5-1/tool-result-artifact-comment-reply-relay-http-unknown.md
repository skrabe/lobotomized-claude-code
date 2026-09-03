<!--
name: Comment reply outcome unknown — relay HTTP error
description: >-
  Artifact tool error telling Claude a comment reply may or may not have posted
  after a relay HTTP failure, and to re-read the comments before retrying.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_COMMENT_REPLY_RELAY_HTTP_UNKNOWN_VAR_0
-->
comment reply outcome unknown (relay HTTP ${TOOL_RESULT_ARTIFACT_COMMENT_REPLY_RELAY_HTTP_UNKNOWN_VAR_0.status}) — it may have posted; re-read the comments before retrying
