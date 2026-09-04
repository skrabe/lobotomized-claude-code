<!--
name: 'Tool Result: Auto Mode No Verdict Not Requested'
description: >-
  Auto-mode permission deny/block message when the classifier was not asked for
  a verdict, instructing a one-shot retry then skip.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_REQUESTED_VAR_0
  - TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_REQUESTED_VAR_1
-->
${TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_REQUESTED_VAR_0} gave no verdict for ${TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_REQUESTED_VAR_1}: the request that produced this action did not ask for one. Issue the action again once, as-is; if it is denied again, continue with other tasks that don't require it and tell the user that auto mode could not evaluate it. 
