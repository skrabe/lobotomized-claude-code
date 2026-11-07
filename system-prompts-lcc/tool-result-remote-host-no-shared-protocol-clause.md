<!--
name: 'Tool Result: Remote host no shared protocol clause'
description: >-
  Clause explaining that the two Claude Code builds share no remote-tool
  protocol version, listing the machine's and this session's versions
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_REMOTE_HOST_NO_SHARED_PROTOCOL_CLAUSE_VAR_0
  - TOOL_RESULT_REMOTE_HOST_NO_SHARED_PROTOCOL_CLAUSE_VAR_1
  - TOOL_RESULT_REMOTE_HOST_NO_SHARED_PROTOCOL_CLAUSE_VAR_2
-->
the two Claude Code builds share no remote-tool protocol version (${TOOL_RESULT_REMOTE_HOST_NO_SHARED_PROTOCOL_CLAUSE_VAR_0.length>0?`its remote-tool protocol ${TOOL_RESULT_REMOTE_HOST_NO_SHARED_PROTOCOL_CLAUSE_VAR_0.map((TOOL_RESULT_REMOTE_HOST_NO_SHARED_PROTOCOL_CLAUSE_VAR_1)=>`v${TOOL_RESULT_REMOTE_HOST_NO_SHARED_PROTOCOL_CLAUSE_VAR_1}`).join("/")}, ours ${TOOL_RESULT_REMOTE_HOST_NO_SHARED_PROTOCOL_CLAUSE_VAR_2}`:`it names no remote-tool protocol version this session reads; ours is ${TOOL_RESULT_REMOTE_HOST_NO_SHARED_PROTOCOL_CLAUSE_VAR_2}`})
