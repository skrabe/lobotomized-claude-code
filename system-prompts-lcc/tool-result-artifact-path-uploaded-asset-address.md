<!--
name: 'Tool Result: Artifact path is an uploaded asset address'
description: >-
  Error when an artifact path is an uploaded asset's address, explaining how to
  read assets by their 32-character id
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_ARTIFACT_PATH_UPLOADED_ASSET_ADDRESS_VAR_0
  - TOOL_RESULT_ARTIFACT_PATH_UPLOADED_ASSET_ADDRESS_VAR_1
  - TOOL_RESULT_ARTIFACT_PATH_UPLOADED_ASSET_ADDRESS_VAR_2
-->
path ${TOOL_RESULT_ARTIFACT_PATH_UPLOADED_ASSET_ADDRESS_VAR_0(TOOL_RESULT_ARTIFACT_PATH_UPLOADED_ASSET_ADDRESS_VAR_1)} is the address of an uploaded asset, not a published file. An asset is read one per call by its 32-character id, the part after "_blob/": ${TOOL_RESULT_ARTIFACT_PATH_UPLOADED_ASSET_ADDRESS_VAR_2('action "read_asset" with the id as `asset_id`',()=>'action "read" with the id as `path`')}
