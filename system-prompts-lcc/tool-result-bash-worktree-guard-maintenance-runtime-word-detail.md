<!--
name: 'Tool result: Bash worktree guard maintenance runtime word detail'
description: >-
  Worktree guard detail when a word after maintenance/scalar run is filled in
  only at runtime.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_RUNTIME_WORD_DETAIL_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_RUNTIME_WORD_DETAIL_VAR_1
  - TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_RUNTIME_WORD_DETAIL_VAR_2
  - TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_RUNTIME_WORD_DETAIL_VAR_3
-->
has a word after ${TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_RUNTIME_WORD_DETAIL_VAR_0?"scalar run":TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_RUNTIME_WORD_DETAIL_VAR_1} (${TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_RUNTIME_WORD_DETAIL_VAR_2(TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_RUNTIME_WORD_DETAIL_VAR_3)}) that is filled in only when the command runs, so this check can't tell whether it registers the repository for background git maintenance, which would write your global git configuration
