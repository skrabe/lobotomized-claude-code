<!--
name: Connector storage failed
description: >-
  Says forwarding the file to the connector's storage failed (with the storage's
  HTTP status when known) and that part of it may be there; ask before retrying.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_FAILED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_FAILED_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_FAILED_VAR_2
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_FAILED_VAR_3
-->
Sending ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_FAILED_VAR_0} on to the connector's storage failed${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_FAILED_VAR_1===void 0?", so the":`: the storage answered HTTP ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_FAILED_VAR_1}. The`} connector should not have the whole file; part of it may be in its storage. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_FAILED_VAR_2}${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_FAILED_VAR_3}
