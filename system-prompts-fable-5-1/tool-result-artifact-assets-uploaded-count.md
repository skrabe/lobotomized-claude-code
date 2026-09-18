<!--
name: 'Tool Result: Artifact Assets Uploaded Count'
description: >-
  Multi-file upload_asset tool_result header stating how many of the requested
  files are now stored in the artifact.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_ASSETS_UPLOADED_COUNT_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSETS_UPLOADED_COUNT_VAR_1
  - TOOL_RESULT_ARTIFACT_ASSETS_UPLOADED_COUNT_VAR_2
-->
Assets uploaded: ${TOOL_RESULT_ARTIFACT_ASSETS_UPLOADED_COUNT_VAR_0.length} of ${TOOL_RESULT_ARTIFACT_ASSETS_UPLOADED_COUNT_VAR_1} ${TOOL_RESULT_ARTIFACT_ASSETS_UPLOADED_COUNT_VAR_2(TOOL_RESULT_ARTIFACT_ASSETS_UPLOADED_COUNT_VAR_1,"file")} ${TOOL_RESULT_ARTIFACT_ASSETS_UPLOADED_COUNT_VAR_0.length===1?"is":"are"} now stored in the artifact.
