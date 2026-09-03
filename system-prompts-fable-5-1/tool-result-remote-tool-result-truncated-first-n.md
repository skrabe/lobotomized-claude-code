<!--
name: 'Remote Tool Result: Truncated To First N Characters'
description: >-
  Suffix appended onto a forwarded tool_result when this session kept only the
  first N characters of the host's answer.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_TOOL_RESULT_TRUNCATED_FIRST_N_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_RESULT_TRUNCATED_FIRST_N_VAR_1
-->
(this session kept only the first ${TOOL_RESULT_REMOTE_TOOL_RESULT_TRUNCATED_FIRST_N_VAR_0.toLocaleString("en-US")} characters of ${TOOL_RESULT_REMOTE_TOOL_RESULT_TRUNCATED_FIRST_N_VAR_1.host.name}'s answer)
