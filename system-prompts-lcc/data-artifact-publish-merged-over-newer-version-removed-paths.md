<!--
name: 'Data: Artifact publish merged-over removed paths'
description: >-
  Merged-over-newer-version notice sentence listing files removed on the live
  version; republishing one recreates it, so only do so if the user wants it
  back.
ccVersion: 2.1.330
variables:
  - DATA_ARTIFACT_PUBLISH_MERGED_OVER_NEWER_VERSION_REMOVED_PATHS_VAR_0
  - DATA_ARTIFACT_PUBLISH_MERGED_OVER_NEWER_VERSION_REMOVED_PATHS_VAR_1
-->
Removed: ${DATA_ARTIFACT_PUBLISH_MERGED_OVER_NEWER_VERSION_REMOVED_PATHS_VAR_0(DATA_ARTIFACT_PUBLISH_MERGED_OVER_NEWER_VERSION_REMOVED_PATHS_VAR_1)}. Publishing one of these again creates it afresh, so do that only if the user wants it back.
