<!--
name: upload_asset Extra Params Error
description: >-
  validateInput rejection when upload_asset is called with fields other than url
  and file_path or file_paths.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_EXTRA_PARAMS_ERROR_VAR_0
-->
action "upload_asset" takes only \`url\` and \`file_path\` (or \`file_paths\`) — remove ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_EXTRA_PARAMS_ERROR_VAR_0.join(", ")}.
