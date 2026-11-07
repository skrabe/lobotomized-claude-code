<!--
name: 'Tool Result: MCP file upload refused, connection lacks extension'
description: >-
  Error saying no file was sent and the tool was not called because the MCP
  connection does not support the file-uploads extension
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_FILE_UPLOAD_CONNECTION_LACKS_EXTENSION_VAR_0
-->
No file was sent and the tool was not called: Claude Code sends a file only on an MCP protocol 2026-07-28 connection to a server that advertises file uploads (the file-uploads extension with "upload"), and this connection to MCP server "${TOOL_RESULT_MCP_FILE_UPLOAD_CONNECTION_LACKS_EXTENSION_VAR_0}" is not one.
