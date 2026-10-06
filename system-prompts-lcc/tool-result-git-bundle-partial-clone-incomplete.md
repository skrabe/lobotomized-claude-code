<!--
name: 'Tool Result: Git Bundle Partial Clone Incomplete'
description: >-
  Bundle-failure result when a partial clone lacks working-tree blobs locally so
  the upload will not fetch them, telling the model to start from the GitHub
  source instead.
ccVersion: 2.1.291
-->
This partial clone does not hold every file of its working tree locally (a sparse checkout, or blobs never downloaded), so it cannot be uploaded without fetching from its remote, which the upload does not do — a full clone, made without --filter, would upload. If no file is missing from the working tree, the index names an object that this repository has lost: `git fsck --name-objects` prints it as “missing blob <id> (:<path>)”, and `git rm --cached <path>` then `git add <path>` stores it again
