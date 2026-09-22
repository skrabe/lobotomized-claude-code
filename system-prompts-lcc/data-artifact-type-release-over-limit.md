<!--
name: 'Data: Artifact Type Release Over Limit'
description: >-
  Type-lock suffix when a newer release cannot apply because together with this
  Artifact's own files it would exceed count or total-size limits.
ccVersion: 2.1.237
variables:
  - DATA_ARTIFACT_TYPE_RELEASE_OVER_LIMIT_VAR_0
  - DATA_ARTIFACT_TYPE_RELEASE_OVER_LIMIT_VAR_1
-->
 ${DATA_ARTIFACT_TYPE_RELEASE_OVER_LIMIT_VAR_0} that can't be applied yet: together with this Artifact's own files it would exceed the limits on an Artifact's files (count or total size), so it stays on release ${DATA_ARTIFACT_TYPE_RELEASE_OVER_LIMIT_VAR_1}; if total size is the cause, publishing smaller own files lets a later open apply it — own files can't be removed from here.
