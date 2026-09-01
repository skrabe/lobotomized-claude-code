<!--
name: Artifact Created From Type Data Guidance
description: >-
  created_from_type tool_result clause telling the model how to publish data
  files onto the new Artifact without type_url.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_DATA_GUIDANCE_VAR_0
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_DATA_GUIDANCE_VAR_1
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_DATA_GUIDANCE_VAR_2
-->
What content it takes depends on the type${TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_DATA_GUIDANCE_VAR_0.kind==="read"?" — follow its instructions below (they cover only this Artifact's own content)":""}. If it takes data files, publish one as \`file_path\` (more via \`files\`) with \`url\`: ${TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_DATA_GUIDANCE_VAR_1(TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_DATA_GUIDANCE_VAR_2)} and no \`type_url\` — never index.html or any of the type's files.
