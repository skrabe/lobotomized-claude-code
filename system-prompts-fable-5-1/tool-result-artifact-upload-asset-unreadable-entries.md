<!--
name: Artifact Upload Asset Unreadable Entries
description: >-
  upload_asset tool_result note that some result rows could not be read and
  list_assets/list scope assets shows what is stored.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_UNREADABLE_ENTRIES_VAR_0
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_UNREADABLE_ENTRIES_VAR_1
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_UNREADABLE_ENTRIES_VAR_2
-->

${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_UNREADABLE_ENTRIES_VAR_0} more ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_UNREADABLE_ENTRIES_VAR_1(TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_UNREADABLE_ENTRIES_VAR_0,"entry","entries")} of this record could not be read; ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_UNREADABLE_ENTRIES_VAR_2('action "list_assets"',()=>'action "list" with `scope: "assets"`')} shows what the artifact holds.
