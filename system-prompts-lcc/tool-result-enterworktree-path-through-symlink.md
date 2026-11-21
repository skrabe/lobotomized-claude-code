<!--
name: 'Tool result: EnterWorktree path through symlink'
description: >-
  EnterWorktree error: session not moved because the worktree path leads
  elsewhere through a symlink; nothing removed, tell the user
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_ENTERWORKTREE_PATH_THROUGH_SYMLINK_VAR_0
  - TOOL_RESULT_ENTERWORKTREE_PATH_THROUGH_SYMLINK_VAR_1
  - TOOL_RESULT_ENTERWORKTREE_PATH_THROUGH_SYMLINK_VAR_2
-->
The session was not moved: ${TOOL_RESULT_ENTERWORKTREE_PATH_THROUGH_SYMLINK_VAR_0(TOOL_RESULT_ENTERWORKTREE_PATH_THROUGH_SYMLINK_VAR_1.worktreePath)} leads to another folder through a symlink. Nothing was removed. Tell the user.${TOOL_RESULT_ENTERWORKTREE_PATH_THROUGH_SYMLINK_VAR_1.enteredExisting?"":TOOL_RESULT_ENTERWORKTREE_PATH_THROUGH_SYMLINK_VAR_1.vcsCopy?.TOOL_RESULT_ENTERWORKTREE_PATH_THROUGH_SYMLINK_VAR_2==="mod"?" The vcs.isolate hook has to answer the folder's real path.":TOOL_RESULT_ENTERWORKTREE_PATH_THROUGH_SYMLINK_VAR_1.hookBased?" The WorktreeCreate hook has to print the folder's real path.":""}
