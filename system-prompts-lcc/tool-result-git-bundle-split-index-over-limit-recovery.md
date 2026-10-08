<!--
name: Oversized split-index recovery
description: >-
  Explains safe recovery when an individual split-index file exceeds the upload
  limit.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_GIT_BUNDLE_SPLIT_INDEX_OVER_LIMIT_RECOVERY_VAR_0
-->
 Do not delete that split-index file by hand: the index may need it. If this project has so many files that a fresh clone’s index would be over that limit too, this upload has no way round it. If not, use ${TOOL_RESULT_GIT_BUNDLE_SPLIT_INDEX_OVER_LIMIT_RECOVERY_VAR_0}
