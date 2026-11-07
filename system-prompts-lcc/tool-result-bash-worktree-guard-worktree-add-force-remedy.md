<!--
name: 'Tool Result: Bash worktree guard worktree add --force remedy'
description: >-
  Tells Claude to drop --force, use -b for a new branch and run git worktree
  prune if the path is registered but missing
ccVersion: 2.1.319
-->
Run it without that option, adding -b <new-branch> to make a new branch. If git says the path is registered but missing, run git worktree prune first.
