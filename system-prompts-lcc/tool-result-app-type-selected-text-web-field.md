<!--
name: 'Tool result: app_type selected text in web field'
description: >-
  Web field refusal: retry app_type mode replace with overwrite_existing and the
  whole text, then check a screenshot.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_WEB_FIELD_VAR_0
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_WEB_FIELD_VAR_1
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_WEB_FIELD_VAR_2
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_WEB_FIELD_VAR_3
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_WEB_FIELD_VAR_4
-->
${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_WEB_FIELD_VAR_0} This is a web field (in a page, or in an app built like one), where one way on is known to hold: retry app_type with mode: "replace", overwrite_existing: true${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_WEB_FIELD_VAR_1(TOOL_RESULT_APP_TYPE_SELECTED_TEXT_WEB_FIELD_VAR_2)} and the WHOLE text that should stand there; what you leave out is lost (this replaces ALL of the field's content, not only what is selected; ${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_WEB_FIELD_VAR_3}); ${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_WEB_FIELD_VAR_4}. Check an app_screenshot afterwards
