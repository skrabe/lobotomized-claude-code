<!--
name: 'Tool Result: Worktree Submodule Gitdir Outside Modules'
description: >-
  ExitWorktree refusal clause when a submodule points at a git directory outside
  this worktree so its contents cannot be vouched for.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_WORKTREE_SUBMODULE_GITDIR_OUTSIDE_MODULES_VAR_0
-->
submodule ${TOOL_RESULT_WORKTREE_SUBMODULE_GITDIR_OUTSIDE_MODULES_VAR_0??"checkout"} points at a git directory outside this worktree's own, or its object alternates or config lead somewhere this worktree cannot vouch for
