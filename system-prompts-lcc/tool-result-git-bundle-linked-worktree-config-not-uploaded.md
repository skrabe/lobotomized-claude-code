<!--
name: 'Git bundle: linked worktree config.worktree'
description: Upload refusal when a linked working tree carries per-worktree configuration
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_GIT_BUNDLE_LINKED_WORKTREE_CONFIG_NOT_UPLOADED_VAR_0
-->
Not uploading this working tree: this checkout is a linked working tree ${TOOL_RESULT_GIT_BUNDLE_LINKED_WORKTREE_CONFIG_NOT_UPLOADED_VAR_0.worktree_config} Start from the repository’s main checkout instead (a new worktree made from this one would be refused too: a current git copies this file into it).
