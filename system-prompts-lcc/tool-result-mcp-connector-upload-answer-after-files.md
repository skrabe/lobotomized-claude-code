<!--
name: 'Tool result: MCP connector upload answer after files'
description: >-
  Connector upload error: the connector asked for something more after files
  were sent, so the call did not finish.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_AFTER_FILES_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_AFTER_FILES_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_AFTER_FILES_VAR_2
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_AFTER_FILES_VAR_0.length===0?"When the call was repeated":"After this call's files were sent"}, the connector asked for something more, which Claude Code does not answer in a call that sends files, so ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_AFTER_FILES_VAR_1} did not finish.${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_AFTER_FILES_VAR_2} Tell the user before ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ANSWER_AFTER_FILES_VAR_0.length===0?"calling it":"sending"} again.
