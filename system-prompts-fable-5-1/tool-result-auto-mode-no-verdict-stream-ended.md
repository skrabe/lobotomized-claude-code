<!--
name: 'Tool Result: Auto Mode No Verdict Stream Ended'
description: >-
  Denies a tool call in auto mode when the classifier stream ended before a
  verdict, telling the model to retry once then continue.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_AUTO_MODE_NO_VERDICT_STREAM_ENDED_VAR_0
  - TOOL_RESULT_AUTO_MODE_NO_VERDICT_STREAM_ENDED_VAR_1
-->
${TOOL_RESULT_AUTO_MODE_NO_VERDICT_STREAM_ENDED_VAR_0} gave no verdict for ${TOOL_RESULT_AUTO_MODE_NO_VERDICT_STREAM_ENDED_VAR_1}: the response ended before this tool call was complete. Issue the action again once, as-is; if it is denied again, continue with other tasks that don't require it and tell the user that auto mode could not evaluate it. 
