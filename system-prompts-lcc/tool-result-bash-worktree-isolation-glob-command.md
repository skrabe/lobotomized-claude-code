<!--
name: 'Tool Result: Bash worktree isolation — glob command'
description: >-
  Refusal-reason clause returned to the model as the Bash tool's stderr when a
  worktree-isolated agent's command names its executable via a runtime-resolved
  glob that can't be verified as git.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_BASH_WORKTREE_ISOLATION_GLOB_COMMAND_VAR_0
-->
spells its command as a glob (${TOOL_RESULT_BASH_WORKTREE_ISOLATION_GLOB_COMMAND_VAR_0}) that bash resolves at runtime, so it can't be verified as anything but git
