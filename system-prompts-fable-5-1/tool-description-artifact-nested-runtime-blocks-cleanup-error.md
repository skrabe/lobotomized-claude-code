<!--
name: 'Tool Description: Artifact Nested Runtime Blocks Cleanup Error'
description: >-
  Publish error when nested frame-runtime comment blocks or data-frame-runtime
  attributes cannot be stripped cleanly.
ccVersion: 2.1.251
-->
This page carries `<!-- frame-runtime -->` serve-marker blocks or `data-frame-runtime` attributes nested so that removing one keeps exposing another — nothing a genuine page or a fetched artifact contains. Delete those comment blocks and attributes from the source and publish again.
