<!--
name: 'Data: Artifact Type Newer Release Will Apply'
description: >-
  Type-lock suffix when a newer release exists and will be applied the next time
  the Artifact is opened or read, with nothing for the model to do now.
ccVersion: 2.1.237
variables:
  - DATA_ARTIFACT_TYPE_NEWER_RELEASE_WILL_APPLY_VAR_0
  - DATA_ARTIFACT_TYPE_NEWER_RELEASE_WILL_APPLY_VAR_1
-->
 Its type has a newer release (${DATA_ARTIFACT_TYPE_NEWER_RELEASE_WILL_APPLY_VAR_0(DATA_ARTIFACT_TYPE_NEWER_RELEASE_WILL_APPLY_VAR_1.latest)}); this Artifact moves to it on its own the next time it is opened or read — nothing to do here.
