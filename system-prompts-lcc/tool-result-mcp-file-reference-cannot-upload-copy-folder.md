<!--
name: 'Tool Result: MCP file reference cannot upload outside copy folder'
description: >-
  File-reference refusal: files under a folder can't be sent by reference, but
  files copied into the named folder can, and base64 still works
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_COPY_FOLDER_VAR_0
  - TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_COPY_FOLDER_VAR_1
  - TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_COPY_FOLDER_VAR_2
-->
Nothing was uploaded: files under ${TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_COPY_FOLDER_VAR_0.copy.from} can't be sent by reference. Files in ${TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_COPY_FOLDER_VAR_1(TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_COPY_FOLDER_VAR_0.copy.into)} can, if nothing else refuses them. ${TOOL_RESULT_MCP_FILE_REFERENCE_CANNOT_UPLOAD_COPY_FOLDER_VAR_2} still accepts a file's base64.
