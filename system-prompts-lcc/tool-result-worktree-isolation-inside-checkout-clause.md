<!--
name: 'Tool Result: Worktree isolation inside checkout clause'
description: >-
  Clause stating the worktree is inside a checkout's area where only worktrees
  that checkout made are accepted
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_INSIDE_CHECKOUT_CLAUSE_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_INSIDE_CHECKOUT_CLAUSE_VAR_1
  - TOOL_RESULT_WORKTREE_ISOLATION_INSIDE_CHECKOUT_CLAUSE_VAR_2
-->
it is inside ${TOOL_RESULT_WORKTREE_ISOLATION_INSIDE_CHECKOUT_CLAUSE_VAR_0}${TOOL_RESULT_WORKTREE_ISOLATION_INSIDE_CHECKOUT_CLAUSE_VAR_1}, where only worktrees that the checkout ${TOOL_RESULT_WORKTREE_ISOLATION_INSIDE_CHECKOUT_CLAUSE_VAR_2} itself made (git worktree add, run in that checkout) are accepted
