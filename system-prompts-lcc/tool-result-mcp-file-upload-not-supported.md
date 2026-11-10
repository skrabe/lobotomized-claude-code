<!--
name: 'Tool Result: MCP file upload not supported'
description: >-
  Error when a tool call sends files to an MCP server that is not on protocol
  2026-07-28 or does not list upload in its file-uploads extension
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_MCP_FILE_UPLOAD_NOT_SUPPORTED_VAR_0
-->
Claude Code didn't send any file or run the tool: it sends files to "${TOOL_RESULT_MCP_FILE_UPLOAD_NOT_SUPPORTED_VAR_0}" only over MCP protocol version 2026-07-28, and only when the server lists "upload" in its file-uploads extension.
