<!--
name: 'Tool result: read ask for UNC path'
description: >-
  Permission ask message when Claude requests to read a UNC path that could
  access network resources
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_UNC_PATH_READ_ASK_VAR_0
  - TOOL_RESULT_UNC_PATH_READ_ASK_VAR_1
-->
Claude requested permissions to read from ${TOOL_RESULT_UNC_PATH_READ_ASK_VAR_0(TOOL_RESULT_UNC_PATH_READ_ASK_VAR_1)}, which appears to be a UNC path that could access network resources.
