<!--
name: 'Tool Result: Git Bundle Worktree Entry Under Temp'
description: >-
  Previous-way clause refusing the upload when .git names a worktree admin entry
  under a temporary directory.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_WORKTREE_ENTRY_UNDER_TEMP_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_WORKTREE_ENTRY_UNDER_TEMP_VAR_1
-->
its .git file names a worktree entry under a temporary directory (${TOOL_RESULT_GIT_BUNDLE_WORKTREE_ENTRY_UNDER_TEMP_VAR_0(TOOL_RESULT_GIT_BUNDLE_WORKTREE_ENTRY_UNDER_TEMP_VAR_1.gitDir)}), where sessions write — run git worktree repair if this tree was moved, or start from the repository’s main checkout
