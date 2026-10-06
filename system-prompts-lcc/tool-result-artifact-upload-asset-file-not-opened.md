<!--
name: 'Tool result: Artifact upload_asset file not opened'
description: Artifact upload_asset error when a listed file is missing or cannot be opened.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_FILE_NOT_OPENED_VAR_0
-->
${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_FILE_NOT_OPENED_VAR_0.kind==="missing"?"the file was not found":TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_FILE_NOT_OPENED_VAR_0.message.replaceAll("file_path","this file").replace(/[.\s]+$/,"")}. Nothing was sent.
