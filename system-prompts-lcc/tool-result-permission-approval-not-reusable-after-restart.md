<!--
name: 'Tool Result: Permission approval not reusable after restart'
description: >-
  Deny message when an approval asked before a restart cannot be reused, telling
  the model to call again
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_PERMISSION_APPROVAL_NOT_REUSABLE_AFTER_RESTART_VAR_0
-->
The approval of ${TOOL_RESULT_PERMISSION_APPROVAL_NOT_REUSABLE_AFTER_RESTART_VAR_0} was asked for before Claude Code restarted, and cannot be reused. Call ${TOOL_RESULT_PERMISSION_APPROVAL_NOT_REUSABLE_AFTER_RESTART_VAR_0} again with the same arguments; it may need approval again. ${TOOL_RESULT_PERMISSION_APPROVAL_NOT_REUSABLE_AFTER_RESTART_VAR_0} was not called.
