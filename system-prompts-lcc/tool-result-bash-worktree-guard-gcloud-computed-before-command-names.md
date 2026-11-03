<!--
name: 'Tool Result: Bash worktree guard gcloud computed value before command names'
description: >-
  Refuses a computed value before gcloud command names and asks to spell command
  names first, as --project="$p"
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_GCLOUD_COMPUTED_BEFORE_COMMAND_NAMES_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GUARD_GCLOUD_COMPUTED_BEFORE_COMMAND_NAMES_VAR_1
-->
with ${TOOL_RESULT_BASH_WORKTREE_GUARD_GCLOUD_COMPUTED_BEFORE_COMMAND_NAMES_VAR_0(TOOL_RESULT_BASH_WORKTREE_GUARD_GCLOUD_COMPUTED_BEFORE_COMMAND_NAMES_VAR_1.value)} before its command names, where this check cannot tell whether the command runs ssh (spell the command names out first and put computed values after them, as --project="$p")
