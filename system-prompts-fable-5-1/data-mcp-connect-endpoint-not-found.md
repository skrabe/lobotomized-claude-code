<!--
name: 'Data: MCP Connect Endpoint Not Found'
description: >-
  HTTP MCP connect error quoted into the failed-servers system reminder when the
  endpoint returns 404.
ccVersion: 2.1.274
variables:
  - DATA_MCP_CONNECT_ENDPOINT_NOT_FOUND_VAR_0
  - DATA_MCP_CONNECT_ENDPOINT_NOT_FOUND_VAR_1
  - DATA_MCP_CONNECT_ENDPOINT_NOT_FOUND_VAR_2
-->
MCP endpoint not found at ${DATA_MCP_CONNECT_ENDPOINT_NOT_FOUND_VAR_0(DATA_MCP_CONNECT_ENDPOINT_NOT_FOUND_VAR_1,DATA_MCP_CONNECT_ENDPOINT_NOT_FOUND_VAR_2,{detail:"origin"})??"(unparseable url)"}. Check the URL in your MCP config.
