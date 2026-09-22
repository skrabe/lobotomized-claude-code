<!--
name: ExitWorktree subagent cwd error
description: >-
  ExitWorktree validation error returned to the model when called from a
  subagent with a cwd override.
ccVersion: 2.1.206
-->
ExitWorktree cannot be called from a subagent with a cwd override (isolation: "worktree" or explicit cwd) — it would mutate the parent session's process-wide working directory. This agent is already isolated; use Bash with `cd` for directory changes within it.
