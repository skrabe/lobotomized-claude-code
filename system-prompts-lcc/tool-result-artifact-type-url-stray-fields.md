<!--
name: 'Tool Result: Artifact type_url stray fields'
description: >-
  Artifact tool error listing fields that must be removed from a publish with
  type_url.
ccVersion: 2.1.291
-->
a publish with `type_url` always creates a new Artifact whose page and settings come from the type — remove `url`, `pr_review`, `capabilities`, `contract`, `deadline`, and `force`
