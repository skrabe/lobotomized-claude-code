<!--
name: 'Tool Result: Bash worktree guard --ignore-other-worktrees remedy'
description: >-
  Tells Claude to create its own branch with git switch -c or checkout -b
  instead
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_IGNORE_OTHER_WORKTREES_REMEDY_VAR_0
-->
Use a branch of its own: git ${TOOL_RESULT_BASH_WORKTREE_GUARD_IGNORE_OTHER_WORKTREES_REMEDY_VAR_0} ${TOOL_RESULT_BASH_WORKTREE_GUARD_IGNORE_OTHER_WORKTREES_REMEDY_VAR_0==="switch"?"-c":"-b"} <new-branch> <commit>.
