<!--
name: 'Tool Result: Remote Host Approval No Longer Accepted'
description: >-
  still_running tool_result when the host was awaiting a permission decision
  that it no longer accepts an answer to.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_NO_LONGER_ACCEPTED_VAR_0
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_NO_LONGER_ACCEPTED_VAR_1
-->
${TOOL_RESULT_REMOTE_HOST_APPROVAL_NO_LONGER_ACCEPTED_VAR_0}${TOOL_RESULT_REMOTE_HOST_APPROVAL_NO_LONGER_ACCEPTED_VAR_1==="unasked"?" —":""} it was waiting for a permission decision and nothing had run, but it no longer accepts an answer to that question, so check on its effect before retrying it, or ask the user.
