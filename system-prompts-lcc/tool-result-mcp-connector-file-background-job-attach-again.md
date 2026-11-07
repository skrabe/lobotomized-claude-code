<!--
name: 'Tool Result: MCP connector file background-job attach-again refusal'
description: >-
  Refuses a connector file upload from a background job because only files
  attached since the job last started can be sent, so the file must be attached
  again
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_ATTACH_AGAIN_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_ATTACH_AGAIN_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_ATTACH_AGAIN_VAR_2
  - TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_ATTACH_AGAIN_VAR_3
-->
Cannot send ${TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_ATTACH_AGAIN_VAR_0} ${TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_ATTACH_AGAIN_VAR_1}: this session runs a background job, and from a background job only a file the user attached to the chat since the job last started can be sent to a connector; a file attached before it restarted, or before a window took it over, has to be attached again. ${TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_ATTACH_AGAIN_VAR_2} ${TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_ATTACH_AGAIN_VAR_3}
