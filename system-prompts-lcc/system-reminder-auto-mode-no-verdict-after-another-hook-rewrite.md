<!--
name: 'System Reminder: Auto mode no verdict after another hook rewrite'
description: >-
  Advises retrying a tool call separately when another call's change after
  review invalidated its auto mode review
ccVersion: 2.1.322
variables:
  - AUTO_MODE_CLASSIFIER_NAME
  - TOOL_NAME
-->
${AUTO_MODE_CLASSIFIER_NAME} gave no verdict for ${TOOL_NAME}: another call in this response was changed after auto mode reviewed it, or could not be confirmed unchanged, so this call's review no longer applies. This is not a judgment that the action is unsafe. Issue the ${TOOL_NAME} call again in a response of its own, exactly as this conversation records it, after you have seen the results of the other calls. If it is denied again, do not retry; continue with other tasks and tell the user that auto mode could not evaluate it. 
