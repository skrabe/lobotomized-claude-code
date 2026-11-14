<!--
name: >-
  System Reminder: MCP Servers Failed To Connect — tell the user they can fix or
  retry it
description: >-
  Tells the model to add, when no failed MCP server is being retried, that the
  user can fix or retry the server.
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_MCP_SERVERS_FAILED_TO_CONNECT_FIX_OR_RETRY_GUIDANCE_2_VAR_0
  - SYSTEM_REMINDER_MCP_SERVERS_FAILED_TO_CONNECT_FIX_OR_RETRY_GUIDANCE_2_VAR_1
-->
so they can fix or retry it${SYSTEM_REMINDER_MCP_SERVERS_FAILED_TO_CONNECT_FIX_OR_RETRY_GUIDANCE_2_VAR_0.some((SYSTEM_REMINDER_MCP_SERVERS_FAILED_TO_CONNECT_FIX_OR_RETRY_GUIDANCE_2_VAR_1)=>SYSTEM_REMINDER_MCP_SERVERS_FAILED_TO_CONNECT_FIX_OR_RETRY_GUIDANCE_2_VAR_1.willRetry===!0)?" (for a server that the session retries in the background: that it may work if they ask again in a minute)":""}; for a server that a search connects to again, do so only after a search that names it finds none of its tools
