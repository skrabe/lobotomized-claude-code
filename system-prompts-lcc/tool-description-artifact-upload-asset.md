<!--
name: Artifact upload_asset action description
description: >-
  Dynamic tool description for the Artifact tool's upload_asset action,
  including list-vs-file wording and the approval-scope clause.
ccVersion: 2.1.276
variables:
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_3
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_4
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_5
  - TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_6
-->
Upload ${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_0.kind==="list"?`a list of ${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_0.paths.length} local ${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_1(TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_0.paths.length,"file")}`:"a local file"} into a published artifact's asset store on claude.ai${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_2(TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_3)} (${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_4}); ${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_5?"each upload asks separately":`approving covers later uploads ${TOOL_DESCRIPTION_ARTIFACT_UPLOAD_ASSET_VAR_6()?"to (and copies of other artifacts' assets into) ":"to "}this artifact this session; CSV, Markdown, JSON and plain-text files, linked files and files outside working paths still ask`}.
