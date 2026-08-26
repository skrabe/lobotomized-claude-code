<!--
name: Artifact upload_asset action description
description: >-
  Dynamic tool description for the Artifact tool's upload_asset action,
  including its approval-scope clause.
ccVersion: 2.1.246
variables:
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_3
-->
Upload a local file into a published artifact's asset store on claude.ai${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_0(TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_1)} (${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_2}); ${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_3?"each upload asks separately":"approving covers later uploads to this artifact this session; text files, linked files and files outside working paths still ask"}.
