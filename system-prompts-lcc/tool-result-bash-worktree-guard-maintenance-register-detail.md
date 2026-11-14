<!--
name: 'Tool result: Bash worktree guard maintenance register detail'
description: >-
  Worktree guard detail when git maintenance register would add the repo to
  global (or --config-file) config.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_REGISTER_DETAIL_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_REGISTER_DETAIL_VAR_1
-->
is git maintenance register, which adds the repository to your global git configuration${TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_REGISTER_DETAIL_VAR_0.some((TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_REGISTER_DETAIL_VAR_1)=>TOOL_RESULT_BASH_WORKTREE_GUARD_MAINTENANCE_REGISTER_DETAIL_VAR_1.startsWith("--config-file"))?" (or to the file --config-file names)":""}, where any scheduled git maintenance keeps running git on it after this session
