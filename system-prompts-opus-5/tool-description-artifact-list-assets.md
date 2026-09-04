<!--
name: Artifact list_assets action description
description: Dynamic tool description for the Artifact tool's list_assets action.
ccVersion: 2.1.261
variables:
  - TOOL_DESCRIPTION_ARTIFACT_LIST_ASSETS_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_LIST_ASSETS_VAR_1
-->
List the files in a published artifact's asset store${TOOL_DESCRIPTION_ARTIFACT_LIST_ASSETS_VAR_0(TOOL_DESCRIPTION_ARTIFACT_LIST_ASSETS_VAR_1)} (ids, types, sizes); the user's own artifacts list without asking, anyone else's ask once per artifact${TOOL_DESCRIPTION_ARTIFACT_LIST_ASSETS_VAR_2()?" — an approval also covers server-side copies of them into other artifacts":""}.
