<!--
name: 'Tool Result: Dir Sync Could Not Take In Refused'
description: >-
  Cause when the host refused mid-turn catch-up (too many concurrent, cancelled,
  failed, or an unknown reason).
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_DIR_SYNC_COULD_NOT_TAKE_IN_REFUSED_VAR_0
  - TOOL_RESULT_DIR_SYNC_COULD_NOT_TAKE_IN_REFUSED_VAR_1
-->
${TOOL_RESULT_DIR_SYNC_COULD_NOT_TAKE_IN_REFUSED_VAR_0} could not take in this session's latest file changes first (${TOOL_RESULT_DIR_SYNC_COULD_NOT_TAKE_IN_REFUSED_VAR_1==="other"?"it refused for a reason this version does not know":`its Claude Code said: ${TOOL_RESULT_DIR_SYNC_COULD_NOT_TAKE_IN_REFUSED_VAR_1.replace(/_/g," ")}`})
