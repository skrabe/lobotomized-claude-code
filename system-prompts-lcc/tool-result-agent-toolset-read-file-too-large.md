<!--
name: 'Agent toolset read: file exceeds byte limit'
description: >-
  Error returned by the agent toolset read tool when a file exceeds the byte
  limit and no view_range was given.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_AGENT_TOOLSET_READ_FILE_TOO_LARGE_VAR_0
  - TOOL_RESULT_AGENT_TOOLSET_READ_FILE_TOO_LARGE_VAR_1
  - TOOL_RESULT_AGENT_TOOLSET_READ_FILE_TOO_LARGE_VAR_2
-->
read: ${TOOL_RESULT_AGENT_TOOLSET_READ_FILE_TOO_LARGE_VAR_0} is ${TOOL_RESULT_AGENT_TOOLSET_READ_FILE_TOO_LARGE_VAR_1.size} bytes, exceeds ${TOOL_RESULT_AGENT_TOOLSET_READ_FILE_TOO_LARGE_VAR_2}-byte limit. Use the view_range parameter to read specific line ranges, e.g. view_range: [1, 500].
