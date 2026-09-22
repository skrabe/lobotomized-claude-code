<!--
name: 'Data: Artifact Type Release Path Collision'
description: >-
  Type-lock suffix when a newer release cannot apply because some of this
  Artifact's own files use paths the release also ships; publishing here cannot
  remove them.
ccVersion: 2.1.237
variables:
  - DATA_ARTIFACT_TYPE_RELEASE_PATH_COLLISION_VAR_0
  - DATA_ARTIFACT_TYPE_RELEASE_PATH_COLLISION_VAR_1
  - DATA_ARTIFACT_TYPE_RELEASE_PATH_COLLISION_VAR_2
  - DATA_ARTIFACT_TYPE_RELEASE_PATH_COLLISION_VAR_3
-->
 ${DATA_ARTIFACT_TYPE_RELEASE_PATH_COLLISION_VAR_0} that can't be applied yet: ${DATA_ARTIFACT_TYPE_RELEASE_PATH_COLLISION_VAR_1} the release also ships${DATA_ARTIFACT_TYPE_RELEASE_PATH_COLLISION_VAR_2}, so it stays on release ${DATA_ARTIFACT_TYPE_RELEASE_PATH_COLLISION_VAR_3} until those files are removed or renamed — worth telling the user, since publishing here adds or updates own files but can't remove them.
