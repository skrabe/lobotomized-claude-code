<!--
name: 'Tool Result: Non-text tool result truncation notice'
description: >-
  Notice appended when a tool_result whose content is a non-string object is
  serialized to text and cut at the size limit, telling the model how many
  characters of that tool result were not shown
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_NON_TEXT_CONTENT_TRUNCATION_NOTICE_VAR_0
  - TOOL_RESULT_NON_TEXT_CONTENT_TRUNCATION_NOTICE_VAR_1
  - TOOL_RESULT_NON_TEXT_CONTENT_TRUNCATION_NOTICE_VAR_2
-->
${TOOL_RESULT_NON_TEXT_CONTENT_TRUNCATION_NOTICE_VAR_0}
[${TOOL_RESULT_NON_TEXT_CONTENT_TRUNCATION_NOTICE_VAR_1} more ${TOOL_RESULT_NON_TEXT_CONTENT_TRUNCATION_NOTICE_VAR_2(TOOL_RESULT_NON_TEXT_CONTENT_TRUNCATION_NOTICE_VAR_1,"character")} of this tool result not shown]
