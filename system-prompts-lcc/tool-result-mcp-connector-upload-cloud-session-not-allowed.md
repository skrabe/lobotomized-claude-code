<!--
name: Connector uploads unavailable in cloud sessions
description: >-
  Says the upload service does not yet take files from cloud Claude Code
  sessions.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CLOUD_SESSION_NOT_ALLOWED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CLOUD_SESSION_NOT_ALLOWED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CLOUD_SESSION_NOT_ALLOWED_VAR_0} was not sent: Claude's upload service does not take files yet from Claude Code sessions that run in the cloud, nor from chats and tasks that run as one, and it took this request for one of those. Do not retry. Tell the user. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CLOUD_SESSION_NOT_ALLOWED_VAR_1}
