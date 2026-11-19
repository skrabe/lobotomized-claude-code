<!--
name: 'Tool Result: ExitWorktree on another branch with commits'
description: >-
  Refusal noting the worktree is now on another branch with commits the starting
  commit lacks; removing keeps the branch but the user may still be working
  there
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_EXITWORKTREE_ON_ANOTHER_BRANCH_COMMITS_VAR_0
  - TOOL_RESULT_EXITWORKTREE_ON_ANOTHER_BRANCH_COMMITS_VAR_1
-->
The worktree is now on another branch, which has ${TOOL_RESULT_EXITWORKTREE_ON_ANOTHER_BRANCH_COMMITS_VAR_0} ${TOOL_RESULT_EXITWORKTREE_ON_ANOTHER_BRANCH_COMMITS_VAR_0===1?"commit":"commits"} that this session's starting commit lacks. Removing the worktree keeps that branch, so no commit is lost, but the user may still be working there.${TOOL_RESULT_EXITWORKTREE_ON_ANOTHER_BRANCH_COMMITS_VAR_1}
