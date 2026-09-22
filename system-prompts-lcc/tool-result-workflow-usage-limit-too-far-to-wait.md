<!--
name: 'Tool Result: Workflow Usage Limit Too Far To Wait'
description: >-
  Workflow wait decline note when the usage-limit reset is too far away, later
  joined into <failures> on the parent task-notification and remote-workflow
  result JSON.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_WORKFLOW_USAGE_LIMIT_TOO_FAR_TO_WAIT_VAR_0
  - TOOL_RESULT_WORKFLOW_USAGE_LIMIT_TOO_FAR_TO_WAIT_VAR_1
-->
usage limit; resets ${TOOL_RESULT_WORKFLOW_USAGE_LIMIT_TOO_FAR_TO_WAIT_VAR_0(TOOL_RESULT_WORKFLOW_USAGE_LIMIT_TOO_FAR_TO_WAIT_VAR_1.resetsAt)}, too far out to wait for
