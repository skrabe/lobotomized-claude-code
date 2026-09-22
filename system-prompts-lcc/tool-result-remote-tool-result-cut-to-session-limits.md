<!--
name: 'Remote Tool Result: Cut To Session Limits'
description: >-
  Suffix appended onto a forwarded tool_result when this session cut the host's
  result to its own text/image/block limits.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_2
  - TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_3
-->
(this session cut ${TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_0.host.name}'s result to its own limits: ${TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_1.toLocaleString("en-US")} characters of text, inline images up to ${TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_2/1048576} MiB, ${TOOL_RESULT_REMOTE_TOOL_RESULT_CUT_TO_SESSION_LIMITS_VAR_3} blocks)
