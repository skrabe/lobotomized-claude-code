<!--
name: Artifact MCP call-contract guidance
description: >-
  Guidance injected into the artifact runtime-capabilities skill body telling
  the model where the window.claude.mcp type definitions (.d.ts) are extracted
  and to read them before writing any window.claude.mcp call.
ccVersion: 2.1.234
variables:
  - DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_0
  - DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_1
  - DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_2
  - DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_3
  - DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_4
-->
**Call contract** (runtime contract ${DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_0.version}). The platform-served \`window.claude\` type definitions for this contract are extracted under \`${DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_1}\`: ${DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_0.files.map((DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_2)=>`\`${DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_2}\``).join(", ")}. ${DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_3} authoritative for this contract version over any remembered API shape. ${DATA_ARTIFACT_MCP_CALL_CONTRACT_GUIDANCE_VAR_4}
