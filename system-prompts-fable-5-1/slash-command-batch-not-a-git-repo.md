<!--
name: /batch not-a-git-repo guard
description: >-
  Guard text returned as the /batch command prompt when the workspace is not a
  git repository, injected into the model's turn.
ccVersion: 2.1.206
-->
This is not a git repository. The `/batch` command requires a git repo because it spawns agents in isolated git worktrees and creates PRs from each. Initialize a repo first, or run this from inside an existing one.
