<!--
name: Artifact mcp capability read-both-files instruction
description: >-
  Fragment of the artifact-capabilities skill prompt telling the model to Read
  both the capability-contract file and mcp.d.ts before writing any code that
  calls the mcp capability.
ccVersion: 2.1.234
variables:
  - DATA_ARTIFACT_MCP_CONTRACT_AND_DEFINITIONS_READ_INSTRUCTION_VAR_0
  - DATA_ARTIFACT_MCP_CONTRACT_AND_DEFINITIONS_READ_INSTRUCTION_VAR_1
  - DATA_ARTIFACT_MCP_CONTRACT_AND_DEFINITIONS_READ_INSTRUCTION_VAR_2
-->
Read \`${DATA_ARTIFACT_MCP_CONTRACT_AND_DEFINITIONS_READ_INSTRUCTION_VAR_0}/${DATA_ARTIFACT_MCP_CONTRACT_AND_DEFINITIONS_READ_INSTRUCTION_VAR_1}\` (how a page reaches any capability on this contract) and \`${DATA_ARTIFACT_MCP_CONTRACT_AND_DEFINITIONS_READ_INSTRUCTION_VAR_0}/${DATA_ARTIFACT_MCP_CONTRACT_AND_DEFINITIONS_READ_INSTRUCTION_VAR_2}\` before writing any code that calls the \`mcp\` capability — they are
