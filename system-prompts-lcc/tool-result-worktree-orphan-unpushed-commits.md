<!--
name: 'Tool Result: worktree orphan unpushed commits'
description: >-
  Error refusing to self-heal an orphaned worktree whose branch has unpushed
  commits.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WORKTREE_ORPHAN_UNPUSHED_COMMITS_VAR_0
  - TOOL_RESULT_WORKTREE_ORPHAN_UNPUSHED_COMMITS_VAR_1
  - TOOL_RESULT_WORKTREE_ORPHAN_UNPUSHED_COMMITS_VAR_2
-->
Orphaned worktree dir at ${TOOL_RESULT_WORKTREE_ORPHAN_UNPUSHED_COMMITS_VAR_0(TOOL_RESULT_WORKTREE_ORPHAN_UNPUSHED_COMMITS_VAR_1)} but branch ${TOOL_RESULT_WORKTREE_ORPHAN_UNPUSHED_COMMITS_VAR_2} has unpushed commits — refusing to self-heal. Push or delete the branch, then retry.
