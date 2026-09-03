<!--
name: 'Tool Result: Artifact Publish Removal Requires Base Version'
description: >-
  Refuses an Artifact publish that removes files without naming the current
  version as baseVersion.
ccVersion: 2.1.246
-->
A removal applies to the artifact's current version, and this publish didn't name that version (`baseVersion`), so nothing was published. Publish again with the version named, or without the `null` entries.
