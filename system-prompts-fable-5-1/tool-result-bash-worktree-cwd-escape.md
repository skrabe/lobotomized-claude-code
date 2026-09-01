<!--
name: 'Worktree isolation lost, refusing to run'
description: >-
  Bash preSpawnError stderr returned to the isolated agent when its worktree cwd
  is gone and recovery would escape isolation.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_BASH_WORKTREE_CWD_ESCAPE_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_CWD_ESCAPE_VAR_1
-->
This agent is isolated in the worktree ${TOOL_RESULT_BASH_WORKTREE_CWD_ESCAPE_VAR_0}, but its working directory "${TOOL_RESULT_BASH_WORKTREE_CWD_ESCAPE_VAR_1}" no longer exists and the only recovery target is the parent session's shared checkout. Refusing to run there — the isolation worktree appears to have been removed. Report this instead of retrying.
