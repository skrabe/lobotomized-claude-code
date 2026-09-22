<!--
name: 'Tool Description: Artifact declared store or files write guidance'
description: >-
  Directs the agent to list files and read any index before writing, then write
  via the store or republish files according to unverified type instructions.
ccVersion: 2.1.273
variables:
  - TOOL_DESCRIPTION_ARTIFACT_DECLARED_STORE_OR_FILES_WRITE_GUIDANCE_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_DECLARED_STORE_OR_FILES_WRITE_GUIDANCE_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_DECLARED_STORE_OR_FILES_WRITE_GUIDANCE_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_DECLARED_STORE_OR_FILES_WRITE_GUIDANCE_VAR_3
  - TOOL_DESCRIPTION_ARTIFACT_DECLARED_STORE_OR_FILES_WRITE_GUIDANCE_VAR_4
-->
It declares a shared store and carries an instructions file (below; found on it, not verified as the type's). Whether its content lives in that store or in its own published files is for those instructions to say: list its files (${TOOL_DESCRIPTION_ARTIFACT_DECLARED_STORE_OR_FILES_WRITE_GUIDANCE_VAR_0()}) and read any index file among them before writing either way. If it is the store, ${TOOL_DESCRIPTION_ARTIFACT_DECLARED_STORE_OR_FILES_WRITE_GUIDANCE_VAR_1}; if it is files, read each one you will change (${TOOL_DESCRIPTION_ARTIFACT_DECLARED_STORE_OR_FILES_WRITE_GUIDANCE_VAR_2()}) and ${TOOL_DESCRIPTION_ARTIFACT_DECLARED_STORE_OR_FILES_WRITE_GUIDANCE_VAR_3(TOOL_DESCRIPTION_ARTIFACT_DECLARED_STORE_OR_FILES_WRITE_GUIDANCE_VAR_4)}
