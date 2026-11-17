<!--
name: 'Tool result: MCP connector upload state-only answer'
description: >-
  Connector upload error when the connector's answer was state-only: call did
  not finish, tell the user before calling again.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_STATE_ONLY_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_STATE_ONLY_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_STATE_ONLY_VAR_2
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_STATE_ONLY_VAR_3
-->
The connector's answer was not one Claude Code can act on: ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_STATE_ONLY_VAR_0.state_only}. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_STATE_ONLY_VAR_1} did not finish.${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_STATE_ONLY_VAR_2} Tell the user before ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_STATE_ONLY_VAR_3.length===0?"calling it":"sending"} again.
