<!--
name: Artifact Upload Asset Reference By Url
description: >-
  upload_asset success instruction to reference stored files by url verbatim and
  store ids in the artifact database.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_REFERENCE_BY_URL_VAR_0
-->
 Reference each from the page by its url verbatim — e.g. <img src="…the url…"> — which resolves in every view of the artifact; store the id in the artifact's database if rows need to point at it.
${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_REFERENCE_BY_URL_VAR_0.join(`
`)}
