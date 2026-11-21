<!--
name: 'Tool result: app element replaced by other control'
description: Windows refusal when another control now sits where the element_index pointed.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_UIA_ELEMENT_REPLACED_BY_OTHER_CONTROL_VAR_0
  - TOOL_RESULT_APP_UIA_ELEMENT_REPLACED_BY_OTHER_CONTROL_VAR_1
-->
Nothing was done: ${TOOL_RESULT_APP_UIA_ELEMENT_REPLACED_BY_OTHER_CONTROL_VAR_0} no longer names what is at its position. Another control (${TOOL_RESULT_APP_UIA_ELEMENT_REPLACED_BY_OTHER_CONTROL_VAR_1}) is there now and would have taken this action: the menu or pane your element was in has probably closed, or the content has moved. Take a fresh app_screenshot and aim at what it lists.
