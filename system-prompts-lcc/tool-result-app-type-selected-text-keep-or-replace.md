<!--
name: 'Tool result: app_type selected text keep or replace'
description: >-
  Native non-plain field: click at a character to keep text and insert, or retry
  with overwrite to replace selection.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_KEEP_OR_REPLACE_VAR_0
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_KEEP_OR_REPLACE_VAR_1
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_KEEP_OR_REPLACE_VAR_2
-->
${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_KEEP_OR_REPLACE_VAR_0} To keep it: app_click by coordinate ON the character before which the text should go; once that answers ok the caret stands there and nothing is selected; then app_type as that answer says, without overwrite_existing. To replace the selected text: ${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_KEEP_OR_REPLACE_VAR_1} (if the insert does not take, this may replace ALL of the field's content instead; ${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_KEEP_OR_REPLACE_VAR_2})
