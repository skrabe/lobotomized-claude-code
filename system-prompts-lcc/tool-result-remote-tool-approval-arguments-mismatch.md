<!--
name: 'Tool Result: remote tool approval used other arguments'
description: >-
  Error when a connector call's late approval came with edited or no arguments,
  telling the model to call the tool again for a new approval.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_TOOL_APPROVAL_ARGUMENTS_MISMATCH_VAR_0
-->
${TOOL_RESULT_REMOTE_TOOL_APPROVAL_ARGUMENTS_MISMATCH_VAR_0.name} was refused: its approval could not be used. This call needs approval of its exact arguments, and the approval came with other arguments or with none. Call ${TOOL_RESULT_REMOTE_TOOL_APPROVAL_ARGUMENTS_MISMATCH_VAR_0.name} again to ask for a new approval.
