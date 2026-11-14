<!--
name: 'Tool Result: Permission approval changed input'
description: >-
  Deny message telling the model nothing ran because the approval came back with
  arguments different from those the user saw, and to call the tool again to
  re-ask
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_PERMISSION_APPROVAL_CHANGED_INPUT_VAR_0
-->
Nothing ran: the approval for ${TOOL_RESULT_PERMISSION_APPROVAL_CHANGED_INPUT_VAR_0.name} came back with arguments different from the ones the user was shown. Call ${TOOL_RESULT_PERMISSION_APPROVAL_CHANGED_INPUT_VAR_0.name} again to ask the user again.
