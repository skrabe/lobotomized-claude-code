<!--
name: 'Tool Result: Remote host classifier-approved call needs a person''s approval'
description: >-
  Tells Claude the session's automatic check approved this tool call but only a
  person's approval counts for that tool on that machine, so nothing ran; retry
  once, then stop and tell the user the tool needs their own approval.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_HOST_CLASSIFIER_APPROVED_NEEDS_PERSON_APPROVAL_VAR_0
  - TOOL_RESULT_REMOTE_HOST_CLASSIFIER_APPROVED_NEEDS_PERSON_APPROVAL_VAR_1
-->
This session's automatic check approved this ${TOOL_RESULT_REMOTE_HOST_CLASSIFIER_APPROVED_NEEDS_PERSON_APPROVAL_VAR_0} call, but only a person's approval counts for ${TOOL_RESULT_REMOTE_HOST_CLASSIFIER_APPROVED_NEEDS_PERSON_APPROVAL_VAR_0} on ${TOOL_RESULT_REMOTE_HOST_CLASSIFIER_APPROVED_NEEDS_PERSON_APPROVAL_VAR_1}, so nothing ran. Retry once if it is still needed. If it is refused again, stop and tell the user that ${TOOL_RESULT_REMOTE_HOST_CLASSIFIER_APPROVED_NEEDS_PERSON_APPROVAL_VAR_0} on ${TOOL_RESULT_REMOTE_HOST_CLASSIFIER_APPROVED_NEEDS_PERSON_APPROVAL_VAR_1} needs their own approval.
