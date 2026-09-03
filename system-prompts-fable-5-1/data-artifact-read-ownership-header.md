<!--
name: Artifact read ownership header
description: >-
  Ownership descriptor for an artifact the session owns, with type-locked and
  co-written qualifiers.
ccVersion: 2.1.239
variables:
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_1
-->
owned by you${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0}${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_1.typeLocked?"; the page comes from its Artifact type and was written by the type's publisher":DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_1.cowritten?"; may include contributions from other writers":""}
