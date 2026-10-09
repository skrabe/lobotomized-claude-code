<!--
name: Truncated Bash output has no saved remainder
description: >-
  Explains that the saved served Bash output contains only the returned start
  and suggests rerunning safely.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_BASH_TRUNCATED_OUTPUT_NO_SAVED_REST_VAR_0
  - TOOL_RESULT_SERVED_BASH_TRUNCATED_OUTPUT_NO_SAVED_REST_VAR_1
  - TOOL_RESULT_SERVED_BASH_TRUNCATED_OUTPUT_NO_SAVED_REST_VAR_2
  - TOOL_RESULT_SERVED_BASH_TRUNCATED_OUTPUT_NO_SAVED_REST_VAR_3
-->
(output truncated: ${typeof TOOL_RESULT_SERVED_BASH_TRUNCATED_OUTPUT_NO_SAVED_REST_VAR_0==="number"?`the command printed ${TOOL_RESULT_SERVED_BASH_TRUNCATED_OUTPUT_NO_SAVED_REST_VAR_1(TOOL_RESULT_SERVED_BASH_TRUNCATED_OUTPUT_NO_SAVED_REST_VAR_0)}; `:""}only the start was returned, so a saved copy of this result holds no more. To see the rest, run the command again with ${TOOL_RESULT_SERVED_BASH_TRUNCATED_OUTPUT_NO_SAVED_REST_VAR_2(TOOL_RESULT_SERVED_BASH_TRUNCATED_OUTPUT_NO_SAVED_REST_VAR_3.name)}, if that is safe.)
