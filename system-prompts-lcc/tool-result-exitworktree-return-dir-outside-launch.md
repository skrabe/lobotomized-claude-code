<!--
name: 'Tool result: ExitWorktree return dir outside launch'
description: >-
  ExitWorktree refusal: the return directory lies outside the launch folders, so
  the session stays in the worktree
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_EXITWORKTREE_RETURN_DIR_OUTSIDE_LAUNCH_VAR_0
  - TOOL_RESULT_EXITWORKTREE_RETURN_DIR_OUTSIDE_LAUNCH_VAR_1
  - TOOL_RESULT_EXITWORKTREE_RETURN_DIR_OUTSIDE_LAUNCH_VAR_2
-->
The session stays in the worktree: ${TOOL_RESULT_EXITWORKTREE_RETURN_DIR_OUTSIDE_LAUNCH_VAR_0(TOOL_RESULT_EXITWORKTREE_RETURN_DIR_OUTSIDE_LAUNCH_VAR_1(TOOL_RESULT_EXITWORKTREE_RETURN_DIR_OUTSIDE_LAUNCH_VAR_2))}, the directory that ExitWorktree would return to, lies outside the folders that this session was launched with, and permissions.blockFileToolReadsOutsideWorkingDirectories keeps the session to those folders. Neither action can leave this worktree: go on working here.
