<!--
name: 'Tool Result: Output Too Large Could Not Be Saved'
description: >-
  Truncation envelope for a tool_result whose full output could not be
  persisted, showing only the first N characters and asking the model to page or
  filter.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_OUTPUT_TOO_LARGE_COULD_NOT_BE_SAVED_VAR_0
  - TOOL_RESULT_OUTPUT_TOO_LARGE_COULD_NOT_BE_SAVED_VAR_1
  - TOOL_RESULT_OUTPUT_TOO_LARGE_COULD_NOT_BE_SAVED_VAR_2
  - TOOL_RESULT_OUTPUT_TOO_LARGE_COULD_NOT_BE_SAVED_VAR_3
  - TOOL_RESULT_OUTPUT_TOO_LARGE_COULD_NOT_BE_SAVED_VAR_4
-->
${TOOL_RESULT_OUTPUT_TOO_LARGE_COULD_NOT_BE_SAVED_VAR_0}
Output too large (${TOOL_RESULT_OUTPUT_TOO_LARGE_COULD_NOT_BE_SAVED_VAR_1}). It could not be saved, so only the first ${TOOL_RESULT_OUTPUT_TOO_LARGE_COULD_NOT_BE_SAVED_VAR_2} are shown; the rest was dropped. If the tool can page or filter its results, call it again for the part you need.

${TOOL_RESULT_OUTPUT_TOO_LARGE_COULD_NOT_BE_SAVED_VAR_3}
${TOOL_RESULT_OUTPUT_TOO_LARGE_COULD_NOT_BE_SAVED_VAR_4}
