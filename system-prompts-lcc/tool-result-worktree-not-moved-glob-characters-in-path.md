<!--
name: 'Tool result: worktree path has glob characters'
description: >-
  EnterWorktree refusal when the worktree real path contains * ? [ ] while
  blockReadsOutsideWorkingDirectories is on.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_WORKTREE_NOT_MOVED_GLOB_CHARACTERS_IN_PATH_VAR_0
  - TOOL_RESULT_WORKTREE_NOT_MOVED_GLOB_CHARACTERS_IN_PATH_VAR_1
  - TOOL_RESULT_WORKTREE_NOT_MOVED_GLOB_CHARACTERS_IN_PATH_VAR_2
-->
The session was not moved: the real path of ${TOOL_RESULT_WORKTREE_NOT_MOVED_GLOB_CHARACTERS_IN_PATH_VAR_0(TOOL_RESULT_WORKTREE_NOT_MOVED_GLOB_CHARACTERS_IN_PATH_VAR_1??TOOL_RESULT_WORKTREE_NOT_MOVED_GLOB_CHARACTERS_IN_PATH_VAR_2)} has one of the characters * ? [ ] in it. While permissions.blockReadsOutsideWorkingDirectories is on, sandboxed commands may not be able to read such a folder. Use a worktree whose path has none of them.
