<!--
name: 'Data: worktree.baseRef setting description'
description: >-
  Description of the `worktree.baseRef` setting in Claude Code's settings JSON
  schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Which ref new worktrees branch from. 'fresh' (default) branches from origin/<default-branch> for a clean tree. 'head' branches from your current local HEAD so unpushed commits and feature-branch state are present. Applies to --worktree, EnterWorktree, and agent isolation.
