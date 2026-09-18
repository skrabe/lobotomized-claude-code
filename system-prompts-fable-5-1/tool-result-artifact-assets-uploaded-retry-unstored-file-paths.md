<!--
name: Artifact Assets Uploaded Retry Unstored File Paths
description: >-
  Partial-failure clause of the upload_asset tool_result telling the model to
  fix failures and retry only the listed file_paths, none of which were stored.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_ASSETS_UPLOADED_RETRY_UNSTORED_FILE_PATHS_VAR_0
-->

To upload the rest, fix what stopped them, then call again with only these in \`file_paths\`: [${TOOL_RESULT_ARTIFACT_ASSETS_UPLOADED_RETRY_UNSTORED_FILE_PATHS_VAR_0.join(", ")}]. None of them is stored, so nothing is stored twice.
