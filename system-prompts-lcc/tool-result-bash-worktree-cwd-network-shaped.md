<!--
name: 'Tool Result: Bash Worktree CWD Network-Shaped Block'
description: >-
  Bash tool refusal returned to the model when a worktree-isolated agent's
  working directory resolves to a network-shaped path (UNC share or /net
  automount) while the protected checkout is local.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_BASH_WORKTREE_CWD_NETWORK_SHAPED_VAR_0
-->
This command was blocked because its working directory is network-shaped (a UNC share or /net automount spelling) while the protected checkout is local. If the directory is genuinely inside the worktree ${TOOL_RESULT_BASH_WORKTREE_CWD_NETWORK_SHAPED_VAR_0}, re-run the command from its local, plainly-spelled path.
