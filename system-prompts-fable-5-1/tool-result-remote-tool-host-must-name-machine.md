<!--
name: Must Name Machine
description: >-
  Tool error telling the model to set the machine argument when several attached
  hosts can run the tool.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_REMOTE_TOOL_HOST_MUST_NAME_MACHINE_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_HOST_MUST_NAME_MACHINE_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_HOST_MUST_NAME_MACHINE_VAR_2
  - TOOL_RESULT_REMOTE_TOOL_HOST_MUST_NAME_MACHINE_VAR_3
-->
${TOOL_RESULT_REMOTE_TOOL_HOST_MUST_NAME_MACHINE_VAR_0} cannot run ${TOOL_RESULT_REMOTE_TOOL_HOST_MUST_NAME_MACHINE_VAR_1()} — this session's own environment has no ${TOOL_RESULT_REMOTE_TOOL_HOST_MUST_NAME_MACHINE_VAR_0} — and ${TOOL_RESULT_REMOTE_TOOL_HOST_MUST_NAME_MACHINE_VAR_2.length} attached machines serve it, so the call must say which: set "${TOOL_RESULT_REMOTE_TOOL_HOST_MUST_NAME_MACHINE_VAR_3}" to one of ${TOOL_RESULT_REMOTE_TOOL_HOST_MUST_NAME_MACHINE_VAR_2.join(", ")}. Nothing ran.
