<!--
name: Auto Mode Classifier No-Verdict Will Not Change
description: >-
  Permission-denial text telling the model a hard auto-mode no-verdict will not
  change if the action is retried.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_0
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_1
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_2
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_3
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_4
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_5
-->
${TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_0} gave no verdict${TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_1(TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_2,TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_3)}${TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_4}${TOOL_RESULT_AUTO_MODE_CLASSIFIER_NO_VERDICT_WILL_NOT_CHANGE_VAR_5}. This is a hard failure, not a transient one: the check cannot or does not judge this request, so retrying this action will get the same answer. Don't retry it. Continue with other tasks that don't require it; if it is essential, stop and tell the user that auto mode could not evaluate it. 
