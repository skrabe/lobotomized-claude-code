<!--
name: 'Send to Project: MCP local server stays on computer'
description: >-
  Per-server label in the /send-to-project MCP tool-call list marking a local
  stdio/sdk server that stays on this computer.
ccVersion: 2.1.314
variables:
  - DATA_SEND_TO_PROJECT_MCP_LOCAL_SERVER_STAYS_VAR_0
  - DATA_SEND_TO_PROJECT_MCP_LOCAL_SERVER_STAYS_VAR_1
-->
local ${DATA_SEND_TO_PROJECT_MCP_LOCAL_SERVER_STAYS_VAR_0.transport??"stdio"} server, stays on ${DATA_SEND_TO_PROJECT_MCP_LOCAL_SERVER_STAYS_VAR_1}
