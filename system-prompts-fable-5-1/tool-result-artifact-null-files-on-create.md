<!--
name: 'Tool Result: Artifact Null Files On Create'
description: >-
  Validation error when `files` contains null removals but the publish would
  create a new artifact, which has nothing to remove.
ccVersion: 2.1.246
-->
A `null` entry in `files` removes a file from an existing artifact, and this publish would create a new artifact, which has nothing to remove. Drop the `null` entries, or, to update an existing artifact, pass its `url`
