<!--
name: 'Tool Result: Persisted output long result guidance'
description: >-
  Tells Claude a result is long and only its start is shown, where the rest is
  saved, and to answer from the shown part only when enough or say so
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_0
  - TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_1
  - TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_2
  - TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_3
  - TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_4
  - TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_5
-->
${TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_0.truncatedAtBytes===void 0?`This result is long (${TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_1}).`:"This result is long."} Only the first ${TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_2} is below. ${TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_3}${TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_4}
Answer from what is below if it is enough. A summary or a count needs the whole result, so open the file for that. If you cannot open it, or your answer rests on only part of the result, say so.${TOOL_RESULT_PERSISTED_OUTPUT_LONG_RESULT_GUIDANCE_VAR_5}
