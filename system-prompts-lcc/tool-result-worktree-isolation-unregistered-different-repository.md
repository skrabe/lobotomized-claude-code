<!--
name: 'Tool Result: Worktree isolation unregistered different repository'
description: >-
  Refusal when a worktree under a checkout's .claude/worktrees leads to a
  different repository
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_DIFFERENT_REPOSITORY_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_DIFFERENT_REPOSITORY_VAR_1
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_DIFFERENT_REPOSITORY_VAR_2
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_DIFFERENT_REPOSITORY_VAR_3
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_DIFFERENT_REPOSITORY_VAR_4
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_DIFFERENT_REPOSITORY_VAR_0} as an isolation worktree: ${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_DIFFERENT_REPOSITORY_VAR_1}, and its .git leads to a different repository, ${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_DIFFERENT_REPOSITORY_VAR_2(TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_DIFFERENT_REPOSITORY_VAR_3.commonDir,"whose path is not repeated here")}. If you or a WorktreeCreate hook made this worktree, recreate it somewhere that is not inside any checkout's .claude/worktrees directory; if ${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_DIFFERENT_REPOSITORY_VAR_4} was never meant to be a repository, its .git is stray — look at what it holds, then remove it; if nobody meant to put a worktree here, do not trust it or run git in it.
