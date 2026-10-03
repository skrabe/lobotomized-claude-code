<!--
name: 'Tool Result: Auto Mode No Verdict Not Shown This Call Repeat'
description: >-
  Auto-mode denial telling the model the call did not run because the classifier
  was not shown it, and to repeat the identical call once.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_SHOWN_THIS_CALL_REPEAT_VAR_0
  - TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_SHOWN_THIS_CALL_REPEAT_VAR_1
-->
${TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_SHOWN_THIS_CALL_REPEAT_VAR_0} did not run. ${TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_SHOWN_THIS_CALL_REPEAT_VAR_1} gave no verdict because it was not shown this call; that is not a judgment that the call is unsafe. Repeat the identical ${TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_SHOWN_THIS_CALL_REPEAT_VAR_0} call once now; the repeat will be reviewed as usual. If the repeat does not run either, continue with other tasks that don't require it and tell the user that auto mode could not evaluate it. 
