<!--
name: Asset list page body
description: >-
  Body of the list_assets tool result introducing the page of asset rows and how
  to reference, read, or delete them.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_1
-->
${TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_0.next!==void 0||TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_1.length<TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_0.usage.files?`This page (${TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_1.length}, oldest first)`:"Oldest first"}; reference one from the page by its relative url, read or delete it by the id after "_blob/":
${TOOL_RESULT_ARTIFACT_ASSET_LIST_PAGE_BODY_VAR_1.join(`
`)}
