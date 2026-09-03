<!--
name: 'Tool Result: Git Bundle Linked Worktree Not Vouched'
description: >-
  Teleport git-bundle refusal when the checkout is a linked working tree whose
  pointer files this upload does not vouch for.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_GIT_BUNDLE_LINKED_WORKTREE_NOT_VOUCHED_VAR_0
-->
Not uploading this working tree: this checkout is a linked working tree ${TOOL_RESULT_GIT_BUNDLE_LINKED_WORKTREE_NOT_VOUCHED_VAR_0[e.detail??"admin_dir"]} Start from the repository’s main checkout, or from a working tree made with git worktree add in an ordinary location, instead.
