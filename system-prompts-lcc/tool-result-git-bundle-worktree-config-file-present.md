<!--
name: 'Git bundle: worktree config file present'
description: >-
  Refusal reason when a linked worktree admin entry carries a per-worktree
  config file
ccVersion: 2.1.281
-->
its administrative entry carries a per-worktree configuration file, one a Claude Code session of this repository could have written there — delete that file only if nothing in it matters (`git rev-parse --git-path config.worktree` names it; git sparse-checkout writes one, and a sparse tree needs it to stay sparse), or start from the repository’s main checkout
