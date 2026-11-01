<!--
name: 'Tool result: Bash worktree guard gcloud scp/ssh flag placement'
description: >-
  Worktree-guard refusal operand naming an --scp-flag or misplaced --ssh-flag
  with its fix
ccVersion: 2.1.316
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_GCLOUD_SCP_SSH_FLAG_PLACEMENT_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_GCLOUD_SCP_SSH_FLAG_PLACEMENT_VAR_1
-->
with ${TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_GCLOUD_SCP_SSH_FLAG_PLACEMENT_VAR_0(TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_GCLOUD_SCP_SSH_FLAG_PLACEMENT_VAR_1??"")} (${/^--scp/.test(TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_GCLOUD_SCP_SSH_FLAG_PLACEMENT_VAR_1??"")?"--scp-flag hands options to scp, which can run a local program; drop it":"put --ssh-flag after the word ssh"})
