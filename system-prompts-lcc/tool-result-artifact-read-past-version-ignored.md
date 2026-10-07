<!--
name: 'Tool Result: Artifact read past version ignored'
description: >-
  Artifact read error returned when the server served a different version than
  the one requested, explaining why nothing was read.
ccVersion: 2.1.292
-->
artifact read failed: the server served a different version from the one asked for, so nothing was read. It does that for an account that cannot edit the artifact; for one that can, the server ignored the version asked for.
