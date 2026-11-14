<!--
name: 'Tool result: ExitWorktree remove outside launch'
description: >-
  ExitWorktree refusal to remove a worktree outside the launch folders under
  blockWritesOutsideWorkingDirectories; use action keep
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_EXITWORKTREE_REMOVE_OUTSIDE_LAUNCH_VAR_0
  - TOOL_RESULT_EXITWORKTREE_REMOVE_OUTSIDE_LAUNCH_VAR_1
  - TOOL_RESULT_EXITWORKTREE_REMOVE_OUTSIDE_LAUNCH_VAR_2
-->
The worktree at ${TOOL_RESULT_EXITWORKTREE_REMOVE_OUTSIDE_LAUNCH_VAR_0(TOOL_RESULT_EXITWORKTREE_REMOVE_OUTSIDE_LAUNCH_VAR_1(TOOL_RESULT_EXITWORKTREE_REMOVE_OUTSIDE_LAUNCH_VAR_2.worktreePath))} lies outside the folders that this session was launched with, and permissions.blockWritesOutsideWorkingDirectories keeps writes to those folders, so this tool will not remove it. Use action: "keep" to exit and leave it on disk.
