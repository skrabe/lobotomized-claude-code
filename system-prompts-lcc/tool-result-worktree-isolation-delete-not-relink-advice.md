<!--
name: 'Tool Result: Worktree isolation delete rather than re-link advice'
description: >-
  Advice to copy out and delete a suspect worktree rather than re-link it with
  git worktree repair, plus registry cleanup guidance
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_DELETE_NOT_RELINK_ADVICE_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_DELETE_NOT_RELINK_ADVICE_VAR_1
  - TOOL_RESULT_WORKTREE_ISOLATION_DELETE_NOT_RELINK_ADVICE_VAR_2
  - TOOL_RESULT_WORKTREE_ISOLATION_DELETE_NOT_RELINK_ADVICE_VAR_3
  - TOOL_RESULT_WORKTREE_ISOLATION_DELETE_NOT_RELINK_ADVICE_VAR_4
-->
If this worktree is yours, copy out what you need and delete it rather than re-link it: git worktree repair could also point other worktrees of that checkout, or this one, at an entry that code in a worktree added. ${TOOL_RESULT_WORKTREE_ISOLATION_DELETE_NOT_RELINK_ADVICE_VAR_0(TOOL_RESULT_WORKTREE_ISOLATION_DELETE_NOT_RELINK_ADVICE_VAR_1,TOOL_RESULT_WORKTREE_ISOLATION_DELETE_NOT_RELINK_ADVICE_VAR_2(TOOL_RESULT_WORKTREE_ISOLATION_DELETE_NOT_RELINK_ADVICE_VAR_3(TOOL_RESULT_WORKTREE_ISOLATION_DELETE_NOT_RELINK_ADVICE_VAR_4,"worktrees"),"that checkout's worktree registry (the worktrees directory in its git directory)"))} If it is not yours, do not trust it or run git in it.
