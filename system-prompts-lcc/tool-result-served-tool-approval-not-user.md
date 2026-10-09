<!--
name: Approval must come from user
description: >-
  Rejects an approval that requires the user but was supplied by another
  approver.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_TOOL_APPROVAL_NOT_USER_VAR_0
-->
${TOOL_RESULT_SERVED_TOOL_APPROVAL_NOT_USER_VAR_0.name} was not run: only the user may approve this call, and its approval did not come from the user. Tell the user what you wanted to run and why.
