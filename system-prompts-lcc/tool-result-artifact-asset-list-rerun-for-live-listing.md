<!--
name: Artifact Asset List Rerun For Live Listing
description: >-
  Shared remedy fragment telling the model to run list_assets / list with scope
  assets again for the live listing.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_LIST_RERUN_FOR_LIVE_LISTING_VAR_0
-->
run ${TOOL_RESULT_ARTIFACT_ASSET_LIST_RERUN_FOR_LIVE_LISTING_VAR_0('action "list_assets"',()=>'action "list" with `scope: "assets"`')} again for the live listing
