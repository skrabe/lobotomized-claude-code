<!--
name: 'Tool Result: Remote tool no built-in tools on host'
description: >-
  Tells the model the session has none of its built-in tools on the named
  machine so the call did not run, and that work there goes through the
  machine's own mcp tools
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_TOOL_NO_BUILT_IN_TOOLS_ON_HOST_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_NO_BUILT_IN_TOOLS_ON_HOST_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_NO_BUILT_IN_TOOLS_ON_HOST_VAR_2
  - TOOL_RESULT_REMOTE_TOOL_NO_BUILT_IN_TOOLS_ON_HOST_VAR_3
  - TOOL_RESULT_REMOTE_TOOL_NO_BUILT_IN_TOOLS_ON_HOST_VAR_4
-->
This session has none of its built-in tools on ${TOOL_RESULT_REMOTE_TOOL_NO_BUILT_IN_TOOLS_ON_HOST_VAR_0}, so ${TOOL_RESULT_REMOTE_TOOL_NO_BUILT_IN_TOOLS_ON_HOST_VAR_1} did not run. Work on ${TOOL_RESULT_REMOTE_TOOL_NO_BUILT_IN_TOOLS_ON_HOST_VAR_0} goes through its own tools (mcp__${TOOL_RESULT_REMOTE_TOOL_NO_BUILT_IN_TOOLS_ON_HOST_VAR_2}__…); omit "${TOOL_RESULT_REMOTE_TOOL_NO_BUILT_IN_TOOLS_ON_HOST_VAR_3}" only for a call that is meant to run ${TOOL_RESULT_REMOTE_TOOL_NO_BUILT_IN_TOOLS_ON_HOST_VAR_4()}.
