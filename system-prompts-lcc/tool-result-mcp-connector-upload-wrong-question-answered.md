<!--
name: 'Tool result: MCP connector upload wrong question answered'
description: >-
  Reports no file was sent because the answered question was not Claude Code's
  upload prompt
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_WRONG_QUESTION_ANSWERED_VAR_0
-->
No file was sent: the question answered for this call was not the upload prompt that says what the call sends and to which connector (a plugin's permission check may have asked in its place), and only an Allow on that prompt sends files. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_WRONG_QUESTION_ANSWERED_VAR_0}
