<!--
name: Artifact Copy From Listing Truncated
description: >-
  Tells the model the copy-from asset listing was truncated and to list assets
  on the destination.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_0
  - TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_1
  - TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_2
-->

(${TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_0.unreadable+TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_0.pastCap} more ${TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_1(TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_0.unreadable+TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_0.pastCap,"row")} not shown — run ${TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_2('action "list_assets"',()=>'action "list" with `scope: "assets"`')} on the destination for the real listing)
