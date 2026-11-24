<!--
name: 'Tool result: ExitWorktree took to launch folder'
description: >-
  ExitWorktree result when the way back was missing or outside launch folders:
  the session is now in a folder it was launched with
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_EXITWORKTREE_TOOK_TO_LAUNCH_FOLDER_VAR_0
  - TOOL_RESULT_EXITWORKTREE_TOOK_TO_LAUNCH_FOLDER_VAR_1
  - TOOL_RESULT_EXITWORKTREE_TOOK_TO_LAUNCH_FOLDER_VAR_2
  - TOOL_RESULT_EXITWORKTREE_TOOK_TO_LAUNCH_FOLDER_VAR_3
-->
${TOOL_RESULT_EXITWORKTREE_TOOK_TO_LAUNCH_FOLDER_VAR_0.originalCwdMissing?`The original directory ${TOOL_RESULT_EXITWORKTREE_TOOK_TO_LAUNCH_FOLDER_VAR_1(TOOL_RESULT_EXITWORKTREE_TOOK_TO_LAUNCH_FOLDER_VAR_2)} ${TOOL_RESULT_EXITWORKTREE_TOOK_TO_LAUNCH_FOLDER_VAR_3}`:"The way back led outside the folders that this session was launched with"}, so the session is now in ${TOOL_RESULT_EXITWORKTREE_TOOK_TO_LAUNCH_FOLDER_VAR_1(TOOL_RESULT_EXITWORKTREE_TOOK_TO_LAUNCH_FOLDER_VAR_0.restoredCwd)}, a folder that it was launched with.
