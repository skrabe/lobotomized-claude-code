<!--
name: 'Tool Result: Project Memory Bridge Has No Memory Route'
description: >-
  Error thrown by the Projects tool when project memory is requested while the
  session runs through the remote-session bridge, which has no memory route;
  adds a hint and says the project's docs are still available through the other
  methods.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_PROJECT_MEMORY_BRIDGE_NO_MEMORY_ROUTE_VAR_0
-->
This tool does not serve project memory in this session: it runs through the remote-session bridge, which has no memory route. ${TOOL_RESULT_PROJECT_MEMORY_BRIDGE_NO_MEMORY_ROUTE_VAR_0} The project's docs are still available through the other methods.
