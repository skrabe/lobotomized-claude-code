<!--
name: 'Tool Result: remote tool result cut to session limits'
description: >-
  Note appended to a remote tool's result when this session cut it to its own
  text/image/block limits.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_2
  - TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_3
-->
(this session cut ${TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_0.host.name}'s result to its own limits: ${(TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_0.maxTextChars??TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_1).toLocaleString("en-US")} characters of text, inline images up to ${TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_2/1048576} MiB, ${TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_3} blocks)
