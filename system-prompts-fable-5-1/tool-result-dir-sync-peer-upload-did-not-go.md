<!--
name: 'Tool Result: Dir Sync Peer Upload Did Not Go'
description: >-
  Cause when the host is holding this session's changes until it can upload its
  own and that upload did not go.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_DIR_SYNC_PEER_UPLOAD_DID_NOT_GO_VAR_0
  - TOOL_RESULT_DIR_SYNC_PEER_UPLOAD_DID_NOT_GO_VAR_1
-->
${TOOL_RESULT_DIR_SYNC_PEER_UPLOAD_DID_NOT_GO_VAR_0.name} holds as many of this session's changes as it takes before uploading its own, and that upload did not go (${TOOL_RESULT_DIR_SYNC_PEER_UPLOAD_DID_NOT_GO_VAR_1.kind==="kept_here"?TOOL_RESULT_DIR_SYNC_PEER_UPLOAD_DID_NOT_GO_VAR_1.detail||TOOL_RESULT_DIR_SYNC_PEER_UPLOAD_DID_NOT_GO_VAR_1.reason:TOOL_RESULT_DIR_SYNC_PEER_UPLOAD_DID_NOT_GO_VAR_1.kind==="failed"?TOOL_RESULT_DIR_SYNC_PEER_UPLOAD_DID_NOT_GO_VAR_1.reason:TOOL_RESULT_DIR_SYNC_PEER_UPLOAD_DID_NOT_GO_VAR_1.kind})
