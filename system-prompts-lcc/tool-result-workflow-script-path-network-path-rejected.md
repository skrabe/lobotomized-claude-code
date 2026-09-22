<!--
name: Workflow scriptPath network path rejected
description: >-
  Validation failure returned to the model when the Workflow tool's scriptPath
  resolves to a UNC, NT-namespace or automount path.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_WORKFLOW_SCRIPT_PATH_NETWORK_PATH_REJECTED_VAR_0
-->
Network (UNC, NT-namespace, or automount) paths are not allowed for workflow scriptPath: ${TOOL_RESULT_WORKFLOW_SCRIPT_PATH_NETWORK_PATH_REJECTED_VAR_0}
