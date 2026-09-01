<!--
name: 'Tool Result: Bash exec-arg-limit worktree deny paths'
description: >-
  Bash spawn-failure (E2BIG) tail explaining the sandbox deny paths added per
  registered git worktree and how to prune them
ccVersion: 2.1.204
variables:
  - TOOL_RESULT_BASH_EXEC_ARG_LIMIT_WORKTREE_DENY_PATHS_VAR_0
-->
, ${TOOL_RESULT_BASH_EXEC_ARG_LIMIT_WORKTREE_DENY_PATHS_VAR_0} of them for registered git worktrees, which grow this list without bound. From another terminal, remove worktrees you no longer need (git worktree remove <path>; git worktree prune for already-deleted checkouts), then restart Claude Code so the profile is rebuilt without them — or relax the Bash sandbox for this session with /sandbox.
