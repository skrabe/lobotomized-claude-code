<!--
name: 'Tool Result: Git Bundle Partial Clone Incomplete'
description: >-
  Bundle-failure result when a partial clone lacks working-tree blobs locally so
  the upload will not fetch them, telling the model to start from the GitHub
  source instead.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_GIT_BUNDLE_PARTIAL_CLONE_INCOMPLETE_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_PARTIAL_CLONE_INCOMPLETE_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_PARTIAL_CLONE_INCOMPLETE_VAR_2
-->
This partial clone does not hold every file of its working tree locally (a sparse checkout, or blobs never downloaded), so it cannot be uploaded without fetching from its remote, which the upload does not do (git: ${TOOL_RESULT_GIT_BUNDLE_PARTIAL_CLONE_INCOMPLETE_VAR_0(TOOL_RESULT_GIT_BUNDLE_PARTIAL_CLONE_INCOMPLETE_VAR_1.stderr,TOOL_RESULT_GIT_BUNDLE_PARTIAL_CLONE_INCOMPLETE_VAR_2)})
