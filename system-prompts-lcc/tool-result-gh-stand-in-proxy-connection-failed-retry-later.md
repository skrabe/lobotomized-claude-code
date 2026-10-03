<!--
name: 'Tool Result: gh stand-in proxy connection failed, retry later'
description: >-
  Error from the built-in gh stand-in when the session's GitHub proxy could not
  open the connection: nothing was sent, wait and retry once, then read the
  proxy's /__agentproxy/status.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_GH_STAND_IN_PROXY_CONNECTION_FAILED_RETRY_LATER_VAR_0
  - TOOL_RESULT_GH_STAND_IN_PROXY_CONNECTION_FAILED_RETRY_LATER_VAR_1
  - TOOL_RESULT_GH_STAND_IN_PROXY_CONNECTION_FAILED_RETRY_LATER_VAR_2
-->
this session's GitHub proxy could not open the connection (${TOOL_RESULT_GH_STAND_IN_PROXY_CONNECTION_FAILED_RETRY_LATER_VAR_0}); nothing was sent. This can be temporary: wait ${TOOL_RESULT_GH_STAND_IN_PROXY_CONNECTION_FAILED_RETRY_LATER_VAR_1} and run the command once more. If it fails again, stop and read GET ${TOOL_RESULT_GH_STAND_IN_PROXY_CONNECTION_FAILED_RETRY_LATER_VAR_2}/__agentproxy/status for the proxy's state.
