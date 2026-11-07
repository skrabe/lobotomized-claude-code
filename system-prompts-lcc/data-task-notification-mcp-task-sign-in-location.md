<!--
name: 'Data: MCP task sign-in location'
description: >-
  Tells where the user can sign in and when Claude Code rechecks the task after
  a sign-in
ccVersion: 2.1.319
variables:
  - DATA_TASK_NOTIFICATION_MCP_TASK_SIGN_IN_LOCATION_VAR_0
  - DATA_TASK_NOTIFICATION_MCP_TASK_SIGN_IN_LOCATION_VAR_1
  - DATA_TASK_NOTIFICATION_MCP_TASK_SIGN_IN_LOCATION_VAR_2
-->
 Where the user can sign in: ${DATA_TASK_NOTIFICATION_MCP_TASK_SIGN_IN_LOCATION_VAR_0()}.${DATA_TASK_NOTIFICATION_MCP_TASK_SIGN_IN_LOCATION_VAR_1?" After a sign-in Claude Code checks again once the server is connected.":` A sign-in made outside this session is seen only once the session connects to the server anew${DATA_TASK_NOTIFICATION_MCP_TASK_SIGN_IN_LOCATION_VAR_2()?" or is resumed":""}.`}
