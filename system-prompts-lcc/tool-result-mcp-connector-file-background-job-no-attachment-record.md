<!--
name: 'Tool Result: MCP connector file background-job no attachment record'
description: >-
  Refuses a connector file upload from a background job because the session
  keeps no record of attached files, and says how the user can send it instead
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_NO_ATTACHMENT_RECORD_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_NO_ATTACHMENT_RECORD_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_NO_ATTACHMENT_RECORD_VAR_2
-->
Cannot send ${TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_NO_ATTACHMENT_RECORD_VAR_0} ${TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_NO_ATTACHMENT_RECORD_VAR_1}: this session runs a background job, and a background job can send to a connector only a file that Claude Code has on record as attached by the user. This session keeps no such record, so no file can be sent from it, not even one attached to the chat. To send this file, the user can ask in a session that runs no background job, which can send a file that is in the folder it was started in or in a folder added for it (--add-dir, or /add-dir with "Yes, for this session", or a folder allowed on a prompt), if that session may read it. ${TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_NO_ATTACHMENT_RECORD_VAR_2}
