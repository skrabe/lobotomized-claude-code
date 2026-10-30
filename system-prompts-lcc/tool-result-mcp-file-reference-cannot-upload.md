<!--
name: 'File reference: cannot upload'
description: The path doesn't exist or can't be sent by reference; base64 still works.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_VAR_0
  - TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_VAR_4
  - TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_VAR_2
  - TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_VAR_1
-->
Nothing was uploaded: ${TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_VAR_0} either does not exist or can't be sent by reference from here (this message doesn't say which). Check the path. If it is right, a reference won't work for this file${TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_VAR_4.readsBlocked?TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_VAR_2:`, but ${TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_VAR_1} still accepts a file's base64.`}
