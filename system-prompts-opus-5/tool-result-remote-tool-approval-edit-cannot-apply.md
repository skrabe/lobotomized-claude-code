<!--
name: 'Remote Tool: Approval Edit Cannot Apply On Host'
description: >-
  insteadOfRejection tool_result when the session approval edited the call in a
  way the host cannot honour (different machine or a privileged field).
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_TOOL_APPROVAL_EDIT_CANNOT_APPLY_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_APPROVAL_EDIT_CANNOT_APPLY_VAR_1
-->
The approval given in this session edited the ${TOOL_RESULT_REMOTE_TOOL_APPROVAL_EDIT_CANNOT_APPLY_VAR_0.name} call in a way ${TOOL_RESULT_REMOTE_TOOL_APPROVAL_EDIT_CANNOT_APPLY_VAR_1.host.name} cannot honour (it named a different machine, or newly set a privileged field this session does not pass on in an edit); nothing ran.
