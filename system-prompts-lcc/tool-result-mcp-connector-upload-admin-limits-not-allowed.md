<!--
name: Connector uploads unavailable with admin limits
description: >-
  Says connector file sending is unavailable in organizations with admin or
  HIPAA connector limits.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ADMIN_LIMITS_NOT_ALLOWED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ADMIN_LIMITS_NOT_ALLOWED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ADMIN_LIMITS_NOT_ALLOWED_VAR_0} was not sent: sending files to connectors is not available yet in organizations where an admin or a HIPAA setting can limit which connectors and tools are used, because Claude's upload service cannot check those limits, and this organization is one of them. Do not retry. Tell the user. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ADMIN_LIMITS_NOT_ALLOWED_VAR_1}
