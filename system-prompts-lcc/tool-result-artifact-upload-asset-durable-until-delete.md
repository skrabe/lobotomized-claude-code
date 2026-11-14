<!--
name: 'Tool Result: Artifact upload asset durable until delete'
description: >-
  Note that stored assets are loadable by anyone who can open the artifact and
  durable until deleted.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_DURABLE_UNTIL_DELETE_VAR_0
-->

Everyone who can open the artifact can load the stored files; each is durable until deleted with ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_DURABLE_UNTIL_DELETE_VAR_0('action "delete_asset"',()=>'action "delete" and its id as `path`')}.
