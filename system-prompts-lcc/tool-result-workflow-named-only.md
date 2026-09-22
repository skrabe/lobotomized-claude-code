<!--
name: Workflow named-only restriction
description: >-
  Workflow tool validateInput error returned to the model when the session
  restricts to named workflows.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_WORKFLOW_NAMED_ONLY_VAR_0
  - TOOL_RESULT_WORKFLOW_NAMED_ONLY_VAR_1
-->
This session restricts the Workflow tool to named workflows (${TOOL_RESULT_WORKFLOW_NAMED_ONLY_VAR_0} is set). Not allowed here: ${TOOL_RESULT_WORKFLOW_NAMED_ONLY_VAR_1.join(", ")}. Invoke as {name, args} only.
