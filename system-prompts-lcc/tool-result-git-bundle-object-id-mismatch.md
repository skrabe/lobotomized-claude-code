<!--
name: 'Tool Result: Git Bundle Object Id Mismatch'
description: >-
  Refuses the upload when a git object does not match the id that names it, and
  tells the model to repair or re-clone.
ccVersion: 2.1.280
-->
Not uploading this working tree: its git directory holds an object that is not what its id names — something other than git wrote it there (`git fsck` usually names it). Nothing was uploaded; repair or re-clone the repository, then retry.
