<!--
name: Artifact read_asset action description
description: Dynamic tool description for the Artifact tool's read_asset action.
ccVersion: 2.1.261
variables:
  - TOOL_DESCRIPTION_ARTIFACT_READ_ASSET_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_READ_ASSET_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_READ_ASSET_VAR_2
-->
Save one file from a published artifact's asset store${TOOL_DESCRIPTION_ARTIFACT_READ_ASSET_VAR_0(TOOL_DESCRIPTION_ARTIFACT_READ_ASSET_VAR_1)} into a local directory; reads of the user's own artifacts need no separate approval, anyone else's ask once per artifact${TOOL_DESCRIPTION_ARTIFACT_READ_ASSET_VAR_2()?" — an approval also covers server-side copies of them into other artifacts":""}, and the destination follows the file-edit rules.
