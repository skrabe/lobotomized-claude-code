<!--
name: 'Tool Result: Permission denied no approval surface'
description: >-
  Explains automatic denial when no approval surface exists and forbids retrying
  approval-requiring actions
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_PERMISSION_DENIED_NO_APPROVAL_SURFACE_VAR_0
-->
${TOOL_RESULT_PERMISSION_DENIED_NO_APPROVAL_SURFACE_VAR_0} — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. 
