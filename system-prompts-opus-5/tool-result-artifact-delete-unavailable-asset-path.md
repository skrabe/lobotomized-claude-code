<!--
name: Artifact Delete Unavailable Use Asset Path
description: >-
  core-verb-unavailable deny/validate/throw message when delete means remove one
  uploaded asset rather than a whole Artifact.
ccVersion: 2.1.257
-->
deleting a whole Artifact is not available in this session — `delete` here takes `path` (an uploaded asset's id, from a `scope: "assets"` listing) and removes that one asset
