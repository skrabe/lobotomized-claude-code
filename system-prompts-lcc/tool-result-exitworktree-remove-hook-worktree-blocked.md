<!--
name: 'Tool result: ExitWorktree hook worktree removal blocked'
description: >-
  ExitWorktree refusal to remove a mod- or hook-made worktree whose removal
  would run outside the sandbox under blockWritesOutsideWorkingDirectories
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_EXITWORKTREE_REMOVE_HOOK_WORKTREE_BLOCKED_VAR_0
  - TOOL_RESULT_EXITWORKTREE_REMOVE_HOOK_WORKTREE_BLOCKED_VAR_1
  - TOOL_RESULT_EXITWORKTREE_REMOVE_HOOK_WORKTREE_BLOCKED_VAR_2
-->
${TOOL_RESULT_EXITWORKTREE_REMOVE_HOOK_WORKTREE_BLOCKED_VAR_0.vcsCopy?.TOOL_RESULT_EXITWORKTREE_REMOVE_HOOK_WORKTREE_BLOCKED_VAR_1==="mod"?`A mod made the worktree at ${TOOL_RESULT_EXITWORKTREE_REMOVE_HOOK_WORKTREE_BLOCKED_VAR_2(TOOL_RESULT_EXITWORKTREE_REMOVE_HOOK_WORKTREE_BLOCKED_VAR_0.worktreePath)}. Its removal, by that mod,`:`A WorktreeCreate hook made the worktree at ${TOOL_RESULT_EXITWORKTREE_REMOVE_HOOK_WORKTREE_BLOCKED_VAR_2(TOOL_RESULT_EXITWORKTREE_REMOVE_HOOK_WORKTREE_BLOCKED_VAR_0.worktreePath)}. Its removal, by a WorktreeRemove hook or by git where none is configured,`} would run outside the sandbox, and permissions.blockWritesOutsideWorkingDirectories keeps this session's writes to the folders that it was launched with, so this tool will not remove it. Use action: "keep" to exit and leave it on disk. If the user wants it gone, they can remove it outside this session with the tool that made it.
