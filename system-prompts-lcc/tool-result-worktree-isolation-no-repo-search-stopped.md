<!--
name: 'Tool Result: Worktree isolation no-repo search stopped'
description: >-
  Refusal when a tree with no repository is inside a checkout's
  .claude/worktrees but git could not find that checkout's repository from it
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SEARCH_STOPPED_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SEARCH_STOPPED_VAR_1
  - TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SEARCH_STOPPED_VAR_2
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SEARCH_STOPPED_VAR_0} as an isolation worktree: it holds no git repository of its own, yet it is inside the .claude/worktrees of ${TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SEARCH_STOPPED_VAR_1}, which holds one, and git could not find that repository from it (a .git file or directory between them, under .claude, stops the search). Remove that entry, or recreate the worktree from ${TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SEARCH_STOPPED_VAR_2}.
