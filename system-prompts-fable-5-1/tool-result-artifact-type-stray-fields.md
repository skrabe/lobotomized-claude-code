<!--
name: 'Tool Result: Artifact Type Stray Fields'
description: >-
  Rejection when a typed Artifact is published with `capabilities`, `contract`,
  or `lang`, which come from the type.
ccVersion: 2.1.237
-->
an Artifact created from an Artifact type takes only its own files — `capabilities`, `contract`, and `lang` come from the type; drop them and publish again
