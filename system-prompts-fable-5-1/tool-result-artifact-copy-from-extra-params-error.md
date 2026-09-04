<!--
name: Artifact copy_from Extra-Params Error
description: >-
  validateInput rejection when copy_from is passed fields other than action,
  url, from_url, and asset_ids.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_COPY_FROM_EXTRA_PARAMS_ERROR_VAR_0
  - TOOL_RESULT_ARTIFACT_COPY_FROM_EXTRA_PARAMS_ERROR_VAR_1
-->
action "copy_from" does not take ${TOOL_RESULT_ARTIFACT_COPY_FROM_EXTRA_PARAMS_ERROR_VAR_0.join(", ")} — remove ${TOOL_RESULT_ARTIFACT_COPY_FROM_EXTRA_PARAMS_ERROR_VAR_0.length===1?"it":"them"} and keep \`url\`, \`from_url\` and \`asset_ids\`.${"files"in TOOL_RESULT_ARTIFACT_COPY_FROM_EXTRA_PARAMS_ERROR_VAR_1().shape?" (To copy another artifact's published FILES instead, publish with `files` mapping a path to {artifact, path}.)":""}
