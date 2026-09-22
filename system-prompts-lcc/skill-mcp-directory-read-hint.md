<!--
name: MCP skill directory-read hint
description: >-
  Fragment appended to an MCP-served skill's description telling the model how
  to list a directory URI's contents.
ccVersion: 2.1.206
variables:
  - SKILL_MCP_DIRECTORY_READ_HINT_VAR_0
  - SKILL_MCP_DIRECTORY_READ_HINT_VAR_1
-->
 Call ${SKILL_MCP_DIRECTORY_READ_HINT_VAR_0} on "${SKILL_MCP_DIRECTORY_READ_HINT_VAR_1.uri}" or a subdirectory URI to list its contents.
