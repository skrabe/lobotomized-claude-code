<!--
name: Artifact Type Applies Only To List
description: >-
  validateInput rejection when type is passed on a non-list call;
  create-from-type must use type_url.
ccVersion: 2.1.257
-->
`type` applies only to action "list" (it names the type whose Artifacts to list) — to create from a type, pass its link as `type_url`
