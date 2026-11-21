<!--
name: 'Tool result: app accessibility write not confirmed'
description: >-
  Result when accessibility accepted the text but read-back did not confirm it;
  do not retype yet.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_0
  - TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_1
  - TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_2
  - TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_3
  - TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_4
  - TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_5
  - TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_6
-->
Not confirmed: ${TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_0(TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_1)} accepted the text for ${TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_2}${TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_3}${TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_4} through accessibility (${TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_5}), but reading the field back did not confirm it. It may have landed or may still land, so no keystrokes were sent. Do NOT type it again yet: take a fresh app_screenshot and look at the field. If the text is there, this call has done its work. If the field is still as it was, the text may still be on its way: ${TOOL_RESULT_APP_AX_WRITE_NOT_CONFIRMED_VAR_6}. If it shows anything else, put that right first.
