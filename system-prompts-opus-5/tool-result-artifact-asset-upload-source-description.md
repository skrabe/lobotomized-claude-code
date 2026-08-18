<!--
name: Artifact asset upload source description
description: >-
  Composed phrase naming the local file and its risk qualifiers, used in the
  upload ask message and its decisionReason.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_1
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_2
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_3
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_4
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_5
-->
the local file "${TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_0}"${TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_1?" (it resolves, through a symbolic link, outside this session’s allowed read paths)":TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_2?" (outside this session’s allowed read paths)":TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_3?" (a path spelling that can name a different file than it appears to)":""}${TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_4&&!TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_2?" (a hard link: the same file may also live elsewhere on this machine)":""} into the asset store of ${TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_SOURCE_DESCRIPTION_VAR_5}
