<!--
name: 'Tool Result: MCP connector path resolves elsewhere'
description: >-
  Refuses sending a file whose path resolves to another path and tells Claude to
  call again with the resolved path
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_PATH_RESOLVES_ELSEWHERE_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_PATH_RESOLVES_ELSEWHERE_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_PATH_RESOLVES_ELSEWHERE_VAR_2
-->
Cannot send ${TOOL_RESULT_MCP_CONNECTOR_PATH_RESOLVES_ELSEWHERE_VAR_0}: it resolves to another path${TOOL_RESULT_MCP_CONNECTOR_PATH_RESOLVES_ELSEWHERE_VAR_1===void 0?", through a link or a name that is stored otherwise":`, "${TOOL_RESULT_MCP_CONNECTOR_PATH_RESOLVES_ELSEWHERE_VAR_1}"`}. A file is sent only by the path it resolves to, so that the path a person approves names the file that is sent. If that is the file you mean, call again with ${TOOL_RESULT_MCP_CONNECTOR_PATH_RESOLVES_ELSEWHERE_VAR_1===void 0?"the path it resolves to":"that path"}. ${TOOL_RESULT_MCP_CONNECTOR_PATH_RESOLVES_ELSEWHERE_VAR_2}
