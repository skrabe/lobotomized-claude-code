<!--
name: 'Tool Result: Auto mode classifier API wait not unsafe'
description: >-
  Reports that the API asked the safety classifier to wait and that this is not
  a safety judgment
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_NOT_UNSAFE_VAR_0
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_NOT_UNSAFE_VAR_1
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_NOT_UNSAFE_VAR_2
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_NOT_UNSAFE_VAR_3
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_NOT_UNSAFE_VAR_4
-->
The API told auto mode's safety classifier (${TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_NOT_UNSAFE_VAR_0}) to wait ${TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_NOT_UNSAFE_VAR_1} from now${TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_NOT_UNSAFE_VAR_2}${TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_NOT_UNSAFE_VAR_3}${TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_NOT_UNSAFE_VAR_4} until then. This is not a judgment that the action is unsafe, so don't rework the action to get around it. 
