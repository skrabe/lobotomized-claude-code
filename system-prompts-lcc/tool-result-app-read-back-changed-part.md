<!--
name: 'Tool result: app read back changed part'
description: >-
  Read-back note quoting the part of the field the call changed, with character
  range and a cut-short marker.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_0
  - TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_1
  - TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_2
-->
 Read back: the part of the field this call changed now reads (${TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_0===TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_1.totalChars?`the whole field, ${TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_1.totalChars} characters`:`characters ${TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_1.firstChar+1}-${TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_1.firstChar+TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_0} of ${TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_1.totalChars}`}${TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_1.cutShort?"; CUT SHORT, the change is longer than 500 characters and this is its beginning":""}): ${TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_2(TOOL_RESULT_APP_READ_BACK_CHANGED_PART_VAR_1.text)}.
