<!--
name: 'Tool Result: remote tool call uncheckable without a working directory'
description: >-
  Refusal ruleMessage when a forwarded remote tool call cannot be checked
  against permission rules because the session has no working directory.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_TOOL_NO_WORKING_DIRECTORY_UNCHECKABLE_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_NO_WORKING_DIRECTORY_UNCHECKABLE_VAR_1
-->
This session can't check this ${TOOL_RESULT_REMOTE_TOOL_NO_WORKING_DIRECTORY_UNCHECKABLE_VAR_0.name} call against its permission rules: it has no working directory to resolve a relative path in, and ${TOOL_RESULT_REMOTE_TOOL_NO_WORKING_DIRECTORY_UNCHECKABLE_VAR_1.name} named none it could use. Retrying the same call won't help; an absolute path may.
