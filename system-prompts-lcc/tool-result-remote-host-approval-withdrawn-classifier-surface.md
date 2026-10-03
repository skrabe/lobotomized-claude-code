<!--
name: 'Tool Result: Remote host approval withdrawn classifier surface'
description: >-
  Tail of the remote-host approval-withdrawn result when the automatic check had
  approved but a sender could not be verified: retry once, and if refused again
  tell the user the tool needs their own approval
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_CLASSIFIER_SURFACE_VAR_0
-->
Retry once if it is still needed. If it is refused again, stop and tell the user that this tool on ${TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_CLASSIFIER_SURFACE_VAR_0} needs their own approval.
