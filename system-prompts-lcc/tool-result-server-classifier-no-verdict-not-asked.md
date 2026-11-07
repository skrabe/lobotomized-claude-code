<!--
name: 'Tool Result: No verdict outside auto mode, not asked'
description: >-
  Deny message when the automatic safety check gave no verdict outside auto mode
  and Claude Code does not ask in its place; do not retry now
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_NOT_ASKED_VAR_0
  - TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_NOT_ASKED_VAR_1
  - TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_NOT_ASKED_VAR_2
-->
${TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_NOT_ASKED_VAR_0.name} did not run. The automatic safety check gave no verdict on this call, and Claude Code doesn't ask for approval in its place here: ${TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_NOT_ASKED_VAR_1}. This is not a judgment that the action is unsafe, ${TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_NOT_ASKED_VAR_2}
