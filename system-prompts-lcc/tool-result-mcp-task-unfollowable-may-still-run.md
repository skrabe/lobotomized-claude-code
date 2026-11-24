<!--
name: 'MCP Task Unfollowable: May Still Be Running'
description: >-
  Tool result when a background MCP task on a linked computer cannot be
  followed, telling Claude it may still be running there and to tell the user.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_MCP_TASK_UNFOLLOWABLE_MAY_STILL_RUN_VAR_0
-->
The tool started a background task on ${TOOL_RESULT_MCP_TASK_UNFOLLOWABLE_MAY_STILL_RUN_VAR_0}, and this session cannot follow it, so its result won't arrive here. It was not stopped and may still be running there, so running the tool again could repeat the work. Tell the user that it may still be running on ${TOOL_RESULT_MCP_TASK_UNFOLLOWABLE_MAY_STILL_RUN_VAR_0}.
