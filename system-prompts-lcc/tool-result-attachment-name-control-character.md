<!--
name: 'Tool Result: Attachment name contains control character'
description: >-
  Validation refusal: cannot send a file whose name holds a line break, control
  or direction-changing character
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_ATTACHMENT_NAME_CONTROL_CHARACTER_VAR_0
  - TOOL_RESULT_ATTACHMENT_NAME_CONTROL_CHARACTER_VAR_1
  - TOOL_RESULT_ATTACHMENT_NAME_CONTROL_CHARACTER_VAR_2
-->
Cannot send ${TOOL_RESULT_ATTACHMENT_NAME_CONTROL_CHARACTER_VAR_0(TOOL_RESULT_ATTACHMENT_NAME_CONTROL_CHARACTER_VAR_1)}: its name contains a line break, another control character or a character that changes text direction. ${TOOL_RESULT_ATTACHMENT_NAME_CONTROL_CHARACTER_VAR_2}
