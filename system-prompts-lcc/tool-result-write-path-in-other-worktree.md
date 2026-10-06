<!--
name: 'Tool Result: Write path in other worktree'
description: >-
  Validation error when an isolated agent's file path lies in a different
  worktree, telling the model to edit the copy under its own worktree instead
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WRITE_PATH_IN_OTHER_WORKTREE_VAR_0
  - TOOL_RESULT_WRITE_PATH_IN_OTHER_WORKTREE_VAR_1
  - TOOL_RESULT_WRITE_PATH_IN_OTHER_WORKTREE_VAR_2
  - TOOL_RESULT_WRITE_PATH_IN_OTHER_WORKTREE_VAR_3
-->
${TOOL_RESULT_WRITE_PATH_IN_OTHER_WORKTREE_VAR_0} is isolated in the worktree ${TOOL_RESULT_WRITE_PATH_IN_OTHER_WORKTREE_VAR_1}, so its writes are limited to that folder. This path is in a different worktree (${TOOL_RESULT_WRITE_PATH_IN_OTHER_WORKTREE_VAR_2(TOOL_RESULT_WRITE_PATH_IN_OTHER_WORKTREE_VAR_3)}). Edit the copy of this file under ${TOOL_RESULT_WRITE_PATH_IN_OTHER_WORKTREE_VAR_1} instead.
