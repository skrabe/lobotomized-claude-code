<!--
name: 'Tool Result: Artifact Type Stray Fields'
description: >-
  Rejection when a typed Artifact is published with `capabilities`, `contract`,
  or `lang`, which come from the type.
ccVersion: 2.1.273
-->
an Artifact created from an Artifact type takes only its own files — `capabilities` and `contract` come from the type; drop them and publish again
