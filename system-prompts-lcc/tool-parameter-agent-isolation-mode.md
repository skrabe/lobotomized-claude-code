<!--
name: 'Tool Parameter: Agent isolation mode'
description: >-
  The isolation enum param in the Task/spawn-agent tool input schema describing
  worktree vs remote execution; model-facing.
ccVersion: 2.1.191
-->
Isolation mode. "worktree" creates a temporary git worktree so the agent works on an isolated copy of the repo. "remote" launches the agent in a remote cloud environment (always runs in background; availability is gated).
