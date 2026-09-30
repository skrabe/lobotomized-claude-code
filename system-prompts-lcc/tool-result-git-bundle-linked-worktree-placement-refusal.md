<!--
name: 'Tool Result: Git Bundle Linked Worktree Placement Refusal'
description: >-
  Upload refusal for a linked working tree whose repository sits in a placement
  the upload does not take, suggesting the main checkout, a worktree in an
  ordinary location, or an ordinary clone.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_GIT_BUNDLE_LINKED_WORKTREE_PLACEMENT_REFUSAL_VAR_0
-->
Not uploading this working tree: this checkout is a linked working tree ${TOOL_RESULT_GIT_BUNDLE_LINKED_WORKTREE_PLACEMENT_REFUSAL_VAR_0.placement} Start from the repository’s main checkout, or from a working tree made with git worktree add in an ordinary location, instead; where neither serves, from an ordinary clone of the repository.
