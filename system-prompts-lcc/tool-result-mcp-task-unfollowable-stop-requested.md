<!--
name: 'MCP Task Unfollowable: Stop Requested'
description: >-
  Tool result when a background MCP task cannot be followed and the session
  asked for it to be stopped; warns rerunning may repeat work.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_MCP_TASK_UNFOLLOWABLE_STOP_REQUESTED_VAR_0
-->
The tool started a background task on ${TOOL_RESULT_MCP_TASK_UNFOLLOWABLE_STOP_REQUESTED_VAR_0}, and this session cannot follow it, so its result won't arrive here. This session has asked for it to be stopped there. It may have done part of its work, so running the tool again could repeat that. Tell the user so.
