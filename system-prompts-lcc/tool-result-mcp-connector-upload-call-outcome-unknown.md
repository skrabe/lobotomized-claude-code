<!--
name: Connector call receipt unknown
description: >-
  Says it is unknown whether the connector received the call and no file was
  sent.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CALL_OUTCOME_UNKNOWN_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CALL_OUTCOME_UNKNOWN_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CALL_OUTCOME_UNKNOWN_VAR_2
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CALL_OUTCOME_UNKNOWN_VAR_3
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CALL_OUTCOME_UNKNOWN_VAR_0}${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CALL_OUTCOME_UNKNOWN_VAR_1==="again"?"The connector had answered by asking for the call to be made again, so it is":TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CALL_OUTCOME_UNKNOWN_VAR_2===void 0?`It is not known whether the connector received the call to ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CALL_OUTCOME_UNKNOWN_VAR_3}, so it is`:"It is"} not known whether ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CALL_OUTCOME_UNKNOWN_VAR_3} ran. No file was sent. Tell the user before calling it again.
