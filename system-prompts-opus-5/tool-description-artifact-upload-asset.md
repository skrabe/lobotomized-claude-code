<!--
name: Artifact upload_asset action description
description: >-
  Dynamic tool description for the Artifact tool's upload_asset action,
  including its approval-scope clause.
ccVersion: 2.1.234
variables:
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_3
-->
Upload a local file into a published artifact's asset store on claude.ai${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_0(TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_1)} (${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_2}); ${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_3?"each upload asks separately":"approving covers further uploads to this artifact for the rest of this session, except files outside the working paths or reached through a link, which ask every time"}.
