<!--
name: 'Tool Description: Bash (sandbox — git worktrees read-only, no override)'
description: >-
  Explains .git/worktrees is read-only in the sandbox so git worktree
  add/move/remove fail halfway, and directs telling the user the command to run
  themselves
ccVersion: 2.1.325
-->
The repository's `.git/worktrees` is read-only in the sandbox, apart from this session's own worktrees, so `git worktree add`, `move` and `remove`, and renaming a branch that another worktree has checked out, fail there halfway. Tell the user the command to run themselves.
