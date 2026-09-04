<!--
name: Artifact copy_from Listing Truncated
description: >-
  copy_from tool_result line when more copied-asset rows exist than were shown,
  directing the model to list_assets on the destination.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_0
  - TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_1
-->

(${TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_0.unreadable+TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_0.pastCap} more ${TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_1(TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_0.unreadable+TOOL_RESULT_ARTIFACT_COPY_FROM_LISTING_TRUNCATED_VAR_0.pastCap,"row")} not shown — run action "list_assets" on the destination for the real listing)
