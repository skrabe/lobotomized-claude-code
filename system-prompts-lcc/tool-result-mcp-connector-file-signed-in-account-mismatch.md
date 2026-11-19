<!--
name: 'Tool Result: MCP connector file signed-in account mismatch'
description: >-
  Says no file was sent because the session and config disagree on the signed-in
  account
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGNED_IN_ACCOUNT_MISMATCH_VAR_0
-->
No file was sent: this session and Claude Code's configuration file do not agree on which Claude account is signed in. That can last a moment while somebody signs in or out in another window. Tell the user: the call can be made again once that is done, or after they run /login. ${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGNED_IN_ACCOUNT_MISMATCH_VAR_0}
