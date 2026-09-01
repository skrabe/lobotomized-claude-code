<!--
name: 'Data: WorktreeCreate hook symlink rejected'
description: >-
  Error surfaced when a repository-committed symlink under the checkout root
  could redirect the hook worktree outside the repository.
ccVersion: 2.1.218
-->
A repository-committed symlink below the checkout root could redirect the worktree outside the repository. Remove the symlink (or emit a path outside the repository) and retry.
