<!--
name: URL elicitation declined by user
description: >-
  MCP tool_result returned to the model when URL elicitation was declined by the
  user and the tool could not complete.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_URL_ELICITATION_DECLINED_USER_VAR_0
  - TOOL_RESULT_URL_ELICITATION_DECLINED_USER_VAR_1
-->
URL elicitation was ${TOOL_RESULT_URL_ELICITATION_DECLINED_USER_VAR_0.action==="decline"?"declined":TOOL_RESULT_URL_ELICITATION_DECLINED_USER_VAR_0.action+"ed"} by the user. The tool "${TOOL_RESULT_URL_ELICITATION_DECLINED_USER_VAR_1}" could not complete because it requires the user to open a URL.
