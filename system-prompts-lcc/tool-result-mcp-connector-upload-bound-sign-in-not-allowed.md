<!--
name: Upload refuses session-bound sign-in
description: >-
  Says the upload service does not take files from a sign-in made for a single
  session or run.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_BOUND_SIGN_IN_NOT_ALLOWED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_BOUND_SIGN_IN_NOT_ALLOWED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_BOUND_SIGN_IN_NOT_ALLOWED_VAR_0} was not sent: Claude's upload service does not take files from the kind of sign-in this request came with: one made for a single session or run, not the user's own sign-in. Do not retry. Tell the user. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_BOUND_SIGN_IN_NOT_ALLOWED_VAR_1}
