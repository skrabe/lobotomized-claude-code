<!--
name: 'Tool description: MCP authenticate intro'
description: >-
  Opening of the MCP authenticate tool description stating which MCP server is
  installed but requires authentication, with an optional search-redial hint.
ccVersion: 2.1.326
variables:
  - TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_0
  - TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_1
  - TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_2
  - TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_3
  - TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_4
  - TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_5
-->
The "${TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_0(TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_1)}" MCP server (${TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_2}) is installed but requires authentication. ${await TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_3().searchRedial?.TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_4({name:TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_1,config:TOOL_DESCRIPTION_MCP_AUTHENTICATE_INTRO_VAR_5})?"A sign-in may still be good: calling one of the server's own tools by name, or searching for the server's name, connects again with the sign-in already held, so try that first. ":""}
