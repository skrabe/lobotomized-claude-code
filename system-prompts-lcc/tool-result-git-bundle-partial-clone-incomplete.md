<!--
name: 'Tool Result: Git Bundle Partial Clone Incomplete'
description: >-
  Bundle-failure result when a partial clone lacks working-tree blobs locally so
  the upload will not fetch them, telling the model to start from the GitHub
  source instead.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_GIT_BUNDLE_PARTIAL_CLONE_INCOMPLETE_VAR_0
-->
This partial clone does not hold every file of its working tree locally (a sparse checkout, or blobs never downloaded), so it cannot be uploaded without fetching from its remote, which the upload does not do — a full clone, made without --filter, would upload (git: ${TOOL_RESULT_GIT_BUNDLE_PARTIAL_CLONE_INCOMPLETE_VAR_0}). If that file is in fact present, its index entry names a stored object this repository has lost: \`git rm --cached <path>\` then \`git add <path>\`, on the path git names, stores it again
