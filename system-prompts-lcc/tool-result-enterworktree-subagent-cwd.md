<!--
name: EnterWorktree subagent cwd error
description: >-
  EnterWorktree validation error returned to the model when called from a
  subagent with a cwd override.
ccVersion: 2.1.206
-->
EnterWorktree cannot create a worktree from a subagent with a cwd override (isolation: "worktree" or explicit cwd) — it would mutate the parent session's process-wide working directory. 
