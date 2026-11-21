<!--
name: 'Tool result: app_type selected text in combo box'
description: >-
  Refusal for selected text in a combo box: no add path in background; how to
  REPLACE whole text, and warning if stopping.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_COMBO_BOX_VAR_0
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_COMBO_BOX_VAR_1
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_COMBO_BOX_VAR_2
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_COMBO_BOX_VAR_3
  - TOOL_RESULT_APP_TYPE_SELECTED_TEXT_COMBO_BOX_VAR_4
-->
${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_COMBO_BOX_VAR_0} Nothing is known that adds to it in the background: app_click presses a combo box and places no caret. To REPLACE the text: ${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_COMBO_BOX_VAR_1} and the WHOLE text that should stand there; what you leave out is lost (this replaces what is selected, which is all of the text if the selection is app_type's own doing; the result names what was replaced; ${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_COMBO_BOX_VAR_2}); ${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_COMBO_BOX_VAR_3}. If you stop here, or that call fails, ${TOOL_RESULT_APP_TYPE_SELECTED_TEXT_COMBO_BOX_VAR_4}
