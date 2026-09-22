<!--
name: Host Detached Nowhere To Run
description: >-
  Tool error telling the model the named host is gone and this session cannot
  run the tool anywhere else.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_REMOTE_TOOL_HOST_DETACHED_NOWHERE_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_HOST_DETACHED_NOWHERE_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_HOST_DETACHED_NOWHERE_VAR_2
-->
${TOOL_RESULT_REMOTE_TOOL_HOST_DETACHED_NOWHERE_VAR_0} is no longer attached to this session, and this session's own environment has no ${TOOL_RESULT_REMOTE_TOOL_HOST_DETACHED_NOWHERE_VAR_1}: there is nowhere to run it until a computer that serves ${TOOL_RESULT_REMOTE_TOOL_HOST_DETACHED_NOWHERE_VAR_1} attaches again. Nothing ran; do not retry it ${TOOL_RESULT_REMOTE_TOOL_HOST_DETACHED_NOWHERE_VAR_2()} with another tool.
