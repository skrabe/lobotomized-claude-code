<!--
name: 'Tool Result: Permission denied, no interactive approval'
description: >-
  Denial result returned to the model when a tool needs interactive approval but
  the session has no permission prompts, telling it not to claim success or
  retry.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_PERMISSION_DENIED_NO_INTERACTIVE_APPROVAL_VAR_0
  - TOOL_RESULT_PERMISSION_DENIED_NO_INTERACTIVE_APPROVAL_VAR_1
-->
${TOOL_RESULT_PERMISSION_DENIED_NO_INTERACTIVE_APPROVAL_VAR_0}, and permission prompts are not available in this session. The action was not performed. Do not claim it succeeded, and do not retry it in this session — report the limitation to the user, or suggest an alternative. What was requested: ${TOOL_RESULT_PERMISSION_DENIED_NO_INTERACTIVE_APPROVAL_VAR_1}
