<!--
name: Artifact Publish Null File Entry On First Publish
description: >-
  Publish refusal when files contains null removals on a first publish that has
  nothing to remove.
ccVersion: 2.1.246
-->
A `null` entry in `files` removes a file from an existing artifact, and a first publish has nothing to remove, so nothing was published. Drop the `null` entries.
