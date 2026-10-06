<!--
name: 'Agent toolset edit: file exceeds byte limit'
description: >-
  Error returned by the agent toolset edit tool when the target file exceeds the
  byte limit.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_AGENT_TOOLSET_EDIT_FILE_TOO_LARGE_VAR_0
  - TOOL_RESULT_AGENT_TOOLSET_EDIT_FILE_TOO_LARGE_VAR_1
  - TOOL_RESULT_AGENT_TOOLSET_EDIT_FILE_TOO_LARGE_VAR_2
-->
edit: ${TOOL_RESULT_AGENT_TOOLSET_EDIT_FILE_TOO_LARGE_VAR_0} is ${TOOL_RESULT_AGENT_TOOLSET_EDIT_FILE_TOO_LARGE_VAR_1.size} bytes, exceeds ${TOOL_RESULT_AGENT_TOOLSET_EDIT_FILE_TOO_LARGE_VAR_2}-byte limit. The edit tool loads the whole file and cannot modify a file this large.
