<!--
name: 'Tool Result: App Action Element Index Out Of Range'
description: >-
  Validation tool-result when element_index is outside the AX summary captured
  by the last app_screenshot.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_APP_ACTION_ELEMENT_INDEX_OUT_OF_RANGE_VAR_0
  - TOOL_RESULT_APP_ACTION_ELEMENT_INDEX_OUT_OF_RANGE_VAR_1
-->
element_index ${TOOL_RESULT_APP_ACTION_ELEMENT_INDEX_OUT_OF_RANGE_VAR_0} is out of range (AX summary has ${TOOL_RESULT_APP_ACTION_ELEMENT_INDEX_OUT_OF_RANGE_VAR_1.axSummary.length} elements).
