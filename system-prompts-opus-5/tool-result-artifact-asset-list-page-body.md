<!--
name: Asset list page body
description: >-
  Body of the list_assets tool result introducing the page of asset rows and how
  to reference, read, or delete them.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_1
  - TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_2
-->
${TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_0||TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_1!==void 0&&TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_2.length<TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_1?`This page (${TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_2.length}, oldest first)`:"Oldest first"}; reference one from the page by its relative url, read or delete it by the id after "_blob/":
${TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_2.join(`
`)}
