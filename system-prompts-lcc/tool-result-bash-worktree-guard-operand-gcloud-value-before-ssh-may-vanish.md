<!--
name: 'Tool result: Bash worktree guard gcloud value before ssh may vanish'
description: >-
  Worktree-guard refusal operand: a computed value before the word ssh may
  expand to nothing so gcloud's subcommand cannot be determined
ccVersion: 2.1.316
variables:
  - >-
    TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_GCLOUD_VALUE_BEFORE_SSH_MAY_VANISH_VAR_0
  - >-
    TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_GCLOUD_VALUE_BEFORE_SSH_MAY_VANISH_VAR_1
-->
with ${TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_GCLOUD_VALUE_BEFORE_SSH_MAY_VANISH_VAR_0(TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_GCLOUD_VALUE_BEFORE_SSH_MAY_VANISH_VAR_1.value)} before the word ssh: it may expand to no word at all and the next word would take its place, so this cannot tell what gcloud will run (spell the value out)
