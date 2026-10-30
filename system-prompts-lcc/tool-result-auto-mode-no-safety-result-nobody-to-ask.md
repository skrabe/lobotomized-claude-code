<!--
name: 'Tool Result: Auto mode no safety result, nobody to ask'
description: >-
  Deny message when auto mode has no safety result for a call and no one can
  approve it; issue it once more, then tell the user
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_AUTO_MODE_NO_SAFETY_RESULT_NOBODY_TO_ASK_VAR_0
  - TOOL_RESULT_AUTO_MODE_NO_SAFETY_RESULT_NOBODY_TO_ASK_VAR_1
-->
${TOOL_RESULT_AUTO_MODE_NO_SAFETY_RESULT_NOBODY_TO_ASK_VAR_0.name} was not run: auto mode has no safety result for this call, and nobody can be asked to approve it here. This is not a judgment that it is unsafe. ${TOOL_RESULT_AUTO_MODE_NO_SAFETY_RESULT_NOBODY_TO_ASK_VAR_1} then tell the user that auto mode has no safety result for it and that they can approve it themselves in another permission mode.
