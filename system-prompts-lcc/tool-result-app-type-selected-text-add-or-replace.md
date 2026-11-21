<!--
name: 'Tool result: app_type selected text add or replace'
description: >-
  Instructions to ADD via click-then-type or REPLACE via mode replace with whole
  text; check screenshot; handling if app_focus refused.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_ADD_OR_REPLACE_VAR_0
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_ADD_OR_REPLACE_VAR_1
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_ADD_OR_REPLACE_VAR_2
-->
To ADD${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_ADD_OR_REPLACE_VAR_0.hasRawKeys?" elsewhere":""}: app_click by coordinate ON the character before which the text should go (a click past the text puts the caret at the start), then app_type as that click's answer says, without overwrite_existing. To REPLACE the text: app_type with mode: "replace", overwrite_existing: true and the WHOLE text that should stand there; what you leave out is lost (${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_ADD_OR_REPLACE_VAR_1}); ${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_ADD_OR_REPLACE_VAR_2}. Check an app_screenshot afterwards. If app_focus is refused, leave it at that; if you stop here, or a later call fails, 
