<!--
name: 'Tool result: EnterWorktree resumed on earlier base'
description: >-
  EnterWorktree result tail: existing worktree resumed on its earlier base
  because reset was skipped; keep working from it and do not merge, rebase, pull
  or reset
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_ENTERWORKTREE_RESUMED_EARLIER_BASE_VAR_0
  - TOOL_RESULT_ENTERWORKTREE_RESUMED_EARLIER_BASE_VAR_1
  - TOOL_RESULT_ENTERWORKTREE_RESUMED_EARLIER_BASE_VAR_2
-->
 A worktree with this name already existed and was resumed on its earlier base, because ${TOOL_RESULT_ENTERWORKTREE_RESUMED_EARLIER_BASE_VAR_0(TOOL_RESULT_ENTERWORKTREE_RESUMED_EARLIER_BASE_VAR_1.resetToFreshBaseSkipped)}. Keep working from this base and do not merge, rebase, pull or reset to catch up; if the task needs the current base, ${TOOL_RESULT_ENTERWORKTREE_RESUMED_EARLIER_BASE_VAR_2(TOOL_RESULT_ENTERWORKTREE_RESUMED_EARLIER_BASE_VAR_1.resetToFreshBaseSkipped)}.
