<!--
name: 'Tool Description: Bash (sandbox — git worktrees read-only, override available)'
description: >-
  Explains .git/worktrees is read-only in the sandbox so git worktree
  add/move/remove fail halfway, and directs running them outside the sandbox
ccVersion: 2.1.325
-->
The repository's `.git/worktrees` is read-only in the sandbox, apart from this session's own worktrees, so `git worktree add`, `move` and `remove`, and renaming a branch that another worktree has checked out, fail there halfway. Run them outside the sandbox, as for a command that already failed because of it.
