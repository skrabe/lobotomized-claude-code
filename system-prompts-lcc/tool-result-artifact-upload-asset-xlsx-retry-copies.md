<!--
name: 'Tool result: .xlsx upload error copies'
description: >-
  Suffix on a failed .xlsx upload error telling the model to delete extra stored
  copies after a retry.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_XLSX_RETRY_COPIES_VAR_0
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_XLSX_RETRY_COPIES_VAR_1
-->
${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_XLSX_RETRY_COPIES_VAR_0.message} Every stored copy of an .xlsx keeps the artifact from being made public or shared outside the organization: after a retry, ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_XLSX_RETRY_COPIES_VAR_1('action "list_assets"',()=>'action "list" with `scope: "assets"`')} shows the copies, so delete any extra one.
