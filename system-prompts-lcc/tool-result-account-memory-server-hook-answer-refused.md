<!--
name: 'Plugin hook answered in a tool''s place: refused'
description: >-
  Tool denial text used when a plugin hook answers a call in place of the tool
  (or account memory server); becomes the tool_result the model reads.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_ACCOUNT_MEMORY_SERVER_HOOK_ANSWER_REFUSED_VAR_0
  - TOOL_RESULT_ACCOUNT_MEMORY_SERVER_HOOK_ANSWER_REFUSED_VAR_1
-->
A plugin hook answered a call to ${TOOL_RESULT_ACCOUNT_MEMORY_SERVER_HOOK_ANSWER_REFUSED_VAR_0(TOOL_RESULT_ACCOUNT_MEMORY_SERVER_HOOK_ANSWER_REFUSED_VAR_1)?"the account memory server in place of the server":`${TOOL_RESULT_ACCOUNT_MEMORY_SERVER_HOOK_ANSWER_REFUSED_VAR_1.name} in place of the tool`}; the call is refused.
