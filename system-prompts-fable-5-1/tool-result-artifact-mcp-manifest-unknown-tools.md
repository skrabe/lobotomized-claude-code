<!--
name: 'Tool Result: Artifact MCP Manifest Unknown Tools'
description: >-
  Artifact publish rejection when a connector's declared tools are not in this
  session, including the MCP-gateway inner-tool guidance.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_0
  - TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_1
  - TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_2
  - TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_3
  - TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_4
  - TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_5
  - TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_6
-->
${TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_0(TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_1.server)} "${TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_2}"${TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_3} has no ${TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_4(TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_1.unknown.length,"tool")} named ${TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_5.join(", ")} in this session — "tools" takes that connector's own top-level tool names${TOOL_RESULT_ARTIFACT_MCP_MANIFEST_UNKNOWN_TOOLS_VAR_6}; if this connector fronts other tools through its own search/execute tools (an MCP gateway), declare those and have the page reach the inner ones through them. The control plane would accept this manifest, but the page's calls would fail for viewers of this connector
