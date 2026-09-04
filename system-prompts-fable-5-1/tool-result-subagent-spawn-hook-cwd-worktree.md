<!--
name: Subagent Spawn Hook Cwd Worktree
description: >-
  Agent-tool error when a plugin agent.spawn hook sets cwd on a
  worktree-isolated spawn.
ccVersion: 2.1.261
-->
A plugin's agent.spawn hook set cwd on a spawn isolated in a worktree; cwd and isolation: "worktree" are mutually exclusive.
