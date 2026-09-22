<!--
name: 'Tool Result: Worktree create — hook emitted a dotted path'
description: >-
  EnterWorktree error (head) when the WorktreeCreate hook returns a worktree
  path containing dot segments the symlink screen cannot verify.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_WORKTREE_CREATE_HOOK_DOTTED_PATH_REJECTED_VAR_0
-->
Cannot use the WorktreeCreate hook's worktree: the hook emitted a path with dot segments (${TOOL_RESULT_WORKTREE_CREATE_HOOK_DOTTED_PATH_REJECTED_VAR_0.worktreePath}). The 
