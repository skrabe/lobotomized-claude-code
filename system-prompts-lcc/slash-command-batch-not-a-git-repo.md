<!--
name: /batch not-a-git-repo guard
description: >-
  Guard text returned as the /batch command prompt when the directory is not a
  git repository and no WorktreeCreate hook is configured, injected into the
  model's turn.
ccVersion: 2.1.281
-->
The `/batch` command runs each agent in its own isolated worktree, and none can be created here: this directory is not in a git repository and no WorktreeCreate hook is configured. Run `/batch` from inside a git repository, or configure WorktreeCreate and WorktreeRemove hooks in settings.json for another version-control system.
