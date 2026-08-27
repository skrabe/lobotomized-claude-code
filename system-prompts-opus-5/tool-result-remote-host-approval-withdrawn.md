<!--
name: 'Tool Result: Remote Host Approval Withdrawn'
description: >-
  approval_not_received tool_result when the permission request was withdrawn on
  the host and nothing ran; retry is safe unless the refusal was unverified, in
  which case the user must re-approve from the terminal or desktop prompt.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_VAR_0
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_VAR_1
-->
${TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_VAR_0}; the request was withdrawn there and nothing ran. ${TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_VAR_1==="unverified_refusal"?"If the user answered from a surface this session cannot verify, send the call again and have them approve from the terminal or desktop prompt, unedited.":"It is safe to retry the call if it is still wanted."}
