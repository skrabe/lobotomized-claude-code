<!--
name: 'Remote Tool: Ask-First With No Prompt Surface'
description: >-
  Error tool_result when ask_first fires but this session has no approve
  callback, so the host is not contacted.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_TOOL_ASK_FIRST_NO_PROMPT_SURFACE_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_ASK_FIRST_NO_PROMPT_SURFACE_VAR_1
-->
${TOOL_RESULT_REMOTE_TOOL_ASK_FIRST_NO_PROMPT_SURFACE_VAR_0.message} This session asks before running this call and could not raise its prompt here; ${TOOL_RESULT_REMOTE_TOOL_ASK_FIRST_NO_PROMPT_SURFACE_VAR_1.name} was not contacted.
