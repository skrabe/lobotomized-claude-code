<!--
name: 'Tool Result: Git Bundle Shallow Not a Plain File'
description: >-
  Remedy clause when a cloud bundle upload refuses because the shallow path is
  not the plain file git would have written.
ccVersion: 2.1.280
-->
 Look at it (ls -l): git keeps the list of this clone’s shallow commits there, as a small plain file — if this clone was not made with --depth, nothing should stand there and it can be removed. Then retry.
